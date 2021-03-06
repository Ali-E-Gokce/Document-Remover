import PyPDF2

def _pdf_info(pdf_name): #extracts  information about a pdf document. The author, title, and subject.

    with open(pdf_name, 'rb') as pdf_object:
        pdf_reader=PyPDF2.PdfFileReader(pdf_object)
        if pdf_reader.isEncrypted: #decrypts file if it can
            try:
                pdf_reader.decrypt('')
            #these are the most common errors I received
            except (NotImplementedError, PyPDF2.utils.PdfReadError,) as e:
                return

        info=pdf_reader.getDocumentInfo()
        subject=info.subject
        title=info.title
        author=info.author
        #If there is no info, the the getDocumentInfo class will return None. Clearly, documents have a title, subject and author, hence they are not neon.


        if author==None: author= "Unspecified"
        if title==None: title="Unspecified"
        if subject==None: subject="Unspecified"


        print("Author is: "+author,"\n"+"Title is: "+title,"\n"+"subject is"+subject)
