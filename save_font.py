import os
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

# آدرس فونت را در اینجا وارد کنید
# Path to the font file
font_file_path = ".\Raleway-BoldItalic.ttf"

# Read the font file
font = TTFont(font_file_path)

# Open a text file for writing
output_file_path = "./font_info.txt"

# Create output directory if it doesn't exist
output_folder = "./output_images/"
os.makedirs(output_folder, exist_ok=True)

with open(output_file_path, "w", encoding="utf-8") as output_file:
    # Redirect standard output to the file
    import sys
    sys.stdout = output_file

    # Display font name
    font_name = font["name"].getName(1, 3, 1, 1033).toStr()
    print("Font Name:", font_name)
    
    # Display font version
    font_version = font["head"].fontRevision
    print("Font Version:", font_version)
    
    # Display line metrics
    print("Ascent:", font["OS/2"].sTypoAscender)
    print("Descent:", font["OS/2"].sTypoDescender)
    print("Line Gap:", font["OS/2"].sTypoLineGap)
        # Display characters information
    for char_table in font["cmap"].tables:
        for char_code, glyph_id in char_table.cmap.items():
            char = chr(char_code)
            print(f"Character: {char} Code: {char_code} Glyph ID: {glyph_id}")


# Restore standard output
sys.stdout = sys.__stdout__


# Create images of characters
for char_table in font["cmap"].tables:
    for char_code, glyph_id in char_table.cmap.items():
        char = chr(char_code)
        if char.isprintable():
            # Create an image
            image = Image.new("RGB", (50, 50), color="white")
            draw = ImageDraw.Draw(image)

            # Load the font
            try:
                font_path = font_file_path
                font_size = 40
                font = ImageFont.truetype(font_path, font_size)
            except Exception as e:
                print("Error:", e)
                continue

            # Render the character
            draw.text((10, 5), char, fill="black", font=font)

            # Save the image
            image.save(f"{output_folder}{char_code}.png")

# Close the font file
# font.close()