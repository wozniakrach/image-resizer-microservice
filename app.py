from flask import Flask, request, render_template
from flask_cors import CORS
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template('imgresizer-home.html')


@app.route("/resize", methods=['GET', 'POST'])
def resizeImg():
    print("Request Received")

    # parse request arguments
    img = request.json.get('img')
    width = request.json.get('width')
    height = request.json.get('height')
    bytes = BytesIO(base64.b64decode(img))
    workingImage = Image.open(bytes)

    # error: invalid params
    if (width is None) and (height is None):
        return "Error. Invalid Request."
    if img is None:
        return "Error. Invalid Request."

    # resize according to base base width
    if (width is not None) and (height is None):
        width = int(width)
        w_ratio = (width / float(workingImage.size[0]))
        h_calc = int((float(workingImage.size[1]) * float(w_ratio)))
        workingImage = workingImage.resize((width, h_calc), Image.ANTIALIAS)
        workingImage.save('resized_img.jpg')

    # resize according to base height
    elif (width is None) and (height is not None):
        height = int(height)
        h_ratio = (height / float(workingImage.size[1]))
        w_calc = int((float(workingImage.size[0]) * float(h_ratio)))
        workingImage = workingImage.resize((w_calc, height), Image.ANTIALIAS)
        workingImage.save('resized_img.jpg')

    # otherwise preserve aspect ratio and make largest possible img with designated width & height
    else:
        workingImage.thumbnail(size=(width, height))
        workingImage.save('resized_img.jpg')

    # send response
    response = {"base64": ""}
    with open("resized_img.jpg", "rb") as file:
        imgstr = base64.b64encode(file.read()).decode('utf-8')
    response['base64'] = imgstr
    return response

if __name__ == "__main__":
    app.run()

