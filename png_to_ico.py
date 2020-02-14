from PIL import Image

#fn_input = input("Enter the full path and filename of the image file: ")
# TODO input validation and error handling
#fn = r"{}".format(fn_input)

fn = r"C:\Users\Ben\Desktop\Internal Tools\png-icons-4.png"

img = Image.open(fn)
img.save('test.ico')
