import cv2


def unnormalize_box(bbox, width, height):
    print(f"width: {width}, height: {height}")

    # centre of the image
    ############################
    x_center = float(bbox[0]) * width
    y_center = float(bbox[1]) * height
    ############################

    width = float(bbox[2]) * width
    height = int(float(bbox[3]) * height)

    x0 = int(x_center - (width / 2))
    x1 = int(x_center + (width / 2))
    y0 = int(y_center - (height / 2))
    y1 = int(y_center + (height / 2))

    return [x0, y0, x1, y1]
# Load the image
image_path = "/home/ntlpt59/Documents/trade_finance_utils/sample_image_all_documents/airway_bill/images/Bill_Of_Landing_133_page_0.png"  # Replace with the actual path to your image
image = cv2.imread(image_path)

# Get the width and height of the image
img_height, img_width, _ = image.shape

print("Image Width:", img_width)
print("Image Height:", img_height)
_,x_normalized,y_normalized,width_normalized,height_normalized = 0,0.253632,0.308811,0.182809,0.025663

x1,y1,x2,y2 = unnormalize_box([x_normalized,y_normalized,width_normalized,height_normalized],img_width,img_height)
print(x1,y1,x2,y2)
