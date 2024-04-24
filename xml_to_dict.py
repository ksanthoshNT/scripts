import json
import os
import xml.etree.ElementTree as ET

def xml_to_dict(xml_path:str):
    result = {"word_coordinates": []}
    with open(xml_path,'r') as f:
        xml = f.read().strip()
    root = ET.fromstring(xml)
    namespace = {'ns': 'http://www.abbyy.com/FineReader_xml/FineReader10-schema-v1.xml'}

    for text_elem in root.findall('.//ns:text', namespace):
        for line_elem in text_elem.findall('.//ns:line', namespace):
            for formatting_elem in line_elem.findall('.//ns:formatting', namespace):
                word = formatting_elem.text.strip()
                left = int(line_elem.get('l'))
                top = int(line_elem.get('t'))
                width = int(line_elem.get('r')) - left
                height = int(line_elem.get('b')) - top
                x1 = left
                y1 = top
                x2 = left + width
                y2 = top + height

                word_data = {
                    "word": word,
                    "left": left,
                    "top": top,
                    "width": width,
                    "height": height,
                    "x1": x1,
                    "y1": y1,
                    "x2": x2,
                    "y2": y2
                }

                result["word_coordinates"].append(word_data)

    # with open("json_output.json",'w') as f:
    #     json.dump(result,f,indent=4)
    return result
if __name__ == "__main__":
    xml_content = "/home/ntlpt59/Downloads/Bill_of_lading_24_page_0.xml"
    os.makedirs("xml_to_dict_100",exist_ok=True)
    for f in os.listdir("abbey_ocr_xml"):
        result = xml_to_dict(os.path.join('abbey_ocr_xml',f))
        with open(f"xml_to_dict_100/{f[:-4]}.json",'w') as f:
            json.dump(result,f,indent=4)


