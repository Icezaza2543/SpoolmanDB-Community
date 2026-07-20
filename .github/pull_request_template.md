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
- [ ] **Data and schemas validate:** Ran `python scripts/validate.py` and passed.
- [ ] **Regression tests pass:** Ran `python -m pytest -q` and passed.
- [ ] **Spoolman compatibility passes:** Ran `python scripts/check_spoolman_compat.py --upstream-file contracts/spoolman_externaldb.py` and passed.

---

## 📌 Additional Notes
Add any other context, compatibility concerns, or details here.
