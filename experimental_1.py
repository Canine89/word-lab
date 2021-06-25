from docx import Document
from PIL import Image
from os.path import basename

document = Document("./1-4장.docx")

_idx = 0
for shape in document.inline_shapes:
    contentId = shape._inline.graphic.graphicData.pic.blipFill.blip.embed
    contentPart = document.part.related_parts[contentId]
    contentType = contentPart.content_type

    if not contentType.startswith("image"):
        continue

    imgName = basename(contentPart.partname)
    imgData = contentPart._blob
    with open(imgName, "wb") as fp:
        fp.write(imgData)
