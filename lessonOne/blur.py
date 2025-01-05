from PIL import Image, ImageFilter

try:
    before = Image.open("me.jpg")
    after = before.filter(ImageFilter.BoxBlur(10))
    after.save("new.jpg")
    print("Image blurred and saved as new.jpg")
except FileNotFoundError:
    print("File me.jpg not found. Ensure it exists in the same directory.")
except Exception as e:
    print(f"An error occurred: {e}")
