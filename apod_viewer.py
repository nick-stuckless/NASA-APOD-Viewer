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
from tkinter import Tk, ttk, messagebox
import inspect
import os
import apod_desktop

# Determine the path and parent directory of this script
#script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
#script_dir = os.path.dirname(script_path)

# Initialize the image cache
#apod_desktop.init_apod_cache(script_dir)

# TODO: Create the GUI
root = Tk()
root.geometry('600x400')
root.title("Astronomy Picture of the Day Viewer")
# Frames
cache_input_frame = ttk.Frame(root)
cache_input_frame.grid(row=0, column=0, sticky="S")


api_input = ttk.LabelFrame(root, text="Get More Images")
api_input.grid(row=0, column=1, sticky="S")
api_but = ttk.Button(api_input, text="Download")
api_but.grid(row=1, column=0)
root.mainloop()