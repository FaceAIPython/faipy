import cv2
import face_recognition

def detect_faces(image_path, draw=True, show=True):
    """
    Detect all faces in the given image and draw rectangles on them.

    Args:
        image_path (str): Path to the image file.
        draw (bool): Whether to draw rectangles around faces.
        show (bool): Whether to display the image with detected faces.

    Returns:
        list: List of face locations (top, right, bottom, left)
    """
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Cannot read image: {image_path}")
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    faces = face_recognition.face_locations(img_rgb)
    if draw:
        for (top, right, bottom, left) in faces:
            cv2.rectangle(img, (left, top), (right, bottom), (0,255,0), 2)
    if show:
        cv2.imshow("faipy Face Detection", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return faces
