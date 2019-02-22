# Usage
$ python extractFacesFromFile.py

## Options
*moveInputFiles bool*
Sortes processed files by moving them into subfolder

*dontExportFaces bool*
Does not save found faces as new images but creates a screen output

# Setup
*Dependencies*
Python 2.7.10
OpenCV 4.0.0

*Folder Structure*
To make the program run, create the following folder structure:
.
├── images
│   └── input
│       ├── [files_to_process.jpg]
│       └── processed
│           ├── found-no-faces
│           └── found-faces
└── output
    └── [extracted_faces.jpg]
