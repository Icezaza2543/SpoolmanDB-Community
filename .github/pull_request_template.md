## 📝 Description

Provide a brief summary of the changes and what they accomplish. 
*Example: Added Hatchbox PLA colors or fixed the density of PETG in materials.*

---

## 📂 Type of Change

- [ ] ➕ **New Filament / Brand Data** (Adding brand new files/records)
- [ ] 🔧 **Data Correction / Update** (Fixing incorrect color hex, temperature, spelling, etc.)
- [ ] ⚙️ **Schema or Tooling** (Modifying json schemas or python compilation scripts)
- [ ] 📚 **Documentation** (Improving README, CONTRIBUTING, etc.)

---

## 🔍 Data Sources & Verification

> [!IMPORTANT]
> Please provide official manufacturer links, product page URLs, or screenshots of packaging/spools as evidence. PRs without verifyable sources may be delayed or closed.

- **Manufacturer Specs URL**: 
- **Other Evidence (optional)**: 

---

## 🧪 Verification Checklist

Please run the following validation checks locally before submitting. Check all that apply:

- [ ] **Data compiles successfully:** Ran `python scripts/compile_filaments.py` with no errors.
- [ ] **Materials schema valid:** Ran `check-jsonschema --schemafile materials.schema.json materials.json` and passed.
- [ ] **Filaments schema valid:** Ran `check-jsonschema --schemafile filaments.schema.json filaments/*` and passed.

---

## 📌 Additional Notes
Add any other context, compatibility concerns, or details here.