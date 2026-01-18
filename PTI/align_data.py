from configs import paths_config
import dlib
from tqdm import tqdm
from utils.alignment import align_face
from PIL import Image
import os

def pre_process_image(image_path, output_dir=None):
    IMAGE_SIZE = 1024
    predictor = dlib.shape_predictor(paths_config.dlib)
    
    try:
        print(f"Processing image: {image_path}")
        aligned_image = align_face(
            filepath=image_path,
            predictor=predictor, 
            output_size=IMAGE_SIZE
        )
        
        base_name = os.path.basename(image_path)
        name_without_ext = os.path.splitext(base_name)[0]
        
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, f"{name_without_ext}_aligned.jpeg")
        else:
            output_path = f"{name_without_ext}_aligned.jpeg"
        
        aligned_image.save(output_path)
        print(f"Saved aligned image to: {output_path}")
        
        return aligned_image
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None


if __name__ == "__main__":
    image_path = './lrq.jpg'
    aligned_image = pre_process_image(image_path)
