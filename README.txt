README

PSO 

A lucid lightweight GUI application to encrypt a plain text file into a cipher text and convert the corresponding cipher text into the plain text i.e. decrypt the cipher text that employs Genetic Algorithms for cryptography and Particle Swarm Optimization for optimizing the algorithm. It will convert the respective document from your Windows, Mac or Linux Computers directly.

________About the software__________ 

This application is totally written in Python uses Tkinter modules and requires a user to install a latest version of python.

_Pre-requisites_ 

1 - Latest version of Python (One can download from https://www.python.org/downloads/ as per your operating system)
2 - 1Gb RAM (recommended)
3 - Any Operating system for current age (likely Windows10, MacOS X or Linux). 

____Features____ 

1 - Works on Mac, Windows and Linux.(Tested and ran successfully) 
2 - Simplistic GUI and lightweight.
3 - Shows the process output in the console area. 


Files included within this project (PSO):

	folder(__pycache__) -> GUI.cpython-37.pyc	 
	folder(build) -> folder(GUI) -> Analysis-00.toc
					 -> base_library.zip
					 -> EXE-00.toc
					 -> PKG-00.pkg	
					 -> PKG-00.toc
					 -> PYZ-00.pyz
					 -> PYZ-00.toc
					 -> Tree-00.toc
					 -> Tree-01.toc
					 -> warn-GUI.txt
					 -> xref-GUI.html
	folder(dist) -> GUI.exec 
	cipherlist.txt	GUI.spec	GUI.py		ciphertext.txt	decryptext.txt	
	privatekey.txt	plaintext.txt		publickey.txt
	

How to run "GUI":
	Run "GUI.exec" file located at path name "PSO/dist" 
	A GUI window will be opened having 3 label buttons namely , FILE, SECURITY, SHOW.
 
	File: It had two sub-options; File-- It will allow you to open the plain text file 		which is an editable file containing the text user wants to encrypt.
		Exit-- which will allow to quit the application at that instant.	
	Security: It had two sub-options Encrypt-- It enables the encryption process of 		  the plain text file/document and also display the public key.
		  Decrypt-- It enables the decryption process of the converted cipher text 		  file/document and also display the private key. 
	Show: It allows the user to see the decrypted text into the console of the 		      terminal.

NOTE:-
1 - To see the code, click on the GUI.py file.
2 - plaintext.txt file can be edited using Notepad/TextEditor.