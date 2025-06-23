````markdown
# faipy

> Face AI Python Library, (by Shosho and Sarah Team), For Everyone

> The Full Face AI Toolkit — faipy Python Library ([PyPI](https://pypi.org/project/faipy/))

**faipy** is a simple, fast, and universal Face AI library for Python.  
Detect faces in images, recognize people, and enable smart voice interaction — in just two lines!

---

## 💡 Quick Install

```bash
pip install faipy
````

---

## 💡 Quick Example

```python
import faipy

# Detect faces in an image and show the result
faipy.detect_faces("myphoto.jpg")
```

---

## ✨ Features

* Face detection in images (with OpenCV and face\_recognition)
* (Coming soon) Face recognition from your custom dataset
* Smart voice notification (macOS 'say' or pyttsx3)
* Easy to use, with simple Python functions
* Cross-platform (Windows, macOS, Linux)
* Beginner-friendly — no AI background needed

---

## 📦 Project Structure

```
faipy/
    __init__.py
    face.py
README.md
setup.py
pyproject.toml
.gitignore
```

---

## 🛠️ Usage

### Detect faces from an image

```python
import faipy

faces = faipy.detect_faces("myphoto.jpg", draw=True, show=True)
print("Found faces at:", faces)
```

* **draw:** Draw rectangles on detected faces (default: True)
* **show:** Show the image in a pop-up window (default: True)

---

## 🏆 Coming Soon

* Real-time face recognition from webcam
* Voice alerts for recognized persons
* Simple dataset training and evaluation
* More documentation, tutorials, and examples

---

## 🎉 Created in the desert, shared with the world by Shosho & Sarah

## License

MIT

---

*If you like faipy, star the repo and share with your friends! For questions, contact [github.com/FaceAIPython/faipy](https://github.com/FaceAIPython/faipy)*

