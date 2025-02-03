import PyPDF2

def unlock_pdf(file_path, password):
    """
    Unlock a pdf file which is protected by a password.
    
    Args:
        file_path (str): The path of the pdf file.
        password (str): The password to unlock the pdf.
    """
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        if pdf_reader.isEncrypted:
            pdf_reader.decrypt(password)
        pdf_writer = PyPDF2.PdfFileWriter()
        for page_num in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_num))
        output_file_path = file_path.split('.pdf')[0] + '_unlocked.pdf'
        with open(C:\Users\ndevr\OneDrive\Desktop\A.I\PRACTICAL LAB - 3\PRACTICAL.pdf, 'wb') as pdf_output:
            pdf_writer.write(pdf_output)

if __name__ == '__main__':
    unlock_pdf('path_to_your_locked_pdf.pdf', 'your_password')
    print('PDF unlocked successfully!')