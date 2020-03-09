from PIL import Image

fn_input = input("Enter the full path and filename of the image file: ")
# TODO input validation and error handling

fn = r"{}".format(fn_input)
print("{}".format(fn))

input("press any key to continue")

img = Image.open(fn)
img.save('test.ico')

input("any key to exit")
