import os

from _pdf_to_sentences import _pdf_to_sentences

from _pdf_info import _pdf_info


#looks through directories for pdf files
#add topdown=False as a variable to traverse bottom up
# "/" is the root directiory You can replcae it with another starting directory
#/Users/username might be a good place to clean
for root, dirs, files in os.walk("/Users/alierengokcelioglu"):

   for name in files:
       location = root + name

       if name.endswith(".pdf"):
           location = os.path.join(root, name)
           #some pdf documents can not be opened, and give different exceptions
           #You can't know what kind of erros they might throw.
           print(location)
           try:
               #prints psdf info of doc
               print(_pdf_info(location))

           except:
               print("couldn't get pdf info")

           try:
               #prints first 4 sentences of pdf
               _pdf_to_sentences(location)
           except:
               print("couldn't pare pdf into sentences")
           #asks if doc should be removed, user presses y or n
           ans=input("Do you wish to remove this document? y/n. \n") #
           #removes doc if answer is y
           if ans=='y':
              os.remove(location)
