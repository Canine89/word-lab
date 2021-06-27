from docx2python import docx2python
import os

docx = docx2python("test3.docx")
saveFolderName = "./test3"

try:
    os.mkdir(saveFolderName)
except:
    pass


for name, imageData in docx.images.items():
    imageData.
    with open(os.path.join(saveFolderName, name), "wb") as fp:
        fp.write(imageData)