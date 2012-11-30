Crypto - Substitution Cipher
Copyright 2012 Lars Schweighauser
This work is licensed under the GPLv3
A version should have been included with Crypto (LICENSE.txt)
If you cannot find it, you can read the full license at:
http://opensource.org/licenses/gpl-3.0.html

1. What is Crypto?

Crypto is a simple substition cipher that can be used to encrypt files. 
It should be noted this program is not intended to keep files secure, it 
is more of a concept than anything. It is important that you know not to 
use this program to attempt to disguise sentsitive data.



2. How is Crypto used?

Crypto is just a script, so it does not need to be installed. To 
run it use your terminal's python commmand or right click on and 
select open with Python Launcher. Crypto supports Python 2.7, 3.0 and 3.3
intuitively. (Thanks K900)

Once you have opened the program simply select encode and pick a 
file. 
Crypto will print the results of encoding that file to the screen 
so that you can be sure it worked.

Decoding is a bit more complex as it requires a key. 
By default the key is: 481282871733
However you can change it at anytime by pressing Create New Key
(After creating a key you can switch back to the default key by pressing 
Default Key)

Crypto only gives you 4 guesses to enter the right key, if you run 
out of guesses Crypto will erase the contents of the file you are 
trying to decode, so it is vitally important to only use Crypto on 
backups. 
SERIOUSLY ONLY BACKUPS UNLESS YOU KNOW WHAT YOU ARE DOING!

After succesfully decoding a file Crypto will print the contents of that
file to the screen that way you can read the decoded message without
launching another program.

Crypto always encodes files the same, so it doesn't matter which key
you use to decode a file. This means you can send an encoded file to 
a friend and they will be able to decode it will no worries.



3. Notes:

If a custom key already exists Crypto will ask if you would like to create a 
new key. (If you say no, it will simply switch to custom key mode with the 
current user key.) You will have to enter the old key before ceating a new 
one.

