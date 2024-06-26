'''
Library for interacting with NASA's Astronomy Picture of the Day API.
      ,'``.._   ,'``.
     :,--._:)\,:,._,.:       All Glory to
     :`--,''   :`...';\      the HYPNO TOAD!
      `,'       `---'  `.
      /                 :
     /                   \
   ,'                     :\.___,-.
  `...,---'``````-..._    |:       \
    (                 )   ;:    )   \  _,-.
     `.              (   //          `'    \
      :               `.//  )      )     , ;
    ,-|`.            _,'/       )    ) ,' ,'
   (  :`.`-..____..=:.-':     .     _,' ,'
    `,'\ ``--....-)='    `._,  \  ,') _ '``._
 _.-/ _ `.       (_)      /     )' ; / \ \`-.'
`--(   `-:`.     `' ___..'  _,-'   |/   `.)
    `-. `.`.``-----``--,  .'
      |/`.\`'        ,','); 
          `         (/  (/
'''
import requests


def main():
    # TODO: Add code to test the functions in this module
   
    return

def get_apod_info(apod_date):
    """Gets information from the NASA API for the Astronomy 
    Picture of the Day (APOD) from a specified date.
    Args:
        apod_date (date): APOD date (Can also be a string formatted as YYYY-MM-DD)

    Returns:
        dict: Dictionary of APOD info, if successful. None if unsuccessful
    """
    #API KEY: ws7sgipbUHySWua9H2HscjRAUnkJ4nRoSJonrt3n
    nasa_url = r'https://api.nasa.gov/planetary/apod'

    parameters = {
        "api_key": "ws7sgipbUHySWua9H2HscjRAUnkJ4nRoSJonrt3n",
        "date": f"{apod_date}"
    }

    resp = requests.get(nasa_url, parameters)
    
    if resp.status_code == requests.codes.ok:
        print("success")
        apod_info_dict = resp.json()
        return apod_info_dict
    else:
        print("Failure: ")
        print(f"{resp.status_code} {resp.reason} ({resp.text})")
        return

def get_apod_image_url(apod_info_dict):
    """Gets the URL of the APOD image from the dictionary of APOD information.

    If the APOD is an image, gets the URL of the high definition image.
    If the APOD is a video, gets the URL of the video thumbnail.

    Args:
        apod_info_dict (dict): Dictionary of APOD info from API

    Returns:
        str: APOD image URL
    """
    
    if apod_info_dict["media_type"] == 'image':
        url = apod_info_dict["hdurl"]
    
    elif apod_info_dict["media_type"] == 'video':
        url = apod_info_dict["thumbnail_url"]
    
    return url


    
if __name__ == '__main__':
    main()