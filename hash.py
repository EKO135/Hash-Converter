from tkinter import *
import tkinter.messagebox as tm
import hashlib

# **** Window ****
root = Tk()
root.geometry("460x750")

# change the window title
root.title('EKO ~ Hash converter')

# give it a nice look'n icon shall ya
#root.iconbitmap(r"path\\to\\.icofile")

# make a frame for the top
topframe = Frame(root, width=400, height=180)
topframe.grid()

# i need to make two different frames so that the length of the hashes will not affect the placment of the widgets 
# make a frame for the hashes
bottomframe = Frame(root, width=400, height=750)
bottomframe.grid()


# **** Stuff In The Window ****

label_1 = Label(topframe, text="EKO's Hash Converter", font=("Courier New", 10, "bold"))
label_1.grid(row=0, column=4)


entry = Entry(topframe)
entry.grid(row=2, column=4) # place the entry


# **** Functions ****

def hash_func(hashtype):
	text = entry.get()
	h = hashlib.new(hashtype)
	h.update(text.encode('utf-8'))
	answer = h.hexdigest()
	
	print("\n------------------------------\n\n[" + hashtype.upper() + "] >> " + answer)
	
	Hash = Label(bottomframe, text="------------------------------\n [" + hashtype.upper() +"]: " + answer)
	Hash.grid(rowspan=36)


###########################
# stuff for keyboard and click events
# i could use lambda in the button plave but im lazy and i want more lines C;

def sha256_func(event):
	hash_func('sha256')


def md5_func(event):
	hash_func('md5')


def sha1_func(event):
	hash_func('sha1')


############################
# decode info

def decodeinfo():
	tm.showinfo("Sorry Buddy, Not Happening", "SHA256 is a hashing function, not an encryption function. "
	"Since SHA256 is not an encryption function (encrytions can be reversed), it cannot be decrypted. ... In that case, " 
	"SHA256 cannot be reversed because it's a one-way function. Reversing it would cause a preimage attack, " 
	"which defeats its design goal.")

def decipher(event):
	decodeinfo()

def program_info():
	tm.showinfo("EKO Hash Info", "this is a security or educational program, the idea is to have a GUI python progam "
	"that can successfully convert text into a selected hash with lots of functionality.")


############################
# other functions

def close(event):
	root.destroy()
	pt = "------------ Program Terminated ------------"
	print("\n" + pt + "\n")


def clear_text():
	entry.delete(0, 'end')

def destory_frame(event):
	bottomframe.destroy()

def new():
	bottomframe.grid_remove()
	bottomframe.grid()

def save():
	print("im working on it... ok")


# create a toplevel menu
menubar = Menu(root)

# create a pulldown menu, and add it to the menu bar
# file menu is now a submenu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", accelerator="Ctrl+N", command=new)
filemenu.add_command(label="Save", accelerator="Ctrl+S", command=save)
# give it a nice ol' line
filemenu.add_separator()

# hashing accessable from the file dropdown menu
filemenu.add_command(label="SHA-256", accelerator="Enter", command=lambda: hash_func('sha256'))
filemenu.add_command(label="MD-5", accelerator="Ctrl-Enter", command=lambda: hash_func('md5'))
filemenu.add_command(label="SHA-1", accelerator="Alt-Enter", command=lambda: hash_func('sha1'))

#name the submenu label "FILE" for convenience
menubar.add_cascade(label="File", menu=filemenu)                                              

# create a edit drop-down menu
# obviously it would have Cut Copy Paste... right?
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: entry.event_generate('<Control-x>'))
editmenu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: entry.event_generate('<Control-c>'))
editmenu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: entry.event_generate('<Control-v>'))
# 
menubar.add_cascade(label="Edit", menu=editmenu)

menubar.add_command(label="decode", accelerator="`", command=decodeinfo)
menubar.add_command(label="Info", accelerator="~", command=program_info)
menubar.add_command(label="Quit", command=root.quit)

# display the menu
root.config(menu=menubar)


# run these if the specified key is pressed
root.bind("<Return>", sha256_func)
root.bind("<Escape>", close)
root.bind("<Delete>", clear_text)
root.bind("<Button-3>", lambda event: tm.showinfo("mate", "why you right click'n bro !!"))
root.bind("<Control-Return>", md5_func)
root.bind("<Alt-Return>", sha1_func)
root.bind("<`>", decipher)
root.bind("<~>", lambda event: program_info)


# submit and run the convert() function
sha256 = Button(topframe, text="SHA-256", command=clear_text)
sha256.bind("<Return>", sha256_func)
sha256.bind("<Button-1>", sha256_func)
sha256.grid(row=3, column=3)


md5 = Button(topframe, text="MD5", command=clear_text)
md5.bind("<Button-1>", md5_func)
md5.grid(row=3, column=4)


sha1 = Button(topframe, text="SHA-1", command=clear_text)
sha1.bind("<Button-1>", sha1_func)
sha1.grid(row=3, column=5)

# keep on a loop until program in closed
root.mainloop()
