# This works in linux if you want to use this in window then simple change fontfamily Nakula to Arial.
import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

mainApplication = tk.Tk()
mainApplication.geometry('1920x1080')
mainApplication.title('Tr Text Editor')


########################################## Main Menu ###################################

mainMenu = tk.Menu()

# File Icons
newIcon = tk.PhotoImage(file = 'Images/new.png')
openIcon = tk.PhotoImage(file = 'Images/open.png')
saveIcon = tk.PhotoImage(file = 'Images/save.png')
saveAsIcon = tk.PhotoImage(file = 'Images/saveAs.png')
exitIcon = tk.PhotoImage(file = 'Images/exit.png')

file = tk.Menu(mainApplication, tearoff = False)

# Edit Icons

copyIcon = tk.PhotoImage(file = 'Images/copy.png')
pasteIcon = tk.PhotoImage(file = 'Images/paste.png')
cutIcon = tk.PhotoImage(file = 'Images/cut.png')
clearAllIcon = tk.PhotoImage(file = 'Images/clearAll.png')
selectAllIcon = tk.PhotoImage(file = 'Images/selectAll.png')
findIcon = tk.PhotoImage(file = 'Images/find.png')

edit = tk.Menu(mainApplication, tearoff = False)

# View Icons

toolBarIcon = tk.PhotoImage(file = 'Images/toolBar.png')
statusBarIcon = tk.PhotoImage(file = 'Images/statusBar.png')

view = tk.Menu(mainApplication, tearoff = False)

# Color Theme   

lightDefaultIcon = tk.PhotoImage(file = 'Images/lightDefault.png')
lightPlusIcon = tk.PhotoImage(file = 'Images/lightPlus.png')
darkIcon = tk.PhotoImage(file = 'Images/dark.png')
redIcon = tk.PhotoImage(file = 'Images/red.png')
monokaiIcon = tk.PhotoImage(file = 'Images/monokai.png')
nightBlueIcon = tk.PhotoImage(file = 'Images/nightBlue.png')

colorTheme = tk.Menu(mainApplication, tearoff = False)

themeChoice = tk.StringVar()
colorIcon = (lightDefaultIcon, lightPlusIcon, darkIcon, redIcon, monokaiIcon, nightBlueIcon)

colorDict = {
	 'Light Default ' : ('#000000', '#ffffff'),
	 'Light Plus' : ('#474747', '#e0e0e0'),
	 'Dark' : ('#c4c4c4', '#2d2d2d'),
	 'Red' : ('#2d2d2d', '#ffe8e8'),
	 'Monokai' : ('#d3b774', '#474747'),
	 'Night Blue' :('#ededed', '#6b9dc2')
	}

# cascade 
mainMenu.add_cascade(label = 'File', menu = file)
mainMenu.add_cascade(label = 'Edit', menu = edit)
mainMenu.add_cascade(label = 'View', menu = view)
mainMenu.add_cascade(label = 'Color Theme', menu = colorTheme)

######################################### End Main Menu ###############################




############################################ ToolBar #################################

# Font Box
toolBar = ttk.Label(mainApplication)
toolBar.pack(side = tk.TOP, fill = tk.X)

# Font Box.
fontTuple = tk.font.families()
fontFamily = tk.StringVar()
fontBox = ttk.Combobox(toolBar, width = 20, textvariable = fontFamily ,state = 'readonly')
fontBox['values'] = fontTuple
fontBox.current(fontTuple.index('Nakula'))
fontBox.grid(row = 0, column = 0, padx = 5)

# Size Box
sizeVar = tk.IntVar()
fontSize = ttk.Combobox(toolBar, width = 5, textvariable = sizeVar, state = 'readonly')
fontSize['values'] = tuple(range(8,81))
fontSize.current(4)
fontSize.grid(row = 0, column = 1, padx = 5 )

# Bold Button
boldIcon = tk.PhotoImage(file ='Images/bold.png')
boldBtn = ttk.Button(toolBar, image = boldIcon)
boldBtn.grid(row = 0, column = 2, padx = 5)

# Italic Button
italicIcon = tk.PhotoImage(file ='Images/italic.png')
italicBtn = ttk.Button(toolBar, image = italicIcon)
italicBtn.grid(row = 0, column = 3, padx = 5)

# Underline Button
underlineIcon = tk.PhotoImage(file ='Images/underline.png')
underlineBtn = ttk.Button(toolBar, image = underlineIcon)
underlineBtn.grid(row = 0, column = 4, padx = 5)

# Font Color Button
fontColorIcon = tk.PhotoImage(file ='Images/fontColor.png')
fontColorBtn = ttk.Button(toolBar, image = fontColorIcon)
fontColorBtn.grid(row = 0, column = 5, padx = 5)

# Align left Button
alignLeftIcon = tk.PhotoImage(file ='Images/alignLeft.png')
alignLeftBtn = ttk.Button(toolBar, image = alignLeftIcon)
alignLeftBtn.grid(row = 0, column = 6, padx = 5)

# Align Center Button
alignCenterIcon = tk.PhotoImage(file ='Images/alignCenter.png')
alignCenterBtn = ttk.Button(toolBar, image = alignCenterIcon)
alignCenterBtn.grid(row = 0, column = 7, padx = 5)

# Align Right Button
alignRightIcon = tk.PhotoImage(file ='Images/alignRight.png')
alignRightBtn = ttk.Button(toolBar, image = alignRightIcon)
alignRightBtn.grid(row = 0, column = 8, padx = 5)

############################################# End ToolBar ###########################


################################################ Text Editor ##########################

textEditor = tk.Text(mainApplication)
textEditor.config(wrap = 'word', relief = tk.FLAT, undo = True)

scrollBar = tk.Scrollbar(mainApplication)
textEditor.focus_set()
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
textEditor.pack(fill = tk.BOTH, expand = True)
scrollBar.config(command = textEditor.yview)
textEditor.config(yscrollcommand = scrollBar.set)

# Font Family fonction..
currentFontFamily = 'Nakula'
currentFontSize = 12

def changeFont(event=None):
	global currentFontFamily
	currentFontFamily = fontFamily.get()
	textEditor.configure(font =(currentFontFamily, currentFontSize))
	
def changeFontsize(event=None):
	global currentFontSize
	currentFontSize = sizeVar.get()
	textEditor.configure(font =(currentFontFamily, currentFontSize))
	
fontBox.bind('<<ComboboxSelected>>', changeFont)
fontSize.bind('<<ComboboxSelected>>', changeFontsize)

# bold Button ka function
def changeBold():
	textProperty = tk.font.Font(font = textEditor['font'])
	if textProperty.actual()['weight'] == 'normal':
		textEditor.configure(font =(currentFontFamily, currentFontSize, 'bold'))
	if textProperty.actual()['weight'] == 'bold':
		textEditor.configure(font =(currentFontFamily, currentFontSize, 'normal'))
boldBtn.configure(command = changeBold)

# Italic Button ka function
def changeItalic():
	textProperty = tk.font.Font(font = textEditor['font'])
	if textProperty.actual()['slant'] == 'roman':
		textEditor.configure(font =(currentFontFamily, currentFontSize, 'italic'))
	if textProperty.actual()['slant'] == 'italic':
		textEditor.configure(font =(currentFontFamily, currentFontSize, 'normal'))
italicBtn.configure(command = changeItalic)

# Underline Button ka function
def changeUnderline():
	textProperty = tk.font.Font(font = textEditor['font'])
	if textProperty.actual()['underline'] == 0:
		textEditor.configure(font =(currentFontFamily, currentFontSize, 'underline'))
	if textProperty.actual()['underline'] == 1:
		textEditor.configure(font =(currentFontFamily, currentFontSize, 'normal'))
underlineBtn.configure(command = changeUnderline)

# font Color ka function
def changeFontColor():
	colorVar = tk.colorchooser.askcolor()
	textEditor.configure(fg = colorVar[1])
	
fontColorBtn.configure(command = changeFontColor)

# Align Left ka function...
def alignLeft():
	textContent = textEditor.get(1.0, 'end')
	textEditor.tag_config('left', justify = tk.LEFT)
	textEditor.delete(1.0, tk.END)
	textEditor.insert(tk.INSERT, textContent, 'left')

alignLeftBtn.configure(command = alignLeft)

# Align Center ka function...
def alignCenter():
	textContent = textEditor.get(1.0, 'end')
	textEditor.tag_config('center', justify = tk.CENTER)
	textEditor.delete(1.0, tk.END)
	textEditor.insert(tk.INSERT, textContent, 'center')

alignCenterBtn.configure(command = alignCenter)

# Align Right ka function...
def alignRight():
	textContent = textEditor.get(1.0, 'end')
	textEditor.tag_config('right', justify = tk.RIGHT)
	textEditor.delete(1.0, tk.END)
	textEditor.insert(tk.INSERT, textContent, 'right')

alignRightBtn.configure(command = alignRight)

textEditor.configure(font=('Nakula', 12))

############################################## End Text Editor #########################



############################################## Status Bar #############################

statusBar = ttk.Label(mainApplication, text = 'Status Bar')
statusBar.pack(side =tk.BOTTOM)
		
textChanged = False	
def changed(event=None):
	global textChanged
	if textEditor.edit_modified():
		textChanged = True
		words = len(textEditor.get(1.0, 'end-1c').split())
		charecters = len(textEditor.get(1.0, 'end-1c').replace(' ',''))
		lines = len(textEditor.get(1.0, 'end-1c').split('\n'))
		statusBar.config(text = f'Lines : {lines}, Charecters : {charecters}, Words : {words}')
	textEditor.edit_modified(False)
	
textEditor.bind('<<Modified>>', changed)

########################################## End Status Bar #############################


########################################## Main Menu Functinality #######################

		
url = ''

# new functionality
def newFile(event=None):
    global url 
    url = ''
    textEditor.delete(1.0, tk.END)

# for file commands
file.add_command(label = 'New', image = newIcon, compound = tk.LEFT, accelerator = 'Ctrl+N', command = newFile)

# Open Function
def openFile(event=None):
	global url
	url = filedialog.askopenfilename(initialdir = os.getcwd(), title = 'Choose File', filetypes = (('Text File', '*.txt'),('Python Files', '*.py'), ('All Files', '*.*')))
	try:
		with open(url, 'r') as fr:
			textEditor.delete(1.0, tk.END)
			textEditor.insert(1.0, fr.read())
	except FileNotFoundError:
		return
	except:
		return
	mainApplication.title(os.path.basename(url))
	
file.add_command(label = 'Open', image = openIcon, compound = tk.LEFT, accelerator = 'Ctrl+O', command = openFile)
file.add_separator()

def saveFile(event=None):
	global url
	try:
		if url:
			content = str(textEditor.get(1.0, tk.END))
			with open(url, 'w', encoding = 'utf-8') as fw:
				fw.write(content)
		else:
			url = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt', filetypes = (('Text File', '*.txt'),('Python Files', '*.py'), ('All Files', '*.*')))
			content2 = textEditor.get(1.0, tk.END)
			url.write(content2)
			url.close()
	except:
		return
		
file.add_command(label = 'Save', image = saveIcon, compound = tk.LEFT, accelerator = 'Ctrl+S', command = saveFile)

def saveAs(event=None):
	global url
	try:
		content = textEditor.get(1.0, tk.END)
		url = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt', filetypes = (('Text File', '*.txt'),('Python Files', '*.py'), ('All Files', '*.*')))
		url.write(content)
		url.close()
	except:
		return

file.add_command(label = 'Save As', image = saveAsIcon, compound = tk.LEFT, accelerator = 'Ctrl+Alt+S', command = saveAs)
file.add_separator()


# Exit ka function

def exitFunc(event=None):
	global url, textChanged
	try:
		if textChanged:
			mbox = messagebox.askyesnocancel('Waring', 'Do you want to save the file ?')
			if mbox is True:
				if url:
					content = textEditor.get(1.0, tk.END)
					with open(url, 'w', encoding = 'utf-8') as fw:
						fw.write(content)
						mainApplication.destroy()
				else:
					content2 = str(textEdior.get(1.0, tk.END))
					url = filedialg.asksaveasfile(mode = 'w', defaultextension = '.txt', filetypes = (('Text File', '*.txt'),('Python Files', '*.py'), ('All Files', '*.*')))
					url.write(content2)
					url.close()
					mainApplication.destroy()
			elif mbox is False:
				mainApplication.destroy()
		else:
			mainApplication.destroy()
	except:
		return
		
file.add_command(label = 'Exit', image = exitIcon, compound = tk.LEFT, accelerator = 'Ctrl+Q', command = exitFunc)

# find Function
def findFunction(event=None):
	def find(): 
		word = findInput.get()
		textEditor.tag_remove('match', '1.0', tk.END)
		matches = 0
		if word:
			startPos = '1.0'
			while True:
				startPos = textEditor.search(word, startPos, stopindex = tk.END)
				if not startPos:
					break
				endPos = f'{startPos}+{len(word)}c'
				textEditor.tag_add('match', startPos, endPos)
				matches +=1
				startPos = endPos
				textEditor.tag_config('match', foreground = 'red', background = 'yellow')
		
	def replace():
		word = findInput.get()
		replaceText = replaceInput.get()
		content = textEditor.get(1.0, tk.END)
		newContent = content.replace(word, replaceText)
		textEditor.delete(1.0, tk.END)
		textEditor.insert(1.0, newContent)
		
	findDialogue = tk.Toplevel()
	findDialogue.geometry('500x200+500+200')
	findDialogue.title('Find')
	findDialogue.resizable(0,0)
	
	# Frame
	findFrame = ttk.LabelFrame(findDialogue, text= 'Fine/Replace')
	findFrame.pack(pady = 20)

	# labels
	textFindLabel = ttk.Label(findFrame, text = 'Find : ')
	textFindLabel.grid(row = 0, column = 0, padx = 5, pady = 5)
	textReplaceLabel = ttk.Label(findFrame, text = 'Replace')
	textReplaceLabel.grid(row = 1, column = 0, padx = 5, pady = 5)
	
	#Entry
	findInput = ttk.Entry(findFrame, width = 30)
	findInput.grid(row =0, column = 1, padx = 5, pady = 5)
	replaceInput = ttk.Entry(findFrame, width = 30)
	replaceInput.grid(row =1, column = 1, padx = 5, pady = 5)
	
	#button
	findButton = ttk.Button(findFrame, text = 'Find', command = find)
	findButton.grid(row = 2, column =0, padx =8, pady =4)
	replaceButton = ttk.Button(findFrame, text = 'Replace', command = replace)
	replaceButton.grid(row =2, column =1, padx =8, pady =4)
	
	findDialogue.mainApplication()



# Select All Command 

def selectAll(event=None):
	textEditor.tag_add('sel','1.0','end')
	
# Edit Commands..

edit.add_command(label = 'Copy', image = copyIcon, compound = tk.LEFT, accelerator = 'Ctrl+C', command = lambda: textEditor.event_generate('<Control c>'))
edit.add_command(label = 'Paste', image = pasteIcon, compound = tk.LEFT, accelerator = 'Ctrl+V', command = lambda: textEditor.event_generate('<Control v>'))
edit.add_command(label = 'Cut', image = cutIcon, compound = tk.LEFT, accelerator = 'Ctrl+X', command = lambda: textEditor.event_generate('<Control x>'))
edit.add_separator()
edit.add_command(label = 'Find', image = findIcon, compound = tk.LEFT, accelerator = 'Ctrl+F', command = findFunction)	
edit.add_command(label = 'Select All', image = selectAllIcon, compound = tk.LEFT, accelerator = 'Ctrl+A', command = selectAll)
edit.add_command(label='Clear All', image=clearAllIcon, compound=tk.LEFT, accelerator='Ctrl+Alt+X', command= lambda:text_editor.delete(1.0, tk.END))

# View ka check button
showStatusbar = tk.BooleanVar()
showStatusbar.set(True)
showToolbar = tk.BooleanVar()
showToolbar.set(True)

def hideToolbar():
	global showToolbar
	if showToolbar:
		toolBar.pack_forget()
		showToolbar = False
	else:
		textEditor.pack_forget()
		statusBar.pack_forget()
		toolBar.pack(side = tk.TOP, fill = tk.X)
		textEditor.pack(fill = tk.BOTH, expand = True)
		showToolbar = True
		
def hideStatusbar():
	global showStatusbar
	if showStatusbar:
		statusBar.pack_forget()
		showStatusbar = False
	else:
		statusBar.pack(side = tk.BOTTOM)
		showStatusbar = True


view.add_checkbutton(label = 'Tool Bar', onvalue = True, offvalue = 0, variable = showToolbar, image = toolBarIcon, accelerator = 'Alt+S', compound = tk.LEFT, command=hideToolbar)
view.add_checkbutton(label = 'Status Bar',  onvalue = 1, offvalue = False, variable = showStatusbar, image = statusBarIcon, compound = tk.LEFT, command=hideStatusbar)

# color Themes 	

def changeTheme():
	chosenTheme = themeChoice.get()
	colorTuple = colorDict.get(chosenTheme)
	fgColor, bgColor = colorTuple[0], colorTuple[1]
	textEditor.config(background = bgColor, fg = fgColor)

count = 0
for i in colorDict:
	colorTheme.add_radiobutton(label = i, image = colorIcon[count], variable = themeChoice, compound = tk.LEFT, command = changeTheme)
	count += 1

m = tk.Menu(mainApplication, tearoff = 0) 
m.add_command(label ="Cut", command = lambda: textEditor.event_generate('<Control x>')) 
m.add_command(label ="Copy", command = lambda: textEditor.event_generate('<Control c>')) 
m.add_command(label ="Paste", command = lambda: textEditor.event_generate('<Control v>')) 
m.add_command(label ="Select All", command = selectAll)
m.add_command(label ="Find/Replace", command = findFunction) 
m.add_separator() 
m.add_command(label ="Exit", command = exitFunc) 
  
def doPopup(event): 
    try: 
        m.tk_popup(event.x_root, event.y_root) 
    finally: 
        m.grab_release() 
  

#################################### End Main Menu Functinality ########################

mainApplication.config(menu = mainMenu)	

# Binding function....		
mainApplication.bind('<Control-n>', newFile)
mainApplication.bind('<Control-o>', openFile)
mainApplication.bind('<Control-s>', saveFile)
mainApplication.bind('<Control-Alt-s>', saveAs)
mainApplication.bind('<Control-q>', exitFunc)
mainApplication.bind('<Control-f>', findFunction)
mainApplication.bind('<Control-a>', selectAll)
mainApplication.bind("<Button-3>", doPopup) 

mainApplication.config(menu = mainMenu)	
mainApplication.mainloop()
