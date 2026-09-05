const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

// Exercise the actual app functions without exporting a test API to production.
const appSource = fs.readFileSync(path.join(__dirname, "../public/app.js"), "utf8");
const ending = /\}\)\(\);\s*$/;
assert.match(appSource, ending);
const testSource = appSource.replace(ending,
    "globalThis.schemaTest = { loadSchemas, renderSchemaViewer, state, SCHEMA_CONFIG };\n})();");

function element() {
    return {
        children: [], value: "", text: "", classes: new Set(),
        appendChild(child) { this.children.push(child); return child; },
        append(...children) { this.children.push(...children); },
        replaceChildren(...children) { this.children = children; this.text = ""; },
        set textContent(value) { this.text = String(value); this.children = []; },
        get textContent() { return this.text + this.children.map(child => child.textContent).join(" "); },
        get classList() {
            return { toggle: (name, enabled) => enabled ? this.classes.add(name) : this.classes.delete(name) };
        },
    };
}

function harness({ pathname = "/SpoolmanDB-Community/", failFile = null } = {}) {
    const nodes = Object.fromEntries([
        "schema-choice", "schema-status", "schema-summary", "schema-fields-body",
        "schema-open-link", "schema-copy-url",
    ].map(id => ["#" + id, element()]));
    nodes["#schema-choice"].value = "compiledFilament";
    const requests = [];
    const failure = { file: failFile };
    const context = {
        window: { location: { pathname, href: "https://example.test" + pathname } },
        document: {
            querySelector: selector => nodes[selector] || null,
            querySelectorAll: () => [],
            addEventListener() {},
            createElement: element,
            createDocumentFragment: element,
        },
        URL, console,
        fetch: async (url, options) => {
            requests.push({ url, options });
            const file = path.basename(url);
            if (file === failure.file) return { ok: false, status: 503 };
            return {
                ok: true,
                json: async () => JSON.parse(fs.readFileSync(path.join(__dirname, "..", file), "utf8")),
            };
        },
    };
    vm.runInNewContext(testSource, context, { filename: "public/app.js" });
    return { api: context.schemaTest, nodes, requests, failure };
}

module.exports = async function testSchemaViewer() {
    for (const pathname of ["/SpoolmanDB-Community/", "/public/"]) {
        const { api, nodes, requests } = harness({ pathname });
        await api.loadSchemas();
        assert.equal(requests.length, Object.keys(api.SCHEMA_CONFIG).length);
        for (const [kind, config] of Object.entries(api.SCHEMA_CONFIG)) {
            assert.ok(api.state.schemas[kind], kind + " must be fetched");
            assert.equal(api.state.schemaPaths[kind], (pathname === "/public/" ? "../" : "") + config.file);
            nodes["#schema-choice"].value = kind;
            api.renderSchemaViewer();
            assert.match(nodes["#schema-status"].textContent, new RegExp(config.title + " loaded from"));
            assert.doesNotMatch(nodes["#schema-summary"].textContent, /Waiting|Loading|Unavailable/);
            assert.ok(nodes["#schema-fields-body"].children[0].children.length > 0);
            assert.equal(nodes["#schema-open-link"].href, api.state.schemaPaths[kind]);
        }
        nodes["#schema-choice"].value = "compiledFilament";
        api.renderSchemaViewer();
        assert.match(nodes["#schema-fields-body"].textContent, /\[\]\.is_refill/);
        assert.match(nodes["#schema-fields-body"].textContent, /\[\]\.tds_url/);
        assert.ok(requests.every(request => request.options.cache === "no-store"));
    }
    console.log("ok schema viewer loads and renders every configured schema on deployed and local paths");

    const { api, nodes, failure } = harness({ failFile: "filaments.compiled.schema.json" });
    await api.loadSchemas();
    assert.match(nodes["#schema-status"].textContent, /filaments\.compiled\.schema\.json.*HTTP 503/);
    assert.match(nodes["#schema-summary"].textContent, /Unavailable/);
    assert.doesNotMatch(nodes["#schema-fields-body"].textContent, /still loading/);
    nodes["#schema-choice"].value = "filament";
    api.renderSchemaViewer();
    assert.match(nodes["#schema-status"].textContent, /Filament source schema loaded/);
    assert.equal(nodes["#schema-status"].classes.has("status-text-error"), false);
    nodes["#schema-choice"].value = "material";
    api.renderSchemaViewer();
    assert.match(nodes["#schema-status"].textContent, /Material defaults schema loaded/);

    failure.file = null;
    nodes["#schema-choice"].value = "compiledFilament";
    await api.loadSchemas();
    assert.match(nodes["#schema-status"].textContent, /Compiled filament schema loaded/);
    assert.equal(api.state.schemaErrors.compiledFilament, undefined);
    console.log("ok schema failure is explicit, isolated, and cleared after successful reload");
};

if (require.main === module) {
    module.exports().catch(error => { console.error(error); process.exitCode = 1; });
}
