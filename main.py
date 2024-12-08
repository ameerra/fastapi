import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount the static directories for CSS and images
app.mount("/static/photos", StaticFiles(directory="photos"), name="photos")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def index():
    # Path to the folder where images are stored
    IMAGES_DIR = "photos/Presentation2"

    # List all the images in the folder 'photos/Presentation2'
    image_paths = [f"/static/photos/Presentation2/{filename}" for filename in os.listdir(IMAGES_DIR) if filename.endswith(".PNG")]

    # If no images found, return a message
    if not image_paths:
        return HTMLResponse(content="<html><body><h1>No images found in the folder.</h1></body></html>")

    # Generate HTML with buttons for navigation
    html_content = f"""
    <html>
    <head>
        <title>תיעוד</title>
        <link rel="stylesheet" href="/static/css/style.css">
        <script>
            let currentIndex = 0;
            const images = {image_paths};  // List of image paths

            function showImage(index) {{
                const imgElement = document.getElementById('image-display');
                if (index >= 0 && index < images.length) {{
                    currentIndex = index;
                    imgElement.src = images[currentIndex];
                }}
            }}

            function nextImage() {{
                if (currentIndex < images.length - 1) {{
                    showImage(currentIndex + 1);
                }}
            }}

            function previousImage() {{
                if (currentIndex > 0) {{
                    showImage(currentIndex - 1);
                }}
            }}

            window.onload = function() {{
                showImage(currentIndex);  // Display the first image on load
            }}
        </script>
    </head>
    <body>

        <h1>תיעוד</h1>
        <img id="image-display" style="max-width: 100%; height: auto; margin: 20px;" />
         <div>
            <button onclick="previousImage()">Previous</button>
            <button onclick="nextImage()">Next</button>

     </div>
    </body>
    </html>
    """

    return HTMLResponse(content=html_content)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
