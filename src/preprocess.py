import cv2
import os


def preprocess_image(input_path, output_path):
    """
    Basic preprocessing for noisy scanned medical document images.

    Parameters
    ----------
    input_path : str
        Path to the input image.
    output_path : str
        Path where the processed image will be saved.

    Returns
    -------
    None
    """

    image = cv2.imread(input_path)

    if image is None:
        raise ValueError(f"Could not read image: {input_path}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    denoised = cv2.medianBlur(gray, 3)

    thresholded = cv2.adaptiveThreshold(
        denoised,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        10
    )

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    cv2.imwrite(output_path, thresholded)


def preprocess_folder(input_folder, output_folder):
    """
    Apply preprocessing to all JPG images in a folder.
    """

    os.makedirs(output_folder, exist_ok=True)

    image_files = [
        f for f in os.listdir(input_folder)
        if f.lower().endswith(".jpg")
    ]

    for filename in image_files:
        input_path = os.path.join(input_folder, filename)
        output_filename = filename.replace(".jpg", "_processed.jpg")
        output_path = os.path.join(output_folder, output_filename)

        preprocess_image(input_path, output_path)

    print(f"Processed {len(image_files)} images.")
