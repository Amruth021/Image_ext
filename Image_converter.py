from PIL import Image
import os

# Supported formats dictionary
format_map = {
    "png": "PNG",
    "bmp": "BMP",
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "gif": "GIF",
    "tiff": "TIFF",
    "webp": "WEBP",
    "eps": "EPS",
    "dds": "DDS",
    "ico": "ICO",
    "tga": "TGA",
    "ppm": "PPM",
    "pcx": "PCX"
}

try:
    input_file = input("Enter image name/path: ").strip()
    image = Image.open(input_file)

    print("Image format:", image.format)
    print("Image mode:", image.mode)

    ch = input("Enter the format to convert (BMP/JPG/PNG/GIF/TIFF/WEBP/EPS/DDS/ICO/TGA/PPM/PCX): ").strip().lower()

    if ch in format_map:
        output_filename = os.path.splitext(input_file)[0] + f".{ch}"
        image.save(output_filename, format_map[ch])
        print(f"Converted {input_file} to {output_filename}")
    else:
        print("Unsupported format. Please enter a valid format.")

except FileNotFoundError:
    print("File not found. Please check the path.")
except Exception as e:
    print("An error occurred:", e)
