import os
import random
import json
import numpy as np
from PIL import Image, ImageDraw

def generate_synthetic_image(image_size, shapes):
    image = Image.new('RGB', image_size, (255, 255, 255))
    draw = ImageDraw.Draw(image)
    
    for shape in shapes:
        shape_type = shape['type']
        color = shape['color']
        bbox = shape['bbox']
        
        if shape_type == 'rectangle':
            draw.rectangle(bbox, fill=color)
        elif shape_type == 'circle':
            draw.ellipse(bbox, fill=color)
        elif shape_type == 'triangle':
            draw.polygon(bbox, fill=color)
    
    return image

def add_noise_and_distortions(image):
    image_array = np.array(image)
    
    # Add random noise
    noise = np.random.normal(0, 25, image_array.shape)
    noisy_image = image_array + noise
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    
    # Convert back to PIL image
    noisy_image = Image.fromarray(noisy_image)
    
    return noisy_image

def create_annotations(shapes, image_id):
    annotations = []
    
    for shape in shapes:
        annotation = {
            'image_id': image_id,
            'category_id': 1,  # Assuming a single category for simplicity
            'bbox': shape['bbox'],
            'area': (shape['bbox'][2] - shape['bbox'][0]) * (shape['bbox'][3] - shape['bbox'][1]),
            'iscrowd': 0
        }
        annotations.append(annotation)
    
    return annotations

def save_dataset(num_images, image_size, output_dir):
    os.makedirs(os.path.join(output_dir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'annotations'), exist_ok=True)
    
    for i in range(num_images):
        shapes = []
        num_shapes = random.randint(1, 5)
        
        
        for _ in range(num_shapes):
            shape_type = random.choice(['rectangle', 'circle', 'triangle'])
            color = tuple(random.randint(0, 255) for _ in range(3))
            x0, x1 = sorted([random.randint(0, image_size[0] - 1) for _ in range(2)])
            y0, y1 = sorted([random.randint(0, image_size[1] - 1) for _ in range(2)])
            bbox = [x0, y0, x1, y1]
            
            shapes.append({
                'type': shape_type,
                'color': color,
                'bbox': bbox
            })
        
        image = generate_synthetic_image(image_size, shapes)
        image = add_noise_and_distortions(image)
        
        image_path = os.path.join(output_dir, 'images', f'image_{i}.png')
        image.save(image_path)
        
        annotations = create_annotations(shapes, i)
        annotation_path = os.path.join(output_dir, 'annotations', f'annotation_{i}.json')
        
        with open(annotation_path, 'w') as f:
            json.dump(annotations, f)

if __name__ == '__main__':
    num_images = 100
    image_size = (32, 32)
    output_dir = 'data'
    
    save_dataset(num_images, image_size, output_dir)
