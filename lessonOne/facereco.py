import cv2
import matplotlib.pyplot as plt

def detect_faces_opencv(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: The file '{image_path}' was not found.")
        return
    
    # Convert to grayscale (required for face detection)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Load the Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    if len(faces) == 0:
        print("No faces detected in the image.")
        return
    
    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Save cropped faces
    for i, (x, y, w, h) in enumerate(faces):
        face = image[y:y+h, x:x+w]
        face_path = f"face_{i+1}.jpg"
        cv2.imwrite(face_path, face)
        print(f"Face {i+1} saved as '{face_path}'.")
    
    # Convert the image from BGR (OpenCV format) to RGB (Matplotlib format)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Display the image with Matplotlib
    plt.imshow(rgb_image)
    plt.axis('off')  # Hide axes for better visualization
    plt.title("Detected Faces")
    plt.show()

# Example usage
image_path = "file.jpg"  # Update with the actual path to your image
detect_faces_opencv(image_path)
