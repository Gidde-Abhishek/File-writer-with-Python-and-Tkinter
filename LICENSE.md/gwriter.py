import tkinter as tk 
'''Imported tkinter as tk, so that we can use tk instead of the whole word, super general'''
from tkinter import *
'''Imported all the modules from tkinter'''
from tkinter import filedialog
'''filedialog needs to be imported seperately'''

root = tk.Tk()
root.title("File Writer")
'''Declared a new window with a custom title'''

g_font = ('Raleway',30)
'''Optional font inclusionm looks good, and you need to have this font installed
you can replace with your favourite font, if you plan to remove this line of code, delete it's usage in the contentInput label'''

''' First read the code that calls these functions then read these, for better understanding'''
def writetofile():
	''' function that writes to the file, called on button click'''
	
	filename=filedialog.askopenfilename()
	'''Gives the user a browse dialog box to select file location and write it to filename variable'''

	FileToWrite=open(filename,"a")
	'''Open the filename with append option writes new content without earsing the old one in the file'''

	content=x.get()
	'''x is the variable assigned to input box, everything that is typed in the input box, will be set into x,
	get() will retreive the value from x and assign it to the content variable'''

	if (len(str(content))==0):
		'''if the user has not typed anything, i.e the input box is empty'''


		content="No Input Provided"
		'''self explanatory'''

		labelFail=tk.Label(root,text=content).pack()
		'''label will be shown when the content is empty'''
		
		return
		'''When you write return, the compiler exits the function, won't run other lines in the function'''
	
	'''If the user has written something, i.e if statement above fails'''
	

	FileToWrite.write(str(content))
	'''the content is finally written to the the file, FileToWrite is our file handler'''
	
	labelSuccess = tk.Label(root,text=content+" was written succesfully to "+filename)
	'''Sucess label which displays content written and also location'''

	labelSuccess.pack()
	'''pack() function displays i.e packs the label or for that matter any widget to the window,
	without pack() the widget won't be displayed'''

'''Main section'''
x = StringVar()
'''x is declared as a variable which will be containing a string, StringVar() belongs to tkinter library'''

LabelContent = Label(root,text="Enter the content to be written, you will be asked for the file later").pack()
'''The label above input box, see how we used pack() here'''

contentInput=Entry(root,textvariable=x,font=g_font).pack()
'''The actual input box, here the font is used, works without the font as well'''

writebtn= Button(root,text="Write to File", command=writetofile).pack()
'''The button that runs our write function'''


root.mainloop()
'''mainloop() function is used when your application is ready to run, this is an infinite loop used to run the application,
keeps on running infinitely and waits for something to happen, unless and until you close the window'''