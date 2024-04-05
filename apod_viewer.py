"""
    GUI for NASA APOD program.

 .   *   ..  . *  *       
*  * @()Ooc()*   o  .
    (Q@*0CG*O()  ___
   |\_________/|/ _ \
   |  |  |  |  | / | |
   |  |  |  |  | | | |
   |  |  |  |  | | | |
   |  |  |  |  | | | |
   |  |  |  |  | | | |
   |  |  |  |  | \_| |
   |  |  |  |  |\___/
   |\_|__|__|_/|
    \_________/
    Final project complete, let the beers flow!
 """
from tkinter import Tk, ttk, messagebox, PhotoImage
import inspect
import os
import apod_desktop
import image_lib
import ctypes
from datetime import date

# Determine the path and parent directory of this script
script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
script_dir = os.path.dirname(script_path)

# Initialize the image cache
apod_desktop.init_apod_cache(script_dir)

# TODO: Create the GUI
root = Tk()
root.geometry('600x400')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.title("Astronomy Picture of the Day Viewer")

# Setting Nasa Icon
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('ApodViewer')
root.iconbitmap(os.path.join(script_dir, "NASA_Logo.ico"))


# Frames
top_frm = ttk.Frame(root)
top_frm.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky='N')

middle_frm = ttk.Frame(root)
middle_frm.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="SEW")


bott_left_frm = ttk.LabelFrame(root, text="View Cached Image")
bott_left_frm.grid(row=2, column=0, padx=5, pady=5, sticky="NSEW")
bott_left_frm.columnconfigure(0, weight=0)
bott_left_frm.columnconfigure(1, weight=1)
bott_left_frm.columnconfigure(2, weight=0)
bott_left_frm.rowconfigure(0, weight=1)

api_input = ttk.LabelFrame(root, text="Get More Images")
api_input.grid(row=2, column=1, padx=5, pady=5, sticky="NSEW")
api_input.columnconfigure(0, weight=0)
api_input.columnconfigure(1,weight=1)
api_input.columnconfigure(1, weight=0)
api_input.rowconfigure(0, weight=1)

#Populating all the frames with Widgets

#Top frame
img_path = os.path.join(script_dir, "Nasa_logo.png")
img = PhotoImage(file=img_path)
img_labl = ttk.Label(top_frm, image=img)
img_labl.grid(padx=0, pady=0, sticky="NSEW")

#Middle frame
mid_labl = ttk.Label(middle_frm)
mid_labl.grid(padx=20, pady=0, sticky="NSEW")


#Bottom Frames
selectimg_lbl = ttk.Label(bott_left_frm, text="Select Image")
selectimg_lbl.grid(row=0, column=0, padx=5, pady=5, sticky="NSEw")

img_cmbox = ttk.Combobox(bott_left_frm, state="readonly", values=apod_desktop.get_all_apod_titles())
img_cmbox.grid(row=0, column=1, padx=5, pady=5, sticky="NSEW")
img_cmbox.set("Select an Image")
img_cmbox.bind("<<ComboboxSelected>>")

selectimg_but = ttk.Button(bott_left_frm, text="Set as Desktop")
selectimg_but.grid(row=0, column=2, padx=5, pady=5, sticky="E")


root.mainloop()