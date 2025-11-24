
# 🖼️ Batch Image Resizer Tool

A Python automation script that processes multiple images at once, resizing them to a specified dimension using the **Pillow (PIL)** library. 
This tool is designed to handle common image formats like JPG, PNG, and JPEG automatically.

## 🚀 Features
- **Batch Processing:** Resizes all images in a specific folder at once.
- **Error Handling:** Skips non-image files or corrupted files without crashing.
- **Automatic Folder Creation:** Automatically creates the output directory if it doesn't exist.
- **Format Support:** Works with .jpg, .jpeg, .png, and .gif.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Library:** [Pillow](https://python-pillow.org/) (Python Imaging Library Fork)
- **Module:** `os` (for file system navigation)

## ⚙️ Installation & Setup

1. **Clone the repository** (or download the files):
   ```bash
   git clone [https://github.com/your-username/Task-7-Image-Resizer.git](https://github.com/your-username/Task-7-Image-Resizer.git)

 * Navigate to the project directory:
   cd Task-7-Image-Resizer

 * Install the required library:
   You need to install Pillow to handle image processing.
   pip install Pillow

📖 How to Use
 * Prepare Input:
   Create a folder named input_images inside the project directory and paste the images you want to resize into it.
 * Run the Script:
   Execute the Python script using your terminal:
   python resizer.py

 * Check Output:
   The script will create a new folder named resized_images. All your resized images will be saved there with their original filenames.
📂 Project Structure
Task-7-Image-Resizer/
│
├── input_images/        # Put your original images here
├── resized_images/      # The script saves resized images here (Auto-generated)
├── resizer.py           # The main Python script
└── README.md            # Project documentation

📝 Code Logic
 * The script uses os.listdir() to scan the input folder.
 * It checks for valid image extensions using .endswith().
 * It opens each image using Image.open() and resizes it using the .resize() method.
 * Finally, it saves the result to the output folder.
👤 Author
Muddam Karthik Python Developer


### 💡 A Quick Tip for VS Code:
VS Code has a built-in **Markdown Preview**.
1. Open your `README.md` file.
2. Press **`Ctrl + Shift + V`**.
3. This will show you exactly how the file will look on GitHub (with the bold text and headers formatted correctly).

