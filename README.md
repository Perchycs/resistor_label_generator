Resistor Label Generator for 3D Printed Storage Box
---------------------------------------------------
This script generates resistor labels as images and compiles them into a printable PDF.
It allows customization of label dimensions, fonts, page sizes, and resistor values.
Currently it will generate a set of labels to fit my print profile found [here](https://makerworld.com/en/models/544850-resistor-storage-parametric?from=search#profileId-1182552)

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
