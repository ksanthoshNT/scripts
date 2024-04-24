import base64
import json
import sys
from io import BytesIO
from typing import Optional, Dict

import uvicorn
from PIL import Image
from pydantic import BaseModel

from struct_doc_keys_wise import informat_structed_doc
from test_classify_key_word_based import get_ocr_vision_api_charConfi
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


class Params(BaseModel):
    GvKey : Optional[Dict] = {}
    ImageBase64: Optional[str]= None
@app.post('/gv_ocr/')
def ocr_extract(request:Params):
    image_b64 = request.ImageBase64
    gvkey = request.GvKey
    if not gvkey:
        key_path = {
            "type": "service_account",
            "project_id": "digital-hall-399509",
            "private_key_id": "b093a49b9d246e1877d5079e8a6d5cead60ec8fc",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDraPQxYW+S1KNL\n9fOXjHKbZeZXRRYt0YSm0QFoLb7PT2l++MWPxYf2JPrrqR5gQeXAn4FADBDpIgl4\n5yQ8C+d7fP/NINT50wSwTn9Hy+vGuZ3GooyVWFrpdD0DyZM/Osqjn5BX+gHsATRp\n6xSbDWHQOL7hinCpie3q5fFiAVGyAqMsiF6ODWLyWRpvTrVMLuORNFlTZbyjwQWr\ngVyxroloPki0W+xE77zEvadcHzPqzwrGLABWLAFeMGwtrgbwpzFA94ansxFd4GSC\nCXYDxmO1lA0yRTtSU4IHl6YKAIaKCsREYhJdN7xL0jzq6d7IuaZbCKyeeIZq/uVb\nJrJD7AClAgMBAAECggEAFHHWhCb5Dvb020CxvNX5RBuHwC+Ju0WPFpyTQAF53CMc\nJedXSeLqKaUd8UAl5hucmp7se9JjpTBydloYqjbC2u78GX9CKXo7b4M5uzoJSlNN\n63Wr7b9KxSvcerFtRNhtx30XOgf5iVrnbh8SkihWeBEQxTsforgnl51yjV23XLuC\nqiUXAjhMKFqWlM/W1atdRgU7l+mse78klbwPaeGocigfR7tPugvboLzLn8ofLqsJ\n0sQfQag/YW458hwTNm7tGAuBUyIj20Vq7JvoUTdislknRio6rYl03DF1rSUxGvO8\n4BcELZQh3sXGdRE1I2azg39uQ5w+RwV7JC8328iqdwKBgQD1nC2Gxjl4jjlZalO2\n+rTmOMWs6+lqPzUqcPFMQ6RBjqfmugP7dc/E7xdX6dDo8pyT3gYiX8xL1yKWNfOD\nW0aYs9V/18epLkChurAo+LlC8ZxLdLvS3xr5euV9aEsfswYvJLmncgkAlJoVgvei\nHGLNmumO8kG28s2nmO2J6aRy0wKBgQD1XlCLic7DHBXoIdLieN478jl7a+B/G9ar\nxOvdu8fxFAKwAw01HBduty0Y0llr7yay3KwLMWcLE4YZNA5rRcvhUnfsCiiKjZRM\n/DbbFPgAWBBZgg//YQfAKZGKze/KIqezwbxUrEM+1IeBwo44PO1x8d+8JUMwWUWh\nn9gVrFzjpwKBgFKCJMkhziyxmpJvJbBSiHLOn5l3pvIKSdH4Hxd/oa5kPgNEehH/\ngcymhTEDWyrmVbNW4ripdfgETZoohaWbBBxITXClDG3JG+04yfT5mULj551xmac9\nS9KDdpSqdJIxkeJEdBnMNTn8scaIOKg84PQxFkTvHSRYbL3goeuykYwBAoGBALhn\nx5T3XwNXykcJlJpMSIk5BGZzrucYnv+9IZ8lj6DpbxOlV3nAwQOeezAadsYdmDH4\nkvxehpjWdYPfka6haBbRiftFry5iNUCelQOWAMURakg67Zb6735GP3HYUAzUesEo\nK0hfprJDvAuTkptFfxaRt5qJTrO5hBFyNk4jmjQlAoGBANe4QWx/cM0RWPsHoHDT\nRvR74XZe7FmFOv9sidSCnFqs6I76huUPvw6PlcxQJOkNH8Cz0z40wrSg8mzMGTOx\n+LuGgTj+tjk/oFL0q/2R7uLBapTYxF0nQMto7FERx5t+9aJ8xsuyWUJBZ9M19pJZ\nArSDdUW8UIYYQ0TUJTdKX/6t\n-----END PRIVATE KEY-----\n",
            "client_email": "vision-api-nt@digital-hall-399509.iam.gserviceaccount.com",
            "client_id": "113848533319767176201",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/vision-api-nt%40digital-hall-399509.iam.gserviceaccount.com",
            "universe_domain": "googleapis.com"
        }
    else:
        key_path = gvkey
    with open('gv_key.json', 'w') as f:
        json.dump(key_path, f)
    image = base64.b64decode(image_b64)
    coordinates, all_text = get_ocr_vision_api_charConfi(image,KEY_PATH = 'gv_key.json')
    ocr_coords = informat_structed_doc(coordinates)
    response = {'coordinates':ocr_coords, 'text':all_text}
    return JSONResponse(content= response)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

