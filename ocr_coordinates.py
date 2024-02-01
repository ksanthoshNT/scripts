from PIL import Image
import pytesseract
import json
import sys

def extract_text_and_coordinates(image_path):
    # Open the image using PIL
    image = Image.open(image_path)

    # Use pytesseract to extract text and coordinates
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

    # Filter out empty text and create a list of dictionaries with text and coordinates
    results = []
    for i in range(len(data['text'])):
        text = data['text'][i].strip()
        if text:
            result = {
                'word': text,
                'word_coordinates': [data['left'][i], data['top'][i], data['left'][i] + data['width'][i], data['top'][i] + data['height'][i]],
                'x1':data['left'][i],
                'y1':data['top'][i],
                'x2':data['left'][i]+data['width'][i],
                'y2':data['top'][i]+data['height'][i],
                'top':data['top'][i],
                'left':data['left'][i]

            }
            results.append(result)

    return results

def save_to_json(data, output_path):
    # Save the extracted data to a JSON file
    print(output_path)
    with open(output_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)

if __name__ == "__main__":
    print(sys.argv)
    src_path = ""
    if len(sys.argv)>1:
        src_path = sys.argv[1]
    dest_path = src_path.split(".")[0] + ".json"

    # Get input image path from the user
    if src_path:
        image_path  = src_path
    else:
        image_path = input("Enter the path of the input image: ")

    # Extract text and coordinates
    extracted_data = extract_text_and_coordinates(image_path)

    # Get output JSON file path from the user
    if dest_path:
        output_path = dest_path
    else:
        output_path = input("Enter the path for the output JSON file: ")
    
    # Save the extracted data to a JSON file
    save_to_json(extracted_data, output_path)

    print(f"Extraction complete. Results saved to {output_path}")

