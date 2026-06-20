(function () {
    "use strict";

    const EXTERNAL_DB_URL = "https://icezaza2543.github.io/SpoolmanDB-Community/";
    const MAX_RENDERED_ROWS = 150;
    const GITHUB_REPO = "https://github.com/Icezaza2543/SpoolmanDB-Community";
    const SOURCE_FINDER_LIMIT = 8;

    const state = {
        filaments: [],
        materials: [],
        matches: [],
        manufacturerCounts: new Map(),
    };

    const elements = {
        loadStatus: document.querySelector("#load-status"),
        statFilaments: document.querySelector("#stat-filaments"),
        statManufacturers: document.querySelector("#stat-manufacturers"),
        statMaterials: document.querySelector("#stat-materials"),
        statMulticolor: document.querySelector("#stat-multicolor"),
        statBarcodes: document.querySelector("#stat-barcodes"),
        filters: document.querySelector("#filters"),
        search: document.querySelector("#search"),
        material: document.querySelector("#material-filter"),
        manufacturer: document.querySelector("#manufacturer-filter"),
        diameter: document.querySelector("#diameter-filter"),
        spool: document.querySelector("#spool-filter"),
        resultsSummary: document.querySelector("#results-summary"),
        activeFilters: document.querySelector("#active-filters"),
        resultsBody: document.querySelector("#results-body"),
        contributorSourceInput: document.querySelector("#contributor-source-input"),
        contributorSourceResults: document.querySelector("#contributor-source-results"),
    };

    document.addEventListener("DOMContentLoaded", init);

    async function init() {
        bindCopyButtons();
        bindContributorHelper();
        elements.filters.addEventListener("input", renderFilteredResults);
        elements.filters.addEventListener("reset", function () {
            window.setTimeout(renderFilteredResults, 0);
        });

        try {
            const [filaments, materials] = await Promise.all([
                fetchJson(["filaments.json", "../filaments.json"]),
                fetchJson(["materials.json", "../materials.json"]),
            ]);

            state.filaments = Array.isArray(filaments) ? filaments : [];
            state.materials = Array.isArray(materials) ? materials : [];

            populateFilters();
            renderStats();
            renderFilteredResults();
            buildManufacturerIndex();
            renderContributorSourceFinder();
            setStatus("Loaded " + formatNumber(state.filaments.length) + " filament variants.");
        } catch (error) {
            setStatus("Could not load JSON data. Serve this page through GitHub Pages or a local web server.", true);
            elements.resultsBody.replaceChildren(emptyRow("Data failed to load: " + error.message));
            renderContributorSourceFinder("Data not loaded. Serve this page through GitHub Pages or a local web server.");
        }
    }

    async function fetchJson(paths) {
        const errors = [];

        for (const path of paths) {
            try {
                const response = await fetch(path, { cache: "no-store" });
                if (!response.ok) {
                    throw new Error(path + " returned HTTP " + response.status);
                }
                return response.json();
            } catch (error) {
                errors.push(error.message);
            }
        }

        throw new Error(errors.join("; "));
    }

    function populateFilters() {
        populateSelect(elements.material, uniqueSorted(state.filaments.map((item) => item.material)));
        populateSelect(elements.manufacturer, uniqueSorted(state.filaments.map((item) => item.manufacturer)));
        populateSelect(
            elements.diameter,
            uniqueSorted(state.filaments.map((item) => item.diameter)).sort((a, b) => Number(a) - Number(b)),
            function (value) {
                return value + " mm";
            }
        );
        populateSelect(elements.spool, uniqueSorted(state.filaments.map((item) => spoolValue(item.spool_type))), labelSpool);
    }

    function populateSelect(select, values, labeler) {
        const first = select.options[0];
        select.replaceChildren(first);

        values.forEach(function (value) {
            if (value === "" || value === undefined || value === null) {
                return;
            }

            const option = document.createElement("option");
            option.value = String(value);
            option.textContent = labeler ? labeler(value) : String(value);
            select.appendChild(option);
        });
    }

    function renderStats() {
        const manufacturers = new Set(state.filaments.map((item) => item.manufacturer).filter(Boolean));
        const materials = new Set(state.filaments.map((item) => item.material).filter(Boolean));
        const multicolor = state.filaments.filter((item) => Array.isArray(item.color_hexes) && item.color_hexes.length > 0);
        const barcodes = state.filaments.filter(hasProductIds);

        elements.statFilaments.textContent = formatNumber(state.filaments.length);
        elements.statManufacturers.textContent = formatNumber(manufacturers.size);
        elements.statMaterials.textContent = formatNumber(materials.size) + " / " + formatNumber(state.materials.length);
        elements.statMulticolor.textContent = formatNumber(multicolor.length);
        elements.statBarcodes.textContent = formatNumber(barcodes.length);
    }

    function renderFilteredResults() {
        const query = elements.search.value.trim().toLowerCase();
        const material = elements.material.value;
        const manufacturer = elements.manufacturer.value;
        const diameter = elements.diameter.value;
        const spool = elements.spool.value;

        state.matches = state.filaments.filter(function (item) {
            if (material && item.material !== material) {
                return false;
            }
            if (manufacturer && item.manufacturer !== manufacturer) {
                return false;
            }
            if (diameter && String(item.diameter) !== diameter) {
                return false;
            }
            if (spool && spoolValue(item.spool_type) !== spool) {
                return false;
            }
            if (query && !searchText(item).includes(query)) {
                return false;
            }
            return true;
        });

        const visible = state.matches.slice(0, MAX_RENDERED_ROWS);
        const fragment = document.createDocumentFragment();

        if (visible.length === 0) {
            fragment.appendChild(emptyRow("No filament variants match the current filters."));
        } else {
            visible.forEach(function (item) {
                fragment.appendChild(renderRow(item));
            });
        }

        elements.resultsBody.replaceChildren(fragment);
        elements.resultsSummary.textContent =
            "Showing " + formatNumber(visible.length) + " of " + formatNumber(state.matches.length) + " matches";
        elements.activeFilters.textContent = describeFilters(query, material, manufacturer, diameter, spool);
    }

    function renderRow(item) {
        const row = document.createElement("tr");
        row.appendChild(cell(renderSwatch(item)));
        row.appendChild(textCell(item.manufacturer));

        const nameCell = document.createElement("td");
        const name = document.createElement("div");
        name.className = "filament-name";
        name.textContent = item.name || "Unnamed filament";
        const id = document.createElement("div");
        id.className = "muted";
        id.textContent = item.id || "";
        nameCell.append(name, id);
        row.appendChild(nameCell);

        row.appendChild(textCell(item.material));
        row.appendChild(textCell(formatNumber(item.diameter) + " mm"));
        row.appendChild(textCell(formatNumber(item.weight) + " g"));
        row.appendChild(textCell(labelSpool(spoolValue(item.spool_type))));
        row.appendChild(textCell(formatTemps(item)));
        row.appendChild(cell(renderTags(item)));
        return row;
    }

    function renderSwatch(item) {
        const swatch = document.createElement("div");
        swatch.className = "swatch";
        swatch.title = colorLabel(item);
        swatch.style.background = colorBackground(item);
        return swatch;
    }

    function renderTags(item) {
        const list = document.createElement("div");
        list.className = "tag-list";

        if (Array.isArray(item.codes) && item.codes.length > 0) {
            list.appendChild(tag("SKU", true));
        }
        if (Array.isArray(item.eans) && item.eans.length > 0) {
            list.appendChild(tag("EAN", true));
        }
        if (Array.isArray(item.eans_refill) && item.eans_refill.length > 0) {
            list.appendChild(tag("REFILL", true));
        }
        if (Array.isArray(item.color_hexes) && item.color_hexes.length > 0) {
            list.appendChild(tag("MULTI", false));
        }
        if (list.children.length === 0) {
            list.appendChild(tag("DATA", false));
        }
        return list;
    }

    function tag(text, orange) {
        const span = document.createElement("span");
        span.className = orange ? "tag tag-orange" : "tag";
        span.textContent = text;
        return span;
    }

    function cell(child) {
        const td = document.createElement("td");
        td.appendChild(child);
        return td;
    }

    function textCell(text) {
        const td = document.createElement("td");
        td.textContent = text || "-";
        return td;
    }

    function emptyRow(message) {
        const row = document.createElement("tr");
        const td = document.createElement("td");
        td.colSpan = 9;
        td.textContent = message;
        row.appendChild(td);
        return row;
    }

    function searchText(item) {
        return [
            item.id,
            item.manufacturer,
            item.name,
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

    function describeFilters(query, material, manufacturer, diameter, spool) {
        const parts = [];
        if (query) {
            parts.push('search "' + query + '"');
        }
        if (material) {
            parts.push("material " + material);
        }
        if (manufacturer) {
            parts.push("manufacturer " + manufacturer);
        }
        if (diameter) {
            parts.push("diameter " + diameter + " mm");
        }
        if (spool) {
            parts.push("spool " + labelSpool(spool));
        }
        return parts.length > 0 ? parts.join(" / ") : "No filters applied.";
    }

    function formatTemps(item) {
        const extruder = item.extruder_temp ? item.extruder_temp + " C" : formatRange(item.extruder_temp_range);
        const bed = item.bed_temp ? item.bed_temp + " C" : formatRange(item.bed_temp_range);
        if (!extruder && !bed) {
            return "-";
        }
        return "E " + (extruder || "-") + " / B " + (bed || "-");
    }

    function formatRange(value) {
        if (!Array.isArray(value) || value.length !== 2) {
            return "";
        }
        return value[0] + "-" + value[1] + " C";
    }

    function colorBackground(item) {
        if (item.color_hex && isHex(item.color_hex)) {
            return "#" + item.color_hex;
        }

        if (Array.isArray(item.color_hexes) && item.color_hexes.length > 0) {
            const safeColors = item.color_hexes.filter(isHex).map((value) => "#" + value);
            if (safeColors.length > 0) {
                const step = 100 / safeColors.length;
                const stops = safeColors.map(function (color, index) {
                    const start = Math.round(index * step);
                    const end = Math.round((index + 1) * step);
                    return color + " " + start + "% " + end + "%";
                });
                return "linear-gradient(90deg, " + stops.join(", ") + ")";
            }
        }

        return "#f6f6f6";
    }

    function colorLabel(item) {
        if (item.color_hex) {
            return "#" + item.color_hex;
        }
        if (Array.isArray(item.color_hexes)) {
            return item.color_hexes.map((hex) => "#" + hex).join(", ");
        }
        return "No color";
    }

    function isHex(value) {
        return /^[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$/.test(String(value));
    }

    function hasProductIds(item) {
        return [item.codes, item.eans, item.eans_refill].some(function (value) {
            return Array.isArray(value) && value.length > 0;
        });
    }

    function uniqueSorted(values) {
        return Array.from(new Set(values.filter((value) => value !== undefined && value !== null))).sort(function (a, b) {
            return String(a).localeCompare(String(b), undefined, { numeric: true, sensitivity: "base" });
        });
    }

    function spoolValue(value) {
        return value || "none";
    }

    function labelSpool(value) {
        if (value === "none") {
            return "Not specified";
        }
        return String(value).replace(/^\w/, function (letter) {
            return letter.toUpperCase();
        });
    }

    function formatNumber(value) {
        if (value === undefined || value === null || value === "") {
            return "-";
        }
        return new Intl.NumberFormat("en-US").format(value);
    }

    function bindContributorHelper() {
        if (!elements.contributorSourceInput) {
            return;
        }

        elements.contributorSourceInput.addEventListener("input", function () {
            renderContributorSourceFinder();
        });
    }

    function buildManufacturerIndex() {
        state.manufacturerCounts = new Map();
        state.filaments.forEach(function (item) {
            if (!item.manufacturer) {
                return;
            }

            const name = String(item.manufacturer);
            state.manufacturerCounts.set(name, (state.manufacturerCounts.get(name) || 0) + 1);
        });
    }

    function renderContributorSourceFinder(forcedMessage) {
        if (!elements.contributorSourceResults) {
            return;
        }

        if (forcedMessage) {
            elements.contributorSourceResults.replaceChildren(sourceFinderMessage(forcedMessage));
            return;
        }

        if (state.manufacturerCounts.size === 0) {
            elements.contributorSourceResults.replaceChildren(sourceFinderMessage("No manufacturer data loaded yet."));
            return;
        }

        const query = elements.contributorSourceInput ? elements.contributorSourceInput.value.trim().toLowerCase() : "";

        if (!query) {
            elements.contributorSourceResults.replaceChildren(
                sourceFinderMessage("Type a manufacturer name to see matches.")
            );
            return;
        }

        const allMatches = Array.from(state.manufacturerCounts.entries())
            .filter(function (entry) {
                return entry[0].toLowerCase().includes(query);
            })
            .sort(function (a, b) {
                return a[0].localeCompare(b[0], undefined, { numeric: true, sensitivity: "base" });
            });
        const matches = allMatches.slice(0, SOURCE_FINDER_LIMIT);

        if (matches.length === 0) {
            elements.contributorSourceResults.replaceChildren(
                sourceFinderMessage('No manufacturers match "' + query + '".')
            );
            return;
        }

        const fragment = document.createDocumentFragment();
        matches.forEach(function (entry) {
            fragment.appendChild(renderSourceFinderHit(entry[0], entry[1]));
        });
        if (allMatches.length > SOURCE_FINDER_LIMIT) {
            fragment.appendChild(
                sourceFinderMessage("Showing first " + SOURCE_FINDER_LIMIT + " matches. Refine the search to narrow it down.")
            );
        }
        elements.contributorSourceResults.replaceChildren(fragment);
    }

    function sourceFinderMessage(message) {
        const item = document.createElement("li");
        item.className = "source-empty";
        item.textContent = message;
        return item;
    }

    function renderSourceFinderHit(name, count) {
        const item = document.createElement("li");
        item.className = "source-hit";

        const meta = document.createElement("div");
        meta.className = "source-hit-meta";

        const title = document.createElement("strong");
        title.textContent = name;

        const variants = document.createElement("span");
        variants.className = "muted";
        variants.textContent = formatNumber(count) + " variants in catalog";

        meta.append(title, variants);

        const link = document.createElement("a");
        link.className = "button";
        link.href = githubSearchUrl(name);
        link.target = "_blank";
        link.rel = "noopener noreferrer";
        link.textContent = "Search on GitHub";

        item.append(meta, link);
        return item;
    }

    function githubSearchUrl(manufacturer) {
        const query = manufacturer + " path:filaments";
        return GITHUB_REPO + "/search?q=" + encodeURIComponent(query) + "&type=code";
    }

    function setStatus(message, isError) {
        elements.loadStatus.textContent = message;
        elements.loadStatus.parentElement.classList.toggle("status-error", Boolean(isError));
    }

    function bindCopyButtons() {
        document.querySelectorAll("[data-copy]").forEach(function (button) {
            button.addEventListener("click", async function () {
                const target = document.querySelector(button.getAttribute("data-copy"));
                if (!target) {
                    return;
                }
                const text = target.textContent.trim() || EXTERNAL_DB_URL;
                const previous = button.textContent;
                try {
                    await copyText(text);
                    button.textContent = "Copied";
                } catch (error) {
                    button.textContent = "Copy failed";
                }
                window.setTimeout(function () {
                    button.textContent = previous;
                }, 1200);
            });
        });
    }

    async function copyText(text) {
        if (navigator.clipboard && window.isSecureContext) {
            try {
                await navigator.clipboard.writeText(text);
                return;
            } catch (error) {
                // Fall back for automated browsers and strict clipboard prompts.
            }
        }

        const textarea = document.createElement("textarea");
        textarea.value = text;
        textarea.setAttribute("readonly", "");
        textarea.style.position = "fixed";
        textarea.style.opacity = "0";
        document.body.appendChild(textarea);
        textarea.select();
        const copied = document.execCommand("copy");
        textarea.remove();

        if (!copied) {
            throw new Error("Copy command failed");
        }
    }
})();
