from . import setup
from . import webcam

setup.start_input()
label_html = 'Capturing...'
img_data = ''
count = 0 
while True:
    js_reply = webcam.take_photo(label_html, img_data)
    if not js_reply:
        break

    image = webcam.js_reply_to_image(js_reply)
    drawing_array = webcam.get_drawing_array(image) 
    drawing_bytes = webcam.drawing_array_to_bytes(drawing_array)
    img_data = drawing_bytes
