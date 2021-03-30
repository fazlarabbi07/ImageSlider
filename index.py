from tkinter import *
from PIL import ImageTk,Image
#top level window
root=Tk()
root.title("Image Slider")
#root.geometry("300x400")
root.iconbitmap("photos/image.ico")

#Image opening
my_image1=ImageTk.PhotoImage(Image.open("photos/1.PNG"))
my_image2=ImageTk.PhotoImage(Image.open("photos/2.PNG"))
my_image3=ImageTk.PhotoImage(Image.open("photos/3.PNG")) 
my_image4=ImageTk.PhotoImage(Image.open("photos/4.PNG"))
my_image5=ImageTk.PhotoImage(Image.open("photos/5.PNG"))
#Image list
image_list=[my_image1,my_image2,my_image3,my_image4,my_image5]
flag=0
#bd means size of Border 
#relief is the style of widget like SUNKEN
#anchor represent which side the status bar will allocate 
status=Label(root,text="Image "+str(flag+1)+ " out of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)

my_label=Label(image=my_image1)
my_label.grid(row=0,column=0,columnspan=3)


def back():
    global flag
    global my_label
    global button_back
    global status
    my_label.grid_forget()
    flag-=1
    if(flag==0):
        button_back=Button(root,text="..",state=DISABLED)
        button_back.grid(row=1,column=0)

    my_label=Label(image=image_list[flag])
    
    #Every back button is clicked, update the status level 
    status=Label(root,text="Image "+str(flag+1)+ " out of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)
def forward():
    global flag
    global button_forward
    global my_label
    global status
    my_label.grid_forget()
    flag+=1
    if(flag==4):
        button_forward=Button(root,text="..",state=DISABLED)
        button_forward.grid(row=1,column=2)
    #Every Forward button clicked, update the status level 
    status=Label(root,text="Image "+str(flag+1)+ " out of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)


    my_label=Label(image=image_list[flag])
    my_label.grid(row=0,column=0,columnspan=3)
    status.grid(row=2,column=1)
   


 

button_back=Button(root,text="<<",command=back)
button_forward=Button(root,text=">>",command=forward)
button_exit=Button(root,text="Exit Program",command=root.quit)
#button Displaying
button_exit.grid(row=1,column=1,pady=10)
button_back.grid(row=1,column=0)
button_forward.grid(row=1,column=2)
#Sticky is to use for the left to right/(East to Wast) movement of status
status.grid(row=2,column=0,columnspan=3,sticky=W+E)





root.mainloop()
