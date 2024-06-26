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
from tkinter import Tk, ttk, PhotoImage
import tkinter as tk
from PIL import ImageTk, Image
from tkcalendar import DateEntry
import inspect
import os
import apod_desktop
import image_lib
import apod_api
import ctypes
from datetime import date

# Determine the path and parent directory of this script
script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
script_dir = os.path.dirname(script_path)


# Initialize the image cache
apod_desktop.init_apod_cache(script_dir)


# Event handlers
def resize(event):
    global win_wid, win_hei
    if event.widget.winfo_class() == "Toplevel":
        if (win_wid != event.width) and (win_hei != event.height):
            win_wid = event.width
            win_hei = event.height
    return

win_wid = 0
win_hei = 0


def apod_handl(event):
    #getting apod info from database
    global img_path
    apod_select = img_cmbox.current() + 1
    info_select = apod_desktop.get_apod_info(apod_select)
    img_path = info_select['file_path']

    #configuring the apod explanation
    

    global apod_img
    apod_img = Image.open(img_path)
    new_img = image_lib.scale_image(image_size=(apod_img.width, apod_img.height), max_size=(root.winfo_width(), top_frm.winfo_height()))
    re_img = apod_img.resize(new_img)


    global final_img
    final_img = ImageTk.PhotoImage(re_img)
    img_labl.configure(image=final_img)
    mid_labl.configure(text=info_select['explanation'], wraplength=middle_frm.winfo_width(), justify="left")
    selectimg_but.state(['!disabled'])

    return


def desk_bg_set():
    if img_cmbox.current() == -1:
        return

    apod_info = img_cmbox.current() + 1

    apod = apod_desktop.get_apod_info(apod_info)
    img_path = apod['file_path']
    image_lib.set_desktop_background_image(img_path)
    return

def img_download_handl():
    entry_dt = entry_selectdt.get_date()

    apod_desktop.add_apod_to_cache(entry_dt)

    img_cmbox.configure(values=apod_desktop.get_all_apod_titles())
    return



# Create the GUI
root = Tk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.title("Astronomy Picture of the Day Viewer")
root.bind("<Configure>", resize)

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

entry_selectdt = DateEntry(api_input, date_pattern="YYYY-MM-DD", state="readonly", mindate=date.fromisoformat("1996-05-16"), maxdate=date.today())
entry_selectdt.grid(row=0, column=1, padx=5, pady=5)


img_cmbox = ttk.Combobox(bott_left_frm, state="readonly", values=apod_desktop.get_all_apod_titles())
img_cmbox.grid(row=0, column=1, padx=5, pady=5, sticky="NSEW")

img_cmbox.set("Select an Image")
img_cmbox.bind("<<ComboboxSelected>>", apod_handl)

selectimg_but = ttk.Button(bott_left_frm, text="Set as Desktop", state='readonly', command=desk_bg_set)
selectimg_but.grid(row=0, column=2, padx=5, pady=5, sticky="E")
selectimg_but.state(['disabled'])


selectdt_lbl = ttk.Label(api_input, text="Select Date:")
selectdt_lbl.grid(row=0, column=0, padx=5, pady=5)


entry_selectdt = DateEntry(api_input, date_pattern="YYYY-MM-DD", state="readonly", mindate=date.fromisoformat("1996-05-16"), maxdate=date.today())
entry_selectdt.grid(row=0, column=1, padx=5, pady=5)

downloadimg_but = ttk.Button(api_input, text="Download Image", command=img_download_handl)
downloadimg_but.grid(row=0, column=2, padx=5, pady=5)








root.mainloop()