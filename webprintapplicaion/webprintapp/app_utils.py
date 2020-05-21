#this function decode the base64 encoded data
# def base64_to_img(data): 
from PIL import Image
from io import BytesIO
import base64
data['img'] = '''R0lGODlhDwAPAKECAAAAzMzM/////wAAACwAAAAADwAPAAACIISPeQHsrZ5ModrLlN48CXF8m2iQ3YmmKqVlRtW4MLwWACH+H09wdGltaXplZCBieSBVbGVhZCBTbWFydFNhdmVyIQAAOw==''' 
im = Image.open(BytesIO(base64.b64decode(data)))	
im.save()