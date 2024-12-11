from flask import Flask, render_template, request, send_file
import requests
from bs4 import BeautifulSoup
import os
from io import BytesIO
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_images', methods=['POST'])
def fetch_images():
    url = request.form['url']
    images = []
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        for img_tag in soup.find_all('img'):
            if 'src' in img_tag.attrs:
                src = img_tag['src']
                if not src.startswith(('http://', 'https://')):
                    # Handle relative URLs
                    src = requests.compat.urljoin(url, src)
                try:
                    img_response = requests.get(src)
                    img = Image.open(BytesIO(img_response.content))
                    images.append({
                        'src': src,
                        'name': os.path.basename(src),
                        'width': img.width,
                        'height': img.height,
                        'size': round(len(img_response.content) / 1024, 2)  # Size in KB
                    })
                except Exception as e:
                    # Handle errors for invalid images
                    continue
        return render_template('index.html', images=images)
    except Exception as e:
        return render_template('index.html', error=str(e))
    
@app.route('/download/<path:image_url>')
def download_image(image_url):
    # Fetch the image
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    # Convert the image to PNG format
    img_io = BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)

    # Set the filename to be the same as the original but with a .png extension
    filename = os.path.basename(image_url).split('.')[0] + '.png'
    return send_file(img_io, as_attachment=True, download_name=filename, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)