from PIL import Image

def apply_tint(image, tint):
    """Apply a sepia tone to a grayscale image."""
    sepia = Image.new("RGB", image.size)
    pixels = image.load()
    sepia_pixels = sepia.load()
    
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            gray = pixels[x, y]  # Grayscale value
            r = min(int(gray * tint[0] / 255), 255)
            g = min(int(gray * tint[1] / 255), 255)
            b = min(int(gray * tint[2] / 255), 255)
            sepia_pixels[x, y] = (r, g, b)
    
    return sepia

def process_image(input_path, output_path):
    # Open the image and convert to grayscale
    img = Image.open(input_path).convert("L")  

    # Apply sepia tone
    sepia_img = apply_tint(img, (250, 200, 150))

    # Save the processed image (no borders)
    sepia_img.save(output_path)

# Example usage
process_image("../raw_photos/Perpetual_Motion.png", "../cover_photos/Perpetual_Motion.jpg")
