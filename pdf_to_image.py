import os
from pdf2image import convert_from_path

os.chdir(r'C:\Users\haeyu\Desktop')
pdf_list = list(filter(lambda x: x.endswith('.pdf'),os.listdir()))
for i,file in enumerate(pdf_list):
    print(f'{i} => {file}')
print()
file_name = pdf_list[int(input(">> 몇 번째 파일인가요 ? : "))]
results_folder = f'{file_name.replace(".pdf","")}_images'

print(f"Result save in {results_folder}")
try:
    os.mkdir(results_folder)
    print(f"Make {results_folder} in {os.getcwd()}")
except FileExistsError:
    print(f"Already Exists {results_folder} in {os.getcwd()}")
    pass

print("Convert pdf to image ...")
images = convert_from_path(file_name, poppler_path = r'C:\Users\haeyu\PycharmProjects\PdfToImage\poppler-20.12.1\Library\bin')

print("Save ...")
for i,page in enumerate(images):
    page.save(f'./{results_folder}/{file_name}_{i+1}.jpg','JPEG')

print("DONE !")
