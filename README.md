# Setup

## Dependencies

- Python 2.7.10
- OpenCV 4.0.0

# Usage

Create folder structure and drop input images

```
.
├── images
│   └── input
│       ├── [files_to_process.jpg]
│       └── processed
│           ├── found-no-face
│           └── found-face
└── output
    └── [extracted_faces.jpg]
```

Run program in terminal

`$ python extractFacesFromFile.py`

## Options

`bool moveInputFiles`

Sortes processed files by moving them into subfolder

`bool dontExportFaces`

Does not save found faces as new images but creates a screen output



