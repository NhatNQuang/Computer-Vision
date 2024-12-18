import os
from PIL import Image

def load_image(image_path):
    """
        Read form given path and return image's object
        Args: image_path
        Returns: image's object
    """
    try:
        img = Image.open(image_path)
        return img
    except Exception as e:
        print("Error when read image from: ", image_path, " ", e)
        return None # return nothing
    

def is_image_file(file_path):
    """
        Return True: it is a image
                False: not image
    """
    extensions = (".jpg", ".png", ".jpeg", ".gif", ".bmp")
    return file_path.lower().endswith(extensions)

def get_image_list(folder_path): # get all images from a folder
    image_list = []
    if os.path.exists(folder_path) and os.path.isdir(folder_path): # whether folder_path exxist and a real folder
        filenames = os.listdir(folder_path) # return name of files and folder within folder_path
        for filename in filenames:
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) and is_image_file(file_path): # whether it is a real file and is a image file or not
                img = load_image(file_path)
                image_list.append(img)
    return image_list
