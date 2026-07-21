import sys
import os
from PIL import Image
from PIL import ImageOps

def input_file():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    root_in, ext_in = os.path.splitext(input_file)
    root_out, ext_out = os.path.splitext(output_file)

    valid_exts = [".jpg", ".jpeg", ".png"]
    if ext_in.lower() not in valid_exts or ext_out.lower() not in valid_exts:
        sys.exit("Invalid input")

    if ext_in.lower() != ext_out.lower():
        sys.exit("Input and output have different extensions")

    return input_file, output_file

def overlay_shirt(read_image, save_image):
    try:
        read = Image.open(read_image)
        shirt = Image.open("shirt.png")

        fit = ImageOps.fit(read, shirt.size)

        fit.paste(shirt, shirt)

        fit.save(save_image)

    except FileNotFoundError:
        sys.exit("File does not exist")

def main():

    read, save = input_file()

    overlay_shirt(read, save)

if __name__ == "__main__":
    main()
