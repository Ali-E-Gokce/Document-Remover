import os

from _pdf_to_sentences import _pdf_to_sentences

from _pdf_info import _pdf_info


#looks through directories for pdf files
for root, dirs, files in os.walk("./"):
   for name in files:

       if name.endswith(".pdf"):
#some pdf documents can not be opened, and give different exceptions
#You can't know what kind of erros they might throw.
           try:
               #prints psdf info of doc
               print(_pdf_info(os.path.join(root, name)))

           except:
               pass
           try:
               #prints first 4 sentences of pdf
               _pdf_to_sentences(os.path.join(root, name))
           except:
               pass
           #asks if doc should be removed, user presses y or n
           ans=input("Do you wish to remove this document? y/n. \n") #
           #removes doc if answer is y
           if ans=='y':
              os.remove(name) #removes doc
