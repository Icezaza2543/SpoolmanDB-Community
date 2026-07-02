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

    function buildFilamentSearchText(item) {
        if (!item) {
            return "";
        }

        return [
            item.id,
            item.manufacturer,
            item.name,
            getDisplayName(item),
            item.material,
            item.color_hex,
            ...(Array.isArray(item.color_hexes) ? item.color_hexes : []),
            ...(Array.isArray(item.codes) ? item.codes : []),
            ...(Array.isArray(item.eans) ? item.eans : []),
            ...(Array.isArray(item.eans_refill) ? item.eans_refill : []),
        ]
            .filter(Boolean)
            .join(" ")
            .toLowerCase();
    }

    const api = {
        materialAppearsInName,
        getDisplayName,
        buildFilamentSearchText,
    };

    global.SpoolmanDisplayName = api;

    if (typeof module !== "undefined" && module.exports) {
        module.exports = api;
    }
})(typeof globalThis !== "undefined" ? globalThis : this);