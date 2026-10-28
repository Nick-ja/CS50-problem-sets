import sys
import os
import PIL
from PIL import Image, ImageOps


def main():
    file_names = command_line_arguments()
    input_picture = file_names[0]
    output = file_names[1]

    # open the images
    try:
        image = Image.open(input_picture)
        shirt = Image.open("shirt.png")
    # raise error when file is not found
    except FileNotFoundError:
        sys.exit("Input does not exist")

    size = shirt.size

    # resize the image
    image = PIL.ImageOps.fit(image, size)
    # Combine the 2 images
    image.paste(shirt)
    # show the combined images
    image.show()


def command_line_arguments():
    # Exit with sys.exit if the user does not specify exactly two command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    # Exit with sys.exit if the user does not specify exactly two command-line arguments
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Save the extensions of the file
    image_1 = os.path.splitext(sys.argv[1])
    image_2 = os.path.splitext(sys.argv[2])

    # Exit with sys.exit if the specified file’s name does not end in .jpg or .jpeg or .png
    if image_1[1] != ".jpg" and image_1[1] != ".jpeg" and image_1[1] != ".png":
        sys.exit("Invalid input")

    # Exit with sys.exit if the specified file’s name does not end in .jpg or .jpeg or .png
    if image_2[1] != ".jpg" and image_2[1] != ".jpeg" and image_2[1] != ".png":
        sys.exit("Invalid output")

    # Exit with sys.exit if the input's name does not have the same extension as the output's name
    if image_1[1] != image_2[1]:
        sys.exit("Input and output have different extensions")

    # Return the 2 file names
    if len(sys.argv) == 3:
        return sys.argv[1:]


if __name__ == "__main__":
    main()