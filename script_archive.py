from zipfile import ZipFile

with ZipFile("tmp/hello.zip") as zip_file:
    print(zip_file.namelist())
    text = zip_file.read('hello.txt')
    print(text)
    zip_file.extract('hello.txt', path="tmp")

