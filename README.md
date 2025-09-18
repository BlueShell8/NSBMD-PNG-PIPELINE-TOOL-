# NSBMD PNG Pipeline Tool - Mega Ultra Edition 😎

## Overview

This tool allows you to edit **NSBMD files** (e.g., `w1.nsbmd`) for **New Super Mario Bros. DS** by exporting the textures as PNGs, editing them (e.g., with **Tinke**), and then importing them back into the NSBMD file.
The tool includes epic ASCII banners, dummy layers, slow-print effects, color animations, random events, and backups for maximum coolness factor.

---

## Features

- Automatically exports NSBMD bitmaps to PNG files
- Prepares the PNGs for editing in Tinke or other graphics tools
- Imports edited PNGs back into the NSBMD file
- Creates backups of the original files
- Epic ASCII banners, loading animations, and color output
- Random events and Easter eggs for fun and epic length
- Fully automated folder creation (`map`, `png`, `finished`)

---

## Installation

1. Install **Python 3.10 or higher**:
[Python Download](https://www.python.org/downloads/)

2. **Install the required library**:
Open CMD or PowerShell and type:
```powershell
pip install pillow
Save the script:
Save the Python script as nsbmd_pipeline_final.py.

Folder Structure
The tool automatically creates folders; you only need to place the files:

scss
Copy code
map       ← Place the original NSBMD file(s) here
png       ← Place the edited PNGs here (after Tinke)
finished  ← The finished NSBMD file will be placed here
Note:

The "map" folder must contain at least the original w1.nsbmd file, otherwise the tool cannot export anything.

The "png" folder only becomes relevant after the PNGs have been edited in Tinke. Usage
Run the script:

powershell
Copy code
cd path\to\script
python nsbmd_pipeline_final.py
An ASCII banner and dummy layers will be displayed.

Edit the PNGs in the "png" folder using Tinke.

When the PNGs are finished, press Enter.

The tool will automatically repack the PNGs into the NSBMD.

The finished NSBMD file will be located in the "finished" folder, e.g.:

Copy code
finished\w1_mega_fixed_4.nsbmd
Tips for Tinke
Make sure the PNG is saved in the correct TEX0/TEX1 format.

Do not change the original resolution or pixel size, otherwise NSMBe might crash.

Use Tinke only for image editing; the script handles repacking into NSBMD.

Notes & Warnings
This tool modifies the NSBMD file, so always create a backup first.

If the PNGs are incorrectly formatted, NSMBe might crash.

Dummy layers, ASCII banners, slow prints, colored outputs, and random events are purely for epic length and coolness – they don't affect the import.

Support / Issues
If the tool can't find the PNGs: Check that the files are in the correct "png" folder.

Error messages about Python packages: Make sure Pillow is installed.

If crashes occur: Check the PNG size, resolution, and TEX0/TEX1 format.

License
This tool is free for personal use.
No guarantee of compatibility with NSMBe, Tinke, or ROMs.
Use at your own risk.

Fun Facts 😎
Mega ASCII banner on startup

Random events & Easter eggs

Epic loading animations with dummy layers

Have fun modding your NSBMD files!