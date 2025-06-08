from PIL import Image

image_files = ['Munkaltatoi_ig_blanar_levente.jpeg']

images = [Image.open(img).convert("RGB") for img in image_files]

images[0].save("Munkaltatoi_ig_blanar_levente.pdf", save_all=True, append_images=images[1:])