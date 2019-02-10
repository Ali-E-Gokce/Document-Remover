import PyPDF2
from nltk import sent_tokenize


def _pdf_to_sentences(pdf_name): #converts the pdf document into sentences
    # creating a pdf file object
    pdfFileObj = open(str(pdf_name), 'rb')



    # creating a pdf reader object
    pdf_reader = PyPDF2.PdfFileReader(pdfFileObj)
    if pdf_reader.isEncrypted: #decrypts pdf if it can
        try:
            pdf_reader.decrypt('')
        #somtimes it can't, these are the two most common errors I received
        except (NotImplementedError, PyPDF2.utils.PdfReadError) as e:
            return
    # creating a page object
    pageObj = pdf_reader.getPage(0)

    #extracting text from page, returns string
    try:
        text = pageObj.extractText()
    except TypeError:
        return


    #Removes new lines on mac OS, Windows and UNIX. NLTK does not do that on it's own.
    text = text.replace('\n', ' ').replace('\r', '')

    #dividing the text into sentences. Returns list.

    sent_text=sent_tokenize(text)
    #creates list of sentences

    #the following block will print the first four sentences of a text as a summary. If there are fewer than four sentences in the document, it will just print all sentences.
    if len(sent_text)>4:
        for sentence in range(0,4):
            print(sent_text[sentence])
    else:
        for sentence in range(0,len(sent_text)):
            print(sent_text[sentence])
