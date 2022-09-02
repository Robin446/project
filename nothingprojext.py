from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title("canvas drawing")
root.geometry("1000x1000")

color_lab = Label(root, text="Enter a color : ")
color_lab.place(relx=0.6,rely=0.9,anchor=CENTER)

inp1 = Entry(root)
inp1.insert(0,"black")
inp1.place(relx=0.8,rely=0.9,anchor=CENTER)


canv=Canvas(root,width=990,height=490,bg="white", highlightbackground="lightgray")
canv.pack()

coordinates = [10,50,100,200,300,400,500,600,700,800,900]
startx = Label(root,text="startx")
d1 = ttk.Combobox(root,state="readonly",values=coordinates,width=10)
startx.place(relx=0.1,rely=0.85,anchor=CENTER)
d1.place(relx=0.2,rely=0.85,anchor=CENTER)
starty = Label(root,text="starty")
d2 = ttk.Combobox(root,state="readonly",values=coordinates,width=10)
starty.place(relx=0.3,rely=0.85,anchor=CENTER)
d2.place(relx=0.4,rely=0.85,anchor=CENTER)


endx = Label(root,text="endx")
d3 = ttk.Combobox(root,state="readonly",values=coordinates,width=10)
endx.place(relx=0.5,rely=0.85,anchor=CENTER)
d3.place(relx=0.6,rely=0.85,anchor=CENTER)
endy = Label(root,text="endy")
d4 = ttk.Combobox(root,state="readonly",values=coordinates,width=10)
endy.place(relx=0.7,rely=0.85,anchor=CENTER)
d4.place(relx=0.8,rely=0.85,anchor=CENTER)

img = ImageTk.PhotoImage(Image.open("start_point1.png"))
my_img = canv.create_image(50,50,image=img)

direction = ""
oldx=50
oldy=50
newx=50
newy=50

def draw(direction,oldx,oldy,newx,newy):
    fill_color = inp1.get()


root.bind("<Right>",right_dir)
root.bind("<Left>",left_dir)
root.bind("<Up>",up_dir)
root.bind("<Down>",down_dir)
root.mainloop()