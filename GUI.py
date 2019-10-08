import tkinter
import urllib.request
from PIL import Image, ImageTk
from io import BytesIO

from main import *

def URL2img(URL):
    response = urllib.request.urlopen(URL)
    data = response.read()

    img = Image.open(BytesIO(data))
    img = img.resize((500,500), Image.ANTIALIAS)

    return ImageTk.PhotoImage(img)

def getImgLabel(image):
    label = tkinter.Label(window,image=image, borderwidth=2,highlightthickness=0,relief='solid')
    label.image = image

    return label

def showImg(label):
    label.pack()

def hideImg(label):
    label.pack_forget()

def callback(e):
   
    url = next(urls,False)
    if not(url):
        return
    img = URL2img(url)

    #update image
    right_label.configure(image=img)
    right_label.image = img

    right_label.place(x=625,y=200)

    right_image = StudentInfo("unknown",url)
    result = verify(left_image,right_image)
    
    if result[0]:
        no_match_label.pack_forget()
        match_label.configure(text='%s%% MATCH' % result[1])
        match_label.pack(expand=1)

    else:
        match_label.pack_forget()
        no_match_label.configure(text='%s%% MATCH' % result[1])
        no_match_label.pack(expand=1)
        
window = tkinter.Tk()

urls = iter(["http://www.trbimg.com/img-581923b8/turbine/la-et-mg-bryan-cranston-donald-trump-canada-20161101",
"http://networthcelebrities.com/wp-content/uploads/2016/01/Sophie-Turner_6.jpg",
"http://digitalminx.com/photos/actresses/k/kunis_mila/MKtiffportraits001.jpg",
"https://d.ibtimes.co.uk/en/full/319654/leonardo-dicaprio.jpg",
"https://static.accessonline.com/uploads/232448.jpg"])


window.geometry("1200x900")
window.title("Face Matcher")

left_URL = "https://www.newdvdreleasedates.com/images/profiles/mila-kunis-01.jpg"
mila_URL = "https://www.newdvdreleasedates.com/images/profiles/mila-kunis-01.jpg"
mila = URL2img(mila_URL)
left_label = getImgLabel(mila)
left_label.place(x=50,y=200)

leo_URL = "https://specials-images.forbesimg.com/imageserve/558c0172e4b0425fd034f8ba/440x0.jpg?fit=scale&background=000000"
leo = URL2img(leo_URL)
right_label = getImgLabel(leo)

# leo = StudentInfo("leo",leo_URL)
left_image = StudentInfo("mila", mila_URL)
# result = verify(mila,leo)
match_label = tkinter.Label(window, bg='green',text='',  borderwidth=2, relief='solid',font="Arial 20", width=10)
no_match_label = tkinter.Label(window, bg='red', text='', borderwidth=2, relief='solid',font="Arial 20", width=10)

window.bind("<Return>", callback)
window.mainloop()