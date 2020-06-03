"""
Batch resize for .jpg's
"""

from PIL import Image
import pathlib

maxsize = (512, 512)  # Sets MAX dimensions

for input_img_path in pathlib.Path("images2").iterdir():  # Folder location
    output_img_path = str(input_img_path).replace("images2", "images3")  # image3 is the output folder
    with Image.open(input_img_path) as im:
        im.thumbnail(maxsize)
        im.save(output_img_path, "JPEG", dpi=(300, 300))
        print(f"processing file {input_img_path} done...")
