import os.path

from pypdf import PdfReader

filepath = r"tmp\Python Testing with Pytest (Brian Okken).pdf"
reader = PdfReader(filepath)

print(reader.pages)
# print(len(reader.pages))

# print(reader.pages[1].extract_text())

print(reader.pages[1])
# assert 'Simple, Rapid, Effective, and Scalable' in reader.pages[1].extract_text()

assert os.path.getsize(filepath) == 3035139