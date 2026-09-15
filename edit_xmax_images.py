from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


ROOT = Path("images/products/xmax-collar")


def christmas_cover():
    source = cv2.imread(str(ROOT / "cover.png"), cv2.IMREAD_COLOR)
    height, width = source.shape[:2]
    background = np.zeros_like(source)
    for y in range(height):
        blend = y / max(height - 1, 1)
        background[y, :, 0] = int(246 - 18 * blend)
        background[y, :, 1] = int(249 - 10 * blend)
        background[y, :, 2] = int(232 + 4 * blend)

    overlay = background.copy()
    cv2.rectangle(overlay, (0, 0), (width, 25), (45, 103, 72), -1)
    cv2.rectangle(overlay, (0, height - 22), (width, height), (159, 43, 47), -1)
    for offset in range(-height, width, 145):
        points = np.array([[offset, height], [offset + 42, height], [offset + height + 42, 0], [offset + height, 0]])
        cv2.fillPoly(overlay, [points], (177, 47, 52))
    background = cv2.addWeighted(overlay, 0.16, background, 0.84, 0)
    blank = np.all(source > 245, axis=2)
    result = source.copy()
    result[blank] = background[blank]
    result[:25] = cv2.addWeighted(source[:25], 0.15, background[:25], 0.85, 0)
    result[height - 22:] = cv2.addWeighted(source[height - 22:], 0.15, background[height - 22:], 0.85, 0)
    cv2.imwrite(str(ROOT / "cover-christmas.png"), result)


def remove_sample_title():
    image = cv2.imread(str(ROOT / "sample.png"), cv2.IMREAD_COLOR)
    height, width = image.shape[:2]
    repaired = image.copy()
    for y in range(0, 86):
        edge_pixels = np.vstack((image[y, :70], image[y, width - 62:]))
        repaired[y, :] = np.median(edge_pixels, axis=0).astype(np.uint8)
    cv2.imwrite(str(ROOT / "sample-clean.png"), repaired)


def replace_intro_labels():
    image = cv2.imread(str(ROOT / "product_intro.png"), cv2.IMREAD_COLOR)
    repaired = image.copy()
    background_color = np.array([224, 231, 234], dtype=np.uint8)
    repaired[42:84, 248:390] = background_color
    repaired[42:116, 450:598] = background_color
    pil_image = Image.fromarray(cv2.cvtColor(repaired, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_image)
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    font = ImageFont.truetype(font_path, 14)
    draw.text((258, 53), "Soft inner layer", fill=(112, 55, 38), font=font)
    draw.text((482, 53), "Padded lining", fill=(112, 55, 38), font=font)
    pil_image.save(ROOT / "product-intro-english.png")


christmas_cover()
replace_intro_labels()
remove_sample_title()