# arianeplast duplicate migration review

Base `7ce42061d422af5155de55a9d26fbc08efcf05ff`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `56921a32d195c1fd1c5d60c16fefd3f53425d01c986aa9d80e602d56e0a58089`.

## Authorization and result

{"groups": 4, "approved_groups": 0, "retired": 0, "deferred": 4, "hard_stops": 0, "before_count": 51719, "after_count": 51719, "brand_before": 318, "brand_after": 318, "registry_before": 1715, "registry_after": 1715, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

All4 same-template Gray/Grey ties deferred: HEX545F67 versus808080 and no same-SKU binding. CurrentPLA+4043D page/TDS disagree printing; no genericPLA lineage assumed. No metadata or identifier changes.

This is an audit-only result: no records are retired and no catalog migration is applied. Packaging, tare and all identities remain unchanged. Future reviewed retirements would not redirect external catalog lookups automatically.

## Current first-party evidence

- {"url": "https://www.arianeplast.com/en/pla-format-1-kg/149-pla-gris-4043d-3d-filament-arianeplast-1kg-fabrique-en-france-.html", "note": "Current4043D page explicitly PLA+,1kg; does not bind genericPLA Gray/Grey across1/2.3kg and1.75/2.85."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|

## Per-group decisions and unresolved metadata

### AR001: dup-0cc758a2422675faf1a34f89902e166bd883c0740f9e96524a9e4c9593a88424

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`arianeplast_pla_plagray_2300_175_p`|`PLA {color_name}`|`Gray`|{"source_file": "arianeplast.json", "definition_index": 0, "weights": 2, "diameters": 2, "colors": 73, "compiled_records": 292} / False|
|`arianeplast_pla_plagrey_2300_175_p`|`PLA {color_name}`|`Grey`|{"source_file": "arianeplast.json", "definition_index": 0, "weights": 2, "diameters": 2, "colors": 73, "compiled_records": 292} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "arianeplast_pla_plagray_2300_175_p": "545F67",
    "arianeplast_pla_plagrey_2300_175_p": "808080"
  }
}
```

### AR002: dup-5eb2b022938e335c640dc8fb90de1d117cf46d7066fd63a363cb63eac4862c1b

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`arianeplast_pla_plagray_1000_285_p`|`PLA {color_name}`|`Gray`|{"source_file": "arianeplast.json", "definition_index": 0, "weights": 2, "diameters": 2, "colors": 73, "compiled_records": 292} / False|
|`arianeplast_pla_plagrey_1000_285_p`|`PLA {color_name}`|`Grey`|{"source_file": "arianeplast.json", "definition_index": 0, "weights": 2, "diameters": 2, "colors": 73, "compiled_records": 292} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "arianeplast_pla_plagray_1000_285_p": "545F67",
    "arianeplast_pla_plagrey_1000_285_p": "808080"
  }
}
```

### AR003: dup-77d9d265bd25eaffeb613674ca293885b09b8ae858b2bef12f3740dfcb87efae

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`arianeplast_pla_plagray_1000_175_p`|`PLA {color_name}`|`Gray`|{"source_file": "arianeplast.json", "definition_index": 0, "weights": 2, "diameters": 2, "colors": 73, "compiled_records": 292} / False|
|`arianeplast_pla_plagrey_1000_175_p`|`PLA {color_name}`|`Grey`|{"source_file": "arianeplast.json", "definition_index": 0, "weights": 2, "diameters": 2, "colors": 73, "compiled_records": 292} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "arianeplast_pla_plagray_1000_175_p": "545F67",
    "arianeplast_pla_plagrey_1000_175_p": "808080"
  }
}
```

### AR004: dup-9c695ad8824644b7e7fa83dda79b27ca8b8fd54c52a23d15a2fc4ae161c869d8

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`arianeplast_pla_plagray_2300_285_p`|`PLA {color_name}`|`Gray`|{"source_file": "arianeplast.json", "definition_index": 0, "weights": 2, "diameters": 2, "colors": 73, "compiled_records": 292} / False|
|`arianeplast_pla_plagrey_2300_285_p`|`PLA {color_name}`|`Grey`|{"source_file": "arianeplast.json", "definition_index": 0, "weights": 2, "diameters": 2, "colors": 73, "compiled_records": 292} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "arianeplast_pla_plagray_2300_285_p": "545F67",
    "arianeplast_pla_plagrey_2300_285_p": "808080"
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

- `arianeplast_pla_plablack_1000_175_p` — PLA Black
- `arianeplast_pla_plawhite_1000_175_p` — PLA White
- `arianeplast_pla_plablue_1000_175_p` — PLA Blue
- `arianeplast_pla_plared_1000_175_p` — PLA Red
- `arianeplast_pla_playellow_1000_175_p` — PLA Yellow
- `arianeplast_pla_plagreen_1000_175_p` — PLA Green
- `arianeplast_pla_plaorange_1000_175_p` — PLA Orange
- `arianeplast_pla_plapurple_1000_175_p` — PLA Purple
- `arianeplast_pla_plapink_1000_175_p` — PLA Pink
- `arianeplast_pla_plaapplegreen_1000_175_p` — PLA apple green
- `arianeplast_pla_plablue/grey_1000_175_p` — PLA blue/grey
- `arianeplast_pla_plabordeaux_1000_175_p` — PLA Bordeaux
- `arianeplast_pla_plabrown_1000_175_p` — PLA brown
- `arianeplast_pla_placopper_1000_175_p` — PLA Copper
- `arianeplast_pla_placoral_1000_175_p` — PLA Coral
- `arianeplast_pla_pladnaanti-counterfeitingblack_1000_175_p` — PLA DNA Anti-counterfeiting Black
- `arianeplast_pla_pladnaanti-counterfeitingwhite_1000_175_p` — PLA DNA Anti-counterfeiting White
- `arianeplast_pla_plaelectricallyconductive_1000_175_p` — PLA Electrically Conductive
- `arianeplast_pla_plafluorescentyellow_1000_175_p` — PLA Fluorescent Yellow
- `arianeplast_pla_plafranceblue_1000_175_p` — PLA France Blue
- `arianeplast_pla_plagold_1000_175_p` — PLA Gold
- `arianeplast_pla_plakhaki_1000_175_p` — PLA Khaki
- `arianeplast_pla_plalightgrey_1000_175_p` — PLA Light grey
- `arianeplast_pla_plametallicaluminum_1000_175_p` — PLA Metallic Aluminum
- `arianeplast_pla_plametallicanthracitegray_1000_175_p` — PLA Metallic Anthracite Gray
- `arianeplast_pla_plametallicblue_1000_175_p` — PLA Metallic blue
- `arianeplast_pla_plametallicinterferentialblue_1000_175_p` — PLA Metallic Interferential Blue
- `arianeplast_pla_plametallicochre_1000_175_p` — PLA metallic ochre
- `arianeplast_pla_plametallicpurple_1000_175_p` — PLA Metallic purple
- `arianeplast_pla_plametallicred_1000_175_p` — PLA Metallic Red
- `arianeplast_pla_plametallicviolet_1000_175_p` — PLA Metallic Violet
- `arianeplast_pla_plamoule_1000_175_p` — PLA Moule
- `arianeplast_pla_plamulticolor_1000_175_p` — PLA Multicolor
- `arianeplast_pla_planatural_1000_175_p` — PLA Natural
- `arianeplast_pla_planavyblue_1000_175_p` — PLA navy blue
- `arianeplast_pla_planoir_1000_175_p` — PLA noir
- `arianeplast_pla_planoirmtallis_1000_175_p` — PLA noir métallisé
- `arianeplast_pla_plaochreorange_1000_175_p` — PLA Ochre Orange
- `arianeplast_pla_plaoyster_1000_175_p` — PLA Oyster
- `arianeplast_pla_plapeach_1000_175_p` — PLA Peach
- `arianeplast_pla_plapearlblue_1000_175_p` — PLA Pearl Blue
- `arianeplast_pla_plapearlwhite_1000_175_p` — PLA Pearl White
- `arianeplast_pla_plapinkbonbon_1000_175_p` — PLA Pink Bonbon
- `arianeplast_pla_plapinkfunky_1000_175_p` — PLA Pink Funky
- `arianeplast_pla_plapistachio_1000_175_p` — PLA Pistachio
- `arianeplast_pla_plarosemetallic_1000_175_p` — PLA Rose Metallic
- `arianeplast_pla_plarosemtallis_1000_175_p` — PLA Rose métallisé
- `arianeplast_pla_plarosetranslucide_1000_175_p` — PLA Rose translucide
- `arianeplast_pla_plarouge_1000_175_p` — PLA rouge
- `arianeplast_pla_plarougemtallis_1000_175_p` — PLA Rouge métallisé
- `arianeplast_pla_plasafetyyellow_1000_175_p` — PLA Safety Yellow
- `arianeplast_pla_plasilver_1000_175_p` — PLA Silver
- `arianeplast_pla_plaskin2r15sp_1000_175_p` — PLA Skin 2R15SP
- `arianeplast_pla_plaskin3y09sp_1000_175_p` — PLA Skin 3Y09SP
- `arianeplast_pla_plaskin5y06sp_1000_175_p` — PLA Skin 5Y06SP
- `arianeplast_pla_plaskin5y09sp_1000_175_p` — PLA Skin 5Y09SP
- `arianeplast_pla_plasky_1000_175_p` — PLA Sky
- `arianeplast_pla_platranslucentblue_1000_175_p` — PLA translucent blue
- `arianeplast_pla_platranslucentbottlegreen_1000_175_p` — PLA Translucent Bottle Green
- `arianeplast_pla_platranslucentgreen_1000_175_p` — PLA Translucent Green
- `arianeplast_pla_platranslucentyellow_1000_175_p` — PLA Translucent Yellow
- `arianeplast_pla_platurquoise_1000_175_p` — PLA Turquoise
- `arianeplast_pla_plaultravioletpantone5f4b8b_1000_175_p` — PLA Ultra Violet Pantone 5F4B8B
- `arianeplast_pla_plavert4043d_1000_175_p` — PLA vert 4043D
- `arianeplast_pla_plavertfluo_1000_175_p` — PLA Vert Fluo
- `arianeplast_pla_plavertmtallis_1000_175_p` — PLA vert métallisé
- `arianeplast_pla_plavertpantone3268c_1000_175_p` — PLA Vert Pantone 3268C
- `arianeplast_pla_plaviolettranslucide_1000_175_p` — PLA Violet translucide
- `arianeplast_pla_playellowgold_1000_175_p` — PLA yellow gold
- `arianeplast_pla_playellowocher_1000_175_p` — PLA Yellow Ocher
- `arianeplast_pla_playellowpantone116u_1000_175_p` — PLA Yellow Pantone 116U
- `arianeplast_pla_plablack_1000_285_p` — PLA Black
- `arianeplast_pla_plawhite_1000_285_p` — PLA White
- `arianeplast_pla_plablue_1000_285_p` — PLA Blue
- `arianeplast_pla_plared_1000_285_p` — PLA Red
- `arianeplast_pla_playellow_1000_285_p` — PLA Yellow
- `arianeplast_pla_plagreen_1000_285_p` — PLA Green
- `arianeplast_pla_plaorange_1000_285_p` — PLA Orange
- `arianeplast_pla_plapurple_1000_285_p` — PLA Purple
- `arianeplast_pla_plapink_1000_285_p` — PLA Pink
- `arianeplast_pla_plaapplegreen_1000_285_p` — PLA apple green
- `arianeplast_pla_plablue/grey_1000_285_p` — PLA blue/grey
- `arianeplast_pla_plabordeaux_1000_285_p` — PLA Bordeaux
- `arianeplast_pla_plabrown_1000_285_p` — PLA brown
- `arianeplast_pla_placopper_1000_285_p` — PLA Copper
- `arianeplast_pla_placoral_1000_285_p` — PLA Coral
- `arianeplast_pla_pladnaanti-counterfeitingblack_1000_285_p` — PLA DNA Anti-counterfeiting Black
- `arianeplast_pla_pladnaanti-counterfeitingwhite_1000_285_p` — PLA DNA Anti-counterfeiting White
- `arianeplast_pla_plaelectricallyconductive_1000_285_p` — PLA Electrically Conductive
- `arianeplast_pla_plafluorescentyellow_1000_285_p` — PLA Fluorescent Yellow
- `arianeplast_pla_plafranceblue_1000_285_p` — PLA France Blue
- `arianeplast_pla_plagold_1000_285_p` — PLA Gold
- `arianeplast_pla_plakhaki_1000_285_p` — PLA Khaki
- `arianeplast_pla_plalightgrey_1000_285_p` — PLA Light grey
- `arianeplast_pla_plametallicaluminum_1000_285_p` — PLA Metallic Aluminum
- `arianeplast_pla_plametallicanthracitegray_1000_285_p` — PLA Metallic Anthracite Gray
- `arianeplast_pla_plametallicblue_1000_285_p` — PLA Metallic blue
- `arianeplast_pla_plametallicinterferentialblue_1000_285_p` — PLA Metallic Interferential Blue
- `arianeplast_pla_plametallicochre_1000_285_p` — PLA metallic ochre
- `arianeplast_pla_plametallicpurple_1000_285_p` — PLA Metallic purple
- `arianeplast_pla_plametallicred_1000_285_p` — PLA Metallic Red
- `arianeplast_pla_plametallicviolet_1000_285_p` — PLA Metallic Violet
- `arianeplast_pla_plamoule_1000_285_p` — PLA Moule
- `arianeplast_pla_plamulticolor_1000_285_p` — PLA Multicolor
- `arianeplast_pla_planatural_1000_285_p` — PLA Natural
- `arianeplast_pla_planavyblue_1000_285_p` — PLA navy blue
- `arianeplast_pla_planoir_1000_285_p` — PLA noir
- `arianeplast_pla_planoirmtallis_1000_285_p` — PLA noir métallisé
- `arianeplast_pla_plaochreorange_1000_285_p` — PLA Ochre Orange
- `arianeplast_pla_plaoyster_1000_285_p` — PLA Oyster
- `arianeplast_pla_plapeach_1000_285_p` — PLA Peach
- `arianeplast_pla_plapearlblue_1000_285_p` — PLA Pearl Blue
- `arianeplast_pla_plapearlwhite_1000_285_p` — PLA Pearl White
- `arianeplast_pla_plapinkbonbon_1000_285_p` — PLA Pink Bonbon
- `arianeplast_pla_plapinkfunky_1000_285_p` — PLA Pink Funky
- `arianeplast_pla_plapistachio_1000_285_p` — PLA Pistachio
- `arianeplast_pla_plarosemetallic_1000_285_p` — PLA Rose Metallic
- `arianeplast_pla_plarosemtallis_1000_285_p` — PLA Rose métallisé
- `arianeplast_pla_plarosetranslucide_1000_285_p` — PLA Rose translucide
- `arianeplast_pla_plarouge_1000_285_p` — PLA rouge
- `arianeplast_pla_plarougemtallis_1000_285_p` — PLA Rouge métallisé
- `arianeplast_pla_plasafetyyellow_1000_285_p` — PLA Safety Yellow
- `arianeplast_pla_plasilver_1000_285_p` — PLA Silver
- `arianeplast_pla_plaskin2r15sp_1000_285_p` — PLA Skin 2R15SP
- `arianeplast_pla_plaskin3y09sp_1000_285_p` — PLA Skin 3Y09SP
- `arianeplast_pla_plaskin5y06sp_1000_285_p` — PLA Skin 5Y06SP
- `arianeplast_pla_plaskin5y09sp_1000_285_p` — PLA Skin 5Y09SP
- `arianeplast_pla_plasky_1000_285_p` — PLA Sky
- `arianeplast_pla_platranslucentblue_1000_285_p` — PLA translucent blue
- `arianeplast_pla_platranslucentbottlegreen_1000_285_p` — PLA Translucent Bottle Green
- `arianeplast_pla_platranslucentgreen_1000_285_p` — PLA Translucent Green
- `arianeplast_pla_platranslucentyellow_1000_285_p` — PLA Translucent Yellow
- `arianeplast_pla_platurquoise_1000_285_p` — PLA Turquoise
- `arianeplast_pla_plaultravioletpantone5f4b8b_1000_285_p` — PLA Ultra Violet Pantone 5F4B8B
- `arianeplast_pla_plavert4043d_1000_285_p` — PLA vert 4043D
- `arianeplast_pla_plavertfluo_1000_285_p` — PLA Vert Fluo
- `arianeplast_pla_plavertmtallis_1000_285_p` — PLA vert métallisé
- `arianeplast_pla_plavertpantone3268c_1000_285_p` — PLA Vert Pantone 3268C
- `arianeplast_pla_plaviolettranslucide_1000_285_p` — PLA Violet translucide
- `arianeplast_pla_playellowgold_1000_285_p` — PLA yellow gold
- `arianeplast_pla_playellowocher_1000_285_p` — PLA Yellow Ocher
- `arianeplast_pla_playellowpantone116u_1000_285_p` — PLA Yellow Pantone 116U
- `arianeplast_pla_plablack_2300_175_p` — PLA Black
- `arianeplast_pla_plawhite_2300_175_p` — PLA White
- `arianeplast_pla_plablue_2300_175_p` — PLA Blue
- `arianeplast_pla_plared_2300_175_p` — PLA Red
- `arianeplast_pla_playellow_2300_175_p` — PLA Yellow
- `arianeplast_pla_plagreen_2300_175_p` — PLA Green
- `arianeplast_pla_plaorange_2300_175_p` — PLA Orange
- `arianeplast_pla_plapurple_2300_175_p` — PLA Purple
- `arianeplast_pla_plapink_2300_175_p` — PLA Pink
- `arianeplast_pla_plaapplegreen_2300_175_p` — PLA apple green
- `arianeplast_pla_plablue/grey_2300_175_p` — PLA blue/grey
- `arianeplast_pla_plabordeaux_2300_175_p` — PLA Bordeaux
- `arianeplast_pla_plabrown_2300_175_p` — PLA brown
- `arianeplast_pla_placopper_2300_175_p` — PLA Copper
- `arianeplast_pla_placoral_2300_175_p` — PLA Coral
- `arianeplast_pla_pladnaanti-counterfeitingblack_2300_175_p` — PLA DNA Anti-counterfeiting Black
- `arianeplast_pla_pladnaanti-counterfeitingwhite_2300_175_p` — PLA DNA Anti-counterfeiting White
- `arianeplast_pla_plaelectricallyconductive_2300_175_p` — PLA Electrically Conductive
- `arianeplast_pla_plafluorescentyellow_2300_175_p` — PLA Fluorescent Yellow
- `arianeplast_pla_plafranceblue_2300_175_p` — PLA France Blue
- `arianeplast_pla_plagold_2300_175_p` — PLA Gold
- `arianeplast_pla_plakhaki_2300_175_p` — PLA Khaki
- `arianeplast_pla_plalightgrey_2300_175_p` — PLA Light grey
- `arianeplast_pla_plametallicaluminum_2300_175_p` — PLA Metallic Aluminum
- `arianeplast_pla_plametallicanthracitegray_2300_175_p` — PLA Metallic Anthracite Gray
- `arianeplast_pla_plametallicblue_2300_175_p` — PLA Metallic blue
- `arianeplast_pla_plametallicinterferentialblue_2300_175_p` — PLA Metallic Interferential Blue
- `arianeplast_pla_plametallicochre_2300_175_p` — PLA metallic ochre
- `arianeplast_pla_plametallicpurple_2300_175_p` — PLA Metallic purple
- `arianeplast_pla_plametallicred_2300_175_p` — PLA Metallic Red
- `arianeplast_pla_plametallicviolet_2300_175_p` — PLA Metallic Violet
- `arianeplast_pla_plamoule_2300_175_p` — PLA Moule
- `arianeplast_pla_plamulticolor_2300_175_p` — PLA Multicolor
- `arianeplast_pla_planatural_2300_175_p` — PLA Natural
- `arianeplast_pla_planavyblue_2300_175_p` — PLA navy blue
- `arianeplast_pla_planoir_2300_175_p` — PLA noir
- `arianeplast_pla_planoirmtallis_2300_175_p` — PLA noir métallisé
- `arianeplast_pla_plaochreorange_2300_175_p` — PLA Ochre Orange
- `arianeplast_pla_plaoyster_2300_175_p` — PLA Oyster
- `arianeplast_pla_plapeach_2300_175_p` — PLA Peach
- `arianeplast_pla_plapearlblue_2300_175_p` — PLA Pearl Blue
- `arianeplast_pla_plapearlwhite_2300_175_p` — PLA Pearl White
- `arianeplast_pla_plapinkbonbon_2300_175_p` — PLA Pink Bonbon
- `arianeplast_pla_plapinkfunky_2300_175_p` — PLA Pink Funky
- `arianeplast_pla_plapistachio_2300_175_p` — PLA Pistachio
- `arianeplast_pla_plarosemetallic_2300_175_p` — PLA Rose Metallic
- `arianeplast_pla_plarosemtallis_2300_175_p` — PLA Rose métallisé
- `arianeplast_pla_plarosetranslucide_2300_175_p` — PLA Rose translucide
- `arianeplast_pla_plarouge_2300_175_p` — PLA rouge
- `arianeplast_pla_plarougemtallis_2300_175_p` — PLA Rouge métallisé
- `arianeplast_pla_plasafetyyellow_2300_175_p` — PLA Safety Yellow
- `arianeplast_pla_plasilver_2300_175_p` — PLA Silver
- `arianeplast_pla_plaskin2r15sp_2300_175_p` — PLA Skin 2R15SP
- `arianeplast_pla_plaskin3y09sp_2300_175_p` — PLA Skin 3Y09SP
- `arianeplast_pla_plaskin5y06sp_2300_175_p` — PLA Skin 5Y06SP
- `arianeplast_pla_plaskin5y09sp_2300_175_p` — PLA Skin 5Y09SP
- `arianeplast_pla_plasky_2300_175_p` — PLA Sky
- `arianeplast_pla_platranslucentblue_2300_175_p` — PLA translucent blue
- `arianeplast_pla_platranslucentbottlegreen_2300_175_p` — PLA Translucent Bottle Green
- `arianeplast_pla_platranslucentgreen_2300_175_p` — PLA Translucent Green
- `arianeplast_pla_platranslucentyellow_2300_175_p` — PLA Translucent Yellow
- `arianeplast_pla_platurquoise_2300_175_p` — PLA Turquoise
- `arianeplast_pla_plaultravioletpantone5f4b8b_2300_175_p` — PLA Ultra Violet Pantone 5F4B8B
- `arianeplast_pla_plavert4043d_2300_175_p` — PLA vert 4043D
- `arianeplast_pla_plavertfluo_2300_175_p` — PLA Vert Fluo
- `arianeplast_pla_plavertmtallis_2300_175_p` — PLA vert métallisé
- `arianeplast_pla_plavertpantone3268c_2300_175_p` — PLA Vert Pantone 3268C
- `arianeplast_pla_plaviolettranslucide_2300_175_p` — PLA Violet translucide
- `arianeplast_pla_playellowgold_2300_175_p` — PLA yellow gold
- `arianeplast_pla_playellowocher_2300_175_p` — PLA Yellow Ocher
- `arianeplast_pla_playellowpantone116u_2300_175_p` — PLA Yellow Pantone 116U
- `arianeplast_pla_plablack_2300_285_p` — PLA Black
- `arianeplast_pla_plawhite_2300_285_p` — PLA White
- `arianeplast_pla_plablue_2300_285_p` — PLA Blue
- `arianeplast_pla_plared_2300_285_p` — PLA Red
- `arianeplast_pla_playellow_2300_285_p` — PLA Yellow
- `arianeplast_pla_plagreen_2300_285_p` — PLA Green
- `arianeplast_pla_plaorange_2300_285_p` — PLA Orange
- `arianeplast_pla_plapurple_2300_285_p` — PLA Purple
- `arianeplast_pla_plapink_2300_285_p` — PLA Pink
- `arianeplast_pla_plaapplegreen_2300_285_p` — PLA apple green
- `arianeplast_pla_plablue/grey_2300_285_p` — PLA blue/grey
- `arianeplast_pla_plabordeaux_2300_285_p` — PLA Bordeaux
- `arianeplast_pla_plabrown_2300_285_p` — PLA brown
- `arianeplast_pla_placopper_2300_285_p` — PLA Copper
- `arianeplast_pla_placoral_2300_285_p` — PLA Coral
- `arianeplast_pla_pladnaanti-counterfeitingblack_2300_285_p` — PLA DNA Anti-counterfeiting Black
- `arianeplast_pla_pladnaanti-counterfeitingwhite_2300_285_p` — PLA DNA Anti-counterfeiting White
- `arianeplast_pla_plaelectricallyconductive_2300_285_p` — PLA Electrically Conductive
- `arianeplast_pla_plafluorescentyellow_2300_285_p` — PLA Fluorescent Yellow
- `arianeplast_pla_plafranceblue_2300_285_p` — PLA France Blue
- `arianeplast_pla_plagold_2300_285_p` — PLA Gold
- `arianeplast_pla_plakhaki_2300_285_p` — PLA Khaki
- `arianeplast_pla_plalightgrey_2300_285_p` — PLA Light grey
- `arianeplast_pla_plametallicaluminum_2300_285_p` — PLA Metallic Aluminum
- `arianeplast_pla_plametallicanthracitegray_2300_285_p` — PLA Metallic Anthracite Gray
- `arianeplast_pla_plametallicblue_2300_285_p` — PLA Metallic blue
- `arianeplast_pla_plametallicinterferentialblue_2300_285_p` — PLA Metallic Interferential Blue
- `arianeplast_pla_plametallicochre_2300_285_p` — PLA metallic ochre
- `arianeplast_pla_plametallicpurple_2300_285_p` — PLA Metallic purple
- `arianeplast_pla_plametallicred_2300_285_p` — PLA Metallic Red
- `arianeplast_pla_plametallicviolet_2300_285_p` — PLA Metallic Violet
- `arianeplast_pla_plamoule_2300_285_p` — PLA Moule
- `arianeplast_pla_plamulticolor_2300_285_p` — PLA Multicolor
- `arianeplast_pla_planatural_2300_285_p` — PLA Natural
- `arianeplast_pla_planavyblue_2300_285_p` — PLA navy blue
- `arianeplast_pla_planoir_2300_285_p` — PLA noir
- `arianeplast_pla_planoirmtallis_2300_285_p` — PLA noir métallisé
- `arianeplast_pla_plaochreorange_2300_285_p` — PLA Ochre Orange
- `arianeplast_pla_plaoyster_2300_285_p` — PLA Oyster
- `arianeplast_pla_plapeach_2300_285_p` — PLA Peach
- `arianeplast_pla_plapearlblue_2300_285_p` — PLA Pearl Blue
- `arianeplast_pla_plapearlwhite_2300_285_p` — PLA Pearl White
- `arianeplast_pla_plapinkbonbon_2300_285_p` — PLA Pink Bonbon
- `arianeplast_pla_plapinkfunky_2300_285_p` — PLA Pink Funky
- `arianeplast_pla_plapistachio_2300_285_p` — PLA Pistachio
- `arianeplast_pla_plarosemetallic_2300_285_p` — PLA Rose Metallic
- `arianeplast_pla_plarosemtallis_2300_285_p` — PLA Rose métallisé
- `arianeplast_pla_plarosetranslucide_2300_285_p` — PLA Rose translucide
- `arianeplast_pla_plarouge_2300_285_p` — PLA rouge
- `arianeplast_pla_plarougemtallis_2300_285_p` — PLA Rouge métallisé
- `arianeplast_pla_plasafetyyellow_2300_285_p` — PLA Safety Yellow
- `arianeplast_pla_plasilver_2300_285_p` — PLA Silver
- `arianeplast_pla_plaskin2r15sp_2300_285_p` — PLA Skin 2R15SP
- `arianeplast_pla_plaskin3y09sp_2300_285_p` — PLA Skin 3Y09SP
- `arianeplast_pla_plaskin5y06sp_2300_285_p` — PLA Skin 5Y06SP
- `arianeplast_pla_plaskin5y09sp_2300_285_p` — PLA Skin 5Y09SP
- `arianeplast_pla_plasky_2300_285_p` — PLA Sky
- `arianeplast_pla_platranslucentblue_2300_285_p` — PLA translucent blue
- `arianeplast_pla_platranslucentbottlegreen_2300_285_p` — PLA Translucent Bottle Green
- `arianeplast_pla_platranslucentgreen_2300_285_p` — PLA Translucent Green
- `arianeplast_pla_platranslucentyellow_2300_285_p` — PLA Translucent Yellow
- `arianeplast_pla_platurquoise_2300_285_p` — PLA Turquoise
- `arianeplast_pla_plaultravioletpantone5f4b8b_2300_285_p` — PLA Ultra Violet Pantone 5F4B8B
- `arianeplast_pla_plavert4043d_2300_285_p` — PLA vert 4043D
- `arianeplast_pla_plavertfluo_2300_285_p` — PLA Vert Fluo
- `arianeplast_pla_plavertmtallis_2300_285_p` — PLA vert métallisé
- `arianeplast_pla_plavertpantone3268c_2300_285_p` — PLA Vert Pantone 3268C
- `arianeplast_pla_plaviolettranslucide_2300_285_p` — PLA Violet translucide
- `arianeplast_pla_playellowgold_2300_285_p` — PLA yellow gold
- `arianeplast_pla_playellowocher_2300_285_p` — PLA Yellow Ocher
- `arianeplast_pla_playellowpantone116u_2300_285_p` — PLA Yellow Pantone 116U
- `arianeplast_petg_petgblack_1000_175_p` — PETG Black
- `arianeplast_petg_petgwhite_1000_175_p` — PETG White
- `arianeplast_petg_petggrey_1000_175_p` — PETG Grey
- `arianeplast_petg_petgblue_1000_175_p` — PETG Blue
- `arianeplast_petg_petgred_1000_175_p` — PETG Red
- `arianeplast_petg_petgtransparent_1000_175_p` — PETG Transparent
- `arianeplast_petg_petgblack_1000_285_p` — PETG Black
- `arianeplast_petg_petgwhite_1000_285_p` — PETG White
- `arianeplast_petg_petggrey_1000_285_p` — PETG Grey
- `arianeplast_petg_petgblue_1000_285_p` — PETG Blue
- `arianeplast_petg_petgred_1000_285_p` — PETG Red
- `arianeplast_petg_petgtransparent_1000_285_p` — PETG Transparent
- `arianeplast_abs_absblack_1000_175_p` — ABS Black
- `arianeplast_abs_abswhite_1000_175_p` — ABS White
- `arianeplast_abs_absgrey_1000_175_p` — ABS Grey
- `arianeplast_abs_absred_1000_175_p` — ABS Red
- `arianeplast_asa_asablack_1000_175_p` — ASA Black
- `arianeplast_asa_asawhite_1000_175_p` — ASA White
- `arianeplast_asa_asagrey_1000_175_p` — ASA Grey
- `arianeplast_pla_placfcarbon_1000_175_p` — PLA CF Carbon
- `arianeplast_pla_glowplaphosphorescent_1000_175_p` — Glow PLA Phosphorescent
- `arianeplast_pla_silkplablack_1000_175_p` — Silk PLA Black
- `arianeplast_pla_silkplablue_1000_175_p` — Silk PLA Blue
- `arianeplast_pla_silkplagray_1000_175_p` — Silk PLA Gray
- `arianeplast_pla_silkplarose_1000_175_p` — Silk PLA Rose
- `arianeplast_pla_silkplawhite_1000_175_p` — Silk PLA White
