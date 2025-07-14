from PIL import Image, ImageChops

def compare_screenshots(baseline, current):
    img1 = Image.open(baseline)
    img2 = Image.open(current)
    diff = ImageChops.difference(img1, img2)
    return sum(diff.getbbox() or [0])