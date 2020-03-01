import docx
import docx2txt
from tkinter import *
from tkinter import filedialog
#docu=docx.Document('Krishna DACA aneurysm 2.docx')
#docu = docx2txt.process("Krishna DACA aneurysm 2.docx")
          
#------------Main Function---------#
root =Tk()
root.title("Document File Searcher")

#--------Frames------#
f=Frame(root,height=200,width=300)
f.pack_propagate(0)
f.pack() 

#-----Search Function-------#
def filesearch():
            root.fileName=filedialog.askopenfilename( filetypes =(("Document Files","*.docx"),("All files","*.*") ) )
            docu = docx2txt.process(root.fileName)
            T=Text(root,height=60,width=60)
            T.pack()
            T.mark_set(INSERT,'5.0')
            T.insert(END,docu)
            return T

#-----Delete Function-------#        
def delete_text(filesearch):
    
    T=Text(root,height=60,width=60)
    T=filesearch()
    T.delete('1.0',END)
    return T

def todelete(delete_text,filesearch):
    return delete_text(filesearch) 

#--------Buttons--------#
button1=Button(root,text="Search File",font="Arial 10 bold italic",command=filesearch,bg="light blue",fg="red",height=5,width=10)
button1.pack(side=LEFT)


button2=Button(f,text="Quit",font="Arial 10 bold italic",command=f.quit,bg="PeachPuff",fg="red",height=5,width=10)
button2.pack(side=LEFT)

button3=Button(root,text="Erase",font="Arial 10 bold italic",bg="Pink",fg="Black",height=5,width=10,command= todelete )
button3.pack(side=LEFT)

#----------Quit Function----------#
def quit():
    root.destroy()

#------------Menus----------------#
menu=Menu(root)
root.config(menu=menu)
submenu1=Menu(menu)
submenu2=Menu(menu)
menu.add_cascade(label="File",menu=submenu1)
#submenu1.add_command(label="Open",command=Search(root))
#submenu.add_command(label="Save",command=Search(root))
#submenu.add_command(label="Save As",command=Search(root))
submenu1.add_command(label="Exit",command=quit)
menu.add_cascade(label="Edit",menu=submenu2)
#submenu2.add_command(label="Cut",command=lambda: root.event_generate("<<Cut>>"))
#submenu2.add_command(label="Copy",command=lambda: root.event_generate("<<Copy>>"))
#submenu2.add_command(label="Select All",command=Search(root))

root.mainloop()



