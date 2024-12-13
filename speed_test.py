from tkinter import *
from speedtest import Speedtest

def update_text():
    speed_test = Speedtest() #intializing 
    download = speed_test.download() #start the download speed
    upload = speed_test.upload() #start the upload speed
    download_speed = round(download / (10**6), 2)
    upload_speed = round(upload / (10**6), 2)
    down_label.config(text= "Download Speed - " + str(download_speed) + "Mbps") 
    up_label.config(text= "Upload Speed - " + str(upload_speed) + "Mbps") 

root = Tk() #creating a frame
root.title("Internet Speed Tracker") #assiging title
root.geometry('300x300') #resizing the frame
button = Button(root, text="Get Speed", width=30, command=update_text) #creating a button
button.pack() #adding a button to the frame
down_label = Label(root, text="") #creating a label
down_label.pack() #adding a label to frame
up_label = Label(root, text="")
up_label.pack()
root.mainloop() #runnig the frame