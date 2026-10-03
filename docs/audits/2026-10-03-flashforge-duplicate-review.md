# flashforge duplicate migration review

Base `a34dfa4a289dccdccb0138cc5bfb84c847cce2d4`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `8f529c8189786635f2ca5371e14885f3c7fadac4606b63b080ef14f86bf8e5ca`.

## Authorization and result

{"groups": 2, "approved_groups": 0, "retired": 0, "deferred": 2, "hard_stops": 0, "before_count": 51702, "after_count": 51702, "brand_before": 240, "brand_after": 240, "registry_before": 1732, "registry_after": 1732, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Two same-template500g/1kg Gray/Grey ties, HEX515F6C versus4D6383, no same-SKU proof; deferred. ExistingPLA1.25/210/60 fits exactPLATDS but no changes on deferred groups. Packaging/tare unchanged.

This is an audit-only result: no records are retired and no catalog migration is applied. Packaging, tare and all identities remain unchanged. Future reviewed retirements would not redirect external catalog lookups automatically.

## Current first-party evidence

- {"url": "https://after-support.flashforge.jp/uploads/datasheet/tds/PLA_TDS_EN.pdf", "density": "1.25–1.26", "nozzle": [190, 220], "bed": "roomtemperature–60", "preferred": [210, 40]}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|

## Per-group decisions and unresolved metadata

### FF001: dup-15c8883805cac462222e42d5763dbfab2f54df800525bb26ddd39e3ed8c276ed

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`flashforge_pla_pla-gray_500_175_p`|`PLA - {color_name}`|`Gray`|{"source_file": "flashforge.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 34, "compiled_records": 68} / True|
|`flashforge_pla_pla-grey_500_175_p`|`PLA - {color_name}`|`Grey`|{"source_file": "flashforge.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 34, "compiled_records": 68} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "flashforge_pla_pla-gray_500_175_p": "515F6C",
    "flashforge_pla_pla-grey_500_175_p": "4D6383"
  }
}
```

### FF002: dup-dc7234d241e0e6efd95b5b3e2d225d674862404f4400033bb3902ca3f5a2fc4f

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`flashforge_pla_pla-gray_1000_175_p`|`PLA - {color_name}`|`Gray`|{"source_file": "flashforge.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 34, "compiled_records": 68} / True|
|`flashforge_pla_pla-grey_1000_175_p`|`PLA - {color_name}`|`Grey`|{"source_file": "flashforge.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 34, "compiled_records": 68} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "flashforge_pla_pla-gray_1000_175_p": "515F6C",
    "flashforge_pla_pla-grey_1000_175_p": "4D6383"
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

- `flashforge_pla_pla-black_500_175_p` — PLA - Black
- `flashforge_pla_pla-white_500_175_p` — PLA - White
- `flashforge_pla_pla-natural_500_175_p` — PLA - Natural
- `flashforge_pla_pla-skin_500_175_p` — PLA - Skin
- `flashforge_pla_pla-red_500_175_p` — PLA - Red
- `flashforge_pla_pla-blue_500_175_p` — PLA - Blue
- `flashforge_pla_pla-yellow_500_175_p` — PLA - Yellow
- `flashforge_pla_pla-green_500_175_p` — PLA - Green
- `flashforge_pla_pla-orange_500_175_p` — PLA - Orange
- `flashforge_pla_pla-silver_500_175_p` — PLA - Silver
- `flashforge_pla_pla-lightgreen_500_175_p` — PLA - Light Green
- `flashforge_pla_pla-pink_500_175_p` — PLA - Pink
- `flashforge_pla_pla-purple_500_175_p` — PLA - Purple
- `flashforge_pla_pla-brown_500_175_p` — PLA - Brown
- `flashforge_pla_pla-gold_500_175_p` — PLA - Gold
- `flashforge_pla_pla-bluetopinkgradient_500_175_p` — PLA - Blue to Pink Gradient
- `flashforge_pla_pla-bluetoyellowgradient_500_175_p` — PLA - Blue to Yellow Gradient
- `flashforge_pla_pla-burnttitanium_500_175_p` — PLA - Burnt Titanium
- `flashforge_pla_pla-flexiblegreen_500_175_p` — PLA - Flexible Green
- `flashforge_pla_pla-flexiblenatural_500_175_p` — PLA - Flexible Natural
- `flashforge_pla_pla-flexibleorange_500_175_p` — PLA - Flexible Orange
- `flashforge_pla_pla-flexiblepurple_500_175_p` — PLA - Flexible Purple
- `flashforge_pla_pla-flexiblered_500_175_p` — PLA - Flexible Red
- `flashforge_pla_pla-flexibleyellow_500_175_p` — PLA - Flexible Yellow
- `flashforge_pla_pla-galaxyblue_500_175_p` — PLA - Galaxy Blue
- `flashforge_pla_pla-marsala_500_175_p` — PLA - Marsala
- `flashforge_pla_pla-orangetogreengradient_500_175_p` — PLA - Orange to Green Gradient
- `flashforge_pla_pla-rainbow_500_175_p` — PLA - Rainbow
- `flashforge_pla_pla-rose_500_175_p` — PLA - Rose
- `flashforge_pla_pla-skydiverblue_500_175_p` — PLA - Skydiver Blue
- `flashforge_pla_pla-sparkleclear_500_175_p` — PLA - Sparkle Clear
- `flashforge_pla_pla-tangerine_500_175_p` — PLA - Tangerine
- `flashforge_pla_pla-black_1000_175_p` — PLA - Black
- `flashforge_pla_pla-white_1000_175_p` — PLA - White
- `flashforge_pla_pla-natural_1000_175_p` — PLA - Natural
- `flashforge_pla_pla-skin_1000_175_p` — PLA - Skin
- `flashforge_pla_pla-red_1000_175_p` — PLA - Red
- `flashforge_pla_pla-blue_1000_175_p` — PLA - Blue
- `flashforge_pla_pla-yellow_1000_175_p` — PLA - Yellow
- `flashforge_pla_pla-green_1000_175_p` — PLA - Green
- `flashforge_pla_pla-orange_1000_175_p` — PLA - Orange
- `flashforge_pla_pla-silver_1000_175_p` — PLA - Silver
- `flashforge_pla_pla-lightgreen_1000_175_p` — PLA - Light Green
- `flashforge_pla_pla-pink_1000_175_p` — PLA - Pink
- `flashforge_pla_pla-purple_1000_175_p` — PLA - Purple
- `flashforge_pla_pla-brown_1000_175_p` — PLA - Brown
- `flashforge_pla_pla-gold_1000_175_p` — PLA - Gold
- `flashforge_pla_pla-bluetopinkgradient_1000_175_p` — PLA - Blue to Pink Gradient
- `flashforge_pla_pla-bluetoyellowgradient_1000_175_p` — PLA - Blue to Yellow Gradient
- `flashforge_pla_pla-burnttitanium_1000_175_p` — PLA - Burnt Titanium
- `flashforge_pla_pla-flexiblegreen_1000_175_p` — PLA - Flexible Green
- `flashforge_pla_pla-flexiblenatural_1000_175_p` — PLA - Flexible Natural
- `flashforge_pla_pla-flexibleorange_1000_175_p` — PLA - Flexible Orange
- `flashforge_pla_pla-flexiblepurple_1000_175_p` — PLA - Flexible Purple
- `flashforge_pla_pla-flexiblered_1000_175_p` — PLA - Flexible Red
- `flashforge_pla_pla-flexibleyellow_1000_175_p` — PLA - Flexible Yellow
- `flashforge_pla_pla-galaxyblue_1000_175_p` — PLA - Galaxy Blue
- `flashforge_pla_pla-marsala_1000_175_p` — PLA - Marsala
- `flashforge_pla_pla-orangetogreengradient_1000_175_p` — PLA - Orange to Green Gradient
- `flashforge_pla_pla-rainbow_1000_175_p` — PLA - Rainbow
- `flashforge_pla_pla-rose_1000_175_p` — PLA - Rose
- `flashforge_pla_pla-skydiverblue_1000_175_p` — PLA - Skydiver Blue
- `flashforge_pla_pla-sparkleclear_1000_175_p` — PLA - Sparkle Clear
- `flashforge_pla_pla-tangerine_1000_175_p` — PLA - Tangerine
- `flashforge_pla_starterpla-red_250_175_p` — Starter PLA - Red
- `flashforge_pla_plapro-natural_1000_175_p` — PLA Pro - Natural
- `flashforge_pla_plapro-white_1000_175_p` — PLA Pro - White
- `flashforge_pla_plapro-coolwhite_1000_175_p` — PLA Pro - Cool White
- `flashforge_pla_plapro-black_1000_175_p` — PLA Pro - Black
- `flashforge_pla_plapro-gray_1000_175_p` — PLA Pro - Gray
- `flashforge_pla_plapro-silvergray_1000_175_p` — PLA Pro - Silver Gray
- `flashforge_pla_plapro-silver_1000_175_p` — PLA Pro - Silver
- `flashforge_pla_plapro-skin_1000_175_p` — PLA Pro - Skin
- `flashforge_pla_plapro-yellow_1000_175_p` — PLA Pro - Yellow
- `flashforge_pla_plapro-green_1000_175_p` — PLA Pro - Green
- `flashforge_pla_plapro-lightblue_1000_175_p` — PLA Pro - Light Blue
- `flashforge_pla_plapro-blue_1000_175_p` — PLA Pro - Blue
- `flashforge_pla_plapro-red_1000_175_p` — PLA Pro - Red
- `flashforge_pla_plapro-lightyellow_1000_175_p` — PLA Pro - Light Yellow
- `flashforge_pla_plapro-rose_1000_175_p` — PLA Pro - Rose
- `flashforge_pla_plapro-pink_1000_175_p` — PLA Pro - Pink
- `flashforge_pla_plapro-purple_1000_175_p` — PLA Pro - Purple
- `flashforge_pla_plapro-orange_1000_175_p` — PLA Pro - Orange
- `flashforge_pla_plapro-lightgreen_1000_175_p` — PLA Pro - Light Green
- `flashforge_pla_plapro-gold_1000_175_p` — PLA Pro - Gold
- `flashforge_pla_plapro-brown_1000_175_p` — PLA Pro - Brown
- `flashforge_pla_plapro-lightred_1000_175_p` — PLA Pro - Light Red
- `flashforge_pla_plapro-trafficred_1000_175_p` — PLA Pro - Traffic Red
- `flashforge_pla_plapro-lightorange_1000_175_p` — PLA Pro - Light Orange
- `flashforge_abs_absblue_1000_175_p` — ABS Blue
- `flashforge_abs_absorange_1000_175_p` — ABS Orange
- `flashforge_abs_absred_1000_175_p` — ABS Red
- `flashforge_abs_abswhite_1000_175_p` — ABS White
- `flashforge_abs_dseriesabsorange_1000_175_p` — D Series ABS Orange
- `flashforge_asa_asablack_1000_175_p` — ASA Black
- `flashforge_asa_asablue_1000_175_p` — ASA Blue
- `flashforge_asa_asaburnttitanium_1000_175_p` — ASA Burnt Titanium
- `flashforge_asa_asagreen_1000_175_p` — ASA Green
- `flashforge_asa_asairongrey_1000_175_p` — ASA Iron Grey
- `flashforge_asa_asanatural_1000_175_p` — ASA Natural
- `flashforge_asa_asaskyblue_1000_175_p` — ASA Sky Blue
- `flashforge_asa_asasparkleblack_1000_175_p` — ASA Sparkle Black
- `flashforge_asa_asasparkleblackgreen_1000_175_p` — ASA Sparkle Black Green
- `flashforge_asa_asasparkleblue_1000_175_p` — ASA Sparkle Blue
- `flashforge_asa_asasparklered_1000_175_p` — ASA Sparkle Red
- `flashforge_asa_asasparkleskyblue_1000_175_p` — ASA Sparkle Sky Blue
- `flashforge_asa_asasparklewhite_1000_175_p` — ASA Sparkle White
- `flashforge_asa_asatrafficred_1000_175_p` — ASA Traffic Red
- `flashforge_asa_asawhite_1000_175_p` — ASA White
- `flashforge_asa_asabasicblack_1000_175_p` — ASA Basic Black
- `flashforge_asa_asabasicmulticolorburnttitanium_1000_175_p` — ASA Basic Multicolor Burnt Titanium
- `flashforge_asa_asabasicwhite_1000_175_p` — ASA Basic White
- `flashforge_petg_chameleonpetgburnttitanium_1000_175_p` — Chameleon PETG Burnt Titanium
- `flashforge_petg_chameleonpetgnebulapurple_1000_175_p` — Chameleon PETG Nebula Purple
- `flashforge_petg_metallicrapidsilkpetggreen_1000_175_p` — Metallic Rapid Silk PETG Green
- `flashforge_petg_metallicrapidsilkpetgpurple_1000_175_p` — Metallic Rapid Silk PETG Purple
- `flashforge_petg_petgblack_1000_175_p` — PETG Black
- `flashforge_petg_petgburnttitanium_1000_175_p` — PETG Burnt Titanium
- `flashforge_petg_petgclear/natural_1000_175_p` — PETG Clear/Natural
- `flashforge_petg_petggreen_1000_175_p` — PETG Green
- `flashforge_petg_petggrey_1000_175_p` — PETG Grey
- `flashforge_petg_petgnatural_1000_175_p` — PETG Natural
- `flashforge_petg_petgpurple_1000_175_p` — PETG Purple
- `flashforge_petg_petgred_1000_175_p` — PETG Red
- `flashforge_petg_petgyellow_1000_175_p` — PETG Yellow
- `flashforge_petg_petgcfblack_1000_175_p` — PETG CF Black
- `flashforge_petg_petgcfgrassgreen_1000_175_p` — PETG CF Grass Green
- `flashforge_petg_rapidpetgblack_1000_175_p` — Rapid PETG Black
- `flashforge_petg_rapidpetgburnttitanium_1000_175_p` — Rapid PETG Burnt Titanium
- `flashforge_petg_rapidpetgmetallicblue_1000_175_p` — Rapid PETG Metallic Blue
- `flashforge_petg_rapidpetgmetallicbrightgold_1000_175_p` — Rapid PETG Metallic Bright Gold
- `flashforge_petg_rapidpetgnatural_1000_175_p` — Rapid PETG Natural
- `flashforge_petg_rapidpetgwhite_1000_175_p` — Rapid PETG White
- `flashforge_pla_gradientrapidchameleonplabluepink_1000_175_p` — Gradient Rapid Chameleon PLA Blue Pink
- `flashforge_pla_gradientrapidchameleonplayellowgreen_1000_175_p` — Gradient Rapid Chameleon PLA Yellow Green
- `flashforge_pla_gradientrapidchameleonplayellowpink_1000_175_p` — Gradient Rapid Chameleon PLA Yellow Pink
- `flashforge_pla_highspeedplablack_1000_175_p` — High Speed PLA Black
- `flashforge_pla_matteplablue_1000_175_p` — Matte PLA Blue
- `flashforge_pla_matteplagalaxyblack_1000_175_p` — Matte PLA Galaxy Black
- `flashforge_pla_matteplagreen_1000_175_p` — Matte PLA Green
- `flashforge_pla_matteplapurple_1000_175_p` — Matte PLA Purple
- `flashforge_pla_matteplared_1000_175_p` — Matte PLA Red
- `flashforge_pla_matteplayellow_1000_175_p` — Matte PLA Yellow
- `flashforge_pla_placfblack_1000_175_p` — PLA CF Black
- `flashforge_pla_placfdustypink_1000_175_p` — PLA CF Dusty Pink
- `flashforge_pla_placfirispurple_1000_175_p` — PLA CF Iris Purple
- `flashforge_pla_placfmarsala_1000_175_p` — PLA CF Marsala
- `flashforge_pla_placfmidnightblue_1000_175_p` — PLA CF Midnight Blue
- `flashforge_pla_placfsailorblue_1000_175_p` — PLA CF Sailor Blue
- `flashforge_pla_placfvolcanicrockgray_1000_175_p` — PLA CF Volcanic Rock Gray
- `flashforge_pla_rapidchameleonplaabyssalpurple_1000_175_p` — Rapid Chameleon PLA Abyssal Purple
- `flashforge_pla_rapidchameleonplaabyssalrede_1000_175_p` — Rapid Chameleon PLA Abyssal Rede
- `flashforge_pla_rapidchameleonplaburnttitanium_1000_175_p` — Rapid Chameleon PLA Burnt Titanium
- `flashforge_pla_rapidchameleonplaburnttitaniumabyssalrede_1000_175_p` — Rapid Chameleon PLA Burnt Titanium Abyssal Rede
- `flashforge_pla_rapidchameleonplaburnttitaniumnebulapurple_1000_175_p` — Rapid Chameleon PLA Burnt Titanium Nebula Purple
- `flashforge_pla_rapidchameleonplanebulapurple_1000_175_p` — Rapid Chameleon PLA Nebula Purple
- `flashforge_pla_rapidglowpladarkgreen_1000_175_p` — Rapid Glow PLA Dark Green
- `flashforge_pla_rapidglowpladarkpurple_1000_175_p` — Rapid Glow PLA Dark Purple
- `flashforge_pla_rapidglowpladarkred_1000_175_p` — Rapid Glow PLA Dark Red
- `flashforge_pla_rapidglowpladarkyellow_1000_175_p` — Rapid Glow PLA Dark Yellow
- `flashforge_pla_rapidglowplaluminousblue_1000_175_p` — Rapid Glow PLA Luminous Blue
- `flashforge_pla_rapidglowplaluminousgreen_1000_175_p` — Rapid Glow PLA Luminous Green
- `flashforge_pla_rapidglowplaluminousmelody_1000_175_p` — Rapid Glow PLA Luminous Melody
- `flashforge_pla_rapidglowplaluminouspurple_1000_175_p` — Rapid Glow PLA Luminous Purple
- `flashforge_pla_rapidglowplaluminousred_1000_175_p` — Rapid Glow PLA Luminous Red
- `flashforge_pla_rapidglowplaluminousyellow_1000_175_p` — Rapid Glow PLA Luminous Yellow
- `flashforge_pla_rapidglowplarainbowmelody_1000_175_p` — Rapid Glow PLA Rainbow Melody
- `flashforge_pla_rapidplaabyssalred_1000_175_p` — Rapid PLA Abyssal Red
- `flashforge_pla_rapidplaaurorablue_1000_175_p` — Rapid PLA Aurora Blue
- `flashforge_pla_rapidplaauroragreen_1000_175_p` — Rapid PLA Aurora Green
- `flashforge_pla_rapidplaaurorapurple_1000_175_p` — Rapid PLA Aurora Purple
- `flashforge_pla_rapidplaaurorared_1000_175_p` — Rapid PLA Aurora Red
- `flashforge_pla_rapidplablack_1000_175_p` — Rapid PLA Black
- `flashforge_pla_rapidplabluetopinkgradient_1000_175_p` — Rapid PLA Blue To Pink Gradient
- `flashforge_pla_rapidplaburnttitanium_1000_175_p` — Rapid PLA Burnt Titanium
- `flashforge_pla_rapidplaburnttitaniumtoabyssalredgradient_1000_175_p` — Rapid PLA Burnt Titanium To Abyssal Red Gradient
- `flashforge_pla_rapidplachocolatebrown_1000_175_p` — Rapid PLA Chocolate Brown
- `flashforge_pla_rapidplagradientrainbowcandy_1000_175_p` — Rapid PLA Gradient Rainbow Candy
- `flashforge_pla_rapidplagradientrainbowcorals_1000_175_p` — Rapid PLA Gradient Rainbow Corals
- `flashforge_pla_rapidplagradientsummerreverie_1000_175_p` — Rapid PLA Gradient Summer Reverie
- `flashforge_pla_rapidplagradientthistlepurpleetherealblue_1000_175_p` — Rapid PLA Gradient Thistle Purple Ethereal Blue
- `flashforge_pla_rapidplagradientyellowblue_1000_175_p` — Rapid PLA Gradient Yellow Blue
- `flashforge_pla_rapidplaiceblue_1000_175_p` — Rapid PLA Ice Blue
- `flashforge_pla_rapidplairongrey_1000_175_p` — Rapid PLA Iron Grey
- `flashforge_pla_rapidplalightbrown_1000_175_p` — Rapid PLA Light Brown
- `flashforge_pla_rapidplalightgreen_1000_175_p` — Rapid PLA Light Green
- `flashforge_pla_rapidplalightgrey_1000_175_p` — Rapid PLA Light Grey
- `flashforge_pla_rapidplamarbleblack_1000_175_p` — Rapid PLA Marble Black
- `flashforge_pla_rapidplamarbleblue_1000_175_p` — Rapid PLA Marble Blue
- `flashforge_pla_rapidplamarblered_1000_175_p` — Rapid PLA Marble Red
- `flashforge_pla_rapidplanatural_1000_175_p` — Rapid PLA Natural
- `flashforge_pla_rapidplaneroyellow_1000_175_p` — Rapid PLA Nero Yellow
- `flashforge_pla_rapidplaorange_1000_175_p` — Rapid PLA Orange
- `flashforge_pla_rapidplapearlgentianblue_1000_175_p` — Rapid PLA Pearl Gentian Blue
- `flashforge_pla_rapidplapinkwhitegradient_1000_175_p` — Rapid PLA Pink White Gradient
- `flashforge_pla_rapidplapurple_1000_175_p` — Rapid PLA Purple
- `flashforge_pla_rapidplarainbowcandy_1000_175_p` — Rapid PLA Rainbow Candy
- `flashforge_pla_rapidplarubyred_1000_175_p` — Rapid PLA Ruby Red
- `flashforge_pla_rapidplawhite_1000_175_p` — Rapid PLA White
- `flashforge_pla_rapidplayellow_1000_175_p` — Rapid PLA Yellow
- `flashforge_pla_rapidplayellowtopinkgradient_1000_175_p` — Rapid PLA Yellow To Pink Gradient
- `flashforge_pla_silkplablack_1000_175_p` — Silk PLA Black
- `flashforge_pla_silkplablue_1000_175_p` — Silk PLA Blue
- `flashforge_pla_silkplablueandgreen2in1_1000_175_p` — Silk PLA Blue and Green 2 in 1
- `flashforge_pla_silkplablueandgreen3in1_1000_175_p` — Silk PLA Blue and Green 3 in 1
- `flashforge_pla_silkplablueandrose2in1_1000_175_p` — Silk PLA Blue and Rose 2 in 1
- `flashforge_pla_silkplabrightgold_1000_175_p` — Silk PLA Bright Gold
- `flashforge_pla_silkplabronze_1000_175_p` — Silk PLA Bronze
- `flashforge_pla_silkplacoffee_1000_175_p` — Silk PLA Coffee
- `flashforge_pla_silkplacopper_1000_175_p` — Silk PLA Copper
- `flashforge_pla_silkpladreamytrio_1000_175_p` — Silk PLA Dreamy Trio
- `flashforge_pla_silkpladualcolorbluerose_1000_175_p` — Silk PLA Dual Color Blue Rose
- `flashforge_pla_silkpladualcolorbrightblue&green_1000_175_p` — Silk PLA Dual Color Bright Blue & Green
- `flashforge_pla_silkpladualcolorgold&rose_1000_175_p` — Silk PLA Dual Color Gold & Rose
- `flashforge_pla_silkpladualcolorpink&yellow_1000_175_p` — Silk PLA Dual Color Pink & Yellow
- `flashforge_pla_silkpladualcoloryellowandgreen2in1_1000_175_p` — Silk PLA Dual Color Yellow and Green 2 in 1
- `flashforge_pla_silkplagoldandrose2in1_1000_175_p` — Silk PLA Gold and Rose 2 in 1
- `flashforge_pla_silkplagoldtoredgradient_1000_175_p` — Silk PLA Gold to Red Gradient
- `flashforge_pla_silkplagradientdreamytrio_1000_175_p` — Silk PLA Gradient Dreamy Trio
- `flashforge_pla_silkplagradientgoldtored_1000_175_p` — Silk PLA Gradient Gold to Red
- `flashforge_pla_silkplagradientmetalrainbow_1000_175_p` — Silk PLA Gradient Metal Rainbow
- `flashforge_pla_silkplagradientrainbowcandy_1000_175_p` — Silk PLA Gradient Rainbow Candy
- `flashforge_pla_silkplagradientsilvertoblue_1000_175_p` — Silk PLA Gradient Silver to Blue
- `flashforge_pla_silkplagreen_1000_175_p` — Silk PLA Green
- `flashforge_pla_silkplametalgrey_1000_175_p` — Silk PLA Metal Grey
- `flashforge_pla_silkplapurple_1000_175_p` — Silk PLA Purple
- `flashforge_pla_silkplarainbow_1000_175_p` — Silk PLA Rainbow
- `flashforge_pla_silkplarainbowwaltz_1000_175_p` — Silk PLA Rainbow Waltz
- `flashforge_pla_silkplaranbowcandy_1000_175_p` — Silk PLA Ranbow Candy
- `flashforge_pla_silkplared_1000_175_p` — Silk PLA Red
- `flashforge_pla_silkplasilver_1000_175_p` — Silk PLA Silver
- `flashforge_pla_silkplaskin_1000_175_p` — Silk PLA Skin
- `flashforge_pla_silkplatri-color_1000_175_p` — Silk PLA Tri-Color
- `flashforge_pla_silkplatri-colorred&yellow&blue_1000_175_p` — Silk PLA Tri-Color Red & Yellow & Blue
- `flashforge_pla_silkplaviolet_1000_175_p` — Silk PLA Violet
- `flashforge_pla_silkplawhite_1000_175_p` — Silk PLA White
