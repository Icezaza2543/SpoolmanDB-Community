const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const source = fs.readFileSync(require('node:path').join(__dirname, '../public/app.js'), 'utf8');
const context = {
    window: { location: { pathname: '/' } },
    document: {
        querySelector: () => null, querySelectorAll: () => [], addEventListener() {},
        createElement: tag => ({ tag, setAttribute() {} }),
    }, URL,
};
vm.runInNewContext(source.replace(/\}\)\(\);\s*$/, 'globalThis.testApi = { documentLink, renderKnowledgeGraphChart };\n})();'), context);
for (const url of ['javascript:alert(1)', 'data:text/html,<script>alert(1)</script>', '//evil.test/doc', 'file:///secret']) {
    const link = context.testApi.documentLink('TDS', url);
    assert.equal(link.href, undefined, url + ' must not be navigable');
}
assert.equal(context.testApi.documentLink('TDS', 'https://example.com/tds.pdf').href, 'https://example.com/tds.pdf');
let option;
context.testApi.renderKnowledgeGraphChart({ setOption: value => { option = value; } }, { graph: { nodes: [], links: [] } });
assert.equal(option.tooltip.renderMode, 'richText', 'Untrusted chart labels must not become HTML');
console.log('Explorer link and tooltip security tests passed');
