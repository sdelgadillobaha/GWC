from PIL import Image

def load_img(image):
    img = Image.open(image)
    return img 

def show_img(object):
    object.show()

def save_img(img_object,save_name):
    img_object.save(save_name)


img_object = load_img("tikki.jpg")

show_img(img_object)
save_img(img_object, "tikki2.jpg")

# should return new img object with filter applied
def obamicon(img_object):
    original_pixels = img_object.getdata()
    intensities[]
    for i in original_pixels:
        cpixel
    # create new empty list which you will put all new pixel values into (HINT: USE APPEND)
    # use for loop to iterate through every single pixel
    #     at every pixel some up the RGB values
    #     use conditionals and boolean checks to determine which new color to change to
