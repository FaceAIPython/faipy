from setuptools import setup, find_packages

setup(
    name="faipy",
    version="0.0.1",
    description="The Full Face AI Toolkit — faipy Python Library",
    author="Shosho & Sarah Team",
    author_email="datasoftcompany@gmail.com",
    packages=find_packages(),
    install_requires=["opencv-python", "face_recognition"],
    python_requires='>=3.7',
    url="https://github.com/FaceAIPython/faipy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
