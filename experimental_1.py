from docx import Document
from PIL import Image
from os.path import basename
import os

document = Document("./test1.docx")
savefilepath = "./test"

try:
    os.mkdir(savefilepath)
except:
    pass

_idx = 0
for shape in document.inline_shapes:
    contentId = shape._inline.graphic.graphicData.pic.blipFill.blip.embed
    contentPart = document.part.related_parts[contentId]
    contentType = contentPart.content_type

    if not contentType.startswith("image"):
        continue

    imgName = basename(contentPart.partname)
    imgData = contentPart._blob
    
    with open(os.path.join(savefilepath, imgName), "wb") as fp:
        fp.write(imgData)
    _idx = _idx + 1
