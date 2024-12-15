<H1 align="center"> Image Extractor Tool </H1>
The Image Extractor Tool is a powerful and user-friendly application designed to fetch, analyze, and download images from any webpage. With a sleek interface, this tool enables users to input a URL and seamlessly retrieve all the images available on the page. It provides detailed information about each image, such as dimensions, file size, and format.<br>
<br>
<div align="center">
  
<img src="https://github.com/user-attachments/assets/4f9e4599-b4fb-40b6-9c32-27026a86c086" style="width: 200px; height: 200px;">

</div>

<h2>Features</h2>

* Automatic Image Retrieval: Extracts both absolute and relative image links.
* Image Preview and Details: Displays image metadata for easy selection.
* Image Conversion: Allows downloading images in PNG format regardless of their original type.

<br>
<h2>Run Instructions for the Image Extractor Tool</h2>
Ensure Python 3.8 or above is installed on your system.<br>
Install pip (Python's package installer).<br>

<br>
<h3>Setup Instructions</h3>
Clone or Download the Project: 

`https://github.com/BlackSheep47/Image-Extractor.git`<br>

Save the Python file and associated templates (e.g., index.html) in a project folder.<br>
Open a terminal or command prompt and navigate to the folder containing the project file

`cd path/to/project/folder`

<h3>Create a Virtual Environment (Optional but Recommended)</h3>

`python -m venv venv` <br>
`source venv/bin/activate    # On Linux/Mac` <br>
`venv\Scripts\activate       # On Windows`<br>

<h3>Install Dependencies</h3>
Use the requirements.txt file to install the necessary Python packages<br>

`pip install -r requirements.txt`<br>

<h3>Run the Application</h3>
Run the Flask application using the following command<br>

`python app.py`

<h3>Access the Application</h3>
Open your browser and navigate to<br>

`http://127.0.0.1:5000/`

<h2>Usage</h2>

* Enter the URL of a webpage containing images.
* View the extracted images and metadata.
* Download images in PNG format using the provided links.

<h3>Stop the Application</h3>
Press Ctrl+C in the terminal to stop the Flask server.

<br>
> [!Note]
> Built with Python and Flask, the tool leverages web scraping (using BeautifulSoup) and image processing (via Pillow) to ensure reliability and efficiency, making it ideal for developers, designers, and content creators.
