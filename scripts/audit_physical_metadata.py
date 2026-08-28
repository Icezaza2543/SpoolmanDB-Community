#!/usr/bin/env python3
"""Audit physical metadata in SpoolmanDB Community filament source files.

Detects suspicious source metadata before it becomes a factual data error:
1. Temperature plausibility & min/max consistency
2. Temperature-field swap heuristic (nozzle <-> bed)
3. Density plausibility & decimal errors
4. Package metadata & spool weight anomalies
5. Product identifier (SKU / EAN) duplicates & collisions (same-family, cross-family, cross-mfr)

Read-only, deterministic, standard library only.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import asdict, dataclass
import json
from pathlib import Path
import sys
from typing import Any, Dict, List, Optional, Tuple


@dataclass(frozen=True)
class AuditFinding:
    severity: str  # "HIGH" or "REVIEW"
    category: str  # "temperature", "temp_swap", "density", "package", "identifier"
    file: str
    manufacturer: str
    family: str
    field: str
    value: Any
    reason: str
    classification: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        if d["classification"] is None:
            del d["classification"]
        return d


def audit_temperatures(fil: Dict[str, Any], fname: str, mfr: str) -> List[AuditFinding]:
    findings: List[AuditFinding] = []
    name = fil.get("name", "<unnamed>")
    material = str(fil.get("material", "")).strip().upper()

    ext = fil.get("extruder_temp_range")
    bed = fil.get("bed_temp_range")
    single_ext = fil.get("extruder_temp")
    single_bed = fil.get("bed_temp")

    # Range checks for extruder
    if ext is not None:
        if isinstance(ext, list) and len(ext) == 2:
            emin, emax = ext
            if emin > emax:
                findings.append(
                    AuditFinding(
                        severity="HIGH",
                        category="temperature",
                        file=fname,
                        manufacturer=mfr,
                        family=name,
                        field="extruder_temp_range",
                        value=ext,
                        reason=f"Extruder min temperature ({emin}°C) > max ({emax}°C)",
                    )
                )
            if emax < 100 and material != "PCL":
                findings.append(
                    AuditFinding(
                        severity="HIGH",
                        category="temperature",
                        file=fname,
                        manufacturer=mfr,
                        family=name,
                        field="extruder_temp_range",
                        value=ext,
                        reason=f"Extruder max temperature ({emax}°C) is implausibly low (< 100°C)",
                    )
                )
    elif single_ext is not None and isinstance(single_ext, (int, float)):
        if single_ext < 100 and material != "PCL":
            findings.append(
                AuditFinding(
                    severity="HIGH",
                    category="temperature",
                    file=fname,
                    manufacturer=mfr,
                    family=name,
                    field="extruder_temp",
                    value=single_ext,
                    reason=f"Extruder temperature ({single_ext}°C) is implausibly low (< 100°C)",
                )
            )

    # Range checks for bed
    if bed is not None:
        if isinstance(bed, list) and len(bed) == 2:
            bmin, bmax = bed
            if bmin > bmax:
                findings.append(
                    AuditFinding(
                        severity="HIGH",
                        category="temperature",
                        file=fname,
                        manufacturer=mfr,
                        family=name,
                        field="bed_temp_range",
                        value=bed,
                        reason=f"Bed min temperature ({bmin}°C) > max ({bmax}°C)",
                    )
                )
            if bmin > 180:
                findings.append(
                    AuditFinding(
                        severity="HIGH",
                        category="temperature",
                        file=fname,
                        manufacturer=mfr,
                        family=name,
                        field="bed_temp_range",
                        value=bed,
                        reason=f"Bed min temperature ({bmin}°C) is implausibly high (> 180°C)",
                    )
                )
    elif single_bed is not None and isinstance(single_bed, (int, float)):
        if single_bed > 180:
            findings.append(
                AuditFinding(
                    severity="HIGH",
                    category="temperature",
                    file=fname,
                    manufacturer=mfr,
                    family=name,
                    field="bed_temp",
                    value=single_bed,
                    reason=f"Bed temperature ({single_bed}°C) is implausibly high (> 180°C)",
                )
            )

    # Temperature-field swap heuristic
    eff_ext_max = ext[1] if (ext and len(ext) == 2) else single_ext
    eff_bed_min = bed[0] if (bed and len(bed) == 2) else single_bed

    if eff_ext_max is not None and eff_bed_min is not None and material != "PCL":
        if eff_ext_max <= 100 and eff_bed_min >= 150:
            findings.append(
                AuditFinding(
                    severity="HIGH",
                    category="temp_swap",
                    file=fname,
                    manufacturer=mfr,
                    family=name,
                    field="extruder/bed",
                    value={"extruder": ext or single_ext, "bed": bed or single_bed},
                    reason=(
                        f"Extruder ({eff_ext_max}°C) and Bed ({eff_bed_min}°C) ranges appear swapped: "
                        f"extruder <= 100°C while bed >= 150°C"
                    ),
                )
            )
        elif eff_ext_max < eff_bed_min and eff_ext_max < 140 and eff_bed_min >= 180:
            findings.append(
                AuditFinding(
                    severity="HIGH",
                    category="temp_swap",
                    file=fname,
                    manufacturer=mfr,
                    family=name,
                    field="extruder/bed",
                    value={"extruder": ext or single_ext, "bed": bed or single_bed},
                    reason=(
                        f"Extruder ({eff_ext_max}°C) is below Bed ({eff_bed_min}°C), indicating inverted temperature fields"
                    ),
                )
            )

    return findings


def audit_density(fil: Dict[str, Any], fname: str, mfr: str) -> List[AuditFinding]:
    findings: List[AuditFinding] = []
    name = fil.get("name", "<unnamed>")
    density = fil.get("density")

    if density is not None and isinstance(density, (int, float)):
        if density <= 0:
            findings.append(
                AuditFinding(
                    severity="HIGH",
                    category="density",
                    file=fname,
                    manufacturer=mfr,
                    family=name,
                    field="density",
                    value=density,
                    reason=f"Density must be positive (found {density} g/cm³)",
                )
            )
        elif density > 8.0:
            findings.append(
                AuditFinding(
                    severity="HIGH",
                    category="density",
                    file=fname,
                    manufacturer=mfr,
                    family=name,
                    field="density",
                    value=density,
                    reason=f"Density ({density} g/cm³) exceeds physical ceiling (> 8.0 g/cm³)",
                )
            )
        elif density < 0.2:
            findings.append(
                AuditFinding(
                    severity="REVIEW",
                    category="density",
                    file=fname,
                    manufacturer=mfr,
                    family=name,
                    field="density",
                    value=density,
                    reason=f"Density ({density} g/cm³) is suspiciously low (< 0.2 g/cm³; check for decimal scaling error)",
                )
            )

    return findings


def audit_package_weights(fil: Dict[str, Any], fname: str, mfr: str) -> List[AuditFinding]:
    findings: List[AuditFinding] = []
    name = fil.get("name", "<unnamed>")

    weights = fil.get("weights", [])
    valid_net_weights = []

    for w_obj in weights:
        if isinstance(w_obj, dict):
            w = w_obj.get("weight")
            sw = w_obj.get("spool_weight")
            is_refill = w_obj.get("is_refill") is True or w_obj.get("spool_type") == "refill"

            if w is not None and isinstance(w, (int, float)):
                if w <= 0:
                    findings.append(
                        AuditFinding(
                            severity="HIGH",
                            category="package",
                            file=fname,
                            manufacturer=mfr,
                            family=name,
                            field="weights.weight",
                            value=w,
                            reason=f"Filament net weight must be positive (found {w}g)",
                        )
                    )
                else:
                    valid_net_weights.append(w)

            if sw is not None and isinstance(sw, (int, float)):
                if sw < 0:
                    findings.append(
                        AuditFinding(
                            severity="HIGH",
                            category="package",
                            file=fname,
                            manufacturer=mfr,
                            family=name,
                            field="weights.spool_weight",
                            value=sw,
                            reason=f"Spool tare weight cannot be negative (found {sw}g)",
                        )
                    )
                elif sw == 0 and not is_refill:
                    findings.append(
                        AuditFinding(
                            severity="HIGH",
                            category="package",
                            file=fname,
                            manufacturer=mfr,
                            family=name,
                            field="weights.spool_weight",
                            value=sw,
                            reason=f"Physical spool tare weight cannot be 0g for non-refill packaging",
                        )
                    )
                elif sw > 0 and w is not None and isinstance(w, (int, float)) and w > 0:
                    if sw > w * 2.0 and sw > 1500:
                        findings.append(
                            AuditFinding(
                                severity="REVIEW",
                                category="package",
                                file=fname,
                                manufacturer=mfr,
                                family=name,
                                field="weights.spool_weight",
                                value={"weight": w, "spool_weight": sw},
                                reason=(
                                    f"Spool tare weight ({sw}g) is implausibly larger than filament net weight ({w}g); "
                                    f"check whether gross package weight was entered"
                                ),
                            )
                        )
        elif isinstance(w_obj, (int, float)):
            if w_obj <= 0:
                findings.append(
                    AuditFinding(
                        severity="HIGH",
                        category="package",
                        file=fname,
                        manufacturer=mfr,
                        family=name,
                        field="weights",
                        value=w_obj,
                        reason=f"Filament net weight must be positive (found {w_obj}g)",
                    )
                )

    return findings


def audit_identifiers(
    all_data: List[Tuple[str, str, Dict[str, Any]]]
) -> List[AuditFinding]:
    findings: List[AuditFinding] = []
    sku_locations: Dict[str, List[Tuple[str, str, str, str]]] = defaultdict(list)
    ean_locations: Dict[str, List[Tuple[str, str, str, str, str]]] = defaultdict(list)

    for fname, mfr, fil in all_data:
        fam_name = fil.get("name", "<unnamed>")
        for color in fil.get("colors", []):
            color_name = color.get("name", "<unnamed>")

            # Codes / SKUs
            for code in color.get("codes", []):
                if code:
                    sku_locations[str(code)].append((fname, mfr, fam_name, color_name))

            # EANs / GTINs
            for ean in color.get("eans", []):
                if ean:
                    ean_locations[str(ean)].append((fname, mfr, fam_name, color_name, "spooled"))
            for ean_refill in color.get("eans_refill", []):
                if ean_refill:
                    ean_locations[str(ean_refill)].append((fname, mfr, fam_name, color_name, "refill"))

    # Classify SKU duplicates
    for sku, locs in sorted(sku_locations.items()):
        if len(locs) > 1:
            mfrs = set(loc[1] for loc in locs)
            fams = set((loc[0], loc[2]) for loc in locs)

            if len(mfrs) > 1:
                cls = "CROSS_MANUFACTURER"
                reason = f"SKU/Code '{sku}' collides across different manufacturers: {sorted(mfrs)}"
            elif len(fams) > 1:
                cls = "CROSS_FAMILY"
                reason = f"SKU/Code '{sku}' reused across different filament families within '{locs[0][1]}'"
            else:
                cls = "SAME_FAMILY"
                reason = f"SKU/Code '{sku}' shared among multiple color variants in family '{locs[0][2]}'"

            findings.append(
                AuditFinding(
                    severity="REVIEW",
                    category="identifier",
                    file=locs[0][0],
                    manufacturer=locs[0][1],
                    family=locs[0][2],
                    field="codes",
                    value=sku,
                    reason=reason,
                    classification=cls,
                )
            )

    # Classify EAN duplicates
    for ean, locs in sorted(ean_locations.items()):
        if len(locs) > 1:
            mfrs = set(loc[1] for loc in locs)
            fams = set((loc[0], loc[2]) for loc in locs)

            if len(mfrs) > 1:
                cls = "CROSS_MANUFACTURER"
                reason = f"EAN/Barcode '{ean}' collides across different manufacturers: {sorted(mfrs)}"
            elif len(fams) > 1:
                cls = "CROSS_FAMILY"
                reason = f"EAN/Barcode '{ean}' reused across different filament families within '{locs[0][1]}'"
            else:
                cls = "SAME_FAMILY"
                reason = f"EAN/Barcode '{ean}' shared across variants in family '{locs[0][2]}'"

            findings.append(
                AuditFinding(
                    severity="REVIEW",
                    category="identifier",
                    file=locs[0][0],
                    manufacturer=locs[0][1],
                    family=locs[0][2],
                    field="eans",
                    value=ean,
                    reason=reason,
                    classification=cls,
                )
            )

    return findings


def run_physical_metadata_audit(
    filaments_dir: Path,
) -> Tuple[List[AuditFinding], Dict[str, Any]]:
    findings: List[AuditFinding] = []
    all_filaments: List[Tuple[str, str, Dict[str, Any]]] = []
    total_families = 0
    total_files = 0

    for fpath in sorted(filaments_dir.glob("*.json")):
        total_files += 1
        fname = fpath.name
        try:
            with fpath.open(encoding="utf-8") as f:
                data = json.load(f)
        except Exception as exc:
            findings.append(
                AuditFinding(
                    severity="HIGH",
                    category="structure",
                    file=fname,
                    manufacturer="<unknown>",
                    family="<file>",
                    field="json",
                    value=None,
                    reason=f"Failed to parse JSON in {fname}: {exc}",
                )
            )
            continue

        mfr = data.get("manufacturer", "<unnamed_mfr>")
        for fil in data.get("filaments", []):
            total_families += 1
            all_filaments.append((fname, mfr, fil))
            findings.extend(audit_temperatures(fil, fname, mfr))
            findings.extend(audit_density(fil, fname, mfr))
            findings.extend(audit_package_weights(fil, fname, mfr))

    # Cross-record identifier audit
    findings.extend(audit_identifiers(all_filaments))

    summary = {
        "total_files": total_files,
        "total_families": total_families,
        "total_findings": len(findings),
        "high_severity_count": sum(1 for f in findings if f.severity == "HIGH"),
        "review_severity_count": sum(1 for f in findings if f.severity == "REVIEW"),
        "categories": {
            cat: sum(1 for f in findings if f.category == cat)
            for cat in ["temperature", "temp_swap", "density", "package", "identifier", "structure"]
            if any(f.category == cat for f in findings)
        },
    }

    return findings, summary


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit physical metadata (temperatures, densities, weights, identifiers) in SpoolmanDB source files."
    )
    parser.add_argument(
        "--filaments-dir",
        type=Path,
        default=Path(__file__).parent.parent / "filaments",
        help="Path to the directory containing filament JSON files (default: filaments/).",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit nonzero (1) if any HIGH severity physical anomalies are found.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="json_output",
        help="Output machine-readable JSON format instead of human-readable text.",
    )

    args = parser.parse_args()

    if not args.filaments_dir.is_dir():
        print(f"Error: filaments directory not found at '{args.filaments_dir}'", file=sys.stderr)
        return 1

    findings, summary = run_physical_metadata_audit(args.filaments_dir)

    if args.json_output:
        output_data = {
            "summary": summary,
            "findings": [f.to_dict() for f in findings],
        }
        print(json.dumps(output_data, indent=2))
    else:
        print("=== SpoolmanDB Physical Metadata Audit ===")
        print(f"Audited {summary['total_files']} files ({summary['total_families']} families)")
        print(
            f"Findings: {summary['total_findings']} "
            f"(HIGH: {summary['high_severity_count']}, REVIEW: {summary['review_severity_count']})"
        )

        if summary["categories"]:
            print("\nFindings by Category:")
            for cat, count in summary["categories"].items():
                print(f"  - {cat}: {count}")

        if findings:
            print("\nDetailed Findings:")
            for f in findings:
                cls_info = f" [{f.classification}]" if f.classification else ""
                print(
                    f"[{f.severity}] {f.file} -> {f.manufacturer} :: {f.family} | "
                    f"field: {f.field}{cls_info}\n       Reason: {f.reason}"
                )

        if summary["high_severity_count"] == 0:
            print("\n✓ No HIGH severity physical metadata anomalies found.")
        else:
            print(f"\n⚠ {summary['high_severity_count']} HIGH severity anomaly(ies) detected.")

    if args.strict and summary["high_severity_count"] > 0:
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
