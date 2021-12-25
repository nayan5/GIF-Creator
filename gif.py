# Make Gif using video file 
# pip install moviepy


"""MoviePy is a Python module for video editing, which can be used for basic operations (like cuts, concatenations, title insertions), video compositing (a.k.a. non-linear editing), video processing, or to create advanced effects. It can read and write the most common video formats, including GIF."""

from moviepy.editor import VideoFileClip
from tkinter.filedialog import *                    #File dialogs help you open, save files or directories.

video = askopenfilename()                           # when called create a modal, native look-and-feel dialog, wait for the user’s selection, then return the selected value(s) or None to the caller.


clip = VideoFileClip(video)                         # loading video gfg
clip.write_gif("mygif.gif",fps = 10)                #frame-rate = 10sec

# A GIF file is created of the video file that user provides
