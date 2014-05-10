import xml2svg 
import stitch
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename

class GUI:
	def __init__(self):
		self.input = ""
		self.output = ""
		self.mainwin = Tk()
		open_button = Button(self.mainwin,\
								text="Open",\
								command=lambda : self.open_button()\
								).grid(row=0, column=0,padx=5,pady=5)
		convert_button = Button(self.mainwin,\
								text="Convert",\
								command=lambda : self.convert_button()\
								).grid(row=0, column=1,padx=5,pady=5)
		
		scale_label = Label(self.mainwin, text="Scale Factor").grid(row=1,column=0)
		self.scale_value = StringVar()
		self.scale_value.set("1")
		self.scale_value_label = Label(self.mainwin,textvariable=self.scale_value).grid(row=1,column=2)
		self.scale = Scale(self.mainwin,from_=1,to=50,orient=HORIZONTAL,command=lambda x : self.scale_value.set(x.split('.')[0]))
		self.scale.grid(row=1,column=1,padx=5,pady=5)
		mainloop()

	def open_button(self):
		self.input = askopenfilename()

		if "." in self.input:
			self.output = self.input.split('.')[0] + ".svg"
		else:
			self.output = self.input + ".svg"
		
	def convert_button(self):
		try:
			xml2svg.convert(self.input,self.output,self.scale.get())
			tkinter.messagebox.showinfo("Success!", "Success! \nSaved to "+self.output)
		except:
			tkinter.messagebox.showerror("Failure", "You Fucked Up")
			raise
		
if __name__ == "__main__":
	gui = GUI()
