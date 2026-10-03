# paramount3d duplicate migration review

Base `fdd0d3886eecd693d8a52ede70c6d7c63639063e`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `88aca11cc43b8b9ac7a663c1f7abe42503d1c893a550f74caeaf506b3c371817`.

## Authorization and result

{"groups": 115, "approved_groups": 114, "retired": 114, "deferred": 1, "hard_stops": 0, "before_count": 52689, "after_count": 52575, "brand_before": 266, "brand_after": 152, "registry_before": 745, "registry_after": 859, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Keep approved older prefixed survivor values. Current exact ASA Decepticon Purple and PETG Iron Red product-page nozzle/bed ranges match those survivors; current PLA MBT Brown page supplies no numeric density/nozzle/bed. No density correction inferred. Other values/HEX conflicts remain unresolved. No packaging/tare changes; no official product-page lot/package extrapolation.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"material": "ASA", "name": "ASA (Decepticon Purple)", "sku": "PRL40077449SA", "url": "https://www.paramount-3d.com/product-page/paramount-3d-asa-decepticon-purple-1-75mm-1kg-filament-derl7006g09sa-a", "nozzle": [220, 260], "bed": [100, 110], "fetched_at": "2026-10-03T16:01:51.902371+00:00", "status": 200, "sha256": "2118ebc55a3900a07081b0adfae0af224df68e8a9bbc12017e7eadf6a33782af", "scope": "Exact product-page spot-check only; not wholesale approval or a lot/package matrix"}
- {"material": "PLA", "name": "PLA (Military MBT Brown)", "sku": "MGRL80007560C", "url": "https://www.paramount-3d.com/product-page/pla-military-mbt-brown-1-75mm-1kg-filament-mgrl80007560c", "fetched_at": "2026-10-03T16:01:56.647086+00:00", "status": 200, "sha256": "70e2d0d7160a7eb4ddf58b0e2fd3a69b77af6f18bd3ba50bbb96f77cba67399c", "scope": "Exact product-page spot-check only; not wholesale approval or a lot/package matrix"}
- {"material": "PETG", "name": "PETG (Iron Red)", "sku": "IRRL30111815G", "url": "https://www.paramount-3d.com/product-page/petg-pantone-iron-red-1815c-1-75mm-1kg-filament-irrl30111815c", "nozzle": [220, 260], "bed": [60, 80], "fetched_at": "2026-10-03T16:02:00.767605+00:00", "status": 200, "sha256": "fd2d1d1c0f5d62a24549cacfdaf8dfa982b17dee4f87b2cf6322673c80907cb3", "scope": "Exact product-page spot-check only; not wholesale approval or a lot/package matrix"}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`paramount3d_abs_abs(autobotblue)_1000_175_p`|`paramount3d_abs_paramount3dabsautobotblue_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Autobot Blue)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(battleshipgray)_1000_175_p`|`paramount3d_abs_paramount3dabsbattleshipgray_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Battleship Gray)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(black)_1000_175_p`|`paramount3d_abs_paramount3dabsblack_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Black)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(blackcherry)_1000_175_p`|`paramount3d_abs_paramount3dabsblackcherry_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Black Cherry)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(britishracinggreen)_1000_175_p`|`paramount3d_abs_paramount3dabsbritishracinggreen_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (British Racing Green)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(castlelimestonegray)_1000_175_p`|`paramount3d_abs_paramount3dabscastlelimestonegray_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Castle Limestone Gray)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(clear)_1000_175_p`|`paramount3d_abs_paramount3dabsclear_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Clear)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(decepticonpurple)_1000_175_p`|`paramount3d_abs_paramount3dabsdecepticonpurple_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Decepticon Purple)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(enzored)_1000_175_p`|`paramount3d_abs_paramount3dabsenzored_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Enzo Red)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(fighterjetblue)_1000_175_p`|`paramount3d_abs_paramount3dabsfighterjetblue_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Fighter Jet Blue)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(gamecartridgegray)_1000_175_p`|`paramount3d_abs_paramount3dabsgamecartridgegray_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Game Cartridge Gray)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(goldkrugerrand)_1000_175_p`|`paramount3d_abs_paramount3dabsgoldkrugerrand_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Gold Krugerrand)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(graphitegray)_1000_175_p`|`paramount3d_abs_paramount3dabsgraphitegray_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Graphite Gray)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(harajukupink)_1000_175_p`|`paramount3d_abs_paramount3dabsharajukupink_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Harajuku Pink)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(ironred)_1000_175_p`|`paramount3d_abs_paramount3dabsironred_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Iron Red)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(mclarenorange)_1000_175_p`|`paramount3d_abs_paramount3dabsmclarenorange_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (McLaren Orange)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(midcenturymodernteal)_1000_175_p`|`paramount3d_abs_paramount3dabsmidcenturymodernteal_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Mid Century Modern Teal)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(militarygreen)_1000_175_p`|`paramount3d_abs_paramount3dabsmilitarygreen_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Military Green)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(militarykhaki)_1000_175_p`|`paramount3d_abs_paramount3dabsmilitarykhaki_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Military Khaki)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(militarymbtbrown)_1000_175_p`|`paramount3d_abs_paramount3dabsmilitarymbtbrown_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Military MBT Brown)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(primordialearth)_1000_175_p`|`paramount3d_abs_paramount3dabsprimordialearth_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Primordial Earth)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(prototypegray)_1000_175_p`|`paramount3d_abs_paramount3dabsprototypegray_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Prototype Gray)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(silverdollar)_1000_175_p`|`paramount3d_abs_paramount3dabssilverdollar_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Silver Dollar)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(simpsonyellow)_1000_175_p`|`paramount3d_abs_paramount3dabssimpsonyellow_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Simpson Yellow)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(skin-darkcomplexion)_1000_175_p`|`paramount3d_abs_paramount3dabsskin-darkcomplexion_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Skin - Dark Complexion)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(skin-faircomplexion)_1000_175_p`|`paramount3d_abs_paramount3dabsskin-faircomplexion_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Skin - Fair Complexion)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(skin-ivory)_1000_175_p`|`paramount3d_abs_paramount3dabsskin-ivory_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Skin - Ivory)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(skin-universalbeige)_1000_175_p`|`paramount3d_abs_paramount3dabsskin-universalbeige_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Skin - Universal Beige)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(steelgray)_1000_175_p`|`paramount3d_abs_paramount3dabssteelgray_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Steel Gray)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(terracotta)_1000_175_p`|`paramount3d_abs_paramount3dabsterracotta_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (Terra Cotta)::ABS::1000::1.75::plastic::False`|
|`paramount3d_abs_abs(white)_1000_175_p`|`paramount3d_abs_paramount3dabswhite_1000_175_p`|`paramount3d.json::Paramount 3D::ABS {color_name}::ABS (White)::ABS::1000::1.75::plastic::False`|
|`paramount3d_asa_asa(black)_1000_175_p`|`paramount3d_asa_paramount3dasablack_1000_175_p`|`paramount3d.json::Paramount 3D::ASA {color_name}::ASA (Black)::ASA::1000::1.75::plastic::False`|
|`paramount3d_asa_asa(decepticonpurple)_1000_175_p`|`paramount3d_asa_paramount3dasadecepticonpurple_1000_175_p`|`paramount3d.json::Paramount 3D::ASA {color_name}::ASA (Decepticon Purple)::ASA::1000::1.75::plastic::False`|
|`paramount3d_asa_asa(enzored)_1000_175_p`|`paramount3d_asa_paramount3dasaenzored_1000_175_p`|`paramount3d.json::Paramount 3D::ASA {color_name}::ASA (Enzo Red)::ASA::1000::1.75::plastic::False`|
|`paramount3d_asa_asa(graphitegray)_1000_175_p`|`paramount3d_asa_paramount3dasagraphitegray_1000_175_p`|`paramount3d.json::Paramount 3D::ASA {color_name}::ASA (Graphite Gray)::ASA::1000::1.75::plastic::False`|
|`paramount3d_asa_asa(ironred)_1000_175_p`|`paramount3d_asa_paramount3dasaironred_1000_175_p`|`paramount3d.json::Paramount 3D::ASA {color_name}::ASA (Iron Red)::ASA::1000::1.75::plastic::False`|
|`paramount3d_asa_asa(mclarenorange)_1000_175_p`|`paramount3d_asa_paramount3dasamclarenorange_1000_175_p`|`paramount3d.json::Paramount 3D::ASA {color_name}::ASA (McLaren Orange)::ASA::1000::1.75::plastic::False`|
|`paramount3d_asa_asa(militarygreen)_1000_175_p`|`paramount3d_asa_paramount3dasamilitarygreen_1000_175_p`|`paramount3d.json::Paramount 3D::ASA {color_name}::ASA (Military Green)::ASA::1000::1.75::plastic::False`|
|`paramount3d_asa_asa(militarykhaki)_1000_175_p`|`paramount3d_asa_paramount3dasamilitarykhaki_1000_175_p`|`paramount3d.json::Paramount 3D::ASA {color_name}::ASA (Military Khaki)::ASA::1000::1.75::plastic::False`|
|`paramount3d_asa_asa(primordialearth)_1000_175_p`|`paramount3d_asa_paramount3dasaprimordialearth_1000_175_p`|`paramount3d.json::Paramount 3D::ASA {color_name}::ASA (Primordial Earth)::ASA::1000::1.75::plastic::False`|
|`paramount3d_asa_asa(stealthgray)_1000_175_p`|`paramount3d_asa_paramount3dasastealthgray_1000_175_p`|`paramount3d.json::Paramount 3D::ASA {color_name}::ASA (Stealth Gray)::ASA::1000::1.75::plastic::False`|
|`paramount3d_asa_asa(vaporgray)_1000_175_p`|`paramount3d_asa_paramount3dasavaporgray_1000_175_p`|`paramount3d.json::Paramount 3D::ASA {color_name}::ASA (Vapor Gray)::ASA::1000::1.75::plastic::False`|
|`paramount3d_asa_asa(white)_1000_175_p`|`paramount3d_asa_paramount3dasawhite_1000_175_p`|`paramount3d.json::Paramount 3D::ASA {color_name}::ASA (White)::ASA::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(autobotblue)_1000_175_p`|`paramount3d_petg_paramount3dpetgautobotblue_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (Autobot Blue)::PETG::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(black)_1000_175_p`|`paramount3d_petg_paramount3dpetgblack_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (Black)::PETG::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(blackcherry)_1000_175_p`|`paramount3d_petg_paramount3dpetgblackcherry_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (Black Cherry)::PETG::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(britishracinggreen)_1000_175_p`|`paramount3d_petg_paramount3dpetgbritishracinggreen_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (British Racing Green)::PETG::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(castlelimestonegray)_1000_175_p`|`paramount3d_petg_paramount3dpetgcastlelimestonegray_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (Castle Limestone Gray)::PETG::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(decepticonpurple)_1000_175_p`|`paramount3d_petg_paramount3dpetgdecepticonpurple_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (Decepticon Purple)::PETG::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(eggyolkyellow)_1000_175_p`|`paramount3d_petg_paramount3dpetgeggyolkyellow_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (Egg Yolk Yellow)::PETG::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(enzored)_1000_175_p`|`paramount3d_petg_paramount3dpetgenzored_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (Enzo Red)::PETG::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(fighterjetblue)_1000_175_p`|`paramount3d_petg_paramount3dpetgfighterjetblue_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (Fighter Jet Blue)::PETG::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(graphitegray)_1000_175_p`|`paramount3d_petg_paramount3dpetggraphitegray_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (Graphite Gray)::PETG::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(hannibalred)_1000_175_p`|`paramount3d_petg_paramount3dpetghannibalred_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (Hannibal Red)::PETG::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(harajukupink)_1000_175_p`|`paramount3d_petg_paramount3dpetgharajukupink_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (Harajuku Pink)::PETG::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(ironred)_1000_175_p`|`paramount3d_petg_paramount3dpetgironred_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (Iron Red)::PETG::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(mclarenorange)_1000_175_p`|`paramount3d_petg_paramount3dpetgmclarenorange_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (McLaren Orange)::PETG::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(midcenturymodernteal)_1000_175_p`|`paramount3d_petg_paramount3dpetgmidcenturymodernteal_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (Mid Century Modern Teal)::PETG::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(militarygreen)_1000_175_p`|`paramount3d_petg_paramount3dpetgmilitarygreen_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (Military Green)::PETG::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(militarykhaki)_1000_175_p`|`paramount3d_petg_paramount3dpetgmilitarykhaki_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (Military Khaki)::PETG::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(militarymbtbrown)_1000_175_p`|`paramount3d_petg_paramount3dpetgmilitarymbtbrown_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (Military MBT Brown)::PETG::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(primordialearth)_1000_175_p`|`paramount3d_petg_paramount3dpetgprimordialearth_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (Primordial Earth)::PETG::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(prototypegray)_1000_175_p`|`paramount3d_petg_paramount3dpetgprototypegray_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (Prototype Gray)::PETG::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(simpsonyellow)_1000_175_p`|`paramount3d_petg_paramount3dpetgsimpsonyellow_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (Simpson Yellow)::PETG::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(skin-ivory)_1000_175_p`|`paramount3d_petg_paramount3dpetgskin-ivory_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (Skin - Ivory)::PETG::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(skin-universalbeige)_1000_175_p`|`paramount3d_petg_paramount3dpetgskin-universalbeige_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (Skin - Universal Beige)::PETG::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(stealthgray)_1000_175_p`|`paramount3d_petg_paramount3dpetgstealthgray_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (Stealth Gray)::PETG::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(terracopper)_1000_175_p`|`paramount3d_petg_paramount3dpetgterracopper_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (Terra Copper)::PETG::1000::1.75::plastic::False`|
|`paramount3d_petg_petg(white)_1000_175_p`|`paramount3d_petg_paramount3dpetgwhite_1000_175_p`|`paramount3d.json::Paramount 3D::PETG {color_name}::PETG (White)::PETG::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(autobotblue)_1000_175_p`|`paramount3d_pla_paramount3dplaautobotblue_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Autobot Blue)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(battleshipgray)_1000_175_p`|`paramount3d_pla_paramount3dplabattleshipgray_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Battleship Gray)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(black)_1000_175_p`|`paramount3d_pla_paramount3dplablack_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Black)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(blackcherry)_1000_175_p`|`paramount3d_pla_paramount3dplablackcherry_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Black Cherry)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(britishracinggreen)_1000_175_p`|`paramount3d_pla_paramount3dplabritishracinggreen_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (British Racing Green)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(cadetblue)_1000_175_p`|`paramount3d_pla_paramount3dplacadetblue_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Cadet Blue)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(caribbeancoral)_1000_175_p`|`paramount3d_pla_paramount3dplacaribbeancoral_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Caribbean Coral)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(castlelimestonegray)_1000_175_p`|`paramount3d_pla_paramount3dplacastlelimestonegray_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Castle Limestone Gray)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(decepticonpurple)_1000_175_p`|`paramount3d_pla_paramount3dpladecepticonpurple_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Decepticon Purple)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(eggyolkyellow)_1000_175_p`|`paramount3d_pla_paramount3dplaeggyolkyellow_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Egg Yolk Yellow)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(enzored)_1000_175_p`|`paramount3d_pla_paramount3dplaenzored_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Enzo Red)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(fighterjetblue)_1000_175_p`|`paramount3d_pla_paramount3dplafighterjetblue_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Fighter Jet Blue)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(gamecartridgegray)_1000_175_p`|`paramount3d_pla_paramount3dplagamecartridgegray_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Game Cartridge Gray)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(geodeblack)_1000_175_p`|`paramount3d_pla_paramount3dplageodeblack_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Geode Black)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(goldkrugerrand)_1000_175_p`|`paramount3d_pla_paramount3dplagoldkrugerrand_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Gold Krugerrand)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(graphitegray)_1000_175_p`|`paramount3d_pla_paramount3dplagraphitegray_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Graphite Gray)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(greatdepressionjadeite)_1000_175_p`|`paramount3d_pla_paramount3dplagreatdepressionjadeite_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Great Depression Jadeite)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(hannibalred)_1000_175_p`|`paramount3d_pla_paramount3dplahannibalred_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Hannibal Red)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(harajukupink)_1000_175_p`|`paramount3d_pla_paramount3dplaharajukupink_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Harajuku Pink)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(ironred)_1000_175_p`|`paramount3d_pla_paramount3dplaironred_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Iron Red)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(ivory)_1000_175_p`|`paramount3d_pla_paramount3dplaivory_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Ivory)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(karnaksandstone)_1000_175_p`|`paramount3d_pla_paramount3dplakarnaksandstone_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Karnak Sandstone)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(leviathanbluegreen)_1000_175_p`|`paramount3d_pla_paramount3dplaleviathanbluegreen_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Leviathan Blue Green)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(mclarenorange)_1000_175_p`|`paramount3d_pla_paramount3dplamclarenorange_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (McLaren Orange)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(medusastonegray)_1000_175_p`|`paramount3d_pla_paramount3dplamedusastonegray_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Medusa Stone Gray)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(midcenturyteal)_1000_175_p`|`paramount3d_pla_paramount3dplamidcenturyteal_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Mid Century Teal)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(militarygreen)_1000_175_p`|`paramount3d_pla_paramount3dplamilitarygreen_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Military Green)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(militarykhaki)_1000_175_p`|`paramount3d_pla_paramount3dplamilitarykhaki_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Military Khaki)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(militarymbtbrown)_1000_175_p`|`paramount3d_pla_paramount3dplamilitarymbtbrown_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Military MBT Brown)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(primordialearth)_1000_175_p`|`paramount3d_pla_paramount3dplaprimordialearth_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Primordial Earth)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(prototypegray)_1000_175_p`|`paramount3d_pla_paramount3dplaprototypegray_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Prototype Gray)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(silverdollar)_1000_175_p`|`paramount3d_pla_paramount3dplasilverdollar_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Silver Dollar)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(simpsonyellow)_1000_175_p`|`paramount3d_pla_paramount3dplasimpsonyellow_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Simpson Yellow)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(skin-darkcomplexion)_1000_175_p`|`paramount3d_pla_paramount3dplaskin-darkcomplexion_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Skin - Dark Complexion)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(skin-deepcomplexion)_1000_175_p`|`paramount3d_pla_paramount3dplaskin-deepcomplexion_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Skin - Deep Complexion)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(skin-faircomplexion)_1000_175_p`|`paramount3d_pla_paramount3dplaskin-faircomplexion_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Skin - Fair Complexion)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(skin-universalbeige)_1000_175_p`|`paramount3d_pla_paramount3dplaskin-universalbeige_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Skin - Universal Beige)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(standrewsgreen)_1000_175_p`|`paramount3d_pla_paramount3dplastandrewsgreen_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (St Andrews Green)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(stealthgray)_1000_175_p`|`paramount3d_pla_paramount3dplastealthgray_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Stealth Gray)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(steelgray)_1000_175_p`|`paramount3d_pla_paramount3dplasteelgray_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Steel Gray)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(terracopper)_1000_175_p`|`paramount3d_pla_paramount3dplaterracopper_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Terra Copper)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(terracotta)_1000_175_p`|`paramount3d_pla_paramount3dplaterracotta_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Terra Cotta)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(tuxedomidnightblue)_1000_175_p`|`paramount3d_pla_paramount3dplatuxedomidnightblue_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Tuxedo Midnight Blue)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(volcanoorange)_1000_175_p`|`paramount3d_pla_paramount3dplavolcanoorange_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (Volcano Orange)::PLA::1000::1.75::plastic::False`|
|`paramount3d_pla_pla(white)_1000_175_p`|`paramount3d_pla_paramount3dplawhite_1000_175_p`|`paramount3d.json::Paramount 3D::PLA {color_name}::PLA (White)::PLA::1000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### PM001: dup-577c727ebc07d4f1ecc600942748cceadb868ae0f5b2cdabb7c85cd82d664870

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsautobotblue_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(autobotblue)_1000_175_p`|`ABS {color_name}`|`(Autobot Blue)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsautobotblue_1000_175_p`|`Paramount 3D ABS {color_name}`|`Autobot Blue`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(autobotblue)_1000_175_p": "2941BD",
    "paramount3d_abs_paramount3dabsautobotblue_1000_175_p": "20214d"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(autobotblue)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsautobotblue_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(autobotblue)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsautobotblue_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(autobotblue)_1000_175_p": null,
    "paramount3d_abs_paramount3dabsautobotblue_1000_175_p": [
      "BRL50022118A"
    ]
  }
}
```

### PM002: dup-f49ce484249bf4c812c89d1d7931982503d4f2695d1c21208d990b52bc4cc46f

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsbattleshipgray_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(battleshipgray)_1000_175_p`|`ABS {color_name}`|`(Battleship Gray)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsbattleshipgray_1000_175_p`|`Paramount 3D ABS {color_name}`|`Battleship Gray`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(battleshipgray)_1000_175_p": "7D8EAA",
    "paramount3d_abs_paramount3dabsbattleshipgray_1000_175_p": "7f868c"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(battleshipgray)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsbattleshipgray_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(battleshipgray)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsbattleshipgray_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(battleshipgray)_1000_175_p": null,
    "paramount3d_abs_paramount3dabsbattleshipgray_1000_175_p": [
      "BGRL7031431A"
    ]
  }
}
```

### PM003: dup-d453407d3a2b49900adafedcd82b1183a67860be224e47814b97ee9fbff62295

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsblackcherry_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(blackcherry)_1000_175_p`|`ABS {color_name}`|`(Black Cherry)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsblackcherry_1000_175_p`|`Paramount 3D ABS {color_name}`|`Black Cherry`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(blackcherry)_1000_175_p": "990303",
    "paramount3d_abs_paramount3dabsblackcherry_1000_175_p": "6b1c23"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(blackcherry)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsblackcherry_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(blackcherry)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsblackcherry_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(blackcherry)_1000_175_p": null,
    "paramount3d_abs_paramount3dabsblackcherry_1000_175_p": [
      "WMRL3005490A"
    ]
  }
}
```

### PM004: dup-5e4af0f7677cc0fa5915357ec9fa81a21236de8c028015ef15b356ebd38a0ae7

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsblack_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(black)_1000_175_p`|`ABS {color_name}`|`(Black)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsblack_1000_175_p`|`Paramount 3D ABS {color_name}`|`Black`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(black)_1000_175_p": "2A3940",
    "paramount3d_abs_paramount3dabsblack_1000_175_p": "0e0e10"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(black)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsblack_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(black)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsblack_1000_175_p": [
      100,
      110
    ]
  }
}
```

### PM005: dup-4355099d6681d0ceb0b6745cbf105846285d880396dbff711e358ce48046c222

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsbritishracinggreen_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(britishracinggreen)_1000_175_p`|`ABS {color_name}`|`(British Racing Green)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsbritishracinggreen_1000_175_p`|`Paramount 3D ABS {color_name}`|`British Racing Green`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(britishracinggreen)_1000_175_p": "1E5A4F",
    "paramount3d_abs_paramount3dabsbritishracinggreen_1000_175_p": "0f4336"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(britishracinggreen)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsbritishracinggreen_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(britishracinggreen)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsbritishracinggreen_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(britishracinggreen)_1000_175_p": null,
    "paramount3d_abs_paramount3dabsbritishracinggreen_1000_175_p": [
      "GRL60053435A"
    ]
  }
}
```

### PM006: dup-146e71850ed1e1abdb1660588922983e69b06f775e62fb849a63c4fb40a7be10

Status: APPROVED; survivor `paramount3d_abs_paramount3dabscastlelimestonegray_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(castlelimestonegray)_1000_175_p`|`ABS {color_name}`|`(Castle Limestone Gray)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabscastlelimestonegray_1000_175_p`|`Paramount 3D ABS {color_name}`|`Castle Limestone Gray`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(castlelimestonegray)_1000_175_p": "A9A8A0",
    "paramount3d_abs_paramount3dabscastlelimestonegray_1000_175_p": "8e9089"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(castlelimestonegray)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabscastlelimestonegray_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(castlelimestonegray)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabscastlelimestonegray_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(castlelimestonegray)_1000_175_p": null,
    "paramount3d_abs_paramount3dabscastlelimestonegray_1000_175_p": [
      "CGRL7023416A"
    ]
  }
}
```

### PM007: dup-18aaf02c38a9ddfee7f7d4c1d12281bcca08da58457d559409649e886d0e97d7

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsclear_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(clear)_1000_175_p`|`ABS {color_name}`|`(Clear)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsclear_1000_175_p`|`Paramount 3D ABS {color_name}`|`Clear`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(clear)_1000_175_p": "E4E7E5",
    "paramount3d_abs_paramount3dabsclear_1000_175_p": "eaeaea"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(clear)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsclear_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(clear)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsclear_1000_175_p": [
      100,
      110
    ]
  },
  "translucent": {
    "paramount3d_abs_abs(clear)_1000_175_p": true,
    "paramount3d_abs_paramount3dabsclear_1000_175_p": false
  }
}
```

### PM008: dup-765140a168c8ac75f5985f0aabf34beb7490619b239cbc62bfe2d9ab7f7664ff

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsdecepticonpurple_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(decepticonpurple)_1000_175_p`|`ABS {color_name}`|`(Decepticon Purple)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsdecepticonpurple_1000_175_p`|`Paramount 3D ABS {color_name}`|`Decepticon Purple`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(decepticonpurple)_1000_175_p": "431E33",
    "paramount3d_abs_paramount3dabsdecepticonpurple_1000_175_p": "7d55c7"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(decepticonpurple)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsdecepticonpurple_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(decepticonpurple)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsdecepticonpurple_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(decepticonpurple)_1000_175_p": null,
    "paramount3d_abs_paramount3dabsdecepticonpurple_1000_175_p": [
      "PRL40077449A"
    ]
  }
}
```

### PM009: dup-bd6bafc52e98dc6bfcc5dfee93ea3a3596b2260fa13c9fa7eca6082d2cc4c8dc

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsenzored_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(enzored)_1000_175_p`|`ABS {color_name}`|`(Enzo Red)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsenzored_1000_175_p`|`Paramount 3D ABS {color_name}`|`Enzo Red`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(enzored)_1000_175_p": "E72F1D",
    "paramount3d_abs_paramount3dabsenzored_1000_175_p": "cc0605"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(enzored)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsenzored_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(enzored)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsenzored_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(enzored)_1000_175_p": null,
    "paramount3d_abs_paramount3dabsenzored_1000_175_p": [
      "TRRL3020485A"
    ]
  }
}
```

### PM010: dup-8fc668a46c7f916d1b97f3fc7a0995f88398d178cd0e55de6a68e66bb2a425c9

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsfighterjetblue_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(fighterjetblue)_1000_175_p`|`ABS {color_name}`|`(Fighter Jet Blue)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsfighterjetblue_1000_175_p`|`Paramount 3D ABS {color_name}`|`Fighter Jet Blue`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(fighterjetblue)_1000_175_p": "394658",
    "paramount3d_abs_paramount3dabsfighterjetblue_1000_175_p": "003b49"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(fighterjetblue)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsfighterjetblue_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(fighterjetblue)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsfighterjetblue_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(fighterjetblue)_1000_175_p": null,
    "paramount3d_abs_paramount3dabsfighterjetblue_1000_175_p": [
      "FBRL50087546C"
    ]
  }
}
```

### PM011: dup-d09927a798197b85efc63d6a4796b5d2bd06912fdac5aaadae720bc610811a4d

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsgamecartridgegray_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(gamecartridgegray)_1000_175_p`|`ABS {color_name}`|`(Game Cartridge Gray)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsgamecartridgegray_1000_175_p`|`Paramount 3D ABS {color_name}`|`Game Cartridge Gray`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(gamecartridgegray)_1000_175_p": "B2B8B8",
    "paramount3d_abs_paramount3dabsgamecartridgegray_1000_175_p": "a7a8aa"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(gamecartridgegray)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsgamecartridgegray_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(gamecartridgegray)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsgamecartridgegray_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(gamecartridgegray)_1000_175_p": null,
    "paramount3d_abs_paramount3dabsgamecartridgegray_1000_175_p": [
      "LGRL7042423A"
    ]
  }
}
```

### PM012: dup-1c14d7899a54eaa46508f951971f1a9e40abc1591abd6fbab5255aceffef8fd1

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsgoldkrugerrand_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(goldkrugerrand)_1000_175_p`|`ABS {color_name}`|`(Gold Krugerrand)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsgoldkrugerrand_1000_175_p`|`Paramount 3D ABS {color_name}`|`Gold Krugerrand`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(goldkrugerrand)_1000_175_p": "F3BC00",
    "paramount3d_abs_paramount3dabsgoldkrugerrand_1000_175_p": "c5a028"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(goldkrugerrand)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsgoldkrugerrand_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(goldkrugerrand)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsgoldkrugerrand_1000_175_p": [
      100,
      110
    ]
  },
  "finish": {
    "paramount3d_abs_abs(goldkrugerrand)_1000_175_p": null,
    "paramount3d_abs_paramount3dabsgoldkrugerrand_1000_175_p": "glossy"
  }
}
```

### PM013: dup-7fc8552ff18504a4a1ec5d9d1c43e5ff46ead2cafa4505e51c58728c772be303

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsgraphitegray_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(graphitegray)_1000_175_p`|`ABS {color_name}`|`(Graphite Gray)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsgraphitegray_1000_175_p`|`Paramount 3D ABS {color_name}`|`Graphite Gray`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(graphitegray)_1000_175_p": "55657C",
    "paramount3d_abs_paramount3dabsgraphitegray_1000_175_p": "494e53"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(graphitegray)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsgraphitegray_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(graphitegray)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsgraphitegray_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(graphitegray)_1000_175_p": null,
    "paramount3d_abs_paramount3dabsgraphitegray_1000_175_p": [
      "BGRL7043425A"
    ]
  }
}
```

### PM014: dup-63e470025fbc94365c2b3257d79f1135a5da97fa2593b8177ad205441355e608

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsharajukupink_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(harajukupink)_1000_175_p`|`ABS {color_name}`|`(Harajuku Pink)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsharajukupink_1000_175_p`|`Paramount 3D ABS {color_name}`|`Harajuku Pink`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(harajukupink)_1000_175_p": "F04C9A",
    "paramount3d_abs_paramount3dabsharajukupink_1000_175_p": "cf3476"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(harajukupink)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsharajukupink_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(harajukupink)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsharajukupink_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(harajukupink)_1000_175_p": null,
    "paramount3d_abs_paramount3dabsharajukupink_1000_175_p": [
      "TMRL4010675A"
    ]
  }
}
```

### PM015: dup-d6df0c6949659271212255e4cef8f2ee0bc21410e90ff36d1254ecaf6784ed02

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsironred_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(ironred)_1000_175_p`|`ABS {color_name}`|`(Iron Red)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsironred_1000_175_p`|`Paramount 3D ABS {color_name}`|`Iron Red`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(ironred)_1000_175_p": "932721",
    "paramount3d_abs_paramount3dabsironred_1000_175_p": "8b2332"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(ironred)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsironred_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(ironred)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsironred_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(ironred)_1000_175_p": null,
    "paramount3d_abs_paramount3dabsironred_1000_175_p": [
      "IRRL30111815A"
    ]
  }
}
```

### PM016: dup-cbca12a79fe33905db07cc5a2041e8976274484f7fd22a2a5db880e37006140e

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsmclarenorange_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(mclarenorange)_1000_175_p`|`ABS {color_name}`|`(McLaren Orange)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsmclarenorange_1000_175_p`|`Paramount 3D ABS {color_name}`|`McLaren Orange`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(mclarenorange)_1000_175_p": "FA8423",
    "paramount3d_abs_paramount3dabsmclarenorange_1000_175_p": "ff8000"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(mclarenorange)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsmclarenorange_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(mclarenorange)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsmclarenorange_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(mclarenorange)_1000_175_p": null,
    "paramount3d_abs_paramount3dabsmclarenorange_1000_175_p": [
      "ORL20112019A"
    ]
  }
}
```

### PM017: dup-0dd8b4f36b6bc84b2b2fd98f74b622fb77724fe4b10582b98d6fc7044758d5de

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsmidcenturymodernteal_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(midcenturymodernteal)_1000_175_p`|`ABS {color_name}`|`(Mid Century Modern Teal)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsmidcenturymodernteal_1000_175_p`|`Paramount 3D ABS {color_name}`|`Mid Century Modern Teal`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(midcenturymodernteal)_1000_175_p": "5CADBF",
    "paramount3d_abs_paramount3dabsmidcenturymodernteal_1000_175_p": "007377"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(midcenturymodernteal)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsmidcenturymodernteal_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(midcenturymodernteal)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsmidcenturymodernteal_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(midcenturymodernteal)_1000_175_p": null,
    "paramount3d_abs_paramount3dabsmidcenturymodernteal_1000_175_p": [
      "ATRL50217718A"
    ]
  }
}
```

### PM018: dup-6d44bc6b47808602e6bf2181dbe329a4b5c240fbf5cd8a3117ba80053299eb68

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsmilitarygreen_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(militarygreen)_1000_175_p`|`ABS {color_name}`|`(Military Green)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsmilitarygreen_1000_175_p`|`Paramount 3D ABS {color_name}`|`Military Green`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(militarygreen)_1000_175_p": "6E8451",
    "paramount3d_abs_paramount3dabsmilitarygreen_1000_175_p": "4b5335"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(militarygreen)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsmilitarygreen_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(militarygreen)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsmilitarygreen_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(militarygreen)_1000_175_p": null,
    "paramount3d_abs_paramount3dabsmilitarygreen_1000_175_p": [
      "OGRL60037764A"
    ]
  }
}
```

### PM019: dup-2456725cf82d47953b541574b53646f5b2b7f9c61e15e54ede1a1041fc831e41

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsmilitarykhaki_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(militarykhaki)_1000_175_p`|`ABS {color_name}`|`(Military Khaki)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsmilitarykhaki_1000_175_p`|`Paramount 3D ABS {color_name}`|`Military Khaki`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(militarykhaki)_1000_175_p": "AE9D7E",
    "paramount3d_abs_paramount3dabsmilitarykhaki_1000_175_p": "b59a6a"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(militarykhaki)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsmilitarykhaki_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(militarykhaki)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsmilitarykhaki_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(militarykhaki)_1000_175_p": null,
    "paramount3d_abs_paramount3dabsmilitarykhaki_1000_175_p": [
      "GBRL10197530A"
    ]
  }
}
```

### PM020: dup-4c31ec80a56e90981f12cbec375d8b32ed5a9727d5a8c778ae810c36862fce25

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsmilitarymbtbrown_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(militarymbtbrown)_1000_175_p`|`ABS {color_name}`|`(Military MBT Brown)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsmilitarymbtbrown_1000_175_p`|`Paramount 3D ABS {color_name}`|`Military MBT Brown`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(militarymbtbrown)_1000_175_p": "C6AD74",
    "paramount3d_abs_paramount3dabsmilitarymbtbrown_1000_175_p": "6b3e2e"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(militarymbtbrown)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsmilitarymbtbrown_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(militarymbtbrown)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsmilitarymbtbrown_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(militarymbtbrown)_1000_175_p": null,
    "paramount3d_abs_paramount3dabsmilitarymbtbrown_1000_175_p": [
      "MGRL80007560A"
    ]
  }
}
```

### PM021: dup-63827e76ed6306ca4621f1ee3826ddb7866b8265bd86cb9e256354b991a358ea

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsprimordialearth_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(primordialearth)_1000_175_p`|`ABS {color_name}`|`(Primordial Earth)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsprimordialearth_1000_175_p`|`Paramount 3D ABS {color_name}`|`Primordial Earth`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(primordialearth)_1000_175_p": "AE9D7E",
    "paramount3d_abs_paramount3dabsprimordialearth_1000_175_p": "5c4033"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(primordialearth)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsprimordialearth_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(primordialearth)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsprimordialearth_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(primordialearth)_1000_175_p": null,
    "paramount3d_abs_paramount3dabsprimordialearth_1000_175_p": [
      "DERL7006G09A"
    ]
  }
}
```

### PM022: dup-7c11eba97abd14666d7a45fb154f590c41d03dbe4d0d6be6c62bb1ecdffa1a80

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsprototypegray_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(prototypegray)_1000_175_p`|`ABS {color_name}`|`(Prototype Gray)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsprototypegray_1000_175_p`|`Paramount 3D ABS {color_name}`|`Prototype Gray`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(prototypegray)_1000_175_p": "DEDDEA",
    "paramount3d_abs_paramount3dabsprototypegray_1000_175_p": "c5c7c4"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(prototypegray)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsprototypegray_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(prototypegray)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsprototypegray_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(prototypegray)_1000_175_p": null,
    "paramount3d_abs_paramount3dabsprototypegray_1000_175_p": [
      "LGRL7035421A"
    ]
  }
}
```

### PM023: dup-cc433266564f11dccf73f11566718fc9f70325510dccbf5792b86f2ae83c8e4d

Status: APPROVED; survivor `paramount3d_abs_paramount3dabssilverdollar_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(silverdollar)_1000_175_p`|`ABS {color_name}`|`(Silver Dollar)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabssilverdollar_1000_175_p`|`Paramount 3D ABS {color_name}`|`Silver Dollar`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(silverdollar)_1000_175_p": "878DA2",
    "paramount3d_abs_paramount3dabssilverdollar_1000_175_p": "8d9093"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(silverdollar)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabssilverdollar_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(silverdollar)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabssilverdollar_1000_175_p": [
      100,
      110
    ]
  },
  "finish": {
    "paramount3d_abs_abs(silverdollar)_1000_175_p": null,
    "paramount3d_abs_paramount3dabssilverdollar_1000_175_p": "glossy"
  }
}
```

### PM024: dup-13e2d47d34b252a0bd2dba9a43d5d40fabf30eb7cdda20ab60e97448d20f8b7a

Status: APPROVED; survivor `paramount3d_abs_paramount3dabssimpsonyellow_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(simpsonyellow)_1000_175_p`|`ABS {color_name}`|`(Simpson Yellow)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabssimpsonyellow_1000_175_p`|`Paramount 3D ABS {color_name}`|`Simpson Yellow`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(simpsonyellow)_1000_175_p": "FADB24",
    "paramount3d_abs_paramount3dabssimpsonyellow_1000_175_p": "f6d600"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(simpsonyellow)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabssimpsonyellow_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(simpsonyellow)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabssimpsonyellow_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(simpsonyellow)_1000_175_p": null,
    "paramount3d_abs_paramount3dabssimpsonyellow_1000_175_p": [
      "YRL1018129A"
    ]
  }
}
```

### PM025: dup-0fcb3faa0d41720965703a501122e381bee0e37820e13459dd702753a7a71818

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsskin-darkcomplexion_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(skin-darkcomplexion)_1000_175_p`|`ABS {color_name}`|`(Skin - Dark Complexion)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsskin-darkcomplexion_1000_175_p`|`Paramount 3D ABS {color_name}`|`Skin - Dark Complexion`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(skin-darkcomplexion)_1000_175_p": "C0894D",
    "paramount3d_abs_paramount3dabsskin-darkcomplexion_1000_175_p": "a67c52"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(skin-darkcomplexion)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsskin-darkcomplexion_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(skin-darkcomplexion)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsskin-darkcomplexion_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(skin-darkcomplexion)_1000_175_p": null,
    "paramount3d_abs_paramount3dabsskin-darkcomplexion_1000_175_p": [
      "BBRL1011729A"
    ]
  }
}
```

### PM026: dup-f4b0ae6c29b398726bb2e5c0828f72e6701ea2a08fa0d9668b387a9e26cc7218

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsskin-faircomplexion_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(skin-faircomplexion)_1000_175_p`|`ABS {color_name}`|`(Skin - Fair Complexion)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsskin-faircomplexion_1000_175_p`|`Paramount 3D ABS {color_name}`|`Skin - Fair Complexion`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(skin-faircomplexion)_1000_175_p": "EFE8D8",
    "paramount3d_abs_paramount3dabsskin-faircomplexion_1000_175_p": "d4b59a"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(skin-faircomplexion)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsskin-faircomplexion_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(skin-faircomplexion)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsskin-faircomplexion_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(skin-faircomplexion)_1000_175_p": null,
    "paramount3d_abs_paramount3dabsskin-faircomplexion_1000_175_p": [
      "LIRL1015468A"
    ]
  }
}
```

### PM027: dup-57085b3bcf46205def2dec63c1faac956ba8adf663d0acbb77b4b21b31a0be85

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsskin-ivory_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(skin-ivory)_1000_175_p`|`ABS {color_name}`|`(Skin - Ivory)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsskin-ivory_1000_175_p`|`Paramount 3D ABS {color_name}`|`Skin - Ivory`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(skin-ivory)_1000_175_p": "F1E6B2",
    "paramount3d_abs_paramount3dabsskin-ivory_1000_175_p": "e1cc4f"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(skin-ivory)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsskin-ivory_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(skin-ivory)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsskin-ivory_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(skin-ivory)_1000_175_p": null,
    "paramount3d_abs_paramount3dabsskin-ivory_1000_175_p": [
      "UBRL10147501A"
    ]
  }
}
```

### PM028: dup-2acae83ec4f89d4a4782e600084ab0e43498f9edb0e75f6df6cb5c2bc7526056

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsskin-universalbeige_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(skin-universalbeige)_1000_175_p`|`ABS {color_name}`|`(Skin - Universal Beige)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsskin-universalbeige_1000_175_p`|`Paramount 3D ABS {color_name}`|`Skin - Universal Beige`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(skin-universalbeige)_1000_175_p": "FBE9B8",
    "paramount3d_abs_paramount3dabsskin-universalbeige_1000_175_p": "d5b59a"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(skin-universalbeige)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsskin-universalbeige_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(skin-universalbeige)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsskin-universalbeige_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(skin-universalbeige)_1000_175_p": null,
    "paramount3d_abs_paramount3dabsskin-universalbeige_1000_175_p": [
      "UBRL10017502A"
    ]
  }
}
```

### PM029: dup-bfb343e34c872200dba435a918607e8d7ac4990d3b78b5200e271cb501ac468a

Status: APPROVED; survivor `paramount3d_abs_paramount3dabssteelgray_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(steelgray)_1000_175_p`|`ABS {color_name}`|`(Steel Gray)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabssteelgray_1000_175_p`|`Paramount 3D ABS {color_name}`|`Steel Gray`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(steelgray)_1000_175_p": "7D8EAA",
    "paramount3d_abs_paramount3dabssteelgray_1000_175_p": "a8a9ad"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(steelgray)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabssteelgray_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(steelgray)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabssteelgray_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(steelgray)_1000_175_p": null,
    "paramount3d_abs_paramount3dabssteelgray_1000_175_p": [
      "SGRL7000430A"
    ]
  }
}
```

### PM030: dup-d0c84e838419bde5a7a5a4ba6cbfaa2f6f1f2f3b6139aab2952cb11f94f730f2

Status: APPROVED; survivor `paramount3d_abs_paramount3dabsterracotta_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(terracotta)_1000_175_p`|`ABS {color_name}`|`(Terra Cotta)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabsterracotta_1000_175_p`|`Paramount 3D ABS {color_name}`|`Terra Cotta`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(terracotta)_1000_175_p": "D99773",
    "paramount3d_abs_paramount3dabsterracotta_1000_175_p": "9f4d36"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(terracotta)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabsterracotta_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(terracotta)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabsterracotta_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_abs_abs(terracotta)_1000_175_p": null,
    "paramount3d_abs_paramount3dabsterracotta_1000_175_p": [
      "BRRL30127591A"
    ]
  }
}
```

### PM031: dup-c8566b00e3c6e194b1e2575dcaf6a51fe758fe484ec17cc811e8fe2157a2d97f

Status: APPROVED; survivor `paramount3d_abs_paramount3dabswhite_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_abs_abs(white)_1000_175_p`|`ABS {color_name}`|`(White)`|{"source_file": "paramount3d.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`paramount3d_abs_paramount3dabswhite_1000_175_p`|`Paramount 3D ABS {color_name}`|`White`|{"source_file": "paramount3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_abs_abs(white)_1000_175_p": "FFFFFF",
    "paramount3d_abs_paramount3dabswhite_1000_175_p": "ffffff"
  },
  "extruder_temp_range": {
    "paramount3d_abs_abs(white)_1000_175_p": [
      230,
      260
    ],
    "paramount3d_abs_paramount3dabswhite_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_abs_abs(white)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_abs_paramount3dabswhite_1000_175_p": [
      100,
      110
    ]
  }
}
```

### PM032: dup-a0f00ef4b8d3cc14baf10cfda1072dbad057ae6ecba6ba44d7984f4fd67922cd

Status: APPROVED; survivor `paramount3d_asa_paramount3dasablack_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_asa_asa(black)_1000_175_p`|`ASA {color_name}`|`(Black)`|{"source_file": "paramount3d.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|
|`paramount3d_asa_paramount3dasablack_1000_175_p`|`Paramount 3D ASA {color_name}`|`Black`|{"source_file": "paramount3d.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "paramount3d_asa_asa(black)_1000_175_p": 1.07,
    "paramount3d_asa_paramount3dasablack_1000_175_p": 1.05
  },
  "color_hex": {
    "paramount3d_asa_asa(black)_1000_175_p": "545252",
    "paramount3d_asa_paramount3dasablack_1000_175_p": "101820"
  },
  "extruder_temp_range": {
    "paramount3d_asa_asa(black)_1000_175_p": [
      235,
      260
    ],
    "paramount3d_asa_paramount3dasablack_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_asa_asa(black)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_asa_paramount3dasablack_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_asa_asa(black)_1000_175_p": null,
    "paramount3d_asa_paramount3dasablack_1000_175_p": [
      "BLACK"
    ]
  }
}
```

### PM033: dup-01aef536f1523b77cdb045e5cc3400583765ac30d17e00739e4462b66167c1a2

Status: APPROVED; survivor `paramount3d_asa_paramount3dasadecepticonpurple_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_asa_asa(decepticonpurple)_1000_175_p`|`ASA {color_name}`|`(Decepticon Purple)`|{"source_file": "paramount3d.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|
|`paramount3d_asa_paramount3dasadecepticonpurple_1000_175_p`|`Paramount 3D ASA {color_name}`|`Decepticon Purple`|{"source_file": "paramount3d.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "paramount3d_asa_asa(decepticonpurple)_1000_175_p": 1.07,
    "paramount3d_asa_paramount3dasadecepticonpurple_1000_175_p": 1.05
  },
  "color_hex": {
    "paramount3d_asa_asa(decepticonpurple)_1000_175_p": "431E33",
    "paramount3d_asa_paramount3dasadecepticonpurple_1000_175_p": "7d55c7"
  },
  "extruder_temp_range": {
    "paramount3d_asa_asa(decepticonpurple)_1000_175_p": [
      235,
      260
    ],
    "paramount3d_asa_paramount3dasadecepticonpurple_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_asa_asa(decepticonpurple)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_asa_paramount3dasadecepticonpurple_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_asa_asa(decepticonpurple)_1000_175_p": null,
    "paramount3d_asa_paramount3dasadecepticonpurple_1000_175_p": [
      "PRL40077449SA"
    ]
  }
}
```

### PM034: dup-8a44fafd2329b974286816b73b6d07ebb8d777aeb76bca8b271acc08b342d377

Status: APPROVED; survivor `paramount3d_asa_paramount3dasaenzored_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_asa_asa(enzored)_1000_175_p`|`ASA {color_name}`|`(Enzo Red)`|{"source_file": "paramount3d.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|
|`paramount3d_asa_paramount3dasaenzored_1000_175_p`|`Paramount 3D ASA {color_name}`|`Enzo Red`|{"source_file": "paramount3d.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "paramount3d_asa_asa(enzored)_1000_175_p": 1.07,
    "paramount3d_asa_paramount3dasaenzored_1000_175_p": 1.05
  },
  "color_hex": {
    "paramount3d_asa_asa(enzored)_1000_175_p": "E72F1D",
    "paramount3d_asa_paramount3dasaenzored_1000_175_p": "da291c"
  },
  "extruder_temp_range": {
    "paramount3d_asa_asa(enzored)_1000_175_p": [
      235,
      260
    ],
    "paramount3d_asa_paramount3dasaenzored_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_asa_asa(enzored)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_asa_paramount3dasaenzored_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_asa_asa(enzored)_1000_175_p": null,
    "paramount3d_asa_paramount3dasaenzored_1000_175_p": [
      "TRRL3020485SA"
    ]
  }
}
```

### PM035: dup-8e517fbdd15d9d54d0aa26726e5335a1a7a1e66e7ef701cee11de994d687d20d

Status: APPROVED; survivor `paramount3d_asa_paramount3dasagraphitegray_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_asa_asa(graphitegray)_1000_175_p`|`ASA {color_name}`|`(Graphite Gray)`|{"source_file": "paramount3d.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|
|`paramount3d_asa_paramount3dasagraphitegray_1000_175_p`|`Paramount 3D ASA {color_name}`|`Graphite Gray`|{"source_file": "paramount3d.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "paramount3d_asa_asa(graphitegray)_1000_175_p": 1.07,
    "paramount3d_asa_paramount3dasagraphitegray_1000_175_p": 1.05
  },
  "color_hex": {
    "paramount3d_asa_asa(graphitegray)_1000_175_p": "9F9F9F",
    "paramount3d_asa_paramount3dasagraphitegray_1000_175_p": "494e53"
  },
  "extruder_temp_range": {
    "paramount3d_asa_asa(graphitegray)_1000_175_p": [
      235,
      260
    ],
    "paramount3d_asa_paramount3dasagraphitegray_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_asa_asa(graphitegray)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_asa_paramount3dasagraphitegray_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_asa_asa(graphitegray)_1000_175_p": null,
    "paramount3d_asa_paramount3dasagraphitegray_1000_175_p": [
      "BGRL7043_425SA"
    ]
  }
}
```

### PM036: dup-d3203950f5ac8e9bb724623c84a5f1fc69be925f48b8775665cce2aa4c3769aa

Status: APPROVED; survivor `paramount3d_asa_paramount3dasaironred_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_asa_asa(ironred)_1000_175_p`|`ASA {color_name}`|`(Iron Red)`|{"source_file": "paramount3d.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|
|`paramount3d_asa_paramount3dasaironred_1000_175_p`|`Paramount 3D ASA {color_name}`|`Iron Red`|{"source_file": "paramount3d.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "paramount3d_asa_asa(ironred)_1000_175_p": 1.07,
    "paramount3d_asa_paramount3dasaironred_1000_175_p": 1.05
  },
  "color_hex": {
    "paramount3d_asa_asa(ironred)_1000_175_p": "932721",
    "paramount3d_asa_paramount3dasaironred_1000_175_p": "8b2332"
  },
  "extruder_temp_range": {
    "paramount3d_asa_asa(ironred)_1000_175_p": [
      235,
      260
    ],
    "paramount3d_asa_paramount3dasaironred_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_asa_asa(ironred)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_asa_paramount3dasaironred_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_asa_asa(ironred)_1000_175_p": null,
    "paramount3d_asa_paramount3dasaironred_1000_175_p": [
      "IRRL30111815SA"
    ]
  }
}
```

### PM037: dup-f0dbe203ef919fb76d75bf8106008412cabedc100970f4a91823e56c84cbf4d6

Status: APPROVED; survivor `paramount3d_asa_paramount3dasamclarenorange_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_asa_asa(mclarenorange)_1000_175_p`|`ASA {color_name}`|`(McLaren Orange)`|{"source_file": "paramount3d.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|
|`paramount3d_asa_paramount3dasamclarenorange_1000_175_p`|`Paramount 3D ASA {color_name}`|`McLaren Orange`|{"source_file": "paramount3d.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "paramount3d_asa_asa(mclarenorange)_1000_175_p": 1.07,
    "paramount3d_asa_paramount3dasamclarenorange_1000_175_p": 1.05
  },
  "color_hex": {
    "paramount3d_asa_asa(mclarenorange)_1000_175_p": "FFB031",
    "paramount3d_asa_paramount3dasamclarenorange_1000_175_p": "ff8000"
  },
  "extruder_temp_range": {
    "paramount3d_asa_asa(mclarenorange)_1000_175_p": [
      235,
      260
    ],
    "paramount3d_asa_paramount3dasamclarenorange_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_asa_asa(mclarenorange)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_asa_paramount3dasamclarenorange_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_asa_asa(mclarenorange)_1000_175_p": null,
    "paramount3d_asa_paramount3dasamclarenorange_1000_175_p": [
      "ORL20112019SA"
    ]
  }
}
```

### PM038: dup-35b4a2f38aae23b648561dc95362ab3f84107b2bd6b249de9d40c3c1c74798a1

Status: APPROVED; survivor `paramount3d_asa_paramount3dasamilitarygreen_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_asa_asa(militarygreen)_1000_175_p`|`ASA {color_name}`|`(Military Green)`|{"source_file": "paramount3d.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|
|`paramount3d_asa_paramount3dasamilitarygreen_1000_175_p`|`Paramount 3D ASA {color_name}`|`Military Green`|{"source_file": "paramount3d.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "paramount3d_asa_asa(militarygreen)_1000_175_p": 1.07,
    "paramount3d_asa_paramount3dasamilitarygreen_1000_175_p": 1.05
  },
  "color_hex": {
    "paramount3d_asa_asa(militarygreen)_1000_175_p": "829778",
    "paramount3d_asa_paramount3dasamilitarygreen_1000_175_p": "4b5335"
  },
  "extruder_temp_range": {
    "paramount3d_asa_asa(militarygreen)_1000_175_p": [
      235,
      260
    ],
    "paramount3d_asa_paramount3dasamilitarygreen_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_asa_asa(militarygreen)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_asa_paramount3dasamilitarygreen_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_asa_asa(militarygreen)_1000_175_p": null,
    "paramount3d_asa_paramount3dasamilitarygreen_1000_175_p": [
      "OGRL60037764SA"
    ]
  }
}
```

### PM039: dup-dec3d8924a601c46ad945b695cea4c6e61fa779c560424cb89f63ba1f5a51c18

Status: APPROVED; survivor `paramount3d_asa_paramount3dasamilitarykhaki_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_asa_asa(militarykhaki)_1000_175_p`|`ASA {color_name}`|`(Military Khaki)`|{"source_file": "paramount3d.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|
|`paramount3d_asa_paramount3dasamilitarykhaki_1000_175_p`|`Paramount 3D ASA {color_name}`|`Military Khaki`|{"source_file": "paramount3d.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "paramount3d_asa_asa(militarykhaki)_1000_175_p": 1.07,
    "paramount3d_asa_paramount3dasamilitarykhaki_1000_175_p": 1.05
  },
  "color_hex": {
    "paramount3d_asa_asa(militarykhaki)_1000_175_p": "AE9D7E",
    "paramount3d_asa_paramount3dasamilitarykhaki_1000_175_p": "b59a6a"
  },
  "extruder_temp_range": {
    "paramount3d_asa_asa(militarykhaki)_1000_175_p": [
      235,
      260
    ],
    "paramount3d_asa_paramount3dasamilitarykhaki_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_asa_asa(militarykhaki)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_asa_paramount3dasamilitarykhaki_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_asa_asa(militarykhaki)_1000_175_p": null,
    "paramount3d_asa_paramount3dasamilitarykhaki_1000_175_p": [
      "GBRL10197530SA"
    ]
  }
}
```

### PM040: dup-f0e667a13d96f3e5b59dfd9009e7b8a76f87782028444577802bc9748dc04a6d

Status: APPROVED; survivor `paramount3d_asa_paramount3dasaprimordialearth_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_asa_asa(primordialearth)_1000_175_p`|`ASA {color_name}`|`(Primordial Earth)`|{"source_file": "paramount3d.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|
|`paramount3d_asa_paramount3dasaprimordialearth_1000_175_p`|`Paramount 3D ASA {color_name}`|`Primordial Earth`|{"source_file": "paramount3d.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "paramount3d_asa_asa(primordialearth)_1000_175_p": 1.07,
    "paramount3d_asa_paramount3dasaprimordialearth_1000_175_p": 1.05
  },
  "color_hex": {
    "paramount3d_asa_asa(primordialearth)_1000_175_p": "C4BCB3",
    "paramount3d_asa_paramount3dasaprimordialearth_1000_175_p": "5c4033"
  },
  "extruder_temp_range": {
    "paramount3d_asa_asa(primordialearth)_1000_175_p": [
      235,
      260
    ],
    "paramount3d_asa_paramount3dasaprimordialearth_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_asa_asa(primordialearth)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_asa_paramount3dasaprimordialearth_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_asa_asa(primordialearth)_1000_175_p": null,
    "paramount3d_asa_paramount3dasaprimordialearth_1000_175_p": [
      "DERL7006G09SA"
    ]
  }
}
```

### PM041: dup-9d1b56e33466d935b2ad483cd5627b4f6c3a3943ae6e93de71f7f03864eb96f9

Status: APPROVED; survivor `paramount3d_asa_paramount3dasastealthgray_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_asa_asa(stealthgray)_1000_175_p`|`ASA {color_name}`|`(Stealth Gray)`|{"source_file": "paramount3d.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|
|`paramount3d_asa_paramount3dasastealthgray_1000_175_p`|`Paramount 3D ASA {color_name}`|`Stealth Gray`|{"source_file": "paramount3d.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "paramount3d_asa_asa(stealthgray)_1000_175_p": 1.07,
    "paramount3d_asa_paramount3dasastealthgray_1000_175_p": 1.05
  },
  "color_hex": {
    "paramount3d_asa_asa(stealthgray)_1000_175_p": "4C5051",
    "paramount3d_asa_paramount3dasastealthgray_1000_175_p": "5c5f63"
  },
  "extruder_temp_range": {
    "paramount3d_asa_asa(stealthgray)_1000_175_p": [
      235,
      260
    ],
    "paramount3d_asa_paramount3dasastealthgray_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_asa_asa(stealthgray)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_asa_paramount3dasastealthgray_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_asa_asa(stealthgray)_1000_175_p": null,
    "paramount3d_asa_paramount3dasastealthgray_1000_175_p": [
      "IGRL7021_419SA"
    ]
  }
}
```

### PM042: dup-3659021394d77467a7b06893e8741b6ee8cd7bf7a7db7fee5cad7227262aaf85

Status: APPROVED; survivor `paramount3d_asa_paramount3dasavaporgray_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_asa_asa(vaporgray)_1000_175_p`|`ASA {color_name}`|`(Vapor Gray)`|{"source_file": "paramount3d.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|
|`paramount3d_asa_paramount3dasavaporgray_1000_175_p`|`Paramount 3D ASA {color_name}`|`Vapor Gray`|{"source_file": "paramount3d.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "paramount3d_asa_asa(vaporgray)_1000_175_p": 1.07,
    "paramount3d_asa_paramount3dasavaporgray_1000_175_p": 1.05
  },
  "color_hex": {
    "paramount3d_asa_asa(vaporgray)_1000_175_p": "C5C7C4",
    "paramount3d_asa_paramount3dasavaporgray_1000_175_p": "a7a8aa"
  },
  "extruder_temp_range": {
    "paramount3d_asa_asa(vaporgray)_1000_175_p": [
      235,
      260
    ],
    "paramount3d_asa_paramount3dasavaporgray_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_asa_asa(vaporgray)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_asa_paramount3dasavaporgray_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_asa_asa(vaporgray)_1000_175_p": null,
    "paramount3d_asa_paramount3dasavaporgray_1000_175_p": [
      "LGRL7035421SA"
    ]
  }
}
```

### PM043: dup-b28e0fb8ab2fec053126e3d0674ecd598d26cbc74b52e2c262273c6530df308a

Status: APPROVED; survivor `paramount3d_asa_paramount3dasawhite_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_asa_asa(white)_1000_175_p`|`ASA {color_name}`|`(White)`|{"source_file": "paramount3d.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|
|`paramount3d_asa_paramount3dasawhite_1000_175_p`|`Paramount 3D ASA {color_name}`|`White`|{"source_file": "paramount3d.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "paramount3d_asa_asa(white)_1000_175_p": 1.07,
    "paramount3d_asa_paramount3dasawhite_1000_175_p": 1.05
  },
  "color_hex": {
    "paramount3d_asa_asa(white)_1000_175_p": "F5F5F5",
    "paramount3d_asa_paramount3dasawhite_1000_175_p": "f4f4f4"
  },
  "extruder_temp_range": {
    "paramount3d_asa_asa(white)_1000_175_p": [
      235,
      260
    ],
    "paramount3d_asa_paramount3dasawhite_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "paramount3d_asa_asa(white)_1000_175_p": [
      90,
      110
    ],
    "paramount3d_asa_paramount3dasawhite_1000_175_p": [
      100,
      110
    ]
  },
  "codes": {
    "paramount3d_asa_asa(white)_1000_175_p": null,
    "paramount3d_asa_paramount3dasawhite_1000_175_p": [
      "WHITE"
    ]
  }
}
```

### PM044: dup-dc6510246b7cb4c0f75bbd1e4d684426b0b5d1b6b8046914cf5ae4533025f854

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetgautobotblue_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetgautobotblue_1000_175_p`|`Paramount 3D PETG {color_name}`|`Autobot Blue`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(autobotblue)_1000_175_p`|`PETG {color_name}`|`(Autobot Blue)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetgautobotblue_1000_175_p": "005eb8",
    "paramount3d_petg_petg(autobotblue)_1000_175_p": "2941BD"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetgautobotblue_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(autobotblue)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetgautobotblue_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(autobotblue)_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "paramount3d_petg_paramount3dpetgautobotblue_1000_175_p": [
      "BRL50022118G"
    ],
    "paramount3d_petg_petg(autobotblue)_1000_175_p": null
  }
}
```

### PM046: dup-12770472269c5d7116ee391dd08fd3583cfdf9b2c70450cb6a03e945c6997ff7

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetgblack_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetgblack_1000_175_p`|`Paramount 3D PETG {color_name}`|`Black`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(black)_1000_175_p`|`PETG {color_name}`|`(Black)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetgblack_1000_175_p": "282828",
    "paramount3d_petg_petg(black)_1000_175_p": "000000"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetgblack_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(black)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetgblack_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(black)_1000_175_p": [
      70,
      90
    ]
  }
}
```

### PM045: dup-5b13a2141e25a6e3b1d51b06b633fc480993975b69c520f083f0d90ef676e84e

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetgblackcherry_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetgblackcherry_1000_175_p`|`Paramount 3D PETG {color_name}`|`Black Cherry`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(blackcherry)_1000_175_p`|`PETG {color_name}`|`(Black Cherry)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetgblackcherry_1000_175_p": "7a263a",
    "paramount3d_petg_petg(blackcherry)_1000_175_p": "520B0F"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetgblackcherry_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(blackcherry)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetgblackcherry_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(blackcherry)_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "paramount3d_petg_paramount3dpetgblackcherry_1000_175_p": [
      "WMRL3005490G"
    ],
    "paramount3d_petg_petg(blackcherry)_1000_175_p": null
  }
}
```

### PM047: dup-1b6275c927652b02307614f8b45fad539b7d8c8d6e674e5ed5ad566d89888163

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetgbritishracinggreen_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetgbritishracinggreen_1000_175_p`|`Paramount 3D PETG {color_name}`|`British Racing Green`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(britishracinggreen)_1000_175_p`|`PETG {color_name}`|`(British Racing Green)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetgbritishracinggreen_1000_175_p": "004225",
    "paramount3d_petg_petg(britishracinggreen)_1000_175_p": "1E5A4F"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetgbritishracinggreen_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(britishracinggreen)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetgbritishracinggreen_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(britishracinggreen)_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "paramount3d_petg_paramount3dpetgbritishracinggreen_1000_175_p": [
      "GRL6005343G"
    ],
    "paramount3d_petg_petg(britishracinggreen)_1000_175_p": null
  }
}
```

### PM048: dup-92606a10666d8520e03ab8339a47587ee1634c2546a64e04c09290f2d3c4fc09

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetgcastlelimestonegray_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetgcastlelimestonegray_1000_175_p`|`Paramount 3D PETG {color_name}`|`Castle Limestone Gray`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(castlelimestonegray)_1000_175_p`|`PETG {color_name}`|`(Castle Limestone Gray)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetgcastlelimestonegray_1000_175_p": "8e9089",
    "paramount3d_petg_petg(castlelimestonegray)_1000_175_p": "C5C7C4"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetgcastlelimestonegray_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(castlelimestonegray)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetgcastlelimestonegray_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(castlelimestonegray)_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "paramount3d_petg_paramount3dpetgcastlelimestonegray_1000_175_p": [
      "CGRL7023416G"
    ],
    "paramount3d_petg_petg(castlelimestonegray)_1000_175_p": null
  }
}
```

### PM049: dup-34b49d26bbae4f9a7ed6d6a743b7a7bab4998fe36189936ef066146b4d00cfa9

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetgdecepticonpurple_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetgdecepticonpurple_1000_175_p`|`Paramount 3D PETG {color_name}`|`Decepticon Purple`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(decepticonpurple)_1000_175_p`|`PETG {color_name}`|`(Decepticon Purple)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetgdecepticonpurple_1000_175_p": "6a6599",
    "paramount3d_petg_petg(decepticonpurple)_1000_175_p": "431E33"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetgdecepticonpurple_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(decepticonpurple)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetgdecepticonpurple_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(decepticonpurple)_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "paramount3d_petg_paramount3dpetgdecepticonpurple_1000_175_p": [
      "PRL40077449G"
    ],
    "paramount3d_petg_petg(decepticonpurple)_1000_175_p": null
  }
}
```

### PM050: dup-edbf4543fe3cabd4f586b054c6eb8e1d71f572432024f5430db89f4051c4a361

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetgeggyolkyellow_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetgeggyolkyellow_1000_175_p`|`Paramount 3D PETG {color_name}`|`Egg Yolk Yellow`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(eggyolkyellow)_1000_175_p`|`PETG {color_name}`|`(Egg Yolk Yellow)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetgeggyolkyellow_1000_175_p": "f6a950",
    "paramount3d_petg_petg(eggyolkyellow)_1000_175_p": "FF9A14"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetgeggyolkyellow_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(eggyolkyellow)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetgeggyolkyellow_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(eggyolkyellow)_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "paramount3d_petg_paramount3dpetgeggyolkyellow_1000_175_p": [
      "SYRL1003137G"
    ],
    "paramount3d_petg_petg(eggyolkyellow)_1000_175_p": null
  }
}
```

### PM051: dup-1ff22e2878a2d61b8a043c048b1e44b01648c0d93edaab75c8fd4180a038cf7b

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetgenzored_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetgenzored_1000_175_p`|`Paramount 3D PETG {color_name}`|`Enzo Red`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(enzored)_1000_175_p`|`PETG {color_name}`|`(Enzo Red)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetgenzored_1000_175_p": "cc0605",
    "paramount3d_petg_petg(enzored)_1000_175_p": "E03F26"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetgenzored_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(enzored)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetgenzored_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(enzored)_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "paramount3d_petg_paramount3dpetgenzored_1000_175_p": [
      "TRRL3020485G"
    ],
    "paramount3d_petg_petg(enzored)_1000_175_p": null
  }
}
```

### PM052: dup-661e2f50a6bb0d14d2b6dadfd6f2e82a04428593faf58056e06341cabc45ae6e

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetgfighterjetblue_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetgfighterjetblue_1000_175_p`|`Paramount 3D PETG {color_name}`|`Fighter Jet Blue`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(fighterjetblue)_1000_175_p`|`PETG {color_name}`|`(Fighter Jet Blue)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetgfighterjetblue_1000_175_p": "003b49",
    "paramount3d_petg_petg(fighterjetblue)_1000_175_p": "4C5975"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetgfighterjetblue_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(fighterjetblue)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetgfighterjetblue_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(fighterjetblue)_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "paramount3d_petg_paramount3dpetgfighterjetblue_1000_175_p": [
      "FBRL50087546G"
    ],
    "paramount3d_petg_petg(fighterjetblue)_1000_175_p": null
  }
}
```

### PM053: dup-4eabb272cf3fd1381e90302ffb8a4391ee05423c34760d17e489881abe2c5054

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetggraphitegray_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetggraphitegray_1000_175_p`|`Paramount 3D PETG {color_name}`|`Graphite Gray`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(graphitegray)_1000_175_p`|`PETG {color_name}`|`(Graphite Gray)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetggraphitegray_1000_175_p": "494e53",
    "paramount3d_petg_petg(graphitegray)_1000_175_p": "545F67"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetggraphitegray_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(graphitegray)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetggraphitegray_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(graphitegray)_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "paramount3d_petg_paramount3dpetggraphitegray_1000_175_p": [
      "BGRL7043425G"
    ],
    "paramount3d_petg_petg(graphitegray)_1000_175_p": null
  }
}
```

### PM054: dup-18e958811b03054a62f5664504d08b6f9f8ac2dc58683b3b4d270dcee81df793

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetghannibalred_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetghannibalred_1000_175_p`|`Paramount 3D PETG {color_name}`|`Hannibal Red`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(hannibalred)_1000_175_p`|`PETG {color_name}`|`(Hannibal Red)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetghannibalred_1000_175_p": "7b292c",
    "paramount3d_petg_petg(hannibalred)_1000_175_p": "7A341C"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetghannibalred_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(hannibalred)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetghannibalred_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(hannibalred)_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "paramount3d_petg_paramount3dpetghannibalred_1000_175_p": [
      "BHRL3009181G"
    ],
    "paramount3d_petg_petg(hannibalred)_1000_175_p": null
  }
}
```

### PM055: dup-333c8c703c032917cb44ee3861a51d3226b5a0458633ca31857fcd7c1596c5b3

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetgharajukupink_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetgharajukupink_1000_175_p`|`Paramount 3D PETG {color_name}`|`Harajuku Pink`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(harajukupink)_1000_175_p`|`PETG {color_name}`|`(Harajuku Pink)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetgharajukupink_1000_175_p": "cf3476",
    "paramount3d_petg_petg(harajukupink)_1000_175_p": "D93382"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetgharajukupink_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(harajukupink)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetgharajukupink_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(harajukupink)_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "paramount3d_petg_paramount3dpetgharajukupink_1000_175_p": [
      "TMRL4010675G"
    ],
    "paramount3d_petg_petg(harajukupink)_1000_175_p": null
  }
}
```

### PM056: dup-045bac5cb4bc0c1fcf31e7a410f773b1e2c61224c3f97678c423572c9dac638d

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetgironred_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetgironred_1000_175_p`|`Paramount 3D PETG {color_name}`|`Iron Red`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(ironred)_1000_175_p`|`PETG {color_name}`|`(Iron Red)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetgironred_1000_175_p": "8b2332",
    "paramount3d_petg_petg(ironred)_1000_175_p": "932721"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetgironred_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(ironred)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetgironred_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(ironred)_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "paramount3d_petg_paramount3dpetgironred_1000_175_p": [
      "IRRL30111815G"
    ],
    "paramount3d_petg_petg(ironred)_1000_175_p": null
  }
}
```

### PM057: dup-9adc06e0ae174980d859c301d452c0829becc4ff48a2a3f658a5a99414ae880b

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetgmclarenorange_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetgmclarenorange_1000_175_p`|`Paramount 3D PETG {color_name}`|`McLaren Orange`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(mclarenorange)_1000_175_p`|`PETG {color_name}`|`(McLaren Orange)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetgmclarenorange_1000_175_p": "ff8000",
    "paramount3d_petg_petg(mclarenorange)_1000_175_p": "FA8423"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetgmclarenorange_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(mclarenorange)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetgmclarenorange_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(mclarenorange)_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "paramount3d_petg_paramount3dpetgmclarenorange_1000_175_p": [
      "ORL20112019G"
    ],
    "paramount3d_petg_petg(mclarenorange)_1000_175_p": null
  }
}
```

### PM058: dup-b2281de3954b965a6d62cc95068bfa8ae2aaf917b5a7abdede8a7ac3472da544

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetgmidcenturymodernteal_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetgmidcenturymodernteal_1000_175_p`|`Paramount 3D PETG {color_name}`|`Mid Century Modern Teal`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(midcenturymodernteal)_1000_175_p`|`PETG {color_name}`|`(Mid Century Modern Teal)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetgmidcenturymodernteal_1000_175_p": "007377",
    "paramount3d_petg_petg(midcenturymodernteal)_1000_175_p": "00B4BC"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetgmidcenturymodernteal_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(midcenturymodernteal)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetgmidcenturymodernteal_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(midcenturymodernteal)_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "paramount3d_petg_paramount3dpetgmidcenturymodernteal_1000_175_p": [
      "ATRL50217718G"
    ],
    "paramount3d_petg_petg(midcenturymodernteal)_1000_175_p": null
  }
}
```

### PM059: dup-b2d19af8a33a68d21503a5b391ca58500220b7c65c11af04b2d4b8b24aa08f40

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetgmilitarygreen_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetgmilitarygreen_1000_175_p`|`Paramount 3D PETG {color_name}`|`Military Green`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(militarygreen)_1000_175_p`|`PETG {color_name}`|`(Military Green)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetgmilitarygreen_1000_175_p": "4b5335",
    "paramount3d_petg_petg(militarygreen)_1000_175_p": "6E8451"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetgmilitarygreen_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(militarygreen)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetgmilitarygreen_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(militarygreen)_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "paramount3d_petg_paramount3dpetgmilitarygreen_1000_175_p": [
      "OGRL60037764G"
    ],
    "paramount3d_petg_petg(militarygreen)_1000_175_p": null
  }
}
```

### PM060: dup-34e9a250e939838f2f927c2023ce708b9c4b4e05fb9b82956667dad1de42f939

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetgmilitarykhaki_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetgmilitarykhaki_1000_175_p`|`Paramount 3D PETG {color_name}`|`Military Khaki`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(militarykhaki)_1000_175_p`|`PETG {color_name}`|`(Military Khaki)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetgmilitarykhaki_1000_175_p": "b59a6a",
    "paramount3d_petg_petg(militarykhaki)_1000_175_p": "AE9D7E"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetgmilitarykhaki_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(militarykhaki)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetgmilitarykhaki_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(militarykhaki)_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "paramount3d_petg_paramount3dpetgmilitarykhaki_1000_175_p": [
      "GBRL10197530G"
    ],
    "paramount3d_petg_petg(militarykhaki)_1000_175_p": null
  }
}
```

### PM061: dup-543c82e52204d0f5679d71898605543e6c046d6ab45af5f134d3fd692ab6b6b0

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetgmilitarymbtbrown_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetgmilitarymbtbrown_1000_175_p`|`Paramount 3D PETG {color_name}`|`Military MBT Brown`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(militarymbtbrown)_1000_175_p`|`PETG {color_name}`|`(Military MBT Brown)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetgmilitarymbtbrown_1000_175_p": "6b3e2e",
    "paramount3d_petg_petg(militarymbtbrown)_1000_175_p": "908253"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetgmilitarymbtbrown_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(militarymbtbrown)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetgmilitarymbtbrown_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(militarymbtbrown)_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "paramount3d_petg_paramount3dpetgmilitarymbtbrown_1000_175_p": [
      "MGRL80007560G"
    ],
    "paramount3d_petg_petg(militarymbtbrown)_1000_175_p": null
  }
}
```

### PM062: dup-0f88e0056f44ef2f1a8a7be6fd8b0da43f49c639bc2de5f3495906170bd1277c

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetgprimordialearth_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetgprimordialearth_1000_175_p`|`Paramount 3D PETG {color_name}`|`Primordial Earth`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(primordialearth)_1000_175_p`|`PETG {color_name}`|`(Primordial Earth)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetgprimordialearth_1000_175_p": "5c4033",
    "paramount3d_petg_petg(primordialearth)_1000_175_p": "90785E"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetgprimordialearth_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(primordialearth)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetgprimordialearth_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(primordialearth)_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "paramount3d_petg_paramount3dpetgprimordialearth_1000_175_p": [
      "DERL7006G09G"
    ],
    "paramount3d_petg_petg(primordialearth)_1000_175_p": null
  }
}
```

### PM063: dup-4339645b954b88587bb95328c8f220853d5367f9283763e6c21e1bc8038bdbfe

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetgprototypegray_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetgprototypegray_1000_175_p`|`Paramount 3D PETG {color_name}`|`Prototype Gray`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(prototypegray)_1000_175_p`|`PETG {color_name}`|`(Prototype Gray)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetgprototypegray_1000_175_p": "a7a8aa",
    "paramount3d_petg_petg(prototypegray)_1000_175_p": "DEDDEA"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetgprototypegray_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(prototypegray)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetgprototypegray_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(prototypegray)_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "paramount3d_petg_paramount3dpetgprototypegray_1000_175_p": [
      "LGRL7035421G"
    ],
    "paramount3d_petg_petg(prototypegray)_1000_175_p": null
  }
}
```

### PM064: dup-44093ed0b6a3a43289a13419306a12621e55377109a78075c85356f422b3d4e7

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetgsimpsonyellow_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetgsimpsonyellow_1000_175_p`|`Paramount 3D PETG {color_name}`|`Simpson Yellow`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(simpsonyellow)_1000_175_p`|`PETG {color_name}`|`(Simpson Yellow)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetgsimpsonyellow_1000_175_p": "faca30",
    "paramount3d_petg_petg(simpsonyellow)_1000_175_p": "FADB24"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetgsimpsonyellow_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(simpsonyellow)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetgsimpsonyellow_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(simpsonyellow)_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "paramount3d_petg_paramount3dpetgsimpsonyellow_1000_175_p": [
      "YRL1018129G"
    ],
    "paramount3d_petg_petg(simpsonyellow)_1000_175_p": null
  }
}
```

### PM065: dup-8e43d0e782e35c008fabed56ad5566c6be2a5665ccc71fdd37e9641fafe0d1e1

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetgskin-ivory_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetgskin-ivory_1000_175_p`|`Paramount 3D PETG {color_name}`|`Skin - Ivory`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(skin-ivory)_1000_175_p`|`PETG {color_name}`|`(Skin - Ivory)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetgskin-ivory_1000_175_p": "e1cc4f",
    "paramount3d_petg_petg(skin-ivory)_1000_175_p": "E3D99F"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetgskin-ivory_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(skin-ivory)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetgskin-ivory_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(skin-ivory)_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "paramount3d_petg_paramount3dpetgskin-ivory_1000_175_p": [
      "IRL10147501G"
    ],
    "paramount3d_petg_petg(skin-ivory)_1000_175_p": null
  }
}
```

### PM066: dup-81ae1fc9bb35b8bd83294e46de536fefa6deca57a9708f9d98ffa8f242a71770

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetgskin-universalbeige_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetgskin-universalbeige_1000_175_p`|`Paramount 3D PETG {color_name}`|`Skin - Universal Beige`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(skin-universalbeige)_1000_175_p`|`PETG {color_name}`|`(Skin - Universal Beige)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetgskin-universalbeige_1000_175_p": "d5b59a",
    "paramount3d_petg_petg(skin-universalbeige)_1000_175_p": "000000"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetgskin-universalbeige_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(skin-universalbeige)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetgskin-universalbeige_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(skin-universalbeige)_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "paramount3d_petg_paramount3dpetgskin-universalbeige_1000_175_p": [
      "UBRL10017502G"
    ],
    "paramount3d_petg_petg(skin-universalbeige)_1000_175_p": null
  }
}
```

### PM067: dup-cc7d389aa02399f7326f5d8293808197e5ef0946340bf4c14ce05124c9ac7301

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetgstealthgray_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetgstealthgray_1000_175_p`|`Paramount 3D PETG {color_name}`|`Stealth Gray`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(stealthgray)_1000_175_p`|`PETG {color_name}`|`(Stealth Gray)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetgstealthgray_1000_175_p": "5c5f63",
    "paramount3d_petg_petg(stealthgray)_1000_175_p": "3B3E3F"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetgstealthgray_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(stealthgray)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetgstealthgray_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(stealthgray)_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "paramount3d_petg_paramount3dpetgstealthgray_1000_175_p": [
      "IGRL7021419G"
    ],
    "paramount3d_petg_petg(stealthgray)_1000_175_p": null
  }
}
```

### PM068: dup-d3323aed35291164db7a4cdf651fd3c12b813fbbc8f1c193b0253eaf27a07abd

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetgterracopper_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetgterracopper_1000_175_p`|`Paramount 3D PETG {color_name}`|`Terra Copper`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(terracopper)_1000_175_p`|`PETG {color_name}`|`(Terra Copper)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetgterracopper_1000_175_p": "b87333",
    "paramount3d_petg_petg(terracopper)_1000_175_p": "BF7473"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetgterracopper_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(terracopper)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetgterracopper_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(terracopper)_1000_175_p": [
      70,
      90
    ]
  },
  "finish": {
    "paramount3d_petg_paramount3dpetgterracopper_1000_175_p": "glossy",
    "paramount3d_petg_petg(terracopper)_1000_175_p": null
  },
  "codes": {
    "paramount3d_petg_paramount3dpetgterracopper_1000_175_p": [
      "CBRL8004484G"
    ],
    "paramount3d_petg_petg(terracopper)_1000_175_p": null
  }
}
```

### PM069: dup-8bd0017a99a557fe4a91f4f029636366d905034a940b14e266f18b20e1ec15c6

Status: APPROVED; survivor `paramount3d_petg_paramount3dpetgwhite_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_petg_paramount3dpetgwhite_1000_175_p`|`Paramount 3D PETG {color_name}`|`White`|{"source_file": "paramount3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|
|`paramount3d_petg_petg(white)_1000_175_p`|`PETG {color_name}`|`(White)`|{"source_file": "paramount3d.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 26, "compiled_records": 26} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_petg_paramount3dpetgwhite_1000_175_p": "ffffff",
    "paramount3d_petg_petg(white)_1000_175_p": "FFFFFF"
  },
  "extruder_temp_range": {
    "paramount3d_petg_paramount3dpetgwhite_1000_175_p": [
      220,
      260
    ],
    "paramount3d_petg_petg(white)_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "paramount3d_petg_paramount3dpetgwhite_1000_175_p": [
      60,
      80
    ],
    "paramount3d_petg_petg(white)_1000_175_p": [
      70,
      90
    ]
  }
}
```

### PM070: dup-a1193cacb2ff8f22a493492cafcb6e459a308c4596b0d316e30ddf4708c8b29a

Status: DEFERRED; survivor `paramount3d_pla_mattepla(black)_1000_175_p`; Owner-deferred Matte Black line/color mismatch (Matte in color versus family); both records retained.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_mattepla(black)_1000_175_p`|`Matte PLA {color_name}`|`( Black)`|{"source_file": "paramount3d.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 1, "compiled_records": 1} / False|
|`paramount3d_pla_paramount3dplamatteblack_1000_175_p`|`Paramount 3D PLA {color_name}`|`Matte Black`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_mattepla(black)_1000_175_p": "000000",
    "paramount3d_pla_paramount3dplamatteblack_1000_175_p": "0e0e10"
  },
  "extruder_temp_range": {
    "paramount3d_pla_mattepla(black)_1000_175_p": [
      190,
      230
    ],
    "paramount3d_pla_paramount3dplamatteblack_1000_175_p": [
      195,
      210
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_mattepla(black)_1000_175_p": [
      50,
      70
    ],
    "paramount3d_pla_paramount3dplamatteblack_1000_175_p": [
      0,
      0
    ]
  }
}
```

### PM071: dup-dcb321090ce373a59c884cc1d2a240ea0241bb75237ca445537516b7c1a7b1c0

Status: APPROVED; survivor `paramount3d_pla_paramount3dplaautobotblue_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplaautobotblue_1000_175_p`|`Paramount 3D PLA {color_name}`|`Autobot Blue`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(autobotblue)_1000_175_p`|`PLA {color_name}`|`(Autobot Blue)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplaautobotblue_1000_175_p": "005eb8",
    "paramount3d_pla_pla(autobotblue)_1000_175_p": "2941BD"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplaautobotblue_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(autobotblue)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplaautobotblue_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(autobotblue)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplaautobotblue_1000_175_p": [
      "BRL50022118C"
    ],
    "paramount3d_pla_pla(autobotblue)_1000_175_p": null
  }
}
```

### PM072: dup-688497724e3f8ec48f70c1f6b34c704e65ac5333e9138ee2a8e84fb77c24e126

Status: APPROVED; survivor `paramount3d_pla_paramount3dplabattleshipgray_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplabattleshipgray_1000_175_p`|`Paramount 3D PLA {color_name}`|`Battleship Gray`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(battleshipgray)_1000_175_p`|`PLA {color_name}`|`(Battleship Gray)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplabattleshipgray_1000_175_p": "7f868c",
    "paramount3d_pla_pla(battleshipgray)_1000_175_p": "7D8EAA"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplabattleshipgray_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(battleshipgray)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplabattleshipgray_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(battleshipgray)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplabattleshipgray_1000_175_p": [
      "BGRL7031431C"
    ],
    "paramount3d_pla_pla(battleshipgray)_1000_175_p": null
  }
}
```

### PM074: dup-e24e7e1fb98edd33af22a92deec6cdb72434cef45cc787b4318a0b4e11bcd501

Status: APPROVED; survivor `paramount3d_pla_paramount3dplablack_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplablack_1000_175_p`|`Paramount 3D PLA {color_name}`|`Black`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(black)_1000_175_p`|`PLA {color_name}`|`(Black)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplablack_1000_175_p": "101820",
    "paramount3d_pla_pla(black)_1000_175_p": "000000"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplablack_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(black)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplablack_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(black)_1000_175_p": [
      50,
      70
    ]
  }
}
```

### PM073: dup-d0e0f5ce706eaebf3b7761214eb9ee7d9f604ab7879bff3c0f06fc0f1a41c196

Status: APPROVED; survivor `paramount3d_pla_paramount3dplablackcherry_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplablackcherry_1000_175_p`|`Paramount 3D PLA {color_name}`|`Black Cherry`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(blackcherry)_1000_175_p`|`PLA {color_name}`|`(Black Cherry)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplablackcherry_1000_175_p": "7a263a",
    "paramount3d_pla_pla(blackcherry)_1000_175_p": "76232F"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplablackcherry_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(blackcherry)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplablackcherry_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(blackcherry)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplablackcherry_1000_175_p": [
      "WMRL3005490C"
    ],
    "paramount3d_pla_pla(blackcherry)_1000_175_p": null
  }
}
```

### PM075: dup-61c5675e633904440728db21b7b5932edc79db16ad3ae7a3a64dfc6ba1c682a6

Status: APPROVED; survivor `paramount3d_pla_paramount3dplabritishracinggreen_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplabritishracinggreen_1000_175_p`|`Paramount 3D PLA {color_name}`|`British Racing Green`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(britishracinggreen)_1000_175_p`|`PLA {color_name}`|`(British Racing Green)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplabritishracinggreen_1000_175_p": "004225",
    "paramount3d_pla_pla(britishracinggreen)_1000_175_p": "1E5A4F"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplabritishracinggreen_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(britishracinggreen)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplabritishracinggreen_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(britishracinggreen)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplabritishracinggreen_1000_175_p": [
      "GRL60053435C"
    ],
    "paramount3d_pla_pla(britishracinggreen)_1000_175_p": null
  }
}
```

### PM076: dup-f4ddfca7415f81c92bce7fbfe7a6511a7d597ae58f2da0be01653eaa846f290e

Status: APPROVED; survivor `paramount3d_pla_paramount3dplacadetblue_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplacadetblue_1000_175_p`|`Paramount 3D PLA {color_name}`|`Cadet Blue`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(cadetblue)_1000_175_p`|`PLA {color_name}`|`(Cadet Blue)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplacadetblue_1000_175_p": "003b5c",
    "paramount3d_pla_pla(cadetblue)_1000_175_p": "375680"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplacadetblue_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(cadetblue)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplacadetblue_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(cadetblue)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplacadetblue_1000_175_p": [
      "CBRL50235405C"
    ],
    "paramount3d_pla_pla(cadetblue)_1000_175_p": null
  }
}
```

### PM077: dup-1e0a7749efd1d97621d4ae3a490bb0cc9a7b39fd0622034d77c2e1c362007e70

Status: APPROVED; survivor `paramount3d_pla_paramount3dplacaribbeancoral_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplacaribbeancoral_1000_175_p`|`Paramount 3D PLA {color_name}`|`Caribbean Coral`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(caribbeancoral)_1000_175_p`|`PLA {color_name}`|`(Caribbean Coral)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplacaribbeancoral_1000_175_p": "e9897e",
    "paramount3d_pla_pla(caribbeancoral)_1000_175_p": "D56B56"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplacaribbeancoral_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(caribbeancoral)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplacaribbeancoral_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(caribbeancoral)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplacaribbeancoral_1000_175_p": [
      "CPRL30227416C"
    ],
    "paramount3d_pla_pla(caribbeancoral)_1000_175_p": null
  }
}
```

### PM078: dup-eb052cadf86c456f54e83ebc831fb77122db0e3d88cbd3249b28d8fbbe241b90

Status: APPROVED; survivor `paramount3d_pla_paramount3dplacastlelimestonegray_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplacastlelimestonegray_1000_175_p`|`Paramount 3D PLA {color_name}`|`Castle Limestone Gray`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(castlelimestonegray)_1000_175_p`|`PLA {color_name}`|`(Castle Limestone Gray)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplacastlelimestonegray_1000_175_p": "8e9089",
    "paramount3d_pla_pla(castlelimestonegray)_1000_175_p": "A9A8A0"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplacastlelimestonegray_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(castlelimestonegray)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplacastlelimestonegray_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(castlelimestonegray)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplacastlelimestonegray_1000_175_p": [
      "CGRL7023416C"
    ],
    "paramount3d_pla_pla(castlelimestonegray)_1000_175_p": null
  }
}
```

### PM079: dup-2c71f0abc2cc0603731d0ab2882b093f57571088e4972803315fe030e5bc0b6f

Status: APPROVED; survivor `paramount3d_pla_paramount3dpladecepticonpurple_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dpladecepticonpurple_1000_175_p`|`Paramount 3D PLA {color_name}`|`Decepticon Purple`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(decepticonpurple)_1000_175_p`|`PLA {color_name}`|`(Decepticon Purple)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dpladecepticonpurple_1000_175_p": "6a6599",
    "paramount3d_pla_pla(decepticonpurple)_1000_175_p": "431E33"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dpladecepticonpurple_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(decepticonpurple)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dpladecepticonpurple_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(decepticonpurple)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dpladecepticonpurple_1000_175_p": [
      "PRL40077449C"
    ],
    "paramount3d_pla_pla(decepticonpurple)_1000_175_p": null
  }
}
```

### PM080: dup-cced37cd53bd139b6ba8e27bff4e4278226bd4743c32c5bdf23da3843dd3db7a

Status: APPROVED; survivor `paramount3d_pla_paramount3dplaeggyolkyellow_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplaeggyolkyellow_1000_175_p`|`Paramount 3D PLA {color_name}`|`Egg Yolk Yellow`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(eggyolkyellow)_1000_175_p`|`PLA {color_name}`|`(Egg Yolk Yellow)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplaeggyolkyellow_1000_175_p": "f6a950",
    "paramount3d_pla_pla(eggyolkyellow)_1000_175_p": "FF9A14"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplaeggyolkyellow_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(eggyolkyellow)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplaeggyolkyellow_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(eggyolkyellow)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplaeggyolkyellow_1000_175_p": [
      "SYRL1003137C"
    ],
    "paramount3d_pla_pla(eggyolkyellow)_1000_175_p": null
  }
}
```

### PM081: dup-1a2b8bc998ff46e1da5d50dff27505bd5bbcc60aaee4be17023e1669ce17b962

Status: APPROVED; survivor `paramount3d_pla_paramount3dplaenzored_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplaenzored_1000_175_p`|`Paramount 3D PLA {color_name}`|`Enzo Red`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(enzored)_1000_175_p`|`PLA {color_name}`|`(Enzo Red)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplaenzored_1000_175_p": "cc0605",
    "paramount3d_pla_pla(enzored)_1000_175_p": "FC496D"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplaenzored_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(enzored)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplaenzored_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(enzored)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplaenzored_1000_175_p": [
      "TRRL3020485C"
    ],
    "paramount3d_pla_pla(enzored)_1000_175_p": null
  }
}
```

### PM082: dup-f59a6d65d39552b04c925de6eaa68078df71a02fd9b8c580a50e5f9f45d9c07b

Status: APPROVED; survivor `paramount3d_pla_paramount3dplafighterjetblue_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplafighterjetblue_1000_175_p`|`Paramount 3D PLA {color_name}`|`Fighter Jet Blue`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(fighterjetblue)_1000_175_p`|`PLA {color_name}`|`(Fighter Jet Blue)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplafighterjetblue_1000_175_p": "003b49",
    "paramount3d_pla_pla(fighterjetblue)_1000_175_p": "55657C"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplafighterjetblue_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(fighterjetblue)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplafighterjetblue_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(fighterjetblue)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplafighterjetblue_1000_175_p": [
      "FBRL50087546C"
    ],
    "paramount3d_pla_pla(fighterjetblue)_1000_175_p": null
  }
}
```

### PM083: dup-90ed12269a3377b2ad7f5bda538d8b5a71cdd51bd6671627db410338eea4a1f0

Status: APPROVED; survivor `paramount3d_pla_paramount3dplagamecartridgegray_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplagamecartridgegray_1000_175_p`|`Paramount 3D PLA {color_name}`|`Game Cartridge Gray`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(gamecartridgegray)_1000_175_p`|`PLA {color_name}`|`(Game Cartridge Gray)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplagamecartridgegray_1000_175_p": "a7a8aa",
    "paramount3d_pla_pla(gamecartridgegray)_1000_175_p": "B2B8B8"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplagamecartridgegray_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(gamecartridgegray)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplagamecartridgegray_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(gamecartridgegray)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplagamecartridgegray_1000_175_p": [
      "DGRL7042423C"
    ],
    "paramount3d_pla_pla(gamecartridgegray)_1000_175_p": null
  }
}
```

### PM084: dup-b6bc6ae91c92c1b27fb4407bdd5fe7df167eab4598a46d1fc3dc0840c2f66557

Status: APPROVED; survivor `paramount3d_pla_paramount3dplageodeblack_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplageodeblack_1000_175_p`|`Paramount 3D PLA {color_name}`|`Geode Black`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(geodeblack)_1000_175_p`|`PLA {color_name}`|`(Geode Black)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplageodeblack_1000_175_p": null,
    "paramount3d_pla_pla(geodeblack)_1000_175_p": "3E413F"
  },
  "color_hexes": {
    "paramount3d_pla_paramount3dplageodeblack_1000_175_p": [
      "1a1a2e",
      "4a4a6a"
    ],
    "paramount3d_pla_pla(geodeblack)_1000_175_p": null
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplageodeblack_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(geodeblack)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplageodeblack_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(geodeblack)_1000_175_p": [
      50,
      70
    ]
  },
  "multi_color_direction": {
    "paramount3d_pla_paramount3dplageodeblack_1000_175_p": "coaxial",
    "paramount3d_pla_pla(geodeblack)_1000_175_p": null
  },
  "codes": {
    "paramount3d_pla_paramount3dplageodeblack_1000_175_p": [
      "GEOBLACK"
    ],
    "paramount3d_pla_pla(geodeblack)_1000_175_p": null
  }
}
```

### PM085: dup-7ebfaf01b3d81b8de70ce412e4b2a1ead4552d7bebd7a8010b20be72b980b36d

Status: APPROVED; survivor `paramount3d_pla_paramount3dplagoldkrugerrand_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplagoldkrugerrand_1000_175_p`|`Paramount 3D PLA {color_name}`|`Gold Krugerrand`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(goldkrugerrand)_1000_175_p`|`PLA {color_name}`|`(Gold Krugerrand)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplagoldkrugerrand_1000_175_p": "c5a028",
    "paramount3d_pla_pla(goldkrugerrand)_1000_175_p": "F3BC00"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplagoldkrugerrand_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(goldkrugerrand)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplagoldkrugerrand_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(goldkrugerrand)_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "paramount3d_pla_paramount3dplagoldkrugerrand_1000_175_p": "glossy",
    "paramount3d_pla_pla(goldkrugerrand)_1000_175_p": null
  }
}
```

### PM086: dup-216c02d81e2e8a17fa330ebeda4ee08b1fcb3a501736421b560dd7373a4f4f37

Status: APPROVED; survivor `paramount3d_pla_paramount3dplagraphitegray_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplagraphitegray_1000_175_p`|`Paramount 3D PLA {color_name}`|`Graphite Gray`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(graphitegray)_1000_175_p`|`PLA {color_name}`|`(Graphite Gray)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplagraphitegray_1000_175_p": "494e53",
    "paramount3d_pla_pla(graphitegray)_1000_175_p": "55657C"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplagraphitegray_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(graphitegray)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplagraphitegray_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(graphitegray)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplagraphitegray_1000_175_p": [
      "BGRL7043425C"
    ],
    "paramount3d_pla_pla(graphitegray)_1000_175_p": null
  }
}
```

### PM087: dup-6782c3177ebd39f0b66c39abf9ae4692cda8f1dde66beab75e0b03d11ca12c93

Status: APPROVED; survivor `paramount3d_pla_paramount3dplagreatdepressionjadeite_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplagreatdepressionjadeite_1000_175_p`|`Paramount 3D PLA {color_name}`|`Great Depression Jadeite`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(greatdepressionjadeite)_1000_175_p`|`PLA {color_name}`|`(Great Depression Jadeite)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplagreatdepressionjadeite_1000_175_p": "6b7c3c",
    "paramount3d_pla_pla(greatdepressionjadeite)_1000_175_p": "B0C799"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplagreatdepressionjadeite_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(greatdepressionjadeite)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplagreatdepressionjadeite_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(greatdepressionjadeite)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplagreatdepressionjadeite_1000_175_p": [
      "JGRL60217494C"
    ],
    "paramount3d_pla_pla(greatdepressionjadeite)_1000_175_p": null
  }
}
```

### PM088: dup-8109069e9b3fddd4bb32302741d1faf8eadfa6bbf62dbbc1f8ff56b42f1fbb20

Status: APPROVED; survivor `paramount3d_pla_paramount3dplahannibalred_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplahannibalred_1000_175_p`|`Paramount 3D PLA {color_name}`|`Hannibal Red`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(hannibalred)_1000_175_p`|`PLA {color_name}`|`(Hannibal Red)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplahannibalred_1000_175_p": "7b292c",
    "paramount3d_pla_pla(hannibalred)_1000_175_p": "8B3A3A"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplahannibalred_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(hannibalred)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplahannibalred_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(hannibalred)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplahannibalred_1000_175_p": [
      "BHRL3009181C"
    ],
    "paramount3d_pla_pla(hannibalred)_1000_175_p": null
  }
}
```

### PM089: dup-e409537046e0f55ae081ece904c965857af301e5ea6946529fb8985f8e933c09

Status: APPROVED; survivor `paramount3d_pla_paramount3dplaharajukupink_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplaharajukupink_1000_175_p`|`Paramount 3D PLA {color_name}`|`Harajuku Pink`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(harajukupink)_1000_175_p`|`PLA {color_name}`|`(Harajuku Pink)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplaharajukupink_1000_175_p": "e45dbf",
    "paramount3d_pla_pla(harajukupink)_1000_175_p": "FD64B3"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplaharajukupink_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(harajukupink)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplaharajukupink_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(harajukupink)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplaharajukupink_1000_175_p": [
      "TMRL4010675C"
    ],
    "paramount3d_pla_pla(harajukupink)_1000_175_p": null
  }
}
```

### PM090: dup-73257ba59473687d6e416f918bb1e5dae7ac819e4712b34f82c0f0d62c9bb928

Status: APPROVED; survivor `paramount3d_pla_paramount3dplaironred_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplaironred_1000_175_p`|`Paramount 3D PLA {color_name}`|`Iron Red`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(ironred)_1000_175_p`|`PLA {color_name}`|`(Iron Red)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplaironred_1000_175_p": "8b2332",
    "paramount3d_pla_pla(ironred)_1000_175_p": "932721"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplaironred_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(ironred)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplaironred_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(ironred)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplaironred_1000_175_p": [
      "IRRL30111815C"
    ],
    "paramount3d_pla_pla(ironred)_1000_175_p": null
  }
}
```

### PM091: dup-7ffa413f1bd7ce08bd48b7dbee41dfcc7bf84375cf5bc51ee86f75ed47491966

Status: APPROVED; survivor `paramount3d_pla_paramount3dplaivory_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplaivory_1000_175_p`|`Paramount 3D PLA {color_name}`|`Ivory`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(ivory)_1000_175_p`|`PLA {color_name}`|`(Ivory)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplaivory_1000_175_p": "e1cc4f",
    "paramount3d_pla_pla(ivory)_1000_175_p": "FBE9B8"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplaivory_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(ivory)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplaivory_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(ivory)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplaivory_1000_175_p": [
      "IRL10147501C"
    ],
    "paramount3d_pla_pla(ivory)_1000_175_p": null
  }
}
```

### PM092: dup-fce517b8afe08d74249079944436efe3672a6d228b4a528dda5827a5c4b0ba03

Status: APPROVED; survivor `paramount3d_pla_paramount3dplakarnaksandstone_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplakarnaksandstone_1000_175_p`|`Paramount 3D PLA {color_name}`|`Karnak Sandstone`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(karnaksandstone)_1000_175_p`|`PLA {color_name}`|`(Karnak Sandstone)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplakarnaksandstone_1000_175_p": "a0957d",
    "paramount3d_pla_pla(karnaksandstone)_1000_175_p": "C6AD74"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplakarnaksandstone_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(karnaksandstone)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplakarnaksandstone_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(karnaksandstone)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplakarnaksandstone_1000_175_p": [
      "GBRL10197530S"
    ],
    "paramount3d_pla_pla(karnaksandstone)_1000_175_p": null
  }
}
```

### PM093: dup-07dcff11ef4c137681fd325340e3d9d4077882548e79944985379b9099218400

Status: APPROVED; survivor `paramount3d_pla_paramount3dplaleviathanbluegreen_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplaleviathanbluegreen_1000_175_p`|`Paramount 3D PLA {color_name}`|`Leviathan Blue Green`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(leviathanbluegreen)_1000_175_p`|`PLA {color_name}`|`(Leviathan Blue Green)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplaleviathanbluegreen_1000_175_p": "00594c",
    "paramount3d_pla_pla(leviathanbluegreen)_1000_175_p": "244852"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplaleviathanbluegreen_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(leviathanbluegreen)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplaleviathanbluegreen_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(leviathanbluegreen)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplaleviathanbluegreen_1000_175_p": [
      "TBRL5020316C"
    ],
    "paramount3d_pla_pla(leviathanbluegreen)_1000_175_p": null
  }
}
```

### PM094: dup-70705f61ecc9b45ccf7d734d8e083f16006643f8e521830f35f03ae07bf2a040

Status: APPROVED; survivor `paramount3d_pla_paramount3dplamclarenorange_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplamclarenorange_1000_175_p`|`Paramount 3D PLA {color_name}`|`McLaren Orange`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(mclarenorange)_1000_175_p`|`PLA {color_name}`|`(McLaren Orange)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplamclarenorange_1000_175_p": "ff8000",
    "paramount3d_pla_pla(mclarenorange)_1000_175_p": "FA8423"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplamclarenorange_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(mclarenorange)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplamclarenorange_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(mclarenorange)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplamclarenorange_1000_175_p": [
      "ORL20112019C"
    ],
    "paramount3d_pla_pla(mclarenorange)_1000_175_p": null
  }
}
```

### PM095: dup-9b73a084b1e0aac743b415be0a2442bf72dcd3e54296543b0da9d6d48bd1be2c

Status: APPROVED; survivor `paramount3d_pla_paramount3dplamedusastonegray_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplamedusastonegray_1000_175_p`|`Paramount 3D PLA {color_name}`|`Medusa Stone Gray`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(medusastonegray)_1000_175_p`|`PLA {color_name}`|`(Medusa Stone Gray)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplamedusastonegray_1000_175_p": "8e9089",
    "paramount3d_pla_pla(medusastonegray)_1000_175_p": "C3C199"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplamedusastonegray_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(medusastonegray)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplamedusastonegray_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(medusastonegray)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplamedusastonegray_1000_175_p": [
      "CGRL7023416S"
    ],
    "paramount3d_pla_pla(medusastonegray)_1000_175_p": null
  }
}
```

### PM096: dup-85b01ad07bee2181431cbad29bb323d7d6575518db707598477c53364b10f781

Status: APPROVED; survivor `paramount3d_pla_paramount3dplamidcenturyteal_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplamidcenturyteal_1000_175_p`|`Paramount 3D PLA {color_name}`|`Mid Century Teal`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(midcenturyteal)_1000_175_p`|`PLA {color_name}`|`(Mid Century Teal)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplamidcenturyteal_1000_175_p": "007377",
    "paramount3d_pla_pla(midcenturyteal)_1000_175_p": "63D6D6"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplamidcenturyteal_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(midcenturyteal)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplamidcenturyteal_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(midcenturyteal)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplamidcenturyteal_1000_175_p": [
      "ATRL50217718C"
    ],
    "paramount3d_pla_pla(midcenturyteal)_1000_175_p": null
  }
}
```

### PM097: dup-44a04f37f1b50cefb486981c1e329c2aec7dc9d5b862ad279dd1825fb5221166

Status: APPROVED; survivor `paramount3d_pla_paramount3dplamilitarygreen_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplamilitarygreen_1000_175_p`|`Paramount 3D PLA {color_name}`|`Military Green`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(militarygreen)_1000_175_p`|`PLA {color_name}`|`(Military Green)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplamilitarygreen_1000_175_p": "4b5335",
    "paramount3d_pla_pla(militarygreen)_1000_175_p": "6E8451"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplamilitarygreen_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(militarygreen)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplamilitarygreen_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(militarygreen)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplamilitarygreen_1000_175_p": [
      "OGRL60037764C"
    ],
    "paramount3d_pla_pla(militarygreen)_1000_175_p": null
  }
}
```

### PM098: dup-8de0f6f1e1df2e9f8cb1e270aaa69bbe55897da41449200c314db9c69eadf566

Status: APPROVED; survivor `paramount3d_pla_paramount3dplamilitarykhaki_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplamilitarykhaki_1000_175_p`|`Paramount 3D PLA {color_name}`|`Military Khaki`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(militarykhaki)_1000_175_p`|`PLA {color_name}`|`(Military Khaki)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplamilitarykhaki_1000_175_p": "b59a6a",
    "paramount3d_pla_pla(militarykhaki)_1000_175_p": "AE9D7E"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplamilitarykhaki_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(militarykhaki)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplamilitarykhaki_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(militarykhaki)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplamilitarykhaki_1000_175_p": [
      "GBRL10197530C"
    ],
    "paramount3d_pla_pla(militarykhaki)_1000_175_p": null
  }
}
```

### PM099: dup-03b1a19593240c68af7d456f6af7e23c0d9368237fb5bc243deb40d8da14e978

Status: APPROVED; survivor `paramount3d_pla_paramount3dplamilitarymbtbrown_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplamilitarymbtbrown_1000_175_p`|`Paramount 3D PLA {color_name}`|`Military MBT Brown`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(militarymbtbrown)_1000_175_p`|`PLA {color_name}`|`(Military MBT Brown)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplamilitarymbtbrown_1000_175_p": "6b3e2e",
    "paramount3d_pla_pla(militarymbtbrown)_1000_175_p": "C6AD74"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplamilitarymbtbrown_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(militarymbtbrown)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplamilitarymbtbrown_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(militarymbtbrown)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplamilitarymbtbrown_1000_175_p": [
      "MGRL80007560C"
    ],
    "paramount3d_pla_pla(militarymbtbrown)_1000_175_p": null
  }
}
```

### PM100: dup-e7a1b9ee42bc8e422202caa45d4a6b8e46ae6f7c45d62a6a26f8fab9eef1e42e

Status: APPROVED; survivor `paramount3d_pla_paramount3dplaprimordialearth_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplaprimordialearth_1000_175_p`|`Paramount 3D PLA {color_name}`|`Primordial Earth`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(primordialearth)_1000_175_p`|`PLA {color_name}`|`(Primordial Earth)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplaprimordialearth_1000_175_p": "5c4033",
    "paramount3d_pla_pla(primordialearth)_1000_175_p": "AE9D7E"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplaprimordialearth_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(primordialearth)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplaprimordialearth_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(primordialearth)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplaprimordialearth_1000_175_p": [
      "DERL7006G09C"
    ],
    "paramount3d_pla_pla(primordialearth)_1000_175_p": null
  }
}
```

### PM101: dup-2c6238f9986d01b1cb2f33c5e35610c242029e4df9da05d60108d06eb8bbc6bd

Status: APPROVED; survivor `paramount3d_pla_paramount3dplaprototypegray_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplaprototypegray_1000_175_p`|`Paramount 3D PLA {color_name}`|`Prototype Gray`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(prototypegray)_1000_175_p`|`PLA {color_name}`|`(Prototype Gray)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplaprototypegray_1000_175_p": "a7a8aa",
    "paramount3d_pla_pla(prototypegray)_1000_175_p": "D6D7D8"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplaprototypegray_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(prototypegray)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplaprototypegray_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(prototypegray)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplaprototypegray_1000_175_p": [
      "LGRL7035421C"
    ],
    "paramount3d_pla_pla(prototypegray)_1000_175_p": null
  }
}
```

### PM102: dup-5eaf116893174926695b9137376b646496d95b23437eee85e8166670cece8a38

Status: APPROVED; survivor `paramount3d_pla_paramount3dplasilverdollar_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplasilverdollar_1000_175_p`|`Paramount 3D PLA {color_name}`|`Silver Dollar`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(silverdollar)_1000_175_p`|`PLA {color_name}`|`(Silver Dollar)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplasilverdollar_1000_175_p": "8d9093",
    "paramount3d_pla_pla(silverdollar)_1000_175_p": "878DA2"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplasilverdollar_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(silverdollar)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplasilverdollar_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(silverdollar)_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "paramount3d_pla_paramount3dplasilverdollar_1000_175_p": "glossy",
    "paramount3d_pla_pla(silverdollar)_1000_175_p": null
  }
}
```

### PM103: dup-1ef56b713961f66b2fdef12baa3852ff3f51c144e12c15f10bebb5cda231ead1

Status: APPROVED; survivor `paramount3d_pla_paramount3dplasimpsonyellow_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplasimpsonyellow_1000_175_p`|`Paramount 3D PLA {color_name}`|`Simpson Yellow`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(simpsonyellow)_1000_175_p`|`PLA {color_name}`|`(Simpson Yellow)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplasimpsonyellow_1000_175_p": "faca30",
    "paramount3d_pla_pla(simpsonyellow)_1000_175_p": "FADB24"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplasimpsonyellow_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(simpsonyellow)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplasimpsonyellow_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(simpsonyellow)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplasimpsonyellow_1000_175_p": [
      "YRL1018129C"
    ],
    "paramount3d_pla_pla(simpsonyellow)_1000_175_p": null
  }
}
```

### PM104: dup-1ef4442c70070c6c43af435ad7949e40aeb527bd7e7e1d9038c3371b62624bec

Status: APPROVED; survivor `paramount3d_pla_paramount3dplaskin-darkcomplexion_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplaskin-darkcomplexion_1000_175_p`|`Paramount 3D PLA {color_name}`|`Skin - Dark Complexion`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(skin-darkcomplexion)_1000_175_p`|`PLA {color_name}`|`(Skin - Dark Complexion)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplaskin-darkcomplexion_1000_175_p": "a67c52",
    "paramount3d_pla_pla(skin-darkcomplexion)_1000_175_p": "C0894D"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplaskin-darkcomplexion_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(skin-darkcomplexion)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplaskin-darkcomplexion_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(skin-darkcomplexion)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplaskin-darkcomplexion_1000_175_p": [
      "BBRL1011729C"
    ],
    "paramount3d_pla_pla(skin-darkcomplexion)_1000_175_p": null
  }
}
```

### PM105: dup-c1845bcf13e5c83783472ab57d60ffd707b0f63d8c13eca14fd9711b12ff0f77

Status: APPROVED; survivor `paramount3d_pla_paramount3dplaskin-deepcomplexion_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplaskin-deepcomplexion_1000_175_p`|`Paramount 3D PLA {color_name}`|`Skin - Deep Complexion`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(skin-deepcomplexion)_1000_175_p`|`PLA {color_name}`|`(Skin - Deep Complexion)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplaskin-deepcomplexion_1000_175_p": "7a4f3b",
    "paramount3d_pla_pla(skin-deepcomplexion)_1000_175_p": "8C7547"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplaskin-deepcomplexion_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(skin-deepcomplexion)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplaskin-deepcomplexion_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(skin-deepcomplexion)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplaskin-deepcomplexion_1000_175_p": [
      "EBRL80282322C"
    ],
    "paramount3d_pla_pla(skin-deepcomplexion)_1000_175_p": null
  }
}
```

### PM106: dup-26c62bb15e55c387df1ecee4b281165f1aa09d82a7d179d2c42d20113cfaa844

Status: APPROVED; survivor `paramount3d_pla_paramount3dplaskin-faircomplexion_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplaskin-faircomplexion_1000_175_p`|`Paramount 3D PLA {color_name}`|`Skin - Fair Complexion`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(skin-faircomplexion)_1000_175_p`|`PLA {color_name}`|`(Skin - Fair Complexion)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplaskin-faircomplexion_1000_175_p": "d4b59a",
    "paramount3d_pla_pla(skin-faircomplexion)_1000_175_p": "F0DDC2"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplaskin-faircomplexion_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(skin-faircomplexion)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplaskin-faircomplexion_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(skin-faircomplexion)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplaskin-faircomplexion_1000_175_p": [
      "LIRL1015468C"
    ],
    "paramount3d_pla_pla(skin-faircomplexion)_1000_175_p": null
  }
}
```

### PM107: dup-4af7a7b891cc02615d199144325926a480e1fedefeae54d70ca85c320e6f38cd

Status: APPROVED; survivor `paramount3d_pla_paramount3dplaskin-universalbeige_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplaskin-universalbeige_1000_175_p`|`Paramount 3D PLA {color_name}`|`Skin - Universal Beige`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(skin-universalbeige)_1000_175_p`|`PLA {color_name}`|`(Skin - Universal Beige)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplaskin-universalbeige_1000_175_p": "d5b59a",
    "paramount3d_pla_pla(skin-universalbeige)_1000_175_p": "E9CB9B"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplaskin-universalbeige_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(skin-universalbeige)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplaskin-universalbeige_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(skin-universalbeige)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplaskin-universalbeige_1000_175_p": [
      "UBRL10017502C"
    ],
    "paramount3d_pla_pla(skin-universalbeige)_1000_175_p": null
  }
}
```

### PM108: dup-62f8808f468357fc43bcdbfab87dd87810610037985056d7b4cc80bc4a4df212

Status: APPROVED; survivor `paramount3d_pla_paramount3dplastandrewsgreen_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplastandrewsgreen_1000_175_p`|`Paramount 3D PLA {color_name}`|`St Andrews Green`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(standrewsgreen)_1000_175_p`|`PLA {color_name}`|`(St Andrews Green)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplastandrewsgreen_1000_175_p": "4a7729",
    "paramount3d_pla_pla(standrewsgreen)_1000_175_p": "446B20"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplastandrewsgreen_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(standrewsgreen)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplastandrewsgreen_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(standrewsgreen)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplastandrewsgreen_1000_175_p": [
      "PGRL60107742C"
    ],
    "paramount3d_pla_pla(standrewsgreen)_1000_175_p": null
  }
}
```

### PM109: dup-346e09c36b60315e38f586a3e7dfea953b95c336f8ace1e53c3689ddc82ed053

Status: APPROVED; survivor `paramount3d_pla_paramount3dplastealthgray_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplastealthgray_1000_175_p`|`Paramount 3D PLA {color_name}`|`Stealth Gray`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(stealthgray)_1000_175_p`|`PLA {color_name}`|`(Stealth Gray)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplastealthgray_1000_175_p": "5c5f63",
    "paramount3d_pla_pla(stealthgray)_1000_175_p": "616469"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplastealthgray_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(stealthgray)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplastealthgray_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(stealthgray)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplastealthgray_1000_175_p": [
      "IGRL7021419C"
    ],
    "paramount3d_pla_pla(stealthgray)_1000_175_p": null
  }
}
```

### PM110: dup-5c4061346db9d9a014bb45403616a5e4fddad1f96095455dc9724fc39237683b

Status: APPROVED; survivor `paramount3d_pla_paramount3dplasteelgray_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplasteelgray_1000_175_p`|`Paramount 3D PLA {color_name}`|`Steel Gray`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(steelgray)_1000_175_p`|`PLA {color_name}`|`(Steel Gray)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplasteelgray_1000_175_p": "a8a9ad",
    "paramount3d_pla_pla(steelgray)_1000_175_p": "818FA0"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplasteelgray_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(steelgray)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplasteelgray_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(steelgray)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplasteelgray_1000_175_p": [
      "SGRL7000430C"
    ],
    "paramount3d_pla_pla(steelgray)_1000_175_p": null
  }
}
```

### PM111: dup-7df90b6bd72a6bb77efba9079b035fa7f0cba90c7a4aea9b96fe58beb2e397c6

Status: APPROVED; survivor `paramount3d_pla_paramount3dplaterracopper_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplaterracopper_1000_175_p`|`Paramount 3D PLA {color_name}`|`Terra Copper`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(terracopper)_1000_175_p`|`PLA {color_name}`|`(Terra Copper)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplaterracopper_1000_175_p": "b87333",
    "paramount3d_pla_pla(terracopper)_1000_175_p": "C88582"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplaterracopper_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(terracopper)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplaterracopper_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(terracopper)_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "paramount3d_pla_paramount3dplaterracopper_1000_175_p": "glossy",
    "paramount3d_pla_pla(terracopper)_1000_175_p": null
  },
  "codes": {
    "paramount3d_pla_paramount3dplaterracopper_1000_175_p": [
      "CBRL8004484C"
    ],
    "paramount3d_pla_pla(terracopper)_1000_175_p": null
  }
}
```

### PM112: dup-114c12faf7414ee194dba7a51ce978ec84fdd08380e799a98f88699bfa2a8b0d

Status: APPROVED; survivor `paramount3d_pla_paramount3dplaterracotta_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplaterracotta_1000_175_p`|`Paramount 3D PLA {color_name}`|`Terra Cotta`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(terracotta)_1000_175_p`|`PLA {color_name}`|`(Terra Cotta)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplaterracotta_1000_175_p": "9f4d36",
    "paramount3d_pla_pla(terracotta)_1000_175_p": "D99773"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplaterracotta_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(terracotta)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplaterracotta_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(terracotta)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplaterracotta_1000_175_p": [
      "BRRL30127591C"
    ],
    "paramount3d_pla_pla(terracotta)_1000_175_p": null
  }
}
```

### PM113: dup-08318ea0867a90726003fda9795e1a121a3e3928d55fe4ea7c2a3de791b33351

Status: APPROVED; survivor `paramount3d_pla_paramount3dplatuxedomidnightblue_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplatuxedomidnightblue_1000_175_p`|`Paramount 3D PLA {color_name}`|`Tuxedo Midnight Blue`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(tuxedomidnightblue)_1000_175_p`|`PLA {color_name}`|`(Tuxedo Midnight Blue)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplatuxedomidnightblue_1000_175_p": "003b5c",
    "paramount3d_pla_pla(tuxedomidnightblue)_1000_175_p": "1E2C73"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplatuxedomidnightblue_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(tuxedomidnightblue)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplatuxedomidnightblue_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(tuxedomidnightblue)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplatuxedomidnightblue_1000_175_p": [
      "NBRL5011296C"
    ],
    "paramount3d_pla_pla(tuxedomidnightblue)_1000_175_p": null
  }
}
```

### PM114: dup-c944d1783a8bd40072521509debac8c9eff876f1c35f8af6a9a6511d0b639351

Status: APPROVED; survivor `paramount3d_pla_paramount3dplavolcanoorange_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplavolcanoorange_1000_175_p`|`Paramount 3D PLA {color_name}`|`Volcano Orange`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(volcanoorange)_1000_175_p`|`PLA {color_name}`|`(Volcano Orange)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplavolcanoorange_1000_175_p": "c74700",
    "paramount3d_pla_pla(volcanoorange)_1000_175_p": "E0493E"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplavolcanoorange_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(volcanoorange)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplavolcanoorange_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(volcanoorange)_1000_175_p": [
      50,
      70
    ]
  },
  "codes": {
    "paramount3d_pla_paramount3dplavolcanoorange_1000_175_p": [
      "VORL20027626C"
    ],
    "paramount3d_pla_pla(volcanoorange)_1000_175_p": null
  }
}
```

### PM115: dup-39f8a3fbcbdfaaac77f178715ceb0a7941955126321b904a6979f9c1a8488b4c

Status: APPROVED; survivor `paramount3d_pla_paramount3dplawhite_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`paramount3d_pla_paramount3dplawhite_1000_175_p`|`Paramount 3D PLA {color_name}`|`White`|{"source_file": "paramount3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 50, "compiled_records": 50} / False|
|`paramount3d_pla_pla(white)_1000_175_p`|`PLA {color_name}`|`(White)`|{"source_file": "paramount3d.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 47, "compiled_records": 47} / False|

Owner-pattern override explicitly approved: older well-formed prefixed family retained; OFD bracketed color names retired. Prefix cleanup deferred; no identifier transfer.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "paramount3d_pla_paramount3dplawhite_1000_175_p": "f4f4f4",
    "paramount3d_pla_pla(white)_1000_175_p": "FFFFFF"
  },
  "extruder_temp_range": {
    "paramount3d_pla_paramount3dplawhite_1000_175_p": [
      195,
      210
    ],
    "paramount3d_pla_pla(white)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "paramount3d_pla_paramount3dplawhite_1000_175_p": [
      0,
      0
    ],
    "paramount3d_pla_pla(white)_1000_175_p": [
      50,
      70
    ]
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

- `paramount3d_pla_paramount3dplaaztecgold_1000_175_p` — Paramount 3D PLA Aztec Gold
- `paramount3d_pla_paramount3dplachameleon_1000_175_p` — Paramount 3D PLA Chameleon
- `paramount3d_pla_paramount3dplacolossuscopper_1000_175_p` — Paramount 3D PLA Colossus Copper
- `paramount3d_pla_paramount3dplaultraviolet_1000_175_p` — Paramount 3D PLA Ultraviolet
- `paramount3d_petg-cf_paramount3dpetg-cfblack_1000_175_p` — Paramount 3D PETG-CF Black
- `paramount3d_petg-cf_paramount3dpetg-cfsteampunk_1000_175_p` — Paramount 3D PETG-CF Steampunk
- `paramount3d_abs-cf_paramount3dabs-cfblack_1000_175_p` — Paramount 3D ABS-CF Black
- `paramount3d_abs_abscf(black)_1000_175_p` — ABS CF (Black)
- `paramount3d_pa6_pa6cfnyloncarbonfiber_1000_175_p` — PA6 CF Nylon Carbon Fiber
- `paramount3d_petg_petgcf(black)_1000_175_p` — PETG CF (Black)
- `paramount3d_petg_petgcf(steampunk)_1000_175_p` — PETG CF (Steampunk)
- `paramount3d_pla_plaflexautobotblue_1000_175_p` — PLA Flex Autobot Blue
- `paramount3d_pla_plaflexblack_1000_175_p` — PLA Flex Black
- `paramount3d_pla_plaflexbritishracinggreen_1000_175_p` — PLA Flex British Racing Green
- `paramount3d_pla_plaflexenzored_1000_175_p` — PLA Flex Enzo Red
- `paramount3d_pla_plaflexgraphitegray_1000_175_p` — PLA Flex Graphite Gray
- `paramount3d_pla_plaflexharajukupink_1000_175_p` — PLA Flex Harajuku Pink
- `paramount3d_pla_plaflexironred_1000_175_p` — PLA Flex Iron Red
- `paramount3d_pla_plaflexmilitarygreen_1000_175_p` — PLA Flex Military Green
- `paramount3d_pla_plaflexmilitarykhaki_1000_175_p` — PLA Flex Military Khaki
- `paramount3d_pla_plaflexprototypegray_1000_175_p` — PLA Flex Prototype Gray
- `paramount3d_pla_plaflexskindarkcomplexion_1000_175_p` — PLA Flex Skin Dark Complexion
- `paramount3d_pla_plaflexskinfaircomplexion_1000_175_p` — PLA Flex Skin Fair Complexion
- `paramount3d_pla_plaflexskinivory_1000_175_p` — PLA Flex Skin Ivory
- `paramount3d_pla_plaflexskinuniversalbeige_1000_175_p` — PLA Flex Skin Universal Beige
- `paramount3d_pla_plaflexwhite_1000_175_p` — PLA Flex White
- `paramount3d_pla_pla(bluetowhite)colorchangingfilament_1000_175_p` — PLA (Blue to White) Color Changing Filament
- `paramount3d_pla_placoolwhite_1000_175_p` — PLA Cool White
- `paramount3d_pla_silkpla(aztecgold)_1000_175_p` — Silk PLA (Aztec Gold)
- `paramount3d_pla_silkpla(chameleon)_1000_175_p` — Silk PLA (Chameleon)
- `paramount3d_pla_silkpla(colossuscopper)_1000_175_p` — Silk PLA (Colossus Copper)
- `paramount3d_pla_silkpla(ultraviolet)_1000_175_p` — Silk PLA (Ultraviolet)
- `paramount3d_pva_pva(natural)dissolvablefilament_1000_175_p` — PVA (Natural) Dissolvable Filament
- `paramount3d_tpu_tpu(black)_1000_175_p` — TPU (Black)
- `paramount3d_tpu_tpu(ironred)_1000_175_p` — TPU (Iron Red)
- `paramount3d_tpu_tpu(midcenturyteal)_1000_175_p` — TPU (Mid Century Teal)
