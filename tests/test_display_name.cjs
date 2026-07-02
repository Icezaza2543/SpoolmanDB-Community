const assert = require("assert");
const { materialAppearsInName, getDisplayName } = require("../public/display-name.js");

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

console.log("display-name tests passed");