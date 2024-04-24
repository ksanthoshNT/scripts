import json
import subprocess

def generate_request_data_lc(lc_no, key_value_pairs):
    data_lc = {
        "collection_name": "lc_extraction",
        "database_name": "trade_finance_santhosh_dev",
        "data": {
            "lc_no": lc_no,
            "data":key_value_pairs
        }
    }

    return json.dumps(data_lc, indent=2)

def generate_request_data_data(lc_no, doc_class, key_value_pairs):
    data_data = {
        "collection_name": "extraction_results",
        "database_name": "trade_finance_santhosh_dev",
        "data": {
            "lc_no": lc_no,
            "docClass": doc_class,
            "keys_extraction": key_value_pairs
        }
    }
    return json.dumps(data_data, indent=2)

def modify_collection(collection_json, lc_data, data_data):
    new_collection = collection_json.copy()

    for item in new_collection["item"]:
        if item["name"] == "ucp_ae_sd_1_LC":
            item["request"]["body"]["raw"] = lc_data
        elif item["name"] == "ucp_ae_sd_1_DATA":
            item["request"]["body"]["raw"] = data_data

    return new_collection

def execute_curl_command(rule_id):
    curl_command = f'curl --location \'http://10.2.3.12:8171/verify_rules\' ' \
                    f'--header \'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbjIiLCJleHAiOjE3MTE4NDg5MjB9.aNR1325dRz3W7ZyeKfGYUkAnKNDTnd64RT62JfPsNvY\' ' \
                    f'--header \'Content-Type: application/json\' ' \
                    f'--data \'{{"lc_no":"42MEX39C24", "rule_mode":"ae", "action":"add", "product_name":"Import Bills", "filter_type":"id_wise", "rule_id":"{rule_id}"}}\''
    subprocess.run(curl_command, shell=True)

def create_dict_from_string(input_key, input_value):
    result = {}
    temp = result
    input_key = input_key.replace("]","")
    keys = input_key.split("[")
    for k in keys[:-1]:
        temp = temp.setdefault(k,{})
    temp[keys[-1]]  = input_value
    return result

if __name__ == "__main__":
    # Input data for ucp_ae_sd_1_LC
    # lc_no_input = input("Enter LC Number: ")
    lc_no_input = "42MEX39C24"
    original_json_path = "/home/ntlpt59/Documents/Trade-Finance-Demo-dec17.postman_collection.json"
    # Input key-value pairs for ucp_ae_sd_1_LC
    lc_data = {}
    lc_key_value_pairs = []
    while True:
        key = input("Enter LC :key (or 'done' to finish): ")
        if key.lower() == 'done' or key.lower() == "":
            break
        value = input("Enter value: ")
        # lc_key_value_pairs.append((key, value))
        data_x = create_dict_from_string(key,value)
        lc_data.update(data_x)
    # Input data for ucp_ae_sd_1_DATA
    print(lc_data)
    doc_class_input = input("Enter Document Class: ")

    # Input key-value pairs for keys_extraction
    data_key_value_pairs = []
    doc_data ={}
    while True:
        key = input("Enter key (or 'done' to finish): ")
        if key.lower() == 'done' or key.lower()=="":
            break
        value = input("Enter value: ")
        data_x = create_dict_from_string(key, value)
        doc_data.update(data_x)
        # data_key_value_pairs.append((key, value))

    # Original collection JSON
    with open(original_json_path, "r") as file:
        original_collection_json = json.load(file)

    # Generate modified data for ucp_ae_sd_1_LC and ucp_ae_sd_1_DATA
    lc_data = generate_request_data_lc(lc_no_input, lc_data)
    data_data = generate_request_data_data(lc_no_input, doc_class_input, doc_data)
    print(lc_data)
    exit('+++++++++++++++++')
    # Modify the collection JSON with the new data
    modified_collection_json = modify_collection(original_collection_json, lc_data, data_data)

    # Save the modified collection JSON to a new file
    with open("modified_collection.json", "w") as file:
        json.dump(modified_collection_json, file, indent=2)

    print("Modified collection JSON generated and saved as 'modified_collection.json'")

    # Extract rule_id from lc_data
    rule_id = lc_data["data"]["rule_id"]

    # Execute curl command
    execute_curl_command(rule_id)
    print(f'Curl command executed for rule_id: {rule_id}')
