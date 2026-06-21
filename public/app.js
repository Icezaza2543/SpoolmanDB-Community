(function () {
    "use strict";

    const EXTERNAL_DB_URL = "https://icezaza2543.github.io/SpoolmanDB-Community/";
    const MAX_RENDERED_ROWS = 150;
    const MAX_QUALITY_ROWS = 140;
    const GITHUB_REPO = "https://github.com/Icezaza2543/SpoolmanDB-Community";
    const SOURCE_FINDER_LIMIT = 8;
    const SCHEMA_CONFIG = {
        filament: {
            title: "Filament source schema",
            file: "filaments.schema.json",
            paths: ["filaments.schema.json", "../filaments.schema.json"],
        },
        material: {
            title: "Material defaults schema",
            file: "materials.schema.json",
            paths: ["materials.schema.json", "../materials.schema.json"],
        },
    };

    const state = {
        filaments: [],
        materials: [],
        matches: [],
        manufacturerCounts: new Map(),
        qualityIssues: [],
        qualityMetrics: null,
        schemas: {},
        schemaPaths: {},
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
        qualitySummary: document.querySelector("#quality-summary"),
        qualityFilter: document.querySelector("#quality-filter"),
        qualityMeta: document.querySelector("#quality-meta"),
        qualityIssuesBody: document.querySelector("#quality-issues-body"),
        schemaChoice: document.querySelector("#schema-choice"),
        schemaStatus: document.querySelector("#schema-status"),
        schemaSummary: document.querySelector("#schema-summary"),
        schemaFieldsBody: document.querySelector("#schema-fields-body"),
        schemaOpenLink: document.querySelector("#schema-open-link"),
        schemaCopyUrl: document.querySelector("#schema-copy-url"),
        contributorSourceInput: document.querySelector("#contributor-source-input"),
        contributorSourceResults: document.querySelector("#contributor-source-results"),
        navLinks: document.querySelectorAll(".nav-link"),
        heroSection: document.querySelector(".hero"),
        statsGrid: document.querySelector(".stats-grid"),
        explorerSection: document.querySelector("#explorer"),
        qualitySection: document.querySelector("#quality"),
        schemaSection: document.querySelector("#schema"),
        contributeSection: document.querySelector("#contribute"),
    };

    document.addEventListener("DOMContentLoaded", init);

    function handleRouting() {
        const hash = window.location.hash || "#explorer";
        const validHashes = ["#explorer", "#quality", "#schema", "#contribute"];
        const activeHash = validHashes.includes(hash) ? hash : "#explorer";

        if (elements.heroSection) {
            elements.heroSection.style.display = activeHash === "#explorer" ? "" : "none";
        }
        if (elements.statsGrid) {
            elements.statsGrid.style.display = activeHash === "#explorer" ? "" : "none";
        }

        const sections = {
            "#explorer": elements.explorerSection,
            "#quality": elements.qualitySection,
            "#schema": elements.schemaSection,
            "#contribute": elements.contributeSection
        };

        Object.entries(sections).forEach(([id, sectionEl]) => {
            if (sectionEl) {
                sectionEl.style.display = activeHash === id ? "" : "none";
            }
        });

        elements.navLinks.forEach((link) => {
            const linkHash = link.getAttribute("href");
            if (linkHash === activeHash) {
                link.classList.add("active");
            } else {
                link.classList.remove("active");
            }
        });

        window.scrollTo(0, 0);
    }

    async function init() {
        window.addEventListener("hashchange", handleRouting);
        handleRouting();

        bindCopyButtons();
        bindQualityDashboard();
        bindSchemaViewer();
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
            computeAndRenderQuality();
            loadSchemas();
            setStatus("Loaded " + formatNumber(state.filaments.length) + " filament variants.");
        } catch (error) {
            setStatus("Could not load JSON data. Serve this page through GitHub Pages or a local web server.", true);
            elements.resultsBody.replaceChildren(emptyRow("Data failed to load: " + error.message));
            renderQualityError("Data failed to load: " + error.message);
            renderContributorSourceFinder("Data not loaded. Serve this page through GitHub Pages or a local web server.");
            loadSchemas();
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

    async function fetchJsonWithPath(paths) {
        const errors = [];

        for (const path of paths) {
            try {
                const response = await fetch(path, { cache: "no-store" });
                if (!response.ok) {
                    throw new Error(path + " returned HTTP " + response.status);
                }
                return {
                    data: await response.json(),
                    path,
                };
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

    function bindQualityDashboard() {
        if (!elements.qualityFilter) {
            return;
        }

        elements.qualityFilter.addEventListener("change", renderQualityIssues);
    }

    function computeAndRenderQuality() {
        const materialSet = new Set(state.materials.map((item) => item.material).filter(Boolean));
        const idCounts = new Map();
        const issueRecords = new Map();
        const metrics = {
            total: state.filaments.length,
            actionable: 0,
            duplicateIds: 0,
            unknownMaterials: 0,
            invalidColors: 0,
            missingSize: 0,
            missingTemps: 0,
            missingProductIds: 0,
            multicolor: 0,
            tempCoverage: 0,
            productIdCoverage: 0,
        };

        state.filaments.forEach(function (item) {
            if (!item.id) {
                return;
            }
            idCounts.set(item.id, (idCounts.get(item.id) || 0) + 1);
        });

        state.qualityIssues = [];
        state.filaments.forEach(function (item) {
            if (item.id && idCounts.get(item.id) > 1) {
                addQualityIssue(item, "duplicate-id", "ID appears " + idCounts.get(item.id) + " times.");
            }
            if (item.material && !materialSet.has(item.material)) {
                addQualityIssue(item, "unknown-material", "No shared material default is published for this material.");
            }
            if (!hasValidColor(item)) {
                addQualityIssue(item, "invalid-color", "Missing or invalid color hex data.");
            }
            if (!isPositiveNumber(item.weight) || !isPositiveNumber(item.diameter)) {
                addQualityIssue(item, "missing-size", "Weight or diameter is missing or not positive.");
            }
            if (!hasTemperatureData(item)) {
                addQualityIssue(item, "missing-temp", "Extruder or bed temperature data is missing.");
            }
            if (!hasProductIds(item)) {
                addQualityIssue(item, "missing-product-id", "No SKU, EAN, or refill EAN is published for this variant.");
            }
            if (Array.isArray(item.color_hexes) && item.color_hexes.length > 0) {
                addQualityIssue(item, "multicolor", "Multi-color row. Verify color order and direction from source evidence.");
            }
        });

        state.qualityIssues.forEach(function (issue) {
            const categoryKey = issue.category + "::" + issue.id;
            if (!issueRecords.has(categoryKey)) {
                issueRecords.set(categoryKey, true);
                if (issue.category === "duplicate-id") {
                    metrics.duplicateIds += 1;
                } else if (issue.category === "unknown-material") {
                    metrics.unknownMaterials += 1;
                } else if (issue.category === "invalid-color") {
                    metrics.invalidColors += 1;
                } else if (issue.category === "missing-size") {
                    metrics.missingSize += 1;
                } else if (issue.category === "missing-temp") {
                    metrics.missingTemps += 1;
                } else if (issue.category === "missing-product-id") {
                    metrics.missingProductIds += 1;
                } else if (issue.category === "multicolor") {
                    metrics.multicolor += 1;
                }
            }
        });

        metrics.actionable = state.qualityIssues.filter(function (issue) {
            return issue.severity !== "Info";
        }).length;
        metrics.tempCoverage = percentLabel(
            state.filaments.filter(hasTemperatureData).length,
            metrics.total
        );
        metrics.productIdCoverage = percentLabel(
            state.filaments.filter(hasProductIds).length,
            metrics.total
        );

        state.qualityMetrics = metrics;
        renderQualitySummary();
        renderQualityIssues();
    }

    function addQualityIssue(item, category, detail) {
        state.qualityIssues.push({
            category,
            severity: qualitySeverity(category),
            id: item.id || "-",
            manufacturer: item.manufacturer || "-",
            name: item.name || "Unnamed filament",
            detail,
        });
    }

    function renderQualitySummary() {
        if (!elements.qualitySummary || !state.qualityMetrics) {
            return;
        }

        const metrics = state.qualityMetrics;
        const status = metrics.actionable === 0 ? "Ready" : formatNumber(metrics.actionable);
        const statusLabel = metrics.actionable === 0 ? "No actionable issues" : "Actionable issues";
        const cards = [
            ["Quality status", status, statusLabel],
            ["No defaults", formatNumber(metrics.unknownMaterials), "Not in materials.json"],
            ["Invalid colors", formatNumber(metrics.invalidColors), "Missing or invalid hex"],
            ["Temp coverage", metrics.tempCoverage, "Extruder and bed data"],
            ["Rows with SKU/EAN", metrics.productIdCoverage, "Product ID coverage"],
            ["Multi-color rows", formatNumber(metrics.multicolor), "Informational review signal"],
        ];

        elements.qualitySummary.replaceChildren(renderMetricCards(cards));
    }

    function renderQualityIssues() {
        if (!elements.qualityIssuesBody || !elements.qualityMeta) {
            return;
        }

        const filter = elements.qualityFilter ? elements.qualityFilter.value : "actionable";
        const filtered = filterQualityIssues(filter);
        const visible = filtered.slice(0, MAX_QUALITY_ROWS);
        const fragment = document.createDocumentFragment();

        if (visible.length === 0) {
            fragment.appendChild(emptyQualityRow("No matching quality signals for this filter."));
        } else {
            visible.forEach(function (issue) {
                fragment.appendChild(renderQualityRow(issue));
            });
        }

        elements.qualityIssuesBody.replaceChildren(fragment);
        elements.qualityMeta.textContent =
            "Showing " + formatNumber(visible.length) + " of " + formatNumber(filtered.length) + " " + qualityFilterLabel(filter) + ".";
    }

    function filterQualityIssues(filter) {
        if (filter === "all") {
            return state.qualityIssues;
        }
        if (filter === "actionable") {
            return state.qualityIssues.filter(function (issue) {
                return issue.severity !== "Info";
            });
        }
        return state.qualityIssues.filter(function (issue) {
            return issue.category === filter;
        });
    }

    function renderQualityRow(issue) {
        const row = document.createElement("tr");
        row.appendChild(cell(severityTag(issue.severity)));
        row.appendChild(textCell(qualityCategoryLabel(issue.category)));

        const filament = document.createElement("td");
        const name = document.createElement("div");
        name.className = "filament-name";
        name.textContent = issue.manufacturer + " / " + issue.name;
        const id = document.createElement("div");
        id.className = "muted";
        id.textContent = issue.id;
        filament.append(name, id);
        row.appendChild(filament);

        row.appendChild(textCell(issue.detail));
        return row;
    }

    function severityTag(severity) {
        const span = document.createElement("span");
        span.className = "tag severity-" + severity.toLowerCase();
        span.textContent = severity;
        return span;
    }

    function emptyQualityRow(message) {
        const row = document.createElement("tr");
        const td = document.createElement("td");
        td.colSpan = 4;
        td.textContent = message;
        row.appendChild(td);
        return row;
    }

    function renderQualityError(message) {
        if (elements.qualitySummary) {
            elements.qualitySummary.replaceChildren(renderMetricCards([["Quality status", "Error", "Data not available"]]));
        }
        if (elements.qualityIssuesBody) {
            elements.qualityIssuesBody.replaceChildren(emptyQualityRow(message));
        }
        if (elements.qualityMeta) {
            elements.qualityMeta.textContent = "Quality checks could not run.";
        }
    }

    function qualitySeverity(category) {
        if (category === "duplicate-id" || category === "invalid-color") {
            return "Critical";
        }
        if (category === "missing-size") {
            return "Warning";
        }
        return "Info";
    }

    function qualityCategoryLabel(category) {
        const labels = {
            "duplicate-id": "Duplicate ID",
            "unknown-material": "No material default",
            "invalid-color": "Invalid color",
            "missing-size": "Missing size data",
            "missing-temp": "Missing temperatures",
            "missing-product-id": "Missing SKU/EAN",
            multicolor: "Multi-color row",
        };
        return labels[category] || category;
    }

    function qualityFilterLabel(filter) {
        if (filter === "all") {
            return "tracked signals";
        }
        if (filter === "actionable") {
            return "actionable issues";
        }
        return qualityCategoryLabel(filter).toLowerCase() + " signals";
    }

    function hasValidColor(item) {
        if (item.color_hex) {
            return isHex(item.color_hex);
        }
        if (Array.isArray(item.color_hexes) && item.color_hexes.length > 0) {
            return item.color_hexes.every(isHex);
        }
        return false;
    }

    function hasTemperatureData(item) {
        return Boolean(item.extruder_temp || validRange(item.extruder_temp_range)) &&
            Boolean(item.bed_temp || validRange(item.bed_temp_range));
    }

    function validRange(value) {
        return Array.isArray(value) && value.length === 2 && value.every(function (item) {
            return item !== undefined && item !== null && item !== "";
        });
    }

    function isPositiveNumber(value) {
        return typeof value === "number" && value > 0;
    }

    function percentLabel(count, total) {
        if (!total) {
            return "0%";
        }
        const rounded = Math.round((count / total) * 100);
        if (rounded === 0 && count > 0) {
            return "<1%";
        }
        return rounded + "%";
    }

    async function loadSchemas() {
        if (!elements.schemaChoice) {
            return;
        }

        setSchemaStatus("Loading source schemas...");
        try {
            const [filament, material] = await Promise.all([
                fetchJsonWithPath(SCHEMA_CONFIG.filament.paths),
                fetchJsonWithPath(SCHEMA_CONFIG.material.paths),
            ]);
            state.schemas.filament = filament.data;
            state.schemas.material = material.data;
            state.schemaPaths.filament = filament.path;
            state.schemaPaths.material = material.path;
            renderSchemaViewer();
        } catch (error) {
            setSchemaStatus("Schema data failed to load: " + error.message, true);
            renderSchemaError("Could not load schema JSON.");
        }
    }

    function bindSchemaViewer() {
        if (!elements.schemaChoice) {
            return;
        }

        elements.schemaChoice.addEventListener("change", renderSchemaViewer);
        updateSchemaLinks();
    }

    function renderSchemaViewer() {
        const kind = elements.schemaChoice ? elements.schemaChoice.value : "filament";
        const schema = state.schemas[kind];
        updateSchemaLinks();

        if (!schema) {
            renderSchemaError("Schema is still loading.");
            return;
        }

        const fields = collectSchemaFields(schema);
        renderSchemaSummary(schema, fields);
        renderSchemaFields(fields);
        setSchemaStatus(SCHEMA_CONFIG[kind].title + " loaded from " + (state.schemaPaths[kind] || SCHEMA_CONFIG[kind].file) + ".");
    }

    function updateSchemaLinks() {
        if (!elements.schemaChoice) {
            return;
        }
        const kind = elements.schemaChoice.value;
        const config = SCHEMA_CONFIG[kind];
        const path = state.schemaPaths[kind] || config.file;
        const url = new URL(path, window.location.href).href;

        if (elements.schemaOpenLink) {
            elements.schemaOpenLink.href = path;
            elements.schemaOpenLink.textContent = "Open " + config.file;
        }
        if (elements.schemaCopyUrl) {
            elements.schemaCopyUrl.textContent = url;
        }
    }

    function renderSchemaSummary(schema, fields) {
        if (!elements.schemaSummary) {
            return;
        }

        const topLevelProperties = topLevelPropertyCount(schema);
        const requiredFields = fields.filter(function (field) {
            return field.required;
        }).length;
        const cards = [
            ["Root type", schemaTypeName(schema), "Schema root"],
            ["Top properties", formatNumber(topLevelProperties), "Immediate fields"],
            ["Required fields", formatNumber(requiredFields), "Across nested objects"],
            ["Field rows", formatNumber(fields.length), "Rendered paths"],
        ];
        elements.schemaSummary.replaceChildren(renderMetricCards(cards));
    }

    function renderSchemaFields(fields) {
        if (!elements.schemaFieldsBody) {
            return;
        }

        const visible = fields.slice(0, 120);
        const fragment = document.createDocumentFragment();

        if (visible.length === 0) {
            fragment.appendChild(emptySchemaRow("No schema fields found."));
        } else {
            visible.forEach(function (field) {
                const row = document.createElement("tr");
                row.appendChild(schemaCell(field.path, "schema-path"));
                row.appendChild(cell(schemaRequiredTag(field.required)));
                row.appendChild(schemaCell(field.type, "schema-type"));
                row.appendChild(schemaCell(field.note || "-", "schema-note-cell"));
                fragment.appendChild(row);
            });
        }

        elements.schemaFieldsBody.replaceChildren(fragment);
    }

    function collectSchemaFields(schema) {
        const fields = [];
        walkSchemaNode(schema, "", false, fields, new Set());
        return fields.filter(function (field) {
            return field.path;
        });
    }

    function walkSchemaNode(node, path, required, fields, seen) {
        if (!node || typeof node !== "object") {
            return;
        }

        const seenKey = path + "::" + schemaTypeName(node);
        if (seen.has(seenKey)) {
            return;
        }
        seen.add(seenKey);

        if (path && !(path.endsWith("[]") && node.properties)) {
            fields.push({
                path,
                required,
                type: describeSchemaNode(node),
                note: node.$comment || "",
            });
        }

        if (node.type === "array" && node.items) {
            walkSchemaNode(node.items, path ? path + "[]" : "[]", false, fields, seen);
            return;
        }

        if (!node.properties) {
            return;
        }

        const requiredSet = new Set(Array.isArray(node.required) ? node.required : []);
        Object.keys(node.properties).forEach(function (name) {
            walkSchemaNode(node.properties[name], path ? path + "." + name : name, requiredSet.has(name), fields, seen);
        });
    }

    function describeSchemaNode(node) {
        const parts = [];
        parts.push(schemaTypeName(node));

        if (Array.isArray(node.enum)) {
            parts.push("enum: " + node.enum.map(function (value) {
                return value === null ? "null" : String(value);
            }).join(", "));
        }
        if (node.oneOf) {
            parts.push("oneOf " + node.oneOf.length + " variants");
        }
        if (node.pattern) {
            parts.push("pattern " + node.pattern);
        }
        if (node.format) {
            parts.push("format " + node.format);
        }
        if (node.minItems !== undefined) {
            parts.push("minItems " + node.minItems);
        }
        if (node.maxItems !== undefined) {
            parts.push("maxItems " + node.maxItems);
        }
        if (node.uniqueItems) {
            parts.push("unique");
        }
        if (node.minimum !== undefined) {
            parts.push("min " + node.minimum);
        }
        if (node.exclusiveMinimum !== undefined) {
            parts.push("exclusiveMin " + node.exclusiveMinimum);
        }

        return parts.join(" / ");
    }

    function schemaTypeName(node) {
        if (Array.isArray(node.type)) {
            return node.type.join(" | ");
        }
        if (node.type) {
            if (node.type === "array" && node.items) {
                return "array of " + schemaTypeName(node.items);
            }
            return node.type;
        }
        if (node.enum) {
            return "enum";
        }
        if (node.oneOf) {
            return "oneOf";
        }
        return "schema";
    }

    function topLevelPropertyCount(schema) {
        if (schema.properties) {
            return Object.keys(schema.properties).length;
        }
        if (schema.items && schema.items.properties) {
            return Object.keys(schema.items.properties).length;
        }
        return 0;
    }

    function schemaCell(text, className) {
        const td = document.createElement("td");
        td.className = className;
        td.textContent = text || "-";
        return td;
    }

    function schemaRequiredTag(required) {
        const span = document.createElement("span");
        span.className = required ? "tag tag-orange" : "tag";
        span.textContent = required ? "Required" : "Optional";
        return span;
    }

    function emptySchemaRow(message) {
        const row = document.createElement("tr");
        const td = document.createElement("td");
        td.colSpan = 4;
        td.textContent = message;
        row.appendChild(td);
        return row;
    }

    function renderSchemaError(message) {
        if (elements.schemaSummary) {
            elements.schemaSummary.replaceChildren(renderMetricCards([["Schema status", "Waiting", "Source schemas"]]));
        }
        if (elements.schemaFieldsBody) {
            elements.schemaFieldsBody.replaceChildren(emptySchemaRow(message));
        }
    }

    function setSchemaStatus(message, isError) {
        if (!elements.schemaStatus) {
            return;
        }
        elements.schemaStatus.textContent = message;
        elements.schemaStatus.classList.toggle("status-text-error", Boolean(isError));
    }

    function renderMetricCards(cards) {
        const fragment = document.createDocumentFragment();
        cards.forEach(function (card) {
            const article = document.createElement("article");
            article.className = "stat-card";
            const label = document.createElement("span");
            label.textContent = card[0];
            const value = document.createElement("strong");
            value.textContent = card[1];
            const detail = document.createElement("small");
            detail.textContent = card[2];
            article.append(label, value, detail);
            fragment.appendChild(article);
        });
        return fragment;
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
        if (!isError && message.startsWith("Loaded")) {
            elements.loadStatus.parentElement.style.display = "none";
        } else {
            elements.loadStatus.parentElement.style.display = "";
        }
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
