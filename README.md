# InstantGallery-Image-Downloader

InstantGallery is a simple and intuitive desktop application for downloading images from the web. Enter a search query, select a destination folder, and the app will automatically scrape and download relevant images from Google Images into a neatly organized sub-folder.

## Features

*   **Simple GUI:** Built with `customtkinter` for a modern, dark-themed interface.
*   **Bulk Image Downloading:** Fetches and downloads up to 20 images based on your search term.
*   **Automated Organization:** Automatically creates a sanitized directory name for each search query to keep your downloads tidy.
*   **User-Friendly:** Easy-to-use interface for entering queries and selecting download locations.
*   **Responsive:** Uses threading to ensure the application remains responsive while images are being downloaded in the background.

## Requirements

*   Python 3
*   `customtkinter`
*   `requests`
*   `beautifulsoup4`

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/rifatsh3ikh/InstantGallery-Image-Downloader.git
    cd InstantGallery-Image-Downloader
    ```

2.  Install the required Python libraries:
    ```bash
    pip install customtkinter requests beautifulsoup4
    ```

## How to Run

Execute the `main.py` script to launch the application.

```bash
python main.py
```

## How to Use

1.  Launch the application by running `main.py`.
2.  In the **Search Query** field, type the subject of the images you want to download (e.g., "classic cars").
3.  Click the **Select Download Folder** button and choose the main directory where you want to save the images.
4.  Click the **Download Images** button to begin.
5.  The application will fetch the images and save them in a new sub-folder within your selected location (e.g., `path/to/your/folder/classic_cars/`).
6.  A success message will appear once the download is complete.

## 🤝 Contributing

Contributions are welcome!
To contribute:

Fork the project

Create a feature branch (git checkout -b feature/your‑idea)

Commit your changes (git commit -m "Add feature")

Push to your branch (git push)

Open a Pull Request

## 📬 Contact

Maintained by rifatsh3ikh
