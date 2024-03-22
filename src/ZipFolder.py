import os
import zipfile

def zip_directory_with_extensions(directory_path, extensions, zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for root, _, files in os.walk(directory_path):
            for file in files:
                if any(file.endswith(ext) for ext in extensions):
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, directory_path))

# Test the function:
directory_path = '.\\assets\\my_stuff'
extensions = ['.txt', '.pdf', '.jpg']  # Specify your desired file extensions
zip_file_path = '.\\assets\my_stuff.zip'

zip_directory_with_extensions(directory_path, extensions, zip_file_path)
