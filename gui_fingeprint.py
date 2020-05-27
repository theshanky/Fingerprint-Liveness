from tkinter import * 
from tkinter import font
from tkinter.filedialog import askopenfile
from PIL import ImageTk, Image,ImageDraw,ImageFont, ImageFilter
from tkinter import filedialog
from fingtest import test_fingeprint
from analyse_fingeprint import inference
from functools import partial
import numpy
import cv2
import os


# from fingtest import test_fingerprint

root = Tk()
root.title('SPOOF IDENTIFIER PRO')
HEIGHT = 500
WIDTH = 700
img1 =  None
w = Canvas(root,width = WIDTH,height = HEIGHT,bg = 'white') 
w.pack()


def scan_img(img,x):

    if img is None:
        print("Please enter a fingerprint")
        return None
    pred , accu = inference(x)
    print(pred , accu)

    if pred:
        im2 =Image.open(r"d.png")
    else :
        im2 =Image.open(r"e.png")

     #bg  #ironman
    im2 = im2.resize((224, 224), Image.ANTIALIAS) 
    im1 =img
    # import pdb;pdb.set_trace()
    text_img = Image.new('RGBA', (224,224), (0, 0, 0, 0))
    text_img.paste(im1, ((text_img.width - im1.width) // 2, (text_img.height - im1.height) // 2))
    text_img.paste(im2, ((text_img.width - im2.width) // 2, (text_img.height - im2.height) // 2),mask=im2.split()[3])
    text_img.save('text1.png',format="png")
    image_read = Image.open(r"text1.png")
    img2= ImageTk.PhotoImage(image_read)
    panel = Label(frame5, image = img2) 
    panel.image = img2
    panel.place(relx= 0.010,rely= 0.010, relheight = 1, relwidth = 1)
    final_str = 'DECISION : %s \n SPOOFNESS SCORE : %s' % (pred,accu)
    
    label1= Label (frame3, bg = '#ffff66')
    label1['text'] = final_str
    label1.place( relheight = 1, relwidth = 1)


    
def openfilename(): 
  
    # open file dialog box to select image 
    # The dialogue box has a title "Open" 
    filename = filedialog.askopenfilename(title ='open') 
    return filename 

def open_img(): 
    global img1
    global x
    # Select the Imagename  from a folder  
    x = openfilename() 
    print(x)
    # opens the image 
   # global image1 
    img = Image.open(x) 
      
    # resize the image and apply a high-quality down sampling filter 
    img1 = img.resize((224, 224), Image.ANTIALIAS) 
    # if img:
    #     import pdb;pdb.set_trace()
    # PhotoImage class is used to add image to widgets, icons etc
    #try:
    
    #pred , accu = test_fingeprint(img1)
    #print(pred , accu)
   # except:
    # import pdb;pdb.set_trace()
    
    img2= ImageTk.PhotoImage(img1)
     
    #image1 = img2
    # create a label 
    
    panel = Label(frame4, image = img2) 
    # pred , accu = test_fingeprint(img)
    # print(pred , accu)
    # set the image as img  
    panel.image = img2
    panel.place(relx= 0.010,rely= 0.010, relheight = 1, relwidth = 1)

frame1 = Frame(root, bg = '#1a1a1a')
frame1.place(relx= 0.010,rely= 0.15, relheight = 0.84, relwidth = 0.51)
frame2 = Frame(root, bg = '#1a1a1a')
frame2.place(relx= 0.53,rely= 0.15, relheight = 0.84, relwidth = 0.46)
frame3 = Frame(frame2, bg = 'white')
frame3.place(relx= 0.2,rely= 0.8, relheight = 0.1, relwidth = 0.55)
frame4 = Frame(frame1, bg = 'white')
frame4.place(relx= 0.15,rely= 0.15, relheight = 0.58, relwidth = 0.70)
frame5 = Frame(frame2, bg = 'white')
frame5.place(relx= 0.15,rely= 0.15, relheight = 0.58, relwidth = 0.70)
frame6 = Frame(root, bg = 'black')
frame6.place(relx= 0.010,rely= 0.010, relheight = 0.13, relwidth =0.88)
frame7 = Frame(root, bg = 'black')
frame7.place(relx= 0.89,rely= 0.010, relheight = 0.13, relwidth =0.10)

button1 = Button(frame1,text = "BROWSE",fg = 'white',bg = '#ff6600',command = open_img)
button1.place(relx= 0.2,rely= 0.8, relheight = 0.1, relwidth = 0.25)
button2 = Button(frame1,text = "TEST",bg = '#ff6600',fg = 'white',command = lambda:(scan_img(img1,x)))
button2.place(relx= 0.55,rely= 0.8, relheight = 0.1, relwidth = 0.25)

img4 = Image.open(r"f.png")
img4 = img4.resize((70, 70), Image.ANTIALIAS)
img4= ImageTk.PhotoImage(img4)
label3 = Label(frame7, image = img4,bg ='#ff6600') 
label3.image = img4
label3.place( relheight = 1, relwidth = 1)

label2= Label (frame6,bg ='#ff6600', fg = 'white',font =('impact',30),anchor ='nw',justify ='left')
final_str1 = 'SPOOF IDENTIFIER PRO'
label2['text'] = final_str1
label2.place( relheight = 1, relwidth = 1)

root.mainloop() 