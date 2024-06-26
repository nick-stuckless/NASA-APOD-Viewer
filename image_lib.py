'''
Library of useful functions for working with images.
  /|  |\            /|  |\
 / |  | \          / |  | \
 | |  | |          | |  | |
 \  \/  /  __  __  \  \/  /
  \    /  / /  \ \  \    /
   \  /   \ \__/ /   \  /
   \  /   /      \   \  /
  _ \ \__/ O    O \__/ / _
  \\ \___          ___/ //
_  \\___/  ______  \___//  _   <--- He will pinch you if  
\\  ----(          )----  //        you give a bad grade.
 \\_____( ________ )_____//
  ~-----(          )-----~ _
   _____( ________ )_____  \\
  /,----(          )----  _//
 //     (  ______  )     /  \
 ~       \        /      \  /
          \  __  /       / /
           \    /       / /
            \   \      / /
             \   ~----~ /
              \________/
'''
import requests
import ctypes

def main():
    # TODO: Add code to test the functions in this module
      
    image = download_image('https://apod.nasa.gov/apod/image/0001/flammarion_halfcolor.gif')
    image_path = "C:/Temp/test.gif"
    save_image_file(image, image_path)

    return

def download_image(image_url):
    """Downloads an image from a specified URL.

    DOES NOT SAVE THE IMAGE FILE TO DISK.

    Args:
        image_url (str): URL of image

    Returns:
        bytes: Binary image data, if succcessful. None, if unsuccessful.
    """
    url = image_url
    resp = requests.get(url)
    print(f'Downloading image from {url}...', end=' ')
    if resp.status_code == requests.codes.ok:
        file_content = resp.content
        print('success')
    else:
        print('Failure')
        print(f'Response code: {resp.status_code} ({resp.reason})')     
    return file_content

def save_image_file(image_data, image_path):
    """Saves image data as a file on disk.
    
    DOES NOT DOWNLOAD THE IMAGE.

    Args:
        image_data (bytes): Binary image data
        image_path (str): Path to save image file

    Returns:
        bytes: True, if succcessful. False, if unsuccessful
    """
    try:
        print(f"Saving image file as {image_path}...", end=' ')
        with open(image_path, 'wb') as file:
            file.write(image_data)
        print("Success")
        return True
    except:
        print("Failure")
        return False

def set_desktop_background_image(image_path):
    """Sets the desktop background image to a specific image.

    Args:
        image_path (str): Path of image file

    Returns:
        bytes: True, if succcessful. False, if unsuccessful        
    """
    print(f"Setting desktop to {image_path}...", end=' ')
    SPI_SETDESKWALLPAPER = 20
    try:
        if ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3):
            print("Success")
            return True
        else:
            print("failure")
    except:
        print("failure")
    return False
    

def scale_image(image_size, max_size=(800, 600)):
    """Calculates the dimensions of an image scaled to a maximum width
    and/or height while maintaining the aspect ratio  

    Args:
        image_size (tuple[int, int]): Original image size in pixels (width, height) 
        max_size (tuple[int, int], optional): Maximum image size in pixels (width, height). Defaults to (800, 600).

    Returns:
        tuple[int, int]: Scaled image size in pixels (width, height)
    """
    ## DO NOT CHANGE THIS FUNCTION ##
    # NOTE: This function is only needed to support the APOD viewer GUI
    resize_ratio = min(max_size[0] / image_size[0], max_size[1] / image_size[1])
    new_size = (int(image_size[0] * resize_ratio), int(image_size[1] * resize_ratio))
    return new_size

if __name__ == '__main__':
    main()