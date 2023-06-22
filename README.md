# Requirements
1. Have a marc file named `items.marc` in this directory
2. Install pymarc

# Workflow
0. Go through the steps in `system_setup.sh` (Manual intervention required)
1. Download the Patrons file from Alexandria
2. Rename it to `patrons.csv`
3. Run the `parse_alexandria_patrons_to_koha.py` script
4. Upload the `patrons_parsed.csv` file to Koha in tools > import patrons
5. Download the Items MARC file from Alexandria
6. Rename it to `items.marc` and place it in this directory
7. Run the `parse_alexandria_items_to_koha.py` script
8. Add item types for each item type printed by this script in admin > item types
9. Upload `items_parsed.marc` to Koha in cataloging > stage records.
10. Download the ciruculations file from Alexandria
11. Rename it to `circulations.csv` and place it in this directory
12. Run the `parse_alexandria_circulations_to_koha.py` script
13. Upload the `circulations_parsed.koc` file to Koha at circulation > add offline circulation
