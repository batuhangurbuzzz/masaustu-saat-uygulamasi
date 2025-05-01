from tkinter import Label, Tk
import time
appWindow = Tk()

appWindow.title("Dijital Saat")
appWindow.geometry("350x200")
appWindow.resizable(0,0)

appWindow.configure(bg="black")

textFont = ("Boulder",36,'bold')
background = 'black'
foreground = "white"
borderWidth = 20

# Saat etiketi
label = Label(appWindow,font=textFont, bg=background, fg=foreground)

label.grid(row=0,column=1,padx=borderWidth,pady=borderWidth)


# Tarih Etiketi

dateLabel = Label(appWindow, font=textFont,bg=background, fg=foreground)
dateLabel.grid(row=1,column=1,padx=borderWidth,pady=borderWidth)


def digitalClock():
    timeLive = time.strftime("%H:%M:%S")
    label.config(text=timeLive)
    dateInfo = time.strftime("%d %B %Y")
    dateLabel.config(text=dateInfo)
    label.after(200,digitalClock),
    
    
digitalClock()

appWindow.mainloop()