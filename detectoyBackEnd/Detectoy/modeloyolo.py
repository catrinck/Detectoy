import cv2
import os
from ultralytics import YOLO

config = {
    'CONFIDENCE_THRESHOLD' : 0.35,
    'MODEL_PATH' : os.path.join(os.path.dirname(__file__), "models", "banana.pt"),
    'IMAGE_DIR' : os.path.join(os.path.dirname(__file__), "images"),
    'OUTPUT_DIR' : os.path.join(os.path.dirname(__file__), "results")
}

# Reads an image name like TYPE-LINE_YYYY-MM-DD-MM-SS-mmmm
def process_image(image_name: str, config: dict = config):
    os.makedirs(config['IMAGE_DIR'], exist_ok=True)
    os.makedirs(config['OUTPUT_DIR'], exist_ok=True)

    print("\nStarted processing with the following config:")
    print("-----")
    for key, value in config.items():
        print(key, " : ", value)
    print("-----")

    print("Loading model...")
    model = YOLO(config['MODEL_PATH'])
    print("Model loaded.")

    print("Setting image path...")
    image_path = os.path.join(config['IMAGE_DIR'], image_name)
    print("Image path set.")

    print(f"Loading image in {image_path}")
    image = cv2.imread(image_path)
    if image is None:
        print(f"Couldn't load image in {image_path}")
        raise TypeError(f"Couldn't load image in {image_path}")
    print("Image loaded.")

    print("Analyzing image...")
    results = model(str(image_path), conf=config['CONFIDENCE_THRESHOLD'])[0]
    print("Image analyzed.")

    print("Plotting analysis...")
    annotated_image = results.plot()
    print("Analysis plotted.")

    print("Writing image...")
    output_path = os.path.join(config['OUTPUT_DIR'], image_name)
    cv2.imwrite(str(output_path), annotated_image)
    print(f"Image written in {output_path}")

    detected_classes = [model.names[int(box.cls)] for box in results.boxes]

    errors = {
        'broken_screen' : False,
        'broken_shell' : False
    }

    if "tela_quebrada" in detected_classes:
        errors['broken_screen'] = True

    if "carcaca_quebrada" in detected_classes:
        errors['broken_shell'] = True

    print("Results of analysis:\n-----")
    for key, value in errors.items():
        print(key, " : ", value)
    print("-----")

    return errors

if __name__=='__main__':
    images_names = ["img1.jpg",
                    "img2.jpg",
                    "img3.jpg",
                    "img4.jpg"
                    ]

    for image_name in images_names:
        print(process_image(image_name))
