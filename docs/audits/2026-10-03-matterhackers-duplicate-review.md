# matterhackers duplicate migration review

Base `79344e671a8b5ce441fd66454b35ce6f1522afe7`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `7aa3a6dfc46d02daac3bd3bcd31ed496e019288f6fcc8f3a18139cc68b866af4`.

## Authorization and result

{"groups": 1, "approved_groups": 0, "retired": 0, "deferred": 1, "hard_stops": 0, "before_count": 51702, "after_count": 51702, "brand_before": 272, "brand_after": 272, "registry_before": 1732, "registry_after": 1732, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

One genericTPU1kgGray/Grey tie cannot bind currentPROSeries0.5kg. Defer rather than rename/rekey or invent availability. No packaging/tare or metadata changes.

This is an audit-only result: no records are retired and no catalog migration is applied. Packaging, tare and all identities remain unchanged. Future reviewed retirements would not redirect external catalog lookups automatically.

## Current first-party evidence

- {"url": "https://www.matterhackers.com/store/c/tpu-thermoplastic-polyurethane", "note": "CurrentPROSeriesGrey1lb/0.5kg,230±10; source genericSeries1kg lacksPRO qualifier."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|

## Per-group decisions and unresolved metadata

### MH001: dup-b8f73bd251b848e33c161f1d6b40855c4e0c0215183388fe73a7acc0c9152f19

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`matterhackers_tpu_tpugrayseries(thermoplasticpolyurethane)_1000_175_p`|`TPU {color_name}`|`Gray Series (Thermoplastic Polyurethane)`|{"source_file": "matterhackers.json", "definition_index": 21, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|
|`matterhackers_tpu_tpugreyseries(thermoplasticpolyurethane)_1000_175_p`|`TPU {color_name}`|`Grey Series (Thermoplastic Polyurethane)`|{"source_file": "matterhackers.json", "definition_index": 21, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "matterhackers_tpu_tpugrayseries(thermoplasticpolyurethane)_1000_175_p": "B6B9BD",
    "matterhackers_tpu_tpugreyseries(thermoplasticpolyurethane)_1000_175_p": "B8BAB8"
  }
}
```

## Exact metadata and identifier decisions

```json
{
  "metadata": [],
  "transfers": []
}
```

## Preserved out-of-scope IDs

- `matterhackers_pla_mhbuildseriesplablack_1000_175_p` — MH Build Series PLA Black
- `matterhackers_pla_mhbuildseriesplawhite_1000_175_p` — MH Build Series PLA White
- `matterhackers_pla_mhbuildseriesplared_1000_175_p` — MH Build Series PLA Red
- `matterhackers_pla_mhbuildseriesplablue_1000_175_p` — MH Build Series PLA Blue
- `matterhackers_pla_mhbuildseriesplagreen_1000_175_p` — MH Build Series PLA Green
- `matterhackers_pla_mhbuildseriesplayellow_1000_175_p` — MH Build Series PLA Yellow
- `matterhackers_pla_mhbuildseriesplaorange_1000_175_p` — MH Build Series PLA Orange
- `matterhackers_pla_mhbuildseriesplagrey_1000_175_p` — MH Build Series PLA Grey
- `matterhackers_pla_mhbuildseriesplapurple_1000_175_p` — MH Build Series PLA Purple
- `matterhackers_pla_mhbuildseriesplapink_1000_175_p` — MH Build Series PLA Pink
- `matterhackers_pla_mhbuildseriesplanatural_1000_175_p` — MH Build Series PLA Natural
- `matterhackers_pla_mhbuildseriesplablack_1000_285_p` — MH Build Series PLA Black
- `matterhackers_pla_mhbuildseriesplawhite_1000_285_p` — MH Build Series PLA White
- `matterhackers_pla_mhbuildseriesplared_1000_285_p` — MH Build Series PLA Red
- `matterhackers_pla_mhbuildseriesplablue_1000_285_p` — MH Build Series PLA Blue
- `matterhackers_pla_mhbuildseriesplagreen_1000_285_p` — MH Build Series PLA Green
- `matterhackers_pla_mhbuildseriesplayellow_1000_285_p` — MH Build Series PLA Yellow
- `matterhackers_pla_mhbuildseriesplaorange_1000_285_p` — MH Build Series PLA Orange
- `matterhackers_pla_mhbuildseriesplagrey_1000_285_p` — MH Build Series PLA Grey
- `matterhackers_pla_mhbuildseriesplapurple_1000_285_p` — MH Build Series PLA Purple
- `matterhackers_pla_mhbuildseriesplapink_1000_285_p` — MH Build Series PLA Pink
- `matterhackers_pla_mhbuildseriesplanatural_1000_285_p` — MH Build Series PLA Natural
- `matterhackers_pla_mhbuildseriesplablack_1000_175_r` — MH Build Series PLA Black
- `matterhackers_pla_mhbuildseriesplawhite_1000_175_r` — MH Build Series PLA White
- `matterhackers_pla_mhbuildseriesplared_1000_175_r` — MH Build Series PLA Red
- `matterhackers_pla_mhbuildseriesplablue_1000_175_r` — MH Build Series PLA Blue
- `matterhackers_pla_mhbuildseriesplagreen_1000_175_r` — MH Build Series PLA Green
- `matterhackers_pla_mhbuildseriesplayellow_1000_175_r` — MH Build Series PLA Yellow
- `matterhackers_pla_mhbuildseriesplaorange_1000_175_r` — MH Build Series PLA Orange
- `matterhackers_pla_mhbuildseriesplagrey_1000_175_r` — MH Build Series PLA Grey
- `matterhackers_pla_mhbuildseriesplapurple_1000_175_r` — MH Build Series PLA Purple
- `matterhackers_pla_mhbuildseriesplapink_1000_175_r` — MH Build Series PLA Pink
- `matterhackers_pla_mhbuildseriesplanatural_1000_175_r` — MH Build Series PLA Natural
- `matterhackers_pla_mhbuildseriesplablack_1000_285_r` — MH Build Series PLA Black
- `matterhackers_pla_mhbuildseriesplawhite_1000_285_r` — MH Build Series PLA White
- `matterhackers_pla_mhbuildseriesplared_1000_285_r` — MH Build Series PLA Red
- `matterhackers_pla_mhbuildseriesplablue_1000_285_r` — MH Build Series PLA Blue
- `matterhackers_pla_mhbuildseriesplagreen_1000_285_r` — MH Build Series PLA Green
- `matterhackers_pla_mhbuildseriesplayellow_1000_285_r` — MH Build Series PLA Yellow
- `matterhackers_pla_mhbuildseriesplaorange_1000_285_r` — MH Build Series PLA Orange
- `matterhackers_pla_mhbuildseriesplagrey_1000_285_r` — MH Build Series PLA Grey
- `matterhackers_pla_mhbuildseriesplapurple_1000_285_r` — MH Build Series PLA Purple
- `matterhackers_pla_mhbuildseriesplapink_1000_285_r` — MH Build Series PLA Pink
- `matterhackers_pla_mhbuildseriesplanatural_1000_285_r` — MH Build Series PLA Natural
- `matterhackers_pla_mhbuildseriesplablack_1000_175_c` — MH Build Series PLA Black
- `matterhackers_pla_mhbuildseriesplagray_1000_175_c` — MH Build Series PLA Gray
- `matterhackers_pla_mhbuildseriesplawhite_1000_175_c` — MH Build Series PLA White
- `matterhackers_petg_mhbuildseriespetgblack_1000_175_p` — MH Build Series PETG Black
- `matterhackers_petg_mhbuildseriespetgwhite_1000_175_p` — MH Build Series PETG White
- `matterhackers_petg_mhbuildseriespetgred_1000_175_p` — MH Build Series PETG Red
- `matterhackers_petg_mhbuildseriespetgblue_1000_175_p` — MH Build Series PETG Blue
- `matterhackers_petg_mhbuildseriespetggreen_1000_175_p` — MH Build Series PETG Green
- `matterhackers_petg_mhbuildseriespetgnatural_1000_175_p` — MH Build Series PETG Natural
- `matterhackers_petg_mhbuildseriespetgblack_1000_285_p` — MH Build Series PETG Black
- `matterhackers_petg_mhbuildseriespetgwhite_1000_285_p` — MH Build Series PETG White
- `matterhackers_petg_mhbuildseriespetgred_1000_285_p` — MH Build Series PETG Red
- `matterhackers_petg_mhbuildseriespetgblue_1000_285_p` — MH Build Series PETG Blue
- `matterhackers_petg_mhbuildseriespetggreen_1000_285_p` — MH Build Series PETG Green
- `matterhackers_petg_mhbuildseriespetgnatural_1000_285_p` — MH Build Series PETG Natural
- `matterhackers_pla_mhbuildseriesplasilver_1000_175_r` — MH Build Series PLA Silver
- `matterhackers_abs_mhbuildseriesabsblack_1000_175_p` — MH Build Series ABS Black
- `matterhackers_abs_mhbuildseriesabswhite_1000_175_p` — MH Build Series ABS White
- `matterhackers_abs_mhbuildseriesabsred_1000_175_p` — MH Build Series ABS Red
- `matterhackers_abs_mhbuildseriesabsblue_1000_175_p` — MH Build Series ABS Blue
- `matterhackers_abs_mhbuildseriesabsyellow_1000_175_p` — MH Build Series ABS Yellow
- `matterhackers_abs_mhbuildseriesabsnatural_1000_175_p` — MH Build Series ABS Natural
- `matterhackers_abs_mhbuildseriesabsblack_1000_285_p` — MH Build Series ABS Black
- `matterhackers_abs_mhbuildseriesabswhite_1000_285_p` — MH Build Series ABS White
- `matterhackers_abs_mhbuildseriesabsred_1000_285_p` — MH Build Series ABS Red
- `matterhackers_abs_mhbuildseriesabsblue_1000_285_p` — MH Build Series ABS Blue
- `matterhackers_abs_mhbuildseriesabsyellow_1000_285_p` — MH Build Series ABS Yellow
- `matterhackers_abs_mhbuildseriesabsnatural_1000_285_p` — MH Build Series ABS Natural
- `matterhackers_tpu_mhbuildseriestpublack_1000_175_p` — MH Build Series TPU Black
- `matterhackers_tpu_mhbuildseriestpuwhite_1000_175_p` — MH Build Series TPU White
- `matterhackers_pla_mhproseriesplablack_1000_175_p` — MH Pro Series PLA Black
- `matterhackers_pla_mhproseriesplawhite_1000_175_p` — MH Pro Series PLA White
- `matterhackers_pla_mhproseriesplared_1000_175_p` — MH Pro Series PLA Red
- `matterhackers_pla_mhproseriesplablue_1000_175_p` — MH Pro Series PLA Blue
- `matterhackers_pla_mhproseriesplagreen_1000_175_p` — MH Pro Series PLA Green
- `matterhackers_pla_mhproseriesplayellow_1000_175_p` — MH Pro Series PLA Yellow
- `matterhackers_pla_mhproseriesplaorange_1000_175_p` — MH Pro Series PLA Orange
- `matterhackers_pla_mhproseriesplagrey_1000_175_p` — MH Pro Series PLA Grey
- `matterhackers_pla_mhproseriesplapurple_1000_175_p` — MH Pro Series PLA Purple
- `matterhackers_pla_mhproseriesplablack_1000_285_p` — MH Pro Series PLA Black
- `matterhackers_pla_mhproseriesplawhite_1000_285_p` — MH Pro Series PLA White
- `matterhackers_pla_mhproseriesplared_1000_285_p` — MH Pro Series PLA Red
- `matterhackers_pla_mhproseriesplablue_1000_285_p` — MH Pro Series PLA Blue
- `matterhackers_pla_mhproseriesplagreen_1000_285_p` — MH Pro Series PLA Green
- `matterhackers_pla_mhproseriesplayellow_1000_285_p` — MH Pro Series PLA Yellow
- `matterhackers_pla_mhproseriesplaorange_1000_285_p` — MH Pro Series PLA Orange
- `matterhackers_pla_mhproseriesplagrey_1000_285_p` — MH Pro Series PLA Grey
- `matterhackers_pla_mhproseriesplapurple_1000_285_p` — MH Pro Series PLA Purple
- `matterhackers_petg_mhproseriespetgblack_1000_175_p` — MH Pro Series PETG Black
- `matterhackers_petg_mhproseriespetgwhite_1000_175_p` — MH Pro Series PETG White
- `matterhackers_petg_mhproseriespetgred_1000_175_p` — MH Pro Series PETG Red
- `matterhackers_petg_mhproseriespetgblue_1000_175_p` — MH Pro Series PETG Blue
- `matterhackers_petg_mhproseriespetgnatural_1000_175_p` — MH Pro Series PETG Natural
- `matterhackers_petg_mhproseriespetgblack_1000_285_p` — MH Pro Series PETG Black
- `matterhackers_petg_mhproseriespetgwhite_1000_285_p` — MH Pro Series PETG White
- `matterhackers_petg_mhproseriespetgred_1000_285_p` — MH Pro Series PETG Red
- `matterhackers_petg_mhproseriespetgblue_1000_285_p` — MH Pro Series PETG Blue
- `matterhackers_petg_mhproseriespetgnatural_1000_285_p` — MH Pro Series PETG Natural
- `matterhackers_pla_mhproseriestoughplablack_1000_175_p` — MH Pro Series Tough PLA Black
- `matterhackers_pla_mhproseriestoughplawhite_1000_175_p` — MH Pro Series Tough PLA White
- `matterhackers_pa-cf_mhnylonxblack_500_175_p` — MH NylonX Black
- `matterhackers_pa-cf_mhnylonxblack_500_285_p` — MH NylonX Black
- `matterhackers_pa-gf_mhnylongnatural_500_175_p` — MH NylonG Natural
- `matterhackers_pa-gf_mhnylongnatural_500_285_p` — MH NylonG Natural
- `matterhackers_abs_absblackmhbuildseries_1000_175_p` — ABS Black MH Build Series
- `matterhackers_abs_absblackseries_1000_175_p` — ABS Black Series
- `matterhackers_abs_absbluemhbuildseries_1000_175_p` — ABS Blue MH Build Series
- `matterhackers_abs_absblueseries_1000_175_p` — ABS Blue Series
- `matterhackers_abs_absbrownmhbuildseries_1000_175_p` — ABS Brown MH Build Series
- `matterhackers_abs_absbrownseries_1000_175_p` — ABS Brown Series
- `matterhackers_abs_absforestgreenmhbuildseries_1000_175_p` — ABS Forest Green MH Build Series
- `matterhackers_abs_absgraymhbuildseries_1000_175_p` — ABS Gray MH Build Series
- `matterhackers_abs_absgrayseries_1000_175_p` — ABS Gray Series
- `matterhackers_abs_absgreenmhbuildseries_1000_175_p` — ABS Green MH Build Series
- `matterhackers_abs_absgreenseries_1000_175_p` — ABS Green Series
- `matterhackers_abs_absjetgrayseries_1000_175_p` — ABS Jet Gray Series
- `matterhackers_abs_abslightbluemhbuildseries_1000_175_p` — ABS Light Blue MH Build Series
- `matterhackers_abs_abslimegreenmhbuildseries_1000_175_p` — ABS Lime Green MH Build Series
- `matterhackers_abs_abslimegreenseries_1000_175_p` — ABS Lime Green Series
- `matterhackers_abs_absmidnightblueseries_1000_175_p` — ABS Midnight Blue Series
- `matterhackers_abs_absnaturalmhbuildseries_1000_175_p` — ABS Natural MH Build Series
- `matterhackers_abs_absnaturalseries_1000_175_p` — ABS Natural Series
- `matterhackers_abs_absorangemhbuildseries_1000_175_p` — ABS Orange MH Build Series
- `matterhackers_abs_absorangeseries_1000_175_p` — ABS Orange Series
- `matterhackers_abs_abspinkmhbuildseries_1000_175_p` — ABS Pink MH Build Series
- `matterhackers_abs_abspurplemhbuildseries_1000_175_p` — ABS Purple MH Build Series
- `matterhackers_abs_abspurpleseries_1000_175_p` — ABS Purple Series
- `matterhackers_abs_absredmhbuildseries_1000_175_p` — ABS Red MH Build Series
- `matterhackers_abs_absredseries_1000_175_p` — ABS Red Series
- `matterhackers_abs_abssilvermhbuildseries_1000_175_p` — ABS Silver MH Build Series
- `matterhackers_abs_abssilverseries_1000_175_p` — ABS Silver Series
- `matterhackers_abs_abswhitemhbuildseries_1000_175_p` — ABS White MH Build Series
- `matterhackers_abs_abswhiteseries_1000_175_p` — ABS White Series
- `matterhackers_abs_absyellowmhbuildseries_1000_175_p` — ABS Yellow MH Build Series
- `matterhackers_abs_absyellowseries_1000_175_p` — ABS Yellow Series
- `matterhackers_cpe_cpeblackseriesryno_1000_175_p` — CPE Black Series Ryno
- `matterhackers_cpe_cpeclearseriesryno_1000_175_p` — CPE Clear Series Ryno
- `matterhackers_cpe_cpegreyseriesryno_1000_175_p` — CPE Grey Series Ryno
- `matterhackers_cpe_cpewhiteseriesryno_1000_175_p` — CPE White Series Ryno
- `matterhackers_pa12_pa12cfnylonxcarbonfiber_1000_175_p` — PA12 CF NylonX Carbon Fiber
- `matterhackers_pa12_pa12gfblacknylongglassfiber_1000_175_p` — PA12 GF Black NylonG Glass Fiber
- `matterhackers_pa12_pa12gfbluenylongglassfiber_1000_175_p` — PA12 GF Blue NylonG Glass Fiber
- `matterhackers_pa12_pa12gfdeserttannylongglassfiber_1000_175_p` — PA12 GF Desert Tan NylonG Glass Fiber
- `matterhackers_pa12_pa12gfolivegreennylongglassfiber_1000_175_p` — PA12 GF Olive Green NylonG Glass Fiber
- `matterhackers_pa12_pa12gfrednylongglassfiber_1000_175_p` — PA12 GF Red NylonG Glass Fiber
- `matterhackers_pa12_pa12gfsafetyorangenylongglassfiber_1000_175_p` — PA12 GF Safety Orange NylonG Glass Fiber
- `matterhackers_pa12_pa12gfsilvernylongglassfiber_1000_175_p` — PA12 GF Silver NylonG Glass Fiber
- `matterhackers_pa12_pa12gfwhitenylongglassfiber_1000_175_p` — PA12 GF White NylonG Glass Fiber
- `matterhackers_pa6_pa6blackseriesnylon_1000_175_p` — PA6 Black Series Nylon
- `matterhackers_pa6_pa6blueseriesnylon_1000_175_p` — PA6 Blue Series Nylon
- `matterhackers_pa6_pa6grayseriesnylon_1000_175_p` — PA6 Gray Series Nylon
- `matterhackers_pa6_pa6greenseriesnylon_1000_175_p` — PA6 Green Series Nylon
- `matterhackers_pa6_pa6orangeseriesnylon_1000_175_p` — PA6 Orange Series Nylon
- `matterhackers_pa6_pa6redseriesnylon_1000_175_p` — PA6 Red Series Nylon
- `matterhackers_pa6_pa6whiteseriesnylon_1000_175_p` — PA6 White Series Nylon
- `matterhackers_petg_petgblackmhbuildseries_1000_175_p` — PETG Black MH Build Series
- `matterhackers_petg_petgblackseries_1000_175_p` — PETG Black Series
- `matterhackers_petg_petgblueseries_1000_175_p` — PETG Blue Series
- `matterhackers_petg_petgcleartranslucentmhbuildseries_1000_175_p` — PETG Clear Translucent MH Build Series
- `matterhackers_petg_petgjetgrayseries_1000_175_p` — PETG Jet Gray Series
- `matterhackers_petg_petgmerlotredseries_1000_175_p` — PETG Merlot Red Series
- `matterhackers_petg_petgorangeseries_1000_175_p` — PETG Orange Series
- `matterhackers_petg_petgparthenongraymarbleseries_1000_175_p` — PETG Parthenon Gray Marble Series
- `matterhackers_petg_petgredmhbuildseries_1000_175_p` — PETG Red MH Build Series
- `matterhackers_petg_petgredseries_1000_175_p` — PETG Red Series
- `matterhackers_petg_petgsilvermhbuildseries_1000_175_p` — PETG Silver MH Build Series
- `matterhackers_petg_petgtranslucentbluemhbuildseries_1000_175_p` — PETG Translucent Blue MH Build Series
- `matterhackers_petg_petgtranslucentblueseries_1000_175_p` — PETG Translucent Blue Series
- `matterhackers_petg_petgtranslucentclearseries_1000_175_p` — PETG Translucent Clear Series
- `matterhackers_petg_petgtranslucentgreenmhbuildseries_1000_175_p` — PETG Translucent Green MH Build Series
- `matterhackers_petg_petgtranslucentorangemhbuildseries_1000_175_p` — PETG Translucent Orange MH Build Series
- `matterhackers_petg_petgtranslucentredmhbuildseries_1000_175_p` — PETG Translucent Red MH Build Series
- `matterhackers_petg_petgtranslucentredseries_1000_175_p` — PETG Translucent Red Series
- `matterhackers_petg_petgwhitemhbuildseries_1000_175_p` — PETG White MH Build Series
- `matterhackers_petg_petgwhiteseries_1000_175_p` — PETG White Series
- `matterhackers_petg_petgyellowmhbuildseries_1000_175_p` — PETG Yellow MH Build Series
- `matterhackers_pla_glowplablueglowinthedarkmhbuildseries_1000_175_p` — Glow PLA Blue Glow in the Dark MH Build Series
- `matterhackers_pla_glowplamhbuildseries_1000_175_p` — Glow PLA MH Build Series
- `matterhackers_pla_glowplaseries_1000_175_p` — Glow PLA Series
- `matterhackers_pla_plablackmhbuildseries_1000_175_p` — PLA Black MH Build Series
- `matterhackers_pla_plablackseries_1000_175_p` — PLA Black Series
- `matterhackers_pla_plabluemhbuildseries_1000_175_p` — PLA Blue MH Build Series
- `matterhackers_pla_plablueseries_1000_175_p` — PLA Blue Series
- `matterhackers_pla_plabrownmhbuildseries_1000_175_p` — PLA Brown MH Build Series
- `matterhackers_pla_plabrownseries_1000_175_p` — PLA Brown Series
- `matterhackers_pla_plaburgundyseries_1000_175_p` — PLA Burgundy Series
- `matterhackers_pla_plaburntorangeseries_1000_175_p` — PLA Burnt Orange Series
- `matterhackers_pla_placaribbeanblueseries_1000_175_p` — PLA Caribbean Blue Series
- `matterhackers_pla_plaelectricmagentaseries_1000_175_p` — PLA Electric Magenta Series
- `matterhackers_pla_plaelectricorangeseries_1000_175_p` — PLA Electric Orange Series
- `matterhackers_pla_plaelectricpinkseries_1000_175_p` — PLA Electric Pink Series
- `matterhackers_pla_plaelectricyellowseries_1000_175_p` — PLA Electric Yellow Series
- `matterhackers_pla_plaemeralddreamseries_1000_175_p` — PLA Emerald Dream Series
- `matterhackers_pla_plafireflygreenseries_1000_175_p` — PLA Firefly Green Series
- `matterhackers_pla_plaforestgreenmhbuildseries_1000_175_p` — PLA Forest Green MH Build Series
- `matterhackers_pla_plagoldmhbuildseries_1000_175_p` — PLA Gold MH Build Series
- `matterhackers_pla_plagoldseries_1000_175_p` — PLA Gold Series
- `matterhackers_pla_plagrayseries_1000_175_p` — PLA Gray Series
- `matterhackers_pla_plagreenmhbuildseries_1000_175_p` — PLA Green MH Build Series
- `matterhackers_pla_plagreenseries_1000_175_p` — PLA Green Series
- `matterhackers_pla_plagreymhbuildseries_1000_175_p` — PLA Grey MH Build Series
- `matterhackers_pla_plajetgrayseries_1000_175_p` — PLA Jet Gray Series
- `matterhackers_pla_plalightbluemhbuildseries_1000_175_p` — PLA Light Blue MH Build Series
- `matterhackers_pla_plalightblueseries_1000_175_p` — PLA Light Blue Series
- `matterhackers_pla_plalilacpastelseries_1000_175_p` — PLA Lilac Pastel Series
- `matterhackers_pla_plalimegreenmhbuildseries_1000_175_p` — PLA Lime Green MH Build Series
- `matterhackers_pla_plalimegreenseries_1000_175_p` — PLA Lime Green Series
- `matterhackers_pla_plamagentamhbuildseries_1000_175_p` — PLA Magenta MH Build Series
- `matterhackers_pla_plamagentaseries_1000_175_p` — PLA Magenta Series
- `matterhackers_pla_plamerlotredseries_1000_175_p` — PLA Merlot Red Series
- `matterhackers_pla_plamidnightblueseries_1000_175_p` — PLA Midnight Blue Series
- `matterhackers_pla_planaturalmhbuildseries_1000_175_p` — PLA Natural MH Build Series
- `matterhackers_pla_planaturaltranslucentseries_1000_175_p` — PLA Natural Translucent Series
- `matterhackers_pla_plaorangemhbuildseries_1000_175_p` — PLA Orange MH Build Series
- `matterhackers_pla_plaorangeseries_1000_175_p` — PLA Orange Series
- `matterhackers_pla_plapaperwhiteseries_1000_175_p` — PLA Paper White Series
- `matterhackers_pla_plaparthenongraymarbleseries_1000_175_p` — PLA Parthenon Gray Marble Series
- `matterhackers_pla_plapinkmhbuildseries_1000_175_p` — PLA Pink MH Build Series
- `matterhackers_pla_plapurplemhbuildseries_1000_175_p` — PLA Purple MH Build Series
- `matterhackers_pla_plapurpleseries_1000_175_p` — PLA Purple Series
- `matterhackers_pla_plaredmhbuildseries_1000_175_p` — PLA Red MH Build Series
- `matterhackers_pla_plaredseries_1000_175_p` — PLA Red Series
- `matterhackers_pla_plaroyalbluemhbuildseries_1000_175_p` — PLA Royal Blue MH Build Series
- `matterhackers_pla_plaroyalblueseries_1000_175_p` — PLA Royal Blue Series
- `matterhackers_pla_plasilvermhbuildseries_1000_175_p` — PLA Silver MH Build Series
- `matterhackers_pla_plasilverseries_1000_175_p` — PLA Silver Series
- `matterhackers_pla_plasolarflareseries_1000_175_p` — PLA Solar Flare Series
- `matterhackers_pla_platanmhbuildseries_1000_175_p` — PLA Tan MH Build Series
- `matterhackers_pla_platanseries_1000_175_p` — PLA Tan Series
- `matterhackers_pla_platealblueseries_1000_175_p` — PLA Teal Blue Series
- `matterhackers_pla_platerracottaredseries_1000_175_p` — PLA Terracotta Red Series
- `matterhackers_pla_platranslucentblueseries_1000_175_p` — PLA Translucent Blue Series
- `matterhackers_pla_platranslucenticeblueseries_1000_175_p` — PLA Translucent Ice Blue Series
- `matterhackers_pla_platranslucentredseries_1000_175_p` — PLA Translucent Red Series
- `matterhackers_pla_platranslucentvioletseries_1000_175_p` — PLA Translucent Violet Series
- `matterhackers_pla_plawhitemhbuildseries_1000_175_p` — PLA White MH Build Series
- `matterhackers_pla_plawhiteseries_1000_175_p` — PLA White Series
- `matterhackers_pla_playellowmhbuildseries_1000_175_p` — PLA Yellow MH Build Series
- `matterhackers_pla_playellowseries_1000_175_p` — PLA Yellow Series
- `matterhackers_pla_silkplabluemhbuildseries_1000_175_p` — Silk PLA Blue MH Build Series
- `matterhackers_pla_silkplabronzemhbuildseries_1000_175_p` — Silk PLA Bronze MH Build Series
- `matterhackers_pla_silkplacoppermhbuildseries_1000_175_p` — Silk PLA Copper MH Build Series
- `matterhackers_pla_silkplagoldmhbuildseries_1000_175_p` — Silk PLA Gold MH Build Series
- `matterhackers_pla_silkplagreenmhbuildseries_1000_175_p` — Silk PLA Green MH Build Series
- `matterhackers_pla_silkplamagentamhbuildseries_1000_175_p` — Silk PLA Magenta MH Build Series
- `matterhackers_pla_silkplapurplemhbuildseries_1000_175_p` — Silk PLA Purple MH Build Series
- `matterhackers_pla_silkplaredmhbuildseries_1000_175_p` — Silk PLA Red MH Build Series
- `matterhackers_pla_silkplasilvermhbuildseries_1000_175_p` — Silk PLA Silver MH Build Series
- `matterhackers_pla_silkplatealmhbuildseries_1000_175_p` — Silk PLA Teal MH Build Series
- `matterhackers_pla_silkplawhitemhbuildseries_1000_175_p` — Silk PLA White MH Build Series
- `matterhackers_pla_silkplayellowmhbuildseries_1000_175_p` — Silk PLA Yellow MH Build Series
- `matterhackers_tpu_mhbuildseriesflexibletpublack_1000_175_p` — Mh Build Series Flexible TPU Black
- `matterhackers_tpu_mhbuildseriesflexibletpuclear_1000_175_p` — Mh Build Series Flexible TPU Clear
- `matterhackers_tpu_mhbuildseriesflexibletpugrey_1000_175_p` — Mh Build Series Flexible TPU Grey
- `matterhackers_tpu_mhbuildseriesflexibletputranslucentblue_1000_175_p` — Mh Build Series Flexible TPU Translucent Blue
- `matterhackers_tpu_mhbuildseriesflexibletputranslucentgreen_1000_175_p` — Mh Build Series Flexible TPU Translucent Green
- `matterhackers_tpu_mhbuildseriesflexibletputranslucentorange_1000_175_p` — Mh Build Series Flexible TPU Translucent Orange
- `matterhackers_tpu_mhbuildseriesflexibletputranslucentpurple_1000_175_p` — Mh Build Series Flexible TPU Translucent Purple
- `matterhackers_tpu_mhbuildseriesflexibletputranslucentred_1000_175_p` — Mh Build Series Flexible TPU Translucent Red
- `matterhackers_tpu_mhbuildseriesflexibletpuwhite_1000_175_p` — Mh Build Series Flexible TPU White
- `matterhackers_tpu_tpublackseries(thermoplasticpolyurethane)_1000_175_p` — TPU Black Series (Thermoplastic Polyurethane)
- `matterhackers_tpu_tpublueseries(thermoplasticpolyurethane)_1000_175_p` — TPU Blue Series (Thermoplastic Polyurethane)
- `matterhackers_tpu_tpugreenseries(thermoplasticpolyurethane)_1000_175_p` — TPU Green Series (Thermoplastic Polyurethane)
- `matterhackers_tpu_tpunaturaltranslucentseries(thermoplasticpolyurethane)_1000_175_p` — TPU Natural Translucent Series (Thermoplastic Polyurethane)
- `matterhackers_tpu_tpuredseries(thermoplasticpolyurethane)_1000_175_p` — TPU Red Series (Thermoplastic Polyurethane)
- `matterhackers_tpu_tpuwhiteseries(thermoplasticpolyurethane)_1000_175_p` — TPU White Series (Thermoplastic Polyurethane)
