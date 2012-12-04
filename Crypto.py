#!/usr/bin/python
"""
Crypto - Substitution Cipher
Copyright 2012 Lars Schweighauser

This work is licensed under the GPLv3
A version should have been included with Crypto (LICENSE.txt)
If you cannot find it, you can read the full license at:
http://opensource.org/licenses/gpl-3.0.html

---

Huge thanks to K900 (GitHub)/K900_ (Reddit) for solving the Python version check.
(Now everything fits into one nice little script.)
And for telling me that the hashbang needs to be in the first line.
And for being awesome in general.

The default key is: 481282871733
No other number will work in default mode
"""

Version = "1.6.2"
Crypto_Status = "Stable"

#Python_2_7_Status = "Stable"
#Python_3_0_Status = "Stable"
#Python_3_3_Status = "Stable"

from decimal import *
import sys
import codecs

if sys.version_info[0] == 1:
    print("The 90s called they want their Python 1 back.")
    sys.exit(1)

elif sys.version_info[0] == 2 and sys.version_info[1] >= 7:
    from Tkinter import *
    from tkMessageBox import askquestion
    from tkSimpleDialog import askstring
    import tkFileDialog

elif sys.version_info[0] == 3:
    from tkinter import *
    from tkinter.messagebox import askquestion
    from tkinter.simpledialog import askstring
    import tkinter.filedialog as tkFileDialog

else:
    print("Crypto does not support Python " + sys.version[0:5:1] + ".\n")
    sys.exit(1)

getcontext().prec = 100


class Encrypt(object):

    def __init__(self, root):
        self.root = root

    def encode(self, string):
        result = []
        for char in string:
            str_ord = ord(char)

            if 247 <= str_ord <= 256:
                str_chr = str_ord - 215 - 1

            elif str_ord >= 33:
                str_chr = str_ord + 9 + 1 - 1

            else:
                str_chr = str_ord

            result.append(chr(str_chr))
        return ''.join(result)

    def encode_file(self, file):
        encode_result = []
        file_read = codecs.open(file, 'r', encoding="utf-8")
        lines = file_read.readlines()

        for l in lines:
            encode_result.append(self.encode(l))
        file_read.close()

        file_write = codecs.open(file, 'w', encoding="utf-8")
        file_write.writelines(''.join(encode_result))
        Start.GUI.write(''.join(encode_result) + "\n")

    def decode(self, key_guess, line):
        decode_result = []
        real_key = (int(key_guess) / 53475874637)

        for char in line:
            str_ord = ord(char)

            if 33 <= str_ord <= 42:
                str_chr = str_ord + int(real_key) + 206

            elif str_ord >= 43:
                str_chr = str_ord - int(real_key)

            else:
                str_chr = str_ord

            decode_result.append(chr(str_chr))
        return ''.join(decode_result)

    def decode_file(self, file, guess_numb):
        result = []

        key_guess = Start.GUI.get_string("Guess", "Give me a key to try:")
        if key_guess == "":
            Start.GUI.write("You didn't enter anything.")

        elif key_guess is not None:

            guess_numb -= 1

            try:

                key_guess = int(key_guess)

                if Decimal(key_guess) / Decimal(str(53475874637)) == 9:

                    file_read = codecs.open(file, 'r', encoding="utf-8")
                    lines = file_read.readlines()

                    for item in lines:
                        result.append(self.decode(key_guess, item))
                    file_read.close()

                    file_write = codecs.open(file, 'w', encoding="utf-8")
                    file_write.writelines(''.join(result))
                    Start.GUI.write(''.join(result) + "\n")
                    return

                if guess_numb < 1:
                    Start.GUI.write("You have no more guesses.\n")

                    file_read = codecs.open(file, 'r', encoding="utf-8")
                    lines = file_read.readlines()
                    file_read.close()

                    lines[:] = []
                    file_write = codecs.open(file, 'w', encoding="utf-8")
                    file_write.writelines(lines)
                    Start.GUI.quit()

                elif guess_numb == 1:
                    Start.GUI.write("You have " + str(guess_numb)
                                    + " guess left.\n")
                    self.decode_file(file, guess_numb)

                elif guess_numb > 1:
                    Start.GUI.write("You have " + str(guess_numb)
                                    + " guesses left.\n")
                    self.decode_file(file, guess_numb)

            except ValueError:
                Start.GUI.write("Oops!  That was not an intereger.\n")
                if guess_numb < 1:

                    Start.GUI.write("You have no more guesses.\n")

                    file_read = codecs.open(file, 'r', encoding="utf-8")
                    lines = file_read.readlines()
                    file_read.close()

                    lines[:] = []
                    file_write = codecs.open(file, 'w', encoding="utf-8")
                    file_write.writelines(lines)
                    Start.GUI.quit()

                elif guess_numb == 1:
                    Start.GUI.write("You have " + str(guess_numb)
                                    + " guess left.\n")
                    self.decode_file(file, guess_numb)

                elif guess_numb > 1:
                    Start.GUI.write("You have " + str(guess_numb)
                                    + " guesses left.\n")
                    self.decode_file(file, guess_numb)
        return

    def decode_new_key(self, line, big_key, user_guess):
        decode_result = []
        real_key = (int(big_key) / int(user_guess))

        py3_subtract = 0
        if sys.version[0] == "3":
            py3_subtract = 1
        for char in line:
            str_ord = ord(char)

            if 33 <= str_ord <= 42:
                str_chr = str_ord + int(real_key) + 206

            elif str_ord >= 43:
                str_chr = str_ord - int(real_key) - py3_subtract

            else:
                str_chr = str_ord

            decode_result.append(chr(str_chr))
        return ''.join(decode_result)

    def decode_file_new_key(self, file, guess_numb, lines_dependant):

        guess_result = ""
        big_key = lines_dependant[8]
        key_guess = Start.GUI.get_string("Guess", "Give me a key to try: ")

        if key_guess is not None:

            for item in key_guess:
                ord_ = ord(item)
                guess_result += str(ord_)

            if Decimal(big_key) / Decimal(guess_result) == 9:
                file_read = codecs.open(file, 'r', encoding="utf-8")
                lines = file_read.readlines()

                new_result = []
                for item in lines:
                    new_result.append(self.decode_new_key(item, big_key,
                                                          guess_result))

                file_read.close()
                file_write = codecs.open(file, 'w', encoding="utf-8")
                file_write.writelines(''.join(new_result))
                Start.GUI.write(''.join(new_result) + "\n")
                return

            if guess_numb < 1:
                Start.GUI.write("You have no more guesses.\n")

                file_read = codecs.open(file, 'r', encoding="utf-8")
                lines = file_read.readlines()
                file_read.close()

                lines[:] = []
                file_write = codecs.open(file, 'w', encoding="utf-8")
                file_write.writelines(lines)
                Start.GUI.quit()
                return

            elif guess_numb == 1:
                Start.GUI.write("You have " + str(guess_numb)
                                + " guess left.\n")
                guess_numb -= 1
                self.decode_file_new_key(file, guess_numb, lines_dependant)

            else:
                Start.GUI.write("You have " + str(guess_numb)
                                + " guesses left.\n")
                guess_numb -= 1
                self.decode_file_new_key(file, guess_numb, lines_dependant)

        return

    def create_key(self, file):

        user_input = Start.GUI.get_string("Custom Key", "Enter a desired key:"
                                          + "\n(alpha-numeric supported since"
                                          + " beta 0.7.2)\n")
        if user_input is not None:

            write_string = ("Your new key is: " + user_input
                            + "\nDon't lose it.\n")
            Start.GUI.write(write_string)

            depend = codecs.open(file, 'r', encoding="utf-8")
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

            depend = codecs.open(file, 'w', encoding="utf-8")
            depend.writelines(lines_depend)

            depend.close()

            Start.GUI.refresh_time(1500)
        return

    def create_key_check(self, file):

        depend = codecs.open(file, 'r', encoding="utf-8")
        lines_depend = depend.readlines()

        if lines_depend[3] != "\n":
            guess_result = ""
            big_key = lines_depend[8]
            key_guess = Start.GUI.get_string("Guess", "Please enter the "
                                             + "current user key first. ")

            if key_guess is not None:

                for item in key_guess:
                    ord_ = ord(item)
                    guess_result += str(ord_)

                if Decimal(big_key) / Decimal(guess_result) == 9:
                    self.create_key(file)
                else:
                    Start.GUI.write("Sorry, "
                                    + "that is not the current user key.\n")
        else:
            self.create_key(file)

    def switch_to_user_key_mode(self, file):

        depend = codecs.open(file, 'r', encoding="utf-8")
        lines_depend = depend.readlines()
        lines_depend[0] = "user_key" + "\n"

        depend = codecs.open(file, 'w', encoding="utf-8")
        depend.writelines(lines_depend)

        depend.close()

        Start.GUI.refresh()

    def default_key(self, file):

        depend = codecs.open(file, 'r', encoding="utf-8")
        lines_depend = depend.readlines()
        lines_depend[0] = "default_key" + "\n"
        depend = codecs.open(file, 'w', encoding="utf-8")
        depend.writelines(lines_depend)

        depend.close()

        Start.GUI.refresh()
        return


class Crypto(Frame):

    def init_ui(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        depend_file = "Depend.txt"
        dependant = codecs.open(depend_file, 'r', encoding="utf-8")
        self.lines_dependant = dependant.readlines()

        title_string = "Crypto Version " + Version
        self.parent.title(title_string)
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        Encode_button = Button(self, text="Encode",
                               command=self.file_dialogue_encode)
        Encode_button.pack()

        if self.lines_dependant[0] != "user_key\n":

            Decode_button = Button(self, text="Decode",
                                   command=self.file_dialogue_decode)
            Decode_button.pack()

            Switch_mode_button = Button(self, text="Set Custom Key",
                                        command=lambda:
                                        self.create_and_quit(depend_file))
            Switch_mode_button.pack()

        else:

            Decode_button = Button(self, text="Decode",
                                   command=lambda:
                                   self.file_dialogue_decode_user_key
                                   (self.lines_dependant))
            Decode_button.pack()

            Switch_mode_button = Button(self, text="Set Default Key",
                                        command=lambda:
                                        self.default_and_quit(depend_file))
            Switch_mode_button.pack()

        self.output = Text(self)
        self.output.pack()
        self.pack()

    def file_dialogue_encode(self):
        dlg = tkFileDialog.Open(self)
        file = dlg.show()
        if file != "":
            Start.Encode_Object.encode_file(file)

    def file_dialogue_decode(self):
        dlg = tkFileDialog.Open(self)
        file = dlg.show()
        if file != "":
            Start.Encode_Object.decode_file(file, 4)

    def file_dialogue_decode_user_key(self, lines_dependant):
        dlg = tkFileDialog.Open(self)
        file = dlg.show()
        if file != "":
            Start.Encode_Object.decode_file_new_key(file, 3, lines_dependant)

    def create_and_quit(self, depend_file):
        if self.lines_dependant[3] != "\n":
            Overwrite_key_Option = askquestion("User Key Found!",
                                               "There is already a user key,"
                                               + " would you like to overwrite"
                                               + " it?")

            if Overwrite_key_Option == "yes":
                Start.Encode_Object.create_key_check(depend_file)

            elif Overwrite_key_Option == "no":
                Start.Encode_Object.switch_to_user_key_mode(depend_file)

        else:
            Start.Encode_Object.create_key_check(depend_file)

    def default_and_quit(self, depend_file):
        Start.Encode_Object.default_key(depend_file)

    def write(self, txt):
        self.output.insert(END, str(txt))

    def get_string(self, win_title, win_question):
        string = askstring(win_title, win_question)
        return string

    def refresh(self):
        self.pack_forget()
        self.init_ui(self.parent)

    def refresh_time(self, time_to_sleep):
        sys.stdout.flush()
        self.after(time_to_sleep, self.refresh)


class Main(object):

    def __main__(self):

        self.root = Tk()
        self.Encode_Object = Encrypt(self.root)
        self.GUI = Crypto()
        self.GUI.init_ui(self.root)
        self.root.geometry("300x250+300+300")
        self.root.mainloop()

#def begin():
if __name__ == "__main__":
    Start = Main()
    Start.__main__()
