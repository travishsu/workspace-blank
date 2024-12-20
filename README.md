# Synthetic Dataset Generation for Object Detection

This repository contains a script to generate a minimal synthetic dataset for training an experimental object detection system. The generated images are 32x32 pixels or less and use RGB channels. Each image contains random shapes (rectangles, circles, and triangles) with varying colors, sizes, and positions. The dataset also includes corresponding annotation files in COCO format.

## Dependencies

To run the script, you need the following libraries:

- Pillow
- NumPy
- random

You can install the required libraries using pip:

```bash
pip install Pillow numpy
```

## Running the Script

To generate the synthetic dataset, run the `generate_dataset.py` script:

```bash
python generate_dataset.py
```

The script will create a `data` directory with the following structure:

```
data/
├── images/
│   ├── image_0.png
│   ├── image_1.png
│   └── ...
└── annotations/
    ├── annotation_0.json
    ├── annotation_1.json
    └── ...
```

- `data/images/`: Contains the generated images.
- `data/annotations/`: Contains the corresponding annotation files in COCO format.

## Dataset Structure

The generated dataset consists of:

- **Images**: Synthetic images with random shapes (rectangles, circles, and triangles) of different sizes, colors, and positions. The images are 32x32 pixels or less and use RGB channels.
- **Annotations**: Corresponding annotation files in COCO format, containing information about the shapes in each image, including their bounding boxes and categories.

## Customization

You can customize the dataset generation by modifying the following parameters in the `generate_dataset.py` script:

- `num_images`: The number of images to generate.
- `image_size`: The size of the generated images (default is 32x32 pixels).
- `output_dir`: The directory where the generated images and annotations will be saved (default is `data`).

Feel free to experiment with different shapes, colors, and noise levels to create a more diverse and challenging dataset.
