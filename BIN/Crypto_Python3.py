'''
The default key is: 481282871733
No other number will work in default mode
python 3.x.x compatable 
Copyright: Lars Schweighauser, 2012
'''

#!/usr/bin/python

Version = "1.4.5 Py3"
Status = "Stable"


from decimal import *
from tkinter import *
from tkinter.messagebox import askquestion
from tkinter.simpledialog import askstring
import sys, tkinter.filedialog


getcontext().prec = 100


class Encrypt():


	def __init__(self, root):
		self.root = root


	def encode(self, string):
	
		result = ""
		
		for item in string:
			str_ord = ord(item)
		
			if str_ord >= 247 and str_ord <= 256:
				str_chr = str_ord - 215

			elif str_ord >= 32:
				str_chr = str_ord + 9 + 1

			else:
				str_chr = str_ord
			
			result += chr(str_chr)	
		return result


	def Encode_File(self, file):
	
		result = ""
		file_read = open(file, 'r')
		lines = file_read.readlines()

		for item in lines:
			result += self.encode(item)
	
		file_read.close()
	
		file_write = open(file, 'w')
		print_result = result + "\n"
		file_write.writelines(result)
		start.gui.write(print_result)


	def decode(self, key_guess, result):
	
		new_result = ""
		real_key = (int(key_guess) / 53475874637)

		for item in result:
			str_ord = ord(item)
			
			if str_ord >= 32 and str_ord <= 41:
				str_chr = str_ord + int(real_key) + 206
				new_result += chr(str_chr)	
				
			elif str_ord >= 42:
				str_chr = str_ord - int(real_key) - 1
				new_result += chr(str_chr)	
				
			else:
				str_chr = str_ord
				new_result += chr(str_chr)	

		return new_result


	def Decode_File(self, file, guess_numb):
		result = ""
		

		if guess_numb == 0:
			start.gui.write("You have no more guesses.\n")

			file_read = open(file, 'r')
			lines = file_read.readlines()
			file_read.close()

			lines[:] = []
			file_write = open(file, 'w')
			file_write.writelines(lines)
			start.gui.quit()
			return
			
			
		else:
			guess_numb -= 1
		
			try:
				key_guess = int(start.gui.get_string("Guess", "Give me a key to try:"))
				
				if Decimal(key_guess) / Decimal(str(53475874637)) == 9.0:

					file_read = open(file, 'r')
					lines = file_read.readlines()


					for item in lines:
						result += self.decode(key_guess, item)
	
					file_read.close()
	
					file_write = open(file, 'w')
					file_write.writelines(result)
					start.gui.write(result)
					return
		
	
				if guess_numb == 1:
					start.gui.write("You have " + str(guess_numb) + " guess left.\n")
					
					self.Decode_File(file, guess_numb)
	
	
				elif guess_numb > 1:
					start.gui.write("You have " + str(guess_numb) + " guesses left.\n")
					
					self.Decode_File(file, guess_numb)
			
			
			except ValueError:
				start.gui.write("Oops!  That was not an intereger.\n")
			

				if guess_numb == 1:
					start.gui.write("You have " + str(guess_numb) + " guess left.\n")
					
					self.Decode_File(file, guess_numb)
	
	
				elif guess_numb > 1:
					start.gui.write("You have " + str(guess_numb) + " guesses left.\n")
					self.Decode_File(file, guess_numb)
		return
		

	def decode_new_key(self, result, big_key, user_guess):
	
		new_result = ""
		real_key = (int(big_key)/int(user_guess))
	
		for item in result:
			str_ord = ord(item)
			
			if str_ord >= 32 and str_ord <= 41:
				str_chr = str_ord + int(real_key) + 206
				new_result += chr(str_chr)
				
			elif str_ord >= 42:
				str_chr = str_ord - int(real_key) - 1
				new_result += chr(str_chr)	
				
			else:
				str_chr = str_ord
				new_result += chr(str_chr)	

		return new_result


	def decode_file_new_key(self, file, guess_numb, lines_dependant):
	
		guess_result = ""
		big_key = lines_dependant[8]

		key_guess = start.gui.get_string("Guess", "Give me a key to try: ")
		for item in key_guess:
			ord_ = ord(item)
			guess_result += str(ord_)

		if Decimal(big_key) / Decimal(guess_result) == 9:
			file_read = open(file, 'r')
			lines = file_read.readlines()
		
			new_result = ""
			for item in lines:
				new_result += self.decode_new_key(item, big_key, guess_result)
	
			file_read.close()

			file_write = open(file, 'w')
			file_write.writelines(new_result)
			start.gui.write(new_result)
			return

		if guess_numb < 1:
			start.gui.write("You have no more guesses.\n")
		
			file_read = open(file, 'r')
			lines = file_read.readlines()
			file_read.close()
		
			lines[:] = []
			file_write = open(file, 'w')
			file_write.writelines(lines)
			start.gui.quit()
			return
		
		elif guess_numb == 1:
			start.gui.write("You have " + str(guess_numb) + " guess left.\n")
			guess_numb -= 1
			self.decode_file_new_key(file, guess_numb, lines_dependant)
	
		else:
			start.gui.write("You have " + str(guess_numb) + " guesses left.\n")
			guess_numb -= 1
			self.decode_file_new_key(file, guess_numb, lines_dependant)
		
		return

		
	def Create_Key(self, file):

		
		user_input = start.gui.get_string("Custom Key", "Enter a desired key:\n(alpha-numeric supported since beta 0.7.2)\n")		
		write_string = "Your new key is: " + user_input + "\nDon't lose it.\n"
		start.gui.write(write_string)
		depend = open(file, 'r')
		lines_depend = depend.readlines()

		result = ""
	
		for item in user_input:
			ord_ = ord(item)
			result += str(ord_)
		
		new_key = int(result) * 9

		lines_depend[0] = "user_key" + "\n"
		lines_depend[2] = "new key is:" + "\n"
		lines_depend[3] = user_input + "\n"
		lines_depend[5] = "new divisor is:" + "\n"
		lines_depend[6] = str(result) + "\n"
		lines_depend[7] = "big key is:" + "\n"
		lines_depend[8] = str(new_key) + "\n"

		depend = open(file, 'w')
		depend.writelines(lines_depend)

		depend.close()
		
		start.gui.Refresh_time(1500)
		return
		
		
	def Create_Key_Check(self, file):
			
		depend = open(file, 'r')
		lines_depend = depend.readlines()
		
		if lines_depend[3] != "\n":
			guess_result = ""
			big_key = lines_depend[8]
			key_guess = start.gui.get_string("Guess", "Please enter the current user key first. ")
			for item in key_guess:
				ord_ = ord(item)
				guess_result += str(ord_)

			if Decimal(big_key) / Decimal(guess_result) == 9:
				self.Create_Key(file)
			else:
				start.gui.write("Sorry, that is not the current user key.")
		else:
			self.Create_Key(file)
			

	def Switch_to_user_key_mode(self, file):
	
		depend = open(file, 'r')
		lines_depend = depend.readlines()
		lines_depend[0] = "user_key" + "\n"

		depend = open(file, 'w')
		depend.writelines(lines_depend)

		depend.close()
		
		start.gui.Refresh()

			
	def Default_Key(self, file):
	
		depend = open(file, 'r')
		lines_depend = depend.readlines()
		lines_depend[0] = "default_key" + "\n"
		depend = open(file, 'w')
		depend.writelines(lines_depend)
		
		depend.close()

		start.gui.Refresh()
		return
				
				
class Crypto(Frame):


	def initUI(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		
		depend_file = "BIN/Depend.txt"
		dependant = open(depend_file, 'r')
		self.lines_dependant = dependant.readlines()
		
		title_string = "Crypto Version " + Version
		self.parent.title(title_string)
		self.pack(fill=BOTH, expand=1)
        
		menubar = Menu(self.parent)
		self.parent.config(menu=menubar)

		Encode_button = Button(self, text="Encode", command=self.File_Dialogue_Encode)
		Encode_button.pack()


		if self.lines_dependant[0] != "user_key\n":
		
			Decode_button = Button(self, text="Decode", command=self.File_Dialogue_Decode)
			Decode_button.pack()

			Switch_mode_button = Button(self, text="Set Custom Key", command=lambda: self.Create_and_Quit(depend_file))
			Switch_mode_button.pack()


		else:
		
			Decode_button = Button(self, text="Decode", command=lambda: self.File_Dialogue_Decode_User_Key(lines_dependant))
			Decode_button.pack()
			
			Switch_mode_button = Button(self, text="Set Default Key", command=lambda: self.Default_and_Quit(depend_file))
			Switch_mode_button.pack()

			
		self.output = Text(self)
		self.output.pack()
		self.pack()

		
	def File_Dialogue_Encode(self):
		dlg = tkinter.filedialog.Open(self)
		file = dlg.show()
		start.Encode_Object.Encode_File(file)
		
		
	def File_Dialogue_Decode(self):
		dlg = tkinter.filedialog.Open(self)
		file = dlg.show()
		start.Encode_Object.Decode_File(file, 4)
		
		
	def File_Dialogue_Decode_User_Key(self, lines_dependant):
		dlg = tkinter.filedialog.Open(self)
		file = dlg.show()
		start.Encode_Object.decode_file_new_key(file, 3, lines_dependant)


	def Create_and_Quit(self, depend_file):
		if self.lines_dependant[3] != "\n":
			Overwrite_key_Option = askquestion("Question", "There is already a user key, would you like to overwrite it?")
			if Overwrite_key_Option == "yes":
				start.Encode_Object.Create_Key_Check(depend_file)
			
			
			elif Overwrite_key_Option == "no":
				start.Encode_Object.Switch_to_user_key_mode(depend_file)
					
		else:		
			start.Encode_Object.Create_Key_Check(depend_file)



	def Default_and_Quit(self, depend_file):
		start.Encode_Object.Default_Key(depend_file)


	def write(self, txt):
		self.output.insert(END,str(txt))


	def get_string(self, win_title, win_question):
		string = askstring(win_title, win_question)
		return string
	
	
	def Refresh(self):
		self.pack_forget()
		self.initUI(self.parent)
		
		
	def Refresh_time(self, time_to_sleep):
		sys.stdout.flush()
		self.after(time_to_sleep, self.Refresh)
	
class main():


	def __main__(self):

		self.root = Tk()
		self.Encode_Object = Encrypt(self.root)
		self.gui = Crypto()
		self.gui.initUI(self.root)
		self.root.geometry("300x250+300+300")
		self.root.mainloop()  


#def begin(self):
if __name__ == "__main__":
	start = main()
	start.__main__()