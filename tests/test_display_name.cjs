const assert = require("assert");
const {
    materialAppearsInName,
    getDisplayName,
    getSpoolValue,
    buildFilamentSearchText,
} = require("../public/display-name.js");

function test(name, fn) {
    try {
        fn();
        console.log("ok " + name);
    } catch (error) {
        console.error("not ok " + name);
        throw error;
    }
}

test("materialAppearsInName detects standalone material tokens", function () {
    assert.strictEqual(materialAppearsInName("ABS Prime White", "ABS"), true);
    assert.strictEqual(materialAppearsInName("HT-PLA Red", "PLA"), true);
    assert.strictEqual(materialAppearsInName("ABS Plus BLACK", "ABS"), true);
});

test("materialAppearsInName avoids embedded material substrings", function () {
    assert.strictEqual(materialAppearsInName("EasyFil ePLA Red", "PLA"), false);
    assert.strictEqual(materialAppearsInName("PCABS Blend", "ABS"), false);
    assert.strictEqual(materialAppearsInName("Plus BLACK", "ABS"), false);
});

test("getDisplayName prefixes material when missing from raw name", function () {
    assert.strictEqual(
        getDisplayName({ name: "Plus BLACK", material: "ABS" }),
        "ABS Plus BLACK"
    );
});

test("getDisplayName leaves names that already include material", function () {
    assert.strictEqual(
        getDisplayName({ name: "ABS Plus BLACK", material: "ABS" }),
        "ABS Plus BLACK"
    );
});

test("getDisplayName does not treat ePLA as standalone PLA", function () {
    assert.strictEqual(
        getDisplayName({ name: "ePLA Matte BLACK", material: "PLA" }),
        "PLA ePLA Matte BLACK"
    );
});

test("getSpoolValue preserves refill packaging separately from spool material", function () {
    assert.strictEqual(getSpoolValue({ spool_type: null, is_refill: true }), "refill");
    assert.strictEqual(getSpoolValue({ spool_type: "plastic", is_refill: false }), "plastic");
    assert.strictEqual(getSpoolValue({ spool_type: null, is_refill: false }), "none");
    assert.strictEqual(getSpoolValue({ spool_type: "unknow" }), "none");
});

test("buildFilamentSearchText makes refill products searchable", function () {
    const searchText = buildFilamentSearchText({
        manufacturer: "Example",
        name: "Black",
        material: "PLA",
        is_refill: true,
    });

    assert.ok(searchText.includes("refill"));
    assert.ok(!buildFilamentSearchText({ name: "Black" }).includes("none"));
});

test("buildFilamentSearchText includes composite display names", function () {
    const item = {
        id: "azurefilm_abs_plusblack_1000_175_p",
        manufacturer: "AzureFilm",
        name: "Plus BLACK",
        material: "ABS",
        color_hex: "000000",
    };
    const searchText = buildFilamentSearchText(item);

    assert.ok(searchText.includes("plus black"));
    assert.ok(searchText.includes("abs plus black"));
    assert.ok(searchText.includes("abs"));
});

test("buildFilamentSearchText keeps names that already include material", function () {
    const item = {
        manufacturer: "Example",
        name: "ABS Prime White",
        material: "ABS",
    };
    const searchText = buildFilamentSearchText(item);

    assert.ok(searchText.includes("abs prime white"));
    assert.strictEqual((searchText.match(/abs prime white/g) || []).length, 2);
});

test("buildFilamentSearchText does not treat ePLA as standalone PLA", function () {
    const item = {
        manufacturer: "Example",
        name: "ePLA Matte BLACK",
        material: "PLA",
    };
    const searchText = buildFilamentSearchText(item);

    assert.ok(searchText.includes("epla matte black"));
    assert.ok(searchText.includes("pla epla matte black"));
});

console.log("display-name tests passed");
