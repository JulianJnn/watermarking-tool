from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageDraw, ImageFont
from PIL.ImageTk import PhotoImage

# Get coordinates from the mouse click,add the specified watermarked text on the picture at the mouse click coordinates.
# Possibility to change the text, fond, size and opacity of the watermark
# Saves the picture in png format in the "images" folder
def getxy(event):
    watermark_x = int(event.x)
    watermark_y = int(event.y)
    draw = ImageDraw.Draw(imageWatermark)
    text = "YourText"
    font = ImageFont.truetype('HelveticaNeue.ttc', 36)
    draw.text((watermark_x, watermark_y), text,fill=(255,255,255,80), font=font)
    my_img = Image.alpha_composite(im, imageWatermark)
    my_img.show()
    real_filename = filename.split("/")
    final_filename = real_filename[-1].split(".")[0]
    my_img.save(f"images/water_{final_filename}.png")

# Launch the file selector and open it in a new window, execute "getxy" func when mouse is clicked
def upload_img():
    global filename
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    global canvas2, im, imageWatermark
    im = Image.open(filename).convert('RGBA')
    imageWatermark = Image.new('RGBA', im.size, (255, 255, 255, 0))
    width, height = im.size
    window2 = Toplevel()
    window2.title(filename.split("/")[-1])
    canvas2 = Canvas(window2, width=width,height=height)
    uploaded_img = PhotoImage(Image.open(filename))
    canvas2.create_image(0, 0, anchor="nw", image=uploaded_img)
    canvas2.grid(column=0, row=0)
    canvas2.bind('<Button-1>', getxy)
    window2.mainloop()

# Create the interface window
window = Tk()
window.title("Watermarker by JJ")
window.config(padx=50, pady=50, bg="#f7f5dd")
canvas = Canvas(window,width=500, height=500)
background_img = PhotoImage(Image.open("hamster.jpeg"))
canvas.create_image(0, 0, anchor = "nw",image=background_img)
canvas.grid(column= 0, row=0)
label_msg = canvas.create_text((250, 50), text="Watermarking Tool", font="MSGothic 50 bold", fill="#652828")
howto_msg = canvas.create_text((250, 130), text="1. Click on 'Upload' and select a picture.\n"
                                                "2. Click where you'd like to put the watermark on the picture.\n"
                                                "3. Close the picture windows (pics are saved in the 'images' folder).",justify="center", font="HelveticaNeue 12 bold", fill="#E5CAB7")


# Creation of Upload button to select the picture to put watermark on
upload_button = Button(window,padx=10,pady=10,bg="#652828",text="Upload", font="Helvetica",command=upload_img)
upload_button.place(x=240,y=370)

window.mainloop()