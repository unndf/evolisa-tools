import xml2svg 
import stitch
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

class GUI:
	def __init__(self):
		self.input = ""
		self.output = ""
		self.mainwin = Tk()
		notebook = Notebook(self.mainwin)
		notebook.grid(column=0,row=0,sticky=N+S+E+W)
		convert_tab = Frame(self.mainwin)
		stitch_tab = Frame(self.mainwin)

		notebook.add(convert_tab,text="Convert", sticky=N+S+E+W)
		notebook.add(stitch_tab,text="Stitch",sticky=N+S+E+W)

		open_button = Button(convert_tab,\
								text="Open",\
								command=lambda : self.convert_open_button()\
								).grid(row=0, column=0,padx=5,pady=5)
		convert_button = Button(convert_tab,\
								text="Convert",\
								command=lambda : self.convert_button()\
								).grid(row=0, column=1,padx=5,pady=5)

		open_dir_button = Button(stitch_tab,\
								text="Open",\
								command=lambda : self.open_dir_button()\
								).grid(row=0, column=0,padx=5,pady=5)

		xml_stitch_button = Button(stitch_tab,\
								text="Stitch xml",\
								command=lambda : self.save_xml_button()\
								).grid(row=0, column=1,padx=5,pady=5)
	
		
		scale_label = Label(convert_tab, text="Scale Factor").grid(row=1,column=0)
		self.scale_value = StringVar()
		self.scale_value.set("1")
		self.scale_value_label = Label(convert_tab,textvariable=self.scale_value).grid(row=1,column=2)
		self.scale = Scale(convert_tab,from_=1,to=50,orient=HORIZONTAL,command=lambda x : self.scale_value.set(x.split('.')[0]))
		self.scale.grid(row=1,column=1,padx=5,pady=5)
		
		#TODO: de-spagetti-fy
		row_scale = Label(stitch_tab, text="Scale Factor").grid(row=1,column=0)
		self.row_scale_value = StringVar()
		self.row_scale_value.set("1")
		self.row_scale_value_label = Label(stitch_tab,textvariable=self.row_scale_value).grid(row=1,column=2)
		self.row_scale = Scale(stitch_tab,from_=1,to=10,orient=HORIZONTAL,command=lambda x : self.row_scale_value.set(x.split('.')[0]))
		self.row_scale.grid(row=1,column=1,padx=5,pady=5)

		mainloop()

	def convert_open_button(self):
		self.input = askopenfilename()

		if "." in self.input:
			self.output = self.input.split('.')[0] + ".svg"
		else:
			self.output = self.input + ".svg"
		
	def convert_button(self):
		try:
			xml2svg.convert(self.input,self.output,scale=self.scale.get()+1) #TODO: make sure the scale doesn't give '0' as a value...
			tkinter.messagebox.showinfo("Success!", "Success! \nSaved to "+self.output)
		except:
			tkinter.messagebox.showerror("Failure", "You Fucked Up")
			raise	
	def open_dir_button(self):
		self.stitch_dir = askdirectory()

		#TODO:check if all the files in the dir are valid DNA files

	def save_xml_button(self):
		#TODO:implement the scale properly

		width = int(self.row_scale.get())
		if width == 0:
			width = 1
		stitch.stitch(self.stitch_dir,width,"result.xml")
		tkinter.messagebox.showinfo("Success!", "Success! \nSaved to result.xml")

if __name__ == "__main__":
	gui = GUI()
