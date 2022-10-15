from PIL import Image
import requests
from io import BytesIO
import base64
import re
import sys
import config
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM


def img_processing(nfts, bundle_id):
    # Create New Image
    bundle_image = Image.new(config.image_mode, (config.image_length, config.image_height))
    # Add extension from config
    file_path = config.bundles_dir + str(bundle_id) + config.image_type

    # Image Starting Coordinates
    x = config.image_height // 2
    y = 0

    # Verify Length
    length = len(nfts)
    if length < 2:
        raise Exception("Bundles must be 2 or greater")

    # Mathematical spacer for symmetry
    math_spacer = x // (length - 1)

    # Special formatting for 2
    if length == 2:
        y = 50
        x = x - y
        math_spacer = 400

    # Loop through all NFT data
    for nft in nfts:
        img = get_image(nft)
        bundle_image.paste(img, (x, y))
        # Calibrate position for next Image
        length -= 1
        x -= math_spacer
        y += math_spacer

    # Add Branding
    branding = get_branding()
    bundle_image.paste(branding, (config.branding_y, config.branding_x), branding)
    # Save Image
    bundle_image.save(file_path)


def get_branding():
    # Add Branding
    branding = Image.open(config.branding_image)
    branding = branding.resize((config.branding_length, config.branding_height))
    return branding


def get_image(nft):
    if not isinstance(nft, str):
        raise Exception("Only string values are supported")

    if is_base64(nft):
        # raise Exception("Base64 currently not supported")
        return get_base64_image(nft)

    # Get Image from URL
    response = requests.get(nft)
    img = Image.open(BytesIO(response.content))
    img = img.resize((500, 500))
    return img


def get_base64_image(nft):
    # Decode the base64 string
    code64 = base64.b64decode(nft)
    img64 = BytesIO(code64)
    # Convert the SVG into a PNG
    svg = svg2rlg(img64)
    # Return PIL Image
    return renderPM.drawToPIL(svg)


def startup(args):
    # No Args
    if len(args) == 0:
        raise Exception("`bundle_id` and an array of NFT tokenURI links are required")

    # Demo Mode
    if args[0] == "demo":
        b_id = config.demo_bundle_id
    else:
        if isinstance(args[0], int):
            b_id = args[0]
        else:
            raise Exception("`bunlde_id` must be an integer")

    # If no nft data provided, use demo data
    if len(args) > 1:
        data = args[1:]
    else:
        data = config.test_nft_data

    return data, b_id


def is_base64(s):
    x = re.search("^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$", s)
    if x:
        return True
    return False


if __name__ == '__main__':
    nft_data, id_bundle = startup(sys.argv[1:])
    img_processing(nft_data, id_bundle)
