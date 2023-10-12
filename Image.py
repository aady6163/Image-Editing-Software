import tkinter as tk
import cv2 
from PIL import Image , ImageTk , ImageEnhance , ImageFilter
from tkinter import filedialog , ttk
import numpy as np


root = tk.Tk()
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()

root.title('Image Editing Website')
root.geometry(f"{screen_width}x{screen_height}")
root.configure(bg="#66CDAA")

# logic behind project 
 

def displayImage(displayImage):
    dispimage = ImageTk.PhotoImage(displayImage)
    panel.configure(image=dispimage)
    panel.image = dispimage

def reset_callback():
    global image
    displayImage(image)


def import_command():
    global image
    imgname = filedialog.askopenfilename(title="Change Image")

    image = Image.open(imgname)
    image = image.resize((700, 550) , Image.BICUBIC)
    displayImage(image)

def nonebutton_function():
    displayImage(image)

def brightness_callback(brightness_position):
    brightness_position = float(brightness_position)
    global outputImage
    enhancer = ImageEnhance.Brightness(image)
    outputImage = enhancer.enhance(brightness_position)
    displayImage(outputImage)

def contrast_callback(contrast_position):
    contrast_position = float(contrast_position)
    global outputImage
    enhancer = ImageEnhance.Contrast(image)
    outputImage = enhancer.enhance(contrast_position)
    displayImage(outputImage)

def sharpness_callback(sharpness_position):
    sharpness_position = float(sharpness_position)
    global outputImage
    enhancer = ImageEnhance.Sharpness(image)
    outputImage = enhancer.enhance(sharpness_position)
    displayImage(outputImage)

def color_callback(color_position):
    color_position = float(color_position)
    global outputImage
    enhancer = ImageEnhance.Color(image)
    outputImage = enhancer.enhance(color_position)
    displayImage(outputImage)

def yellowbutton_function():
    opencvimage = cv2.cvtColor(np.array(image) , cv2.COLOR_RGB2BGR)
    opencvimage[:,:,0] = 20
    outputImage = Image.fromarray(cv2.cvtColor(opencvimage , cv2.COLOR_BGR2RGB))
    displayImage(outputImage)

def purplebutton_function():
    opencvimage = cv2.cvtColor(np.array(image) , cv2.COLOR_RGB2BGR)
    opencvimage[:,:,1] = 0
    outputImage = Image.fromarray(cv2.cvtColor(opencvimage , cv2.COLOR_BGR2RGB))
    displayImage(outputImage)

def aquabutton_function():
    opencvimage = cv2.cvtColor(np.array(image) , cv2.COLOR_RGB2BGR)
    opencvimage[:,:,2] = 0
    outputImage = Image.fromarray(cv2.cvtColor(opencvimage , cv2.COLOR_BGR2RGB))
    displayImage(outputImage)

def orangebutton_function():
    opencvimage = cv2.cvtColor(np.array(image) , cv2.COLOR_RGB2BGR)
    opencvimage[:,:,2] = 200
    outputImage = Image.fromarray(cv2.cvtColor(opencvimage , cv2.COLOR_BGR2RGB))
    displayImage(outputImage)

def pinkbutton_function():
    opencvimage = cv2.cvtColor(np.array(image) , cv2.COLOR_RGB2BGR)
    opencvimage[:,:,1] = 100
    outputImage = Image.fromarray(cv2.cvtColor(opencvimage , cv2.COLOR_BGR2RGB))
    displayImage(outputImage)

def rotate_callback():
    global image
    image= image.rotate(90)
    displayImage(image)


def flip_callback():
    imgage = image.transpose((Image.FLIP_LEFT_RIGHT))
    displayImage(imgage)

def emboss_callback():
    global image
    image = image.filter(ImageFilter.EMBOSS)
    displayImage(image)

def smooth_callback():
    global image
    image = image.filter(ImageFilter.SMOOTH)
    displayImage(image)

def edgeEnhance_callback():
    global image
    image =image.filter(ImageFilter.FIND_EDGES)
    displayImage(image)

def blurr_callback():
    global image
    image = image.filter(ImageFilter.BLUR)
    displayImage(image)

def crop_callback():
    global image
    image = image.crop(( 1, 2 , 300 , 300))
    displayImage(image)

def resize_callback():
    global image
    image = image.resize((700, 550) )
    displayImage(image)
    


def save_image():
    savefile = filedialog.asksaveasfile(defaultextension=".png")
    outputImage.save(savefile)

   
    


# Top frame
title_frame = tk.Frame(root , height=100, width= screen_width , bg= "white")
title_frame.place(x=0 , y=0)

right_frame = tk.Frame(root , width=700 , height=600, bg="#66CDAA")
right_frame.place(x=780 , y=160)

# default image
img = Image.open("white_background.png")
img = img.resize((700, 550))

# image display 
panel = tk.Label(root )
panel.place( x=20 , y=180)
displayImage(img)


image_logo = tk.PhotoImage(file="logo_image.png"  )
tk.Label(title_frame , image=image_logo , bg="white" , padx=25).place(x=10 , y=5)

tk.Label(title_frame, text="Edit Your Images Here" , font=("ariel 20 bold" ) , bg="white" , fg="black").place(x=100 , y=30)


import_button = tk.Button(title_frame , text="Import" , bg="#000080" , foreground="white" , font=("ariel 12 bold" ) , pady=3 , padx=25 , command=import_command)
import_button.place(x=1200 , y=35 )

save_button = tk.Button(title_frame , text="Save" , bg="#000080" , foreground="white" , font=("ariel 12 bold" ) , pady=3 , padx=25, command=save_image)
save_button.place( x=1330 , y=35 )

style = ttk.Style()
style.configure("TScale" , background="#66CDAA" )

# brightness slider
brightness_label=tk.Label(right_frame , text="Brightness" , font= ("poppin 13 bold" ) , bg="#66CDAA")
brightness_label.place(y=30 , x=30)
brightness_slide = ttk.Scale(right_frame , from_=0 , to=2, orient='horizontal', length=200, style="TScale" , command=brightness_callback )
brightness_slide.set(1)
brightness_slide.place(y=30 , x=130)

# contrast slider
contrast_label=tk.Label(right_frame , text="Contrast" , font= ("poppin 13 bold" ) , bg="#66CDAA")
contrast_label.place(y=30 , x=370)
contrast_slide = ttk.Scale(right_frame , from_=0 , to=2 , orient='horizontal', length=200, style="TScale" , command=contrast_callback)
contrast_slide.set(1)
contrast_slide.place(y=30 , x=450)

# sharpness slider
sharpness_label=tk.Label(right_frame , text="Sharpness" , font= ("poppin 13 bold" ) , bg="#66CDAA")
sharpness_label.place(y=70 , x=30)
sharpness_slide = ttk.Scale(right_frame , from_=0 , to=2 , orient='horizontal', length=200, style="TScale", command=sharpness_callback )
sharpness_slide.set(1)
sharpness_slide.place(y=70 , x=130)

# colors slider
colors_label=tk.Label(right_frame , text="Colours" , font= ("poppin 13 bold" ) , bg="#66CDAA")
colors_label.place(y=70 , x=370)
colors_slide = ttk.Scale(right_frame , from_=0 , to=2 , orient='horizontal', length=200, style="TScale", command=color_callback)
colors_slide.set(1)
colors_slide.place(y=70 , x=450)

tk.Label(right_frame, text="____________________________________________________________________________________________________________________________" , bg="#66CDAA").place(y=105 , x=30)

# Radiobuttons

radiobutton_style = ttk.Style()
radiobutton_style.configure("TRadiobutton" , background="#66CDAA", font="poppin 13 bold" )
yellow_button = ttk.Radiobutton(right_frame, text="Yellow Filter" , value=1  , style="TRadiobutton" , command=yellowbutton_function)
yellow_button.place(x=80 , y=145)

purple_button = ttk.Radiobutton(right_frame, text="Purple Filter" , value=2  , style="TRadiobutton" , command=purplebutton_function)
purple_button.place(x=260 , y=145)

aqua_button = ttk.Radiobutton(right_frame, text="Aqua Filter" , value=3  , style="TRadiobutton" , command=aquabutton_function)
aqua_button.place(x=440 , y=145)

orange_button = ttk.Radiobutton(right_frame, text="Orange Filter" , value=4  , style="TRadiobutton" , command=orangebutton_function)
orange_button.place(x=80 , y=195)

black_white_button = ttk.Radiobutton(right_frame, text="Pink Filter" , value=5  , style="TRadiobutton" , command=pinkbutton_function)
black_white_button.place(x=260 , y=195)

none_button = ttk.Radiobutton(right_frame, text="No Filter" , value=6  , style="TRadiobutton", command=nonebutton_function)
none_button.place(x=440 , y=195)

tk.Label(right_frame, text="____________________________________________________________________________________________________________________________" , bg="#66CDAA").place(y=235 , x=30)

# buttons


rotate_buttton = tk.Button(right_frame, text="Rotate" , width=12 , background="#E3CF57" , font="poppin 13 bold" , bd=0 , command=rotate_callback)
rotate_buttton.place( x=30 , y=285)

flip_buttton = tk.Button(right_frame, text="Flip" , width=12 , background="#EE1289" , font="poppin 13 bold" , bd=0 , command=flip_callback)
flip_buttton.place( x=190 , y=285)

emboss_buttton = tk.Button(right_frame, text="Emboss" , width=12 , background="#FF4040" , font="poppin 13 bold" , bd=0 , command=emboss_callback)
emboss_buttton.place( x=360 , y=285)

edgenhance_buttton = tk.Button(right_frame, text="EdgeEnhance" , width=12 , background="#FF6103" , font="poppin 13 bold" , bd=0 , command=edgeEnhance_callback)
edgenhance_buttton.place( x=520 , y=285)

blur_buttton = tk.Button(right_frame, text="Blur" , width=12 , background="#76EE00" , font="poppin 13 bold" , bd=0 , command=blurr_callback)
blur_buttton.place( x=30, y=345)

crop_buttton = tk.Button(right_frame, text="Crop" , width=12 , background="#FF7256" , font="poppin 13 bold" , bd=0 , command=crop_callback)
crop_buttton.place( x=190, y=345)

rotate_buttton = tk.Button(right_frame, text="Resize" , width=12 , background="#DC143C" , font="poppin 13 bold" , bd=0 , command=resize_callback)
rotate_buttton.place( x=360, y=345)

smooth_buttton = tk.Button(right_frame, text="Smooth" , width=12 , background="#B23AEE" , font="poppin 13 bold" , bd=0 , command=smooth_callback)
smooth_buttton.place( x=520, y=345)

tk.Label(right_frame, text="____________________________________________________________________________________________________________________________" , bg="#66CDAA").place(y=395 , x=30)

root.mainloop()