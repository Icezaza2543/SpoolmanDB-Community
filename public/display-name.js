(function (global) {
    "use strict";

    function escapeRegExp(value) {
        return String(value).replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    }

    function materialAppearsInName(name, material) {
        if (!name || !material) {
            return false;
        }

        const pattern = new RegExp(
            "(?<![A-Z0-9])" + escapeRegExp(String(material).toUpperCase()) + "(?![A-Z0-9])"
        );
        return pattern.test(String(name).toUpperCase());
    }

    function getDisplayName(item) {
        const name = item && item.name ? String(item.name) : "";
        const material = item && item.material ? String(item.material) : "";

        if (!name) {
            return name;
        }

        if (!material || materialAppearsInName(name, material)) {
            return name;
        }

        return material + " " + name;
    }

    const api = {
        materialAppearsInName,
        getDisplayName,
    };

    global.SpoolmanDisplayName = api;

    if (typeof module !== "undefined" && module.exports) {
        module.exports = api;
    }
})(typeof globalThis !== "undefined" ? globalThis : this);