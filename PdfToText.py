import os
import PyPDF2

splits = 15
pdf_file = input("Enter file location: ")

with open(pdf_file, 'rb') as pdf:

    pdf_reader = PyPDF2.PdfFileReader(pdf)
    num_pages = pdf_reader.getNumPages()
    extracted_text = ""

    for i in range(num_pages):
        page = pdf_reader.getPage(i)
        text = page.extractText()
        extracted_text += text


        if len(extracted_text) % 2000 == 0:
            extracted_text += '\n' * splits


    output_file_path = os.path.splitext(pdf_file)[0] + '_output.txt'

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        lines = extracted_text.split('\n')

        for i, line in enumerate(lines):
            output_file.write(line)
            if (i + 1) % 50 == 0:
                output_file.write('\n' * splits)
            else:
                output_file.write('\n')

    print(f"Output file saved at: {output_file_path}")
