from fileinput import filename
from tkinter import *
from urllib.request import ProxyBasicAuthHandler
from pygame import mixer
from tkinter import filedialog
import tkinter.messagebox

window = Tk()

mixer.init()

window.geometry('300x300')
window.title('Python Music Player')

def help_me():
    tkinter.messagebox.showinfo("Help", "How can i help you")

def browse_file():
    global filename
    fileclose = filedialog.askopenfilename()

menubar = Menu(window)
submenu = Menu(menubar, tearoff=0)
window.config(menu=menubar)

menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Open", command=browse_file)
submenu.add_command(label="Exit", command=window.destroy)
submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="About Us", menu=submenu)
submenu.add_command(label1="Help", command=help_me)



textLabel = Label(window, text="This is a Play Station")
textLabel.pack()

def play_music():
    try:
        paused
    except:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text']="Music is Playing"
        except:
            tkinter.messagebox.showerror('File Error' , 'File not Found')
            statusbar['text']="Music is resumed"
        else:
            mixer.music.unpause()
             
def stop_music():
    mixer.music.stop()
    statusbar['text']="Music is stopped"

def set_volume():
    volume=int(value)/100
    mixer.music.set_volume(volume)

def pause_music():
    global pausad
    pausad = True
    mixer.music.pause()
    statusbar['text']="Music is paused"

def rewind_music():
    play_music()
    statusbar['text']="Music is rewinded"

frame = Frame(window)
frame.pack(padx=10, pady=10)


photo = PhotoImage(file='play.png')
playbutton = Button(frame, image=photo, command=play_music)
playbutton.grid(row=0, column=0, padx=10)

stopphoto = PhotoImage(file='stop.png')
stopbutton = Button(frame, image=stopphoto, command=stop_music)
stopbutton.grid(row=0, column=1, padx=10)

pausePhoto = PhotoImage(file='pause.png')
pauseBtn = Button(frame, image=pausePhoto,command=pause_music)
pauseBtn.pack(row=0, column=2, padx=10)

buttonframe = Frame(window)
buttonframe.pack()

rewindPhoto = PhotoImage(file = 'rewind.png')
rewindButton = Button(buttonFrame, image=rewindPhoto, command=rewind_music)
rewindButton.grid(row=0, column=0)

scale = Scale(frame, from_= 0, to=100, orient=HORIZONTAL,command=set_volume)
scale.set(70)
scale.grid(row=0, column=1)

statusbar = Label(window, text="Keep enjoying the music", relief=SUNKED, anchor=W)
statusbar.pack(side=BOTTOM,fill=X)

window.mainloop()
