import os
from PIL import Image

# Define our input and output folders
source_folder = 'images'
destination_folder = 'resized_images'

# Create the destination folder if it doesn't exist (Good practice)
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

def resize_images():
    # 1. Use os to read all files in the directory
    files = os.listdir(source_folder)
    
    print(f"Found {len(files)} files. Starting process...")

    for file_name in files:
        # Construct the full path to the file
        input_path = os.path.join(source_folder, file_name)
        
        # Check if the file is actually an image (skip system files)
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            try:
                # 2. Open the image
                img = Image.open(input_path)
                
                # 3. Resize the image (e.g., to 300x300 pixels)
                # We use 'thumbnail' to keep aspect ratio, or 'resize' to force dimensions
                new_size = (300, 300) 
                img = img.resize(new_size)
                
                # Create output path
                output_path = os.path.join(destination_folder, file_name)
                
                # 4. Save the image
                img.save(output_path)
                print(f"Resized: {file_name}")
                
            except Exception as e:
                # Try-Except block handles errors (like corrupted files) without crashing
                print(f"Error processing {file_name}: {e}")
        else:
            print(f"Skipped: {file_name} (not an image)")

    print("Task Completed!")

# Run the function
if __name__ == "__main__":
    resize_images()