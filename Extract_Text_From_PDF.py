# ****************************** Read and Extract Text from PDF ******************************************8

# This is the practice problem on how to read and extract text in pdf
""" With the help of this module we will play with pdfs and much more """
# Note: This project is under development and we inviting all to contribute in this group.

# Importing Libraries
import PyPDF2

# Extracting Text
def Text(PDF):
    # printing number of pages in pdf file
    print(PDF.numPages)
    # creating a page object
    for i in range(PDF.getNumPages()):
        pageObj = PDF.getPage(i)
        print(i+1)
        # extracting text from page
        print(pageObj.extractText())


if __name__ == '__main__':
    # Function that we have available from our side
    Dict_PDF = {'1': 'PDF Information', '2': 'Content Page Number', '3': 'PDF Fields', '4': 'Text Fields in PDF',
                '5': 'Text Destination', '6': 'Total PDF Pages', '7': 'PDF Outline', '8': 'Get Page Number',
                '9': 'PDF Layout', '10': 'PDF Mode', '11': 'PDF Decodeness', '12': "PDF Text Extraction"}
    while True:
        try:
            pdf_file = input("Enter the path of PDF file: ")
            pdf_File = open(pdf_file, 'rb')
            PDF = PyPDF2.PdfFileReader(pdf_File)
        except Exception as E:
            print("\nplease give the correct PDF path...!")
        else:
            try:
                for i, item in enumerate(Dict_PDF.values()):
                    print(i + 1, item)
                choice = input("\nEnter the option number (Ex. 1, 2, 3...) : ")
                if choice in Dict_PDF.keys():
                    if choice == '1':  # the document information of this PDF file
                        print(f"\nPDF information: {PDF.getDocumentInfo()}")
                    elif choice == '2':
                        try:  # Retrieve page number of a given Destination object
                            destination = input("Enter the Destination(content): ")
                            print(f"\nPDF Destination Page Number: {PDF.getDestinationPageNumber(destination)}")
                        except Exception:
                            print("\nData not found...!")
                        else:
                            print(f"Page found successfully...!")
                    elif choice == '3':  # Extracts field data if this PDF contains interactive form fields. The tree and retval parameters are for recursive use.
                        print(f"\nFields in PDF are: {PDF.getFields()}")
                    elif choice == '4':  # Retrieves form fields from the document with textual data (inputs, dropdowns)
                        print(f'\nText fields in PDF are: {PDF.getFormTextFields()}')
                    elif choice == '5':  # Retrieves the named destinations present in the document.
                        print(f"\nName Destination Present in PDF: {PDF.getNamedDestinations()}")
                    elif choice == '6':  # Calculates the number of pages in this PDF file.
                        print(f"\nTotal Pages in PDF: {PDF.getNumPages()}")
                    elif choice == '7':  # Retrieves the document outline present in the document.
                        print(f"\nThe Outlines in the PDF: {PDF.getOutlines()}")
                    elif choice == '8':  # Retrieves a page by number from this PDF file.
                        pageNo = int(
                            input("Enter the page number: "))  # The page number to retrieve (pages begin at zero)
                        print(f"\n{pageNoD:\Sachin folder\Sachin\programming\programming pdfs\Python pdfs\Beginning-Python.pdf} page from PDF: {PDF.getPage(pageNo + 1)}")
                    elif choice == '9':  # Page layout currently being used
                        print(f"\nPage layout of PDF: {PDF.getPageLayout()}")
                    elif choice == '10':  # Page mode currently being used.
                        print(f"\nPage Mode of PDF: {PDF.getPageMode()}")
                    elif choice == '11':  # Read-only boolean property showing whether this PDF file is encrypted
                        print(f"\nPDF Decodeness: {PDF.isEncrypted()}")
                    elif choice == '12':
                        print(f"\nText in the PDF: ")
                        Text(PDF)
                    else:
                        print("\nSomething went wrong...!")
                else:
                    print("Command not in Dict_PDF...!")
            except Exception as E:
                print(f"\nError Occur: {E}")
        finally:
            pdf_File.close()
            print(" \n** Thanks for your valuable time ** \n")
        continue
# 2, 3, 4, 5, 9,
# Not working functions are:
# Here I have mentioned that what are the commands that are not working. I am unable to develop it fully so, this is where you can help me.
