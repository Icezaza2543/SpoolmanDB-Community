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
        homeCharts: [],
        dashboardMetrics: null,
        homeInitialized: false,
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
        homeSection: document.querySelector("#home"),
        explorerSection: document.querySelector("#explorer"),
        qualitySection: document.querySelector("#quality"),
        schemaSection: document.querySelector("#schema"),
        contributeSection: document.querySelector("#contribute"),
        chartKnowledge: document.querySelector("#knowledge-graph-chart"),
        chartMaterial: document.querySelector("#material-composition-chart"),
        chartManufacturer: document.querySelector("#top-manufacturers-chart"),
        chartSpool: document.querySelector("#spool-type-chart"),
        chartColor: document.querySelector("#color-spectrum-chart"),
    };

    document.addEventListener("DOMContentLoaded", init);

    function handleRouting() {
        const hash = window.location.hash || "#home";
        const validHashes = ["#home", "#explorer", "#quality", "#schema", "#contribute"];
        const activeHash = validHashes.includes(hash) ? hash : "#home";

        const sections = {
            "#home": elements.homeSection,
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

        if (activeHash === "#home") {
            if (!state.homeInitialized) {
                if (state.filaments.length > 0) {
                    initHomeDashboard();
                }
            } else {
                resizeHomeCharts();
            }
        }

        window.scrollTo(0, 0);
    }

    async function init() {
        window.addEventListener("hashchange", handleRouting);
        
        let resizeTimeout;
        window.addEventListener("resize", function () {
            clearTimeout(resizeTimeout);
            resizeTimeout = setTimeout(function () {
                if (window.location.hash === "#home" || !window.location.hash) {
                    resizeHomeCharts();
                }
            }, 100);
        });

        bindCopyButtons();
        bindQualityDashboard();
        bindSchemaViewer();
        bindContributorHelper();
        elements.filters.addEventListener("input", renderFilteredResults);
        elements.filters.addEventListener("reset", function () {
            window.setTimeout(renderFilteredResults, 0);
        });

        // Initial route handling
        handleRouting();

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

            buildDashboardMetrics();
            handleRouting();

            setStatus("Loaded " + formatNumber(state.filaments.length) + " filament variants.");
        } catch (error) {
            setStatus("Could not load JSON data. Serve this page through GitHub Pages or a local web server.", true);
            elements.resultsBody.replaceChildren(emptyRow("Data failed to load: " + error.message));
            renderQualityError("Data failed to load: " + error.message);
            renderContributorSourceFinder("Data not loaded. Serve this page through GitHub Pages or a local web server.");
            loadSchemas();
        }
    }

    function hexToHsl(hex) {
        if (!hex || hex.length < 6) return { h: 0, s: 0, l: 0 };
        const r = parseInt(hex.substring(0, 2), 16) / 255;
        const g = parseInt(hex.substring(2, 4), 16) / 255;
        const b = parseInt(hex.substring(4, 6), 16) / 255;
        const max = Math.max(r, g, b), min = Math.min(r, g, b);
        let h, s, l = (max + min) / 2;
        if (max === min) {
            h = s = 0;
        } else {
            const d = max - min;
            s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
            switch (max) {
                case r: h = (g - b) / d + (g < b ? 6 : 0); break;
                case g: h = (b - r) / d + 2; break;
                case b: h = (r - g) / d + 4; break;
            }
            h /= 6;
        }
        return {
            h: Math.round(h * 360),
            s: Math.round(s * 100),
            l: Math.round(l * 100)
        };
    }

    function getColorFamily(h, s, l) {
        if (l < 15) return "Black";
        if (l > 85) return "White";
        if (s < 10) return "Grey";
        if (h >= 345 || h < 15) return "Red";
        if (h >= 15 && h < 45) {
            return l < 45 ? "Brown" : "Orange";
        }
        if (h >= 45 && h < 75) return "Yellow";
        if (h >= 75 && h < 165) return "Green";
        if (h >= 165 && h < 255) return "Blue";
        if (h >= 255 && h < 315) return "Purple";
        return "Pink";
    }

    function normalizeSpoolType(type) {
        if (!type || type === "null" || type === "none") return "Unknown";
        return type.charAt(0).toUpperCase() + type.slice(1);
    }

    function buildDashboardMetrics() {
        if (state.dashboardMetrics) return;

        const materialMap = new Map();
        const mfgMap = new Map();
        const spoolMap = new Map();
        const uniqueColorSet = new Set();
        const colorPoints = [];

        state.filaments.forEach((item) => {
            const mat = item.material || "Unknown";
            materialMap.set(mat, (materialMap.get(mat) || 0) + 1);

            const mfg = item.manufacturer || "Unknown";
            mfgMap.set(mfg, (mfgMap.get(mfg) || 0) + 1);

            const spool = normalizeSpoolType(item.spool_type);
            spoolMap.set(spool, (spoolMap.get(spool) || 0) + 1);

            const hexes = item.color_hex ? [item.color_hex] : (item.color_hexes || []);
            hexes.forEach((hex) => {
                const hexClean = String(hex).toUpperCase();
                if (!isHex(hexClean)) return;
                const key = hexClean + "::" + mfg + "::" + mat;
                if (!uniqueColorSet.has(key)) {
                    uniqueColorSet.add(key);
                    const hsl = hexToHsl(hexClean);
                    colorPoints.push({
                        hex: hexClean,
                        h: hsl.h,
                        s: hsl.s,
                        l: hsl.l,
                        name: item.name,
                        manufacturer: mfg,
                        material: mat
                    });
                }
            });
        });

        const sortedMfg = Array.from(mfgMap.entries()).sort((a, b) => b[1] - a[1]);

        const nodes = [];
        const edges = new Set();
        const nodeMap = new Map();

        const addNode = (id, name, val, category) => {
            if (!nodeMap.has(id)) {
                nodeMap.set(id, nodes.length);
                nodes.push({
                    id,
                    name,
                    value: val,
                    symbolSize: val,
                    category
                });
            } else {
                nodes[nodeMap.get(id)].value += val;
            }
        };

        const top25Mfg = sortedMfg.slice(0, 25);
        if (top25Mfg.length > 0) {
            const maxVal = top25Mfg[0][1];
            top25Mfg.forEach(([name, count]) => {
                const size = Math.round(15 + (count / maxVal) * 35);
                addNode("mfg_" + name, name, size, 0);
            });
        }

        const sortedMat = Array.from(materialMap.entries()).sort((a, b) => b[1] - a[1]);
        const topMaterials = sortedMat.slice(0, 10);
        if (topMaterials.length > 0) {
            const maxVal = topMaterials[0][1];
            topMaterials.forEach(([name, count]) => {
                const size = Math.round(12 + (count / maxVal) * 28);
                addNode("mat_" + name, name, size, 1);
            });
        }

        const colorFamilies = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Brown", "Black", "White", "Grey", "Clear"];
        colorFamilies.forEach((name) => {
            addNode("col_" + name, name, 18, 2);
        });

        const spoolTypes = ["Plastic", "Cardboard", "Metal", "Refill", "Unknown"];
        spoolTypes.forEach((name) => {
            addNode("spl_" + name, name, 15, 3);
        });

        state.filaments.forEach((item) => {
            const mfg = item.manufacturer || "Unknown";
            const mat = item.material || "Unknown";
            const spool = normalizeSpoolType(item.spool_type);

            if (top25Mfg.some(e => e[0] === mfg) && topMaterials.some(e => e[0] === mat)) {
                edges.add("mfg_" + mfg + "->mat_" + mat);
                edges.add("mat_" + mat + "->spl_" + spool);

                const hexes = item.color_hex ? [item.color_hex] : (item.color_hexes || []);
                hexes.forEach((hex) => {
                    const hexClean = String(hex).toUpperCase();
                    if (!isHex(hexClean)) return;
                    const hsl = hexToHsl(hexClean);
                    const family = getColorFamily(hsl.h, hsl.s, hsl.l);
                    edges.add("mat_" + mat + "->col_" + family);
                });
            }
        });

        const graphLinks = Array.from(edges).map((linkStr) => {
            const [source, target] = linkStr.split("->");
            return { source, target };
        });

        state.dashboardMetrics = {
            materials: sortedMat,
            manufacturers: sortedMfg,
            spools: Array.from(spoolMap.entries()).sort((a, b) => b[1] - a[1]),
            colorPoints,
            graph: {
                nodes,
                links: graphLinks
            }
        };
    }

    function renderKnowledgeGraphChart(chart, metrics) {
        const option = {
            backgroundColor: "transparent",
            tooltip: {
                trigger: "item",
                formatter: function (params) {
                    if (params.dataType === "node") {
                        const catLabels = ["Manufacturer", "Material", "Color Family", "Spool Type"];
                        return `<strong>${params.name}</strong><br/>Type: ${catLabels[params.data.category]}`;
                    }
                    return `Connection: ${params.data.source.replace(/^\w+_/, "")} → ${params.data.target.replace(/^\w+_/, "")}`;
                },
                backgroundColor: "rgba(24, 24, 30, 0.95)",
                borderColor: "rgba(160, 132, 232, 0.3)",
                textStyle: { color: "#f4f4f5" }
            },
            legend: [{
                data: ["Manufacturers", "Materials", "Color Families", "Spool Types"],
                textStyle: { color: "#9f9fbf" },
                bottom: 10
            }],
            series: [{
                type: "graph",
                layout: "force",
                data: metrics.graph.nodes,
                links: metrics.graph.links,
                categories: [
                    { name: "Manufacturers", itemStyle: { color: "#a084e8" } },
                    { name: "Materials", itemStyle: { color: "#4ec5a5" } },
                    { name: "Color Families", itemStyle: { color: "#f38ba8" } },
                    { name: "Spool Types", itemStyle: { color: "#f9e2af" } }
                ],
                roam: true,
                label: {
                    show: true,
                    position: "right",
                    formatter: function(params) {
                        return params.name.replace(/^\w+_/, "");
                    },
                    color: "#d9d9e3",
                    fontSize: 10,
                    minMargin: 5
                },
                force: {
                    repulsion: 150,
                    gravity: 0.1,
                    edgeLength: 70,
                    layoutAnimation: true
                },
                lineStyle: {
                    color: "rgba(160, 132, 232, 0.15)",
                    width: 1,
                    curveness: 0.1
                },
                emphasis: {
                    focus: "adjacency",
                    lineStyle: {
                        width: 3,
                        color: "rgba(160, 132, 232, 0.6)"
                    }
                }
            }]
        };
        chart.setOption(option);
    }

    function renderMaterialCompositionChart(chart, metrics) {
        const sortedData = metrics.materials;
        const mainData = [];
        let otherSum = 0;
        sortedData.forEach(([name, count], index) => {
            if (index < 7) {
                mainData.push({ name, value: count });
            } else {
                otherSum += count;
            }
        });
        if (otherSum > 0) {
            mainData.push({ name: "Other", value: otherSum });
        }

        const option = {
            backgroundColor: "transparent",
            tooltip: {
                trigger: "item",
                formatter: "{b}: {c} ({d}%)",
                backgroundColor: "rgba(24, 24, 30, 0.95)",
                borderColor: "rgba(160, 132, 232, 0.3)",
                textStyle: { color: "#f4f4f5" }
            },
            series: [{
                name: "Materials",
                type: "pie",
                radius: ["40%", "70%"],
                avoidLabelOverlap: true,
                itemStyle: {
                    borderRadius: 8,
                    borderColor: "#101014",
                    borderWidth: 2
                },
                label: {
                    show: true,
                    color: "#d9d9e3",
                    fontSize: 11
                },
                labelLine: {
                    lineStyle: { color: "rgba(160, 132, 232, 0.3)" }
                },
                data: mainData
            }]
        };
        chart.setOption(option);
    }

    function renderTopManufacturersChart(chart, metrics) {
        const topData = metrics.manufacturers.slice(0, 12).reverse();
        const yAxisData = topData.map(e => e[0]);
        const seriesData = topData.map(e => e[1]);

        const option = {
            backgroundColor: "transparent",
            tooltip: {
                trigger: "axis",
                axisPointer: { type: "shadow" },
                backgroundColor: "rgba(24, 24, 30, 0.95)",
                borderColor: "rgba(160, 132, 232, 0.3)",
                textStyle: { color: "#f4f4f5" }
            },
            grid: {
                left: "3%",
                right: "4%",
                bottom: "3%",
                top: "3%",
                containLabel: true
            },
            xAxis: {
                type: "value",
                splitLine: { lineStyle: { color: "rgba(160, 132, 232, 0.1)" } },
                axisLabel: { color: "#9f9fbf" }
            },
            yAxis: {
                type: "category",
                data: yAxisData,
                axisLabel: { color: "#d9d9e3", fontSize: 11 }
            },
            series: [{
                name: "Variants",
                type: "bar",
                data: seriesData,
                itemStyle: {
                    color: {
                        type: "linear",
                        x: 0, y: 0, x2: 1, y2: 0,
                        colorStops: [
                            { offset: 0, color: "rgba(160, 132, 232, 0.2)" },
                            { offset: 1, color: "#a084e8" }
                        ]
                    },
                    borderRadius: [0, 4, 4, 0]
                }
            }]
        };
        chart.setOption(option);
    }

    function renderSpoolTypeChart(chart, metrics) {
        const data = metrics.spools.map(([name, count]) => ({ name, value: count }));

        const option = {
            backgroundColor: "transparent",
            tooltip: {
                trigger: "item",
                formatter: "{b}: {c} ({d}%)",
                backgroundColor: "rgba(24, 24, 30, 0.95)",
                borderColor: "rgba(160, 132, 232, 0.3)",
                textStyle: { color: "#f4f4f5" }
            },
            series: [{
                name: "Spool Material",
                type: "pie",
                radius: ["0%", "65%"],
                avoidLabelOverlap: true,
                itemStyle: {
                    borderRadius: 6,
                    borderColor: "#101014",
                    borderWidth: 2
                },
                label: {
                    show: true,
                    color: "#d9d9e3",
                    fontSize: 11
                },
                labelLine: {
                    lineStyle: { color: "rgba(160, 132, 232, 0.3)" }
                },
                data: data
            }]
        };
        chart.setOption(option);
    }

    function renderColorSpectrumChart(chart, metrics) {
        const data = metrics.colorPoints.map(p => [
            p.h, 
            p.l, 
            "#" + p.hex, 
            p.name || "Unnamed", 
            p.manufacturer, 
            p.material
        ]);

        const option = {
            backgroundColor: "transparent",
            tooltip: {
                trigger: "item",
                formatter: function (params) {
                    const val = params.value;
                    return `<strong>${val[3]}</strong><br/>` +
                           `Hex: <span style="display:inline-block;width:12px;height:12px;background-color:${val[2]};border:1px solid #fff;border-radius:50%;margin-right:4px;vertical-align:middle;"></span>${val[2]}<br/>` +
                           `Maker: ${val[4]}<br/>` +
                           `Material: ${val[5]}`;
                },
                backgroundColor: "rgba(24, 24, 30, 0.95)",
                borderColor: "rgba(160, 132, 232, 0.3)",
                textStyle: { color: "#f4f4f5" }
            },
            xAxis: {
                type: "value",
                min: 0,
                max: 360,
                splitLine: { show: false },
                axisLabel: {
                    formatter: function (value) {
                        if (value === 0 || value === 360) return "Red";
                        if (value === 60) return "Yellow";
                        if (value === 120) return "Green";
                        if (value === 180) return "Cyan";
                        if (value === 240) return "Blue";
                        if (value === 300) return "Magenta";
                        return "";
                    },
                    color: "#9f9fbf"
                }
            },
            yAxis: {
                type: "value",
                min: 0,
                max: 100,
                splitLine: { lineStyle: { color: "rgba(160, 132, 232, 0.1)" } },
                name: "Lightness",
                nameTextStyle: { color: "#9f9fbf" },
                axisLabel: { color: "#9f9fbf" }
            },
            series: [{
                type: "scatter",
                data: data,
                symbolSize: 8,
                large: true,
                progressive: 500,
                progressiveThreshold: 2000,
                itemStyle: {
                    color: function (params) {
                        return params.value[2];
                    },
                    borderColor: "rgba(255, 255, 255, 0.2)",
                    borderWidth: 1
                }
            }]
        };
        chart.setOption(option);
    }

    function initHomeDashboard() {
        if (state.homeInitialized) return;
        if (typeof echarts === "undefined") {
            console.error("Apache ECharts library is not loaded.");
            return;
        }
        if (!state.dashboardMetrics) buildDashboardMetrics();

        if (elements.chartKnowledge) {
            const chart = echarts.init(elements.chartKnowledge);
            renderKnowledgeGraphChart(chart, state.dashboardMetrics);
            state.homeCharts.push(chart);
        }
        if (elements.chartMaterial) {
            const chart = echarts.init(elements.chartMaterial);
            renderMaterialCompositionChart(chart, state.dashboardMetrics);
            state.homeCharts.push(chart);
        }
        if (elements.chartManufacturer) {
            const chart = echarts.init(elements.chartManufacturer);
            renderTopManufacturersChart(chart, state.dashboardMetrics);
            state.homeCharts.push(chart);
        }
        if (elements.chartSpool) {
            const chart = echarts.init(elements.chartSpool);
            renderSpoolTypeChart(chart, state.dashboardMetrics);
            state.homeCharts.push(chart);
        }
        if (elements.chartColor) {
            const chart = echarts.init(elements.chartColor);
            renderColorSpectrumChart(chart, state.dashboardMetrics);
            state.homeCharts.push(chart);
        }

        state.homeInitialized = true;
    }

    function resizeHomeCharts() {
        state.homeCharts.forEach((chart) => {
            if (chart) {
                chart.resize();
            }
        });
    }

    function disposeHomeCharts() {
        state.homeCharts.forEach((chart) => {
            if (chart) {
                chart.dispose();
            }
        });
        state.homeCharts = [];
        state.homeInitialized = false;
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
