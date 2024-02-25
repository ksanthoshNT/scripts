import os
import base64
import requests
import json
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import sys

root_path = '/home/ntlpt19/TF_testing_EXT/V2_Eval_FP'
out_put_path = '/home/ntlpt19/TF_testing_EXT/output'

def metric_calculation(u_true, u_pred):
    label_names = ['BOE', 'LCAPPLICATION', 'OTHERS', 'CS', 'BGCANCELLATION', 'COO', 'CI', 'BGCHECKLIST', 'BOL', 'IC', 'PL', 'PI', 'AWB', 'PO']
    # Convert true labels and predicted labels to numpy arrays
    true_labels = np.array(u_true)
    predicted_labels = np.array(u_pred)

    if len(true_labels) != len(predicted_labels):
        raise ValueError(
            "Inconsistent numbers of samples: true_labels: {}, predicted_labels: {}".format(len(true_labels),
                                                                                            len(predicted_labels)))
    # Calculate accuracy
    accuracy = accuracy_score(true_labels, predicted_labels)
    print("Accuracy:", accuracy)

    # Calculate precision
    precision = precision_score(true_labels, predicted_labels, average="weighted")
    print("Precision:", precision)

    # Calculate recall
    recall = recall_score(true_labels, predicted_labels, average="weighted")
    print("Recall:", recall)

    # Calculate F1 score
    f1 = f1_score(true_labels, predicted_labels, average="weighted")
    print("F1 Score:", f1)

    # Calculate confusion matrix
    # true_labels = [idx2label[label_idx] for label_idx in true_labels]
    # predicted_labels = [idx2label[label_idx] for label_idx in predicted_labels]
    confusion_mat = confusion_matrix(true_labels, predicted_labels, labels=label_names)
    
    fig = plt.figure(figsize=(8, 6), facecolor='w')

# Add the heatmap plot to the figure
    heatmap = sns.heatmap(confusion_mat, annot=True, fmt="d", cmap="Blues", xticklabels=label_names, yticklabels=label_names,
                        annot_kws={"color": "black", "fontsize": 12})
    plt.xlabel("Predicted Labels")
    plt.ylabel("True Labels")
    plt.title("Confusion Matrix")

    # Save the plot as an image file (e.g., PNG format)
    fig.savefig("confusion_matrix.png", bbox_inches="tight", dpi=300, pad_inches=0.1)
    print("Confusion Matrix:")
    #print(confusion_mat)    
    return accuracy, precision, recall, f1

def draw_bounding_boxes(image_path, extraction_data, save_img_path):
    # Read the image using cv2
    img = cv2.imread(image_path)
    print(image_path)
    # Iterate over the keys_extraction dictionary
    for key, data in extraction_data.items():
        print(data)
        if 'coordinate' in data:
            # Extract bounding box coordinates
            for bbox in data['coordinate']:
                print(bbox)
                # Draw bounding box on the image
                cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 0, 255), 2)

                # Add label text
                cv2.putText(img, key, (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    # Save the modified image
    cv2.imwrite(save_img_path, img)

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        # Read the binary data of the image
        image_binary = image_file.read()

        # Encode the binary data into Base64
        base64_encoded = base64.b64encode(image_binary)

        # Decode the bytes to a UTF-8 string
        base64_string = base64_encoded.decode("utf-8")

    return base64_string


import os
from google.cloud import vision



def get_ocr_vision_api_charConfi(image, KEY_PATH=None):
    # Set your Google Cloud service account credentials
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = KEY_PATH #"/home/nt/Rakesh/Final_delivery/TradeFinance/client_code/trade_finance_apis_extraction/src/main/spheric-time-383904-f1b421d86eef.json"

    # Initialize the Vision API client
    client = vision.ImageAnnotatorClient()



    # Perform text detection
    image = vision.Image(content=image)
    response = client.document_text_detection(image=image)

    # Initialize a list to store the formatted results
    formatted_results = []

    # Initialize a string to store all the extracted text
    all_extracted_text = ""

    # Extract and format the text and bounding box information
    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    word_text = "".join([symbol.text for symbol in word.symbols])
                    confidence = word.confidence
                    char_confidences = [symbol.confidence for symbol in word.symbols]

                    vertices = [(vertex.x, vertex.y) for vertex in word.bounding_box.vertices]
                    x1 = min([v[0] for v in vertices])
                    x2 = max([v[0] for v in vertices])
                    y1 = min([v[1] for v in vertices])
                    y2 = max([v[1] for v in vertices])

                    formatted_word = {
                        "word": word_text,
                        "left": x1,
                        "top": y1,
                        "width": x2 - x1,
                        "height": y2 - y1,
                        "confidence": confidence,
                        # 'char_confi': char_confidences,  # List of character-level confidences
                        "x1": x1,
                        "y1": y1,
                        "x2": x2,
                        "y2": y2,
                    }
                    formatted_results.append(formatted_word)
                    all_extracted_text += word_text + ' '
    print(formatted_results)
    return formatted_results, all_extracted_text




def __main__ ():
    
    GT_list = []
    predicted_list = []
    confi_list = []
    image_name = []



    for doc_type in os.listdir(root_path):
        for imgs_folder in os.listdir(os.path.join(root_path, doc_type)):
            for imgs in os.listdir(os.path.join(root_path, doc_type, imgs_folder)):
                img_base64 = image_to_base64((os.path.join(root_path, doc_type, imgs_folder, imgs)))
                # doc_class = doc_type
                # image=request.image
                # ground_truth=request.docClass
                # doc_type = 'CS'
                img_path = os.path.join(root_path, doc_type, imgs_folder, imgs)
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print(img_path)
                WC, all_words = get_ocr_vision_api_charConfi(img_path)
                print(WC)
                ground_truth = doc_type
                input_dict = {'image':img_base64, 'ocr_data': WC}#, 'docClass':doc_type}
                # exit('>')
                
                # x =  request.json()  # request in str
                # x = json.loads(x) 
                url = 'http://10.2.3.12:7191/intelligent_trade_finance/classification/rule-based'
                response = requests.post(url, json=input_dict)
                x = response.json()
                print('*************')
                print(type(x))
                print(x)
                doc_class = x["class"]
                # confidence_score = x["confidenceScore"]
                
                image_name.append(img_path)
                GT_list.append(ground_truth)
                predicted_list.append(doc_class)
                print(x)
                print('*************')
                
    data = {'ImageName': image_name, 'ground_truth': GT_list, 'Prediction': predicted_list}#, 'Confidence': confi_list, }
    df = pd.DataFrame(data)

    # Define the CSV file name
    csv_file = 'output.csv'
    df.to_csv(csv_file, index=False)
    accuracy, precision, recall, f1 = metric_calculation(GT_list, predicted_list)


    with open('accuracy.txt', 'w') as f:
    # Redirect standard output to the file
        sys.stdout = f
        print("Accuracy:", accuracy)
        print("Precision:", precision)
        print("Recall:", recall)
        print("F1 Score:", f1)
        # Reset standard output
        sys.stdout = sys.__stdout__

