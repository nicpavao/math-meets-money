from PIL import Image

def apply_tint(image, tint_rgb):
    r_tint, g_tint, b_tint= tint_rgb
    img = Image.merge("RGB", (
        image.point(lambda p: p * (r_tint / 255)),
        image.point(lambda p: p * (g_tint / 255)),
        image.point(lambda p: p * (b_tint / 255))
    ))
    return img

def process_image(input_path, output_path):
    # Open the image and convert to grayscale
    img = Image.open(input_path).convert("L")  

    # Apply the custom tint
    tinted_img = apply_tint(img, (250, 200, 150))

    # Get image dimensions
    img_w, img_h = tinted_img.size
    print(img_w,img_h)
    aspect_ratio = 7 / 5

    # Determine target dimensions to enforce the aspect ratio
    if img_w / img_h > aspect_ratio:
        pad_w = int(img_w/10)
        pad_h = int(((img_w + 2 * pad_w) / aspect_ratio - img_h)/2)
    else:
        pad_h = int(img_h/10)
        pad_w = int(((img_h + 2 * pad_h) * aspect_ratio - img_w)/2)

    # Calculate final canvas size
    final_w = int(img_w + 2 * pad_w)
    final_h = int(img_h + 2 * pad_h)

    # Create a white background
    background = Image.new("RGB", (final_w, final_h), (255, 255, 255))
    print(final_w,final_h, final_w/final_h)
    # Paste the processed image onto the white background
    background.paste(tinted_img, (pad_w, pad_h))
    print(pad_w/img_w,pad_h/img_h)
    # Save the processed image
    background.save(output_path)

# Example usage
process_image("/Users/nicpavao/Desktop/Bigger_Boat.png", "../cover_photos/Bigger_Boat.jpg")
