from tkinter import *

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
   
def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)
    
# winfo_x means top left corner of x axis in window  
# winfo_y means top left corner of y axis in window
    
window = Tk()
window.geometry("500x300")

label1 = Label(bg="red",width=10,height=5) #red box
label1.place(x=2,y=3)

label2 = Label(bg="blue",width=10,height=5) #blue box
label2.place(x=200,y=100)

label1.bind("<Button-1>",drag_start) #press the mouse
label1.bind("<B1-Motion>",drag_motion) #holding mouse

label2.bind("<Button-1>",drag_start) #press the box
label2.bind("<B1-Motion>",drag_motion) #holding mouse

window.mainloop()