# Document-Remover

A program that goes through all the pdf documents in a directory and its subdirectories in a top-down fashion , gives you a basic overview of the document, and then asks you if you want to keep the document or not. It will delete the document if you press y, and do nothing if you press n. It can be helpful if you
have a lot of pdf documents on your laptop you no longer need, and want to get rid of. 

Runnong it from your downloads directory might be helpful. You can also manually put in names of directories to traverse in the script if you want want to run the script from a certain directory.

The code uses the NLTK and PyPDF2 library, so you will need to have those installed. You can find more information about those here:

For NLTK:
https://www.nltk.org/

for PyPDF2:
http://mstamy2.github.io/PyPDF2/
