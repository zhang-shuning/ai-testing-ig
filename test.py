from PIL import Image, ExifTags

# Load the image
img = Image.open(r"C:\Users\user\Desktop\Python\ai-testing-ig\images_to_use\Abyssinian_1.jpg")

# Extract EXIF data
exif_data = img._getexif()

if exif_data:
    for tag_id, value in exif_data.items():
        # Get human-readable tag name (e.g., 'Make', 'DateTime', 'GPSInfo')
        tag_name = ExifTags.TAGS.get(tag_id, tag_id)
        print(f"{tag_name}: {value}")
else:
    print("No EXIF metadata found.")