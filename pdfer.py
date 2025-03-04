#!/usr/bin/env python3
"""
Resistor Label Generator for 3D Printed Storage Box
---------------------------------------------------
This script generates resistor labels as images and compiles them into a printable PDF.
It allows customization of label dimensions, fonts, page sizes, and resistor values.

## How to Use
This process is easiest if all steps are done in the terminal.

1. **Install Python (if not installed)**
   - Download and install Python from https://www.python.org/

2. **Create a Directory for the Script**
   ```sh
   mkdir -p ~/Downloads/resistor_labels
   cd ~/Downloads/resistor_labels
   ```

3. **Download or Copy the Script**
   - Save this script as `resistor_labels.py` inside the `resistor_labels` folder.

4. **Set Up a Virtual Environment**
   ```sh
   python3 -m venv venv
   ```

5. **Activate the Virtual Environment**
   ```sh
   source venv/bin/activate  # On macOS/Linux
   venv/Scripts/activate    # On Windows (Command Prompt) (may need to swap to backslashes)
   ```

6. **Install Dependencies**
   ```sh
   pip install Pillow reportlab
   ```

7. **Ensure a Valid Font File is Available**
   - The script requires a TrueType font file (TTF). If `Arial.ttf` is missing, either:
     - Place an `Arial.ttf` file in the script directory.
     - Change `FONT_PATH` in the script to another available font (e.g., `/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf`).

8. **Run the Script**
   ```sh
   python resistor_labels.py
   ```
   - This will generate resistor label images in the `labels/` folder and create `labels.pdf`
     containing all labels arranged for printing.

## Customization
Modify the values in the script under each section to change label dimensions, page size, font, etc.
"""

from PIL import Image, ImageDraw, ImageFont
import os, math, glob
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.colors import gray

# =============================================================================
# 1. GENERAL SETTINGS
# =============================================================================
DPI = 300                              # Image resolution in dots per inch (DPI)
LABEL_WIDTH_MM = 15                    # Label width in millimeters
LABEL_HEIGHT_MM = 15                   # Label height in millimeters
PAGE_SIZE = A4                         # PDF page size (A4, Letter, or custom tuple)

# =============================================================================
# 2. RESISTOR LABEL SETTINGS
# =============================================================================
RESISTOR_VALUES = [
    10, 22, 47, 100, 150, 200, 220, 270, 330, 470, 510, 680, 1000, 2200, 2700, 3300, 4700,
    5100, 6800, 10000, 20000, 47000, 51000, 68000, 100000, 220000, 300000, 470000, 680000, 1000000
]
RESISTOR_BANDS = 5  # 4-band or 5-band resistor color coding
BAR_COLORS = {
    "black": "#1D1616", "brown": "#A66E38", "red": "#F95454", "orange": "#FA812F",
    "yellow": "#FFEB00", "green": "#829460", "blue": "#1EAFED", "violet": "#B771E5",
    "gray": "#929AAB", "white": "#F6F1E9", "gold": "#D4AF37", "silver": "#C0C0C0"
}

# =============================================================================
# 3. FONT SETTINGS
# =============================================================================
FONT_PATH = "Arial.ttf"  # Update this path to a valid TTF font file
FONT_SIZE_PERCENT = 23   # Font size as percentage of label height

# =============================================================================
# 4. LAYOUT SETTINGS (for Label Generation)
# =============================================================================
TEXT_AREA_HEIGHT_PERCENT = 25  # Percentage of label height occupied by text
GAP_PERCENT = 3                # Gap between text and resistor drawing
RESISTOR_WIDTH_PERCENT = 80    # Percentage of label width occupied by resistor
BAND_WIDTH_PERCENT = 70        # Percentage of resistor body occupied by bands

# =============================================================================
# 5. PDF SHEET LAYOUT SETTINGS
# =============================================================================
mm_to_pt = 2.83465             # Conversion factor: 1 mm = 2.83465 points
DRAWER_WIDTH_MM = 101.5        # Total drawer width (used for label layout)
NUM_COLUMNS = 6                # Number of labels per row in the PDF

# Compute label sizes in points for the PDF
cell_width_pt = (DRAWER_WIDTH_MM * mm_to_pt) / NUM_COLUMNS
label_height_pt = LABEL_HEIGHT_MM * mm_to_pt
img_width = cell_width_pt * 0.9
img_height = label_height_pt * 0.9
margin = 20
left_margin_pdf = margin
page_width, page_height = PAGE_SIZE

# =============================================================================
# Conversion: mm to pixels for Label Generation
# =============================================================================
LABEL_WIDTH = int(LABEL_WIDTH_MM * DPI / 25.4)
LABEL_HEIGHT = int(LABEL_HEIGHT_MM * DPI / 25.4)

# =============================================================================
# LABEL GENERATION (PIL)
# =============================================================================
def create_label(value, output_folder="labels"):
    """Generate a single label image for a resistor value."""
    os.makedirs(output_folder, exist_ok=True)
    try:
        font = ImageFont.truetype(FONT_PATH, int(LABEL_HEIGHT * FONT_SIZE_PERCENT / 100))
    except OSError:
        print(f"Error: Could not load font '{FONT_PATH}'. Ensure the file exists or update FONT_PATH.")
        return
    img = Image.new("RGB", (LABEL_WIDTH, LABEL_HEIGHT), "white")
    draw = ImageDraw.Draw(img)
    text = f"{value}Ω"
    bbox = draw.textbbox((0, 0), text, font=font)
    draw.text(((LABEL_WIDTH - (bbox[2] - bbox[0])) / 2, (LABEL_HEIGHT * TEXT_AREA_HEIGHT_PERCENT / 100 - (bbox[3] - bbox[1])) / 2), text, font=font, fill="black")
    img.save(os.path.join(output_folder, f"{value}.png"))

def generate_labels(values):
    """Generate labels for all resistor values."""
    for v in values:
        create_label(v)

generate_labels(RESISTOR_VALUES)
print("Labels generated in 'labels' folder.")
