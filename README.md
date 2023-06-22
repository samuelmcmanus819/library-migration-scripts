# Requirements
1. Have a KOC template with no data in it called `master.koc` in this directory
2. Install pymarc

# Workflow
0. Go through the steps in `system_setup.sh` (Manual intervention required)
1. Make the new patron categories ADUL, MINO, VOL, FOL in admin > patron categories
2. Download the Patrons file from Alexandria with the header set to Field Names
3. Rename it to `patrons.csv`
4. Run the `parse_alexandria_patrons_to_koha.py` script
5. Upload the `patrons_parsed.csv` file to Koha in tools > import patrons
6. Download the Items MARC file from Alexandria in title-based MARC21 format
7. Rename it to `items.marc` and place it in this directory
8. Run the `parse_alexandria_items_to_koha.py` script
9. Add item types for each item type printed by this script in admin > item types
10. Upload `items_parsed.marc` to Koha in cataloging > stage records.
11. Download the ciruculations file from Alexandria with the header set to Field Names
12. Rename it to `circulations.csv` and place it in this directory
13. Run the `parse_alexandria_circulations_to_koha.py` script
14. Upload the `circulations_parsed.koc` file to Koha at circulation > add offline circulation
15. Library staff to update item types and process offline circulations