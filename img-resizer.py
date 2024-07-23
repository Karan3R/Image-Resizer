from PIL import Image

def resize_image(input_path, output_path, size):
    with Image.open(input_path) as img:
        img = img.resize(size)
        img.save(output_path)

# Example usage resize_image('original image path', 'new image path', (width, height))

resize_image('C:/Users/ADMIN/Downloads/18.png', 'C:/Users/ADMIN/Downloads/186.png', (6000, 6000))
