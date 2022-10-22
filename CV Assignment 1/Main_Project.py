#Loiy Ehsan 1830887
#10/21/2022

from Dependencies import *
from tkinter import *
from tkinter import ttk

default_font=("Helvetica", 14)
root=Tk()
root.title("Assignment 1")
s = ttk.Style()

s.configure('default.TButton', font=default_font)
s.configure('first.TButton', font=default_font,foreground="red")
s.configure('second.TButton', font=default_font,foreground="green")
s.configure('third.TButton', font=default_font,foreground="blue")

greetings=ttk.Label(root, text="Welcome to my first CV Assignment", font=default_font)
geo_op=ttk.Label(root, text="Image Geometry", font=default_font)
vid_capture=ttk.Button(root, text="Capture a Picture",style='default.TButton', command=image_capture)
open_capture=ttk.Button(root, text="Open Your Image",style='default.TButton', command=show_image)
extract_single_color=ttk.Label(root, text="Extracting a single color image", font=default_font)
chunk=ttk.Button(root, text="Chunk of Image", command=chunk,style="default.TButton")
grey=ttk.Button(root, text="Grey-Scale of image", style="default.TButton",command=grey_scale)
Blur=ttk.Button(root, text="Blur Image", style="default.TButton",command=blur_image)
Derivative=ttk.Button(root, text="Find Edges", style="default.TButton",command=find_edge)
Edge=ttk.Button(root, text="Edge Magnitude", style="default.TButton",command=edge_mag)
phase=ttk.Button(root, text="Image Phase", style="default.TButton",command=phase_image)
histo=ttk.Button(root, text="Histogram of Image", style="default.TButton",command=histogram)
mask=ttk.Button(root, text="Mask Image", style="default.TButton",command=masking_image)
rotate=ttk.Button(root, text="Rotate 60", style="default.TButton",command=image_rotate)
f_h=ttk.Button(root, text="flip Horizontally", style="default.TButton",command=image_h_flip)
f_v=ttk.Button(root, text="flip Vertically", style="default.TButton",command=image_v_flip)
red_B=ttk.Button(root, text="Red", style="first.TButton",command=display_red)
green_B=ttk.Button(root, text="Green", style="second.TButton",command=display_green)
blue_B=ttk.Button(root, text="Blue", style="third.TButton",command=display_blue)

greetings.pack()
vid_capture.pack()
open_capture.pack()
chunk.pack()
grey.pack()
Blur.pack()
Derivative.pack()
Edge.pack()
phase.pack()
histo.pack()
mask.pack()
geo_op.pack()
rotate.pack()
f_h.pack()
f_v.pack()
extract_single_color.pack()
red_B.pack()
green_B.pack()
blue_B.pack()
root.mainloop()