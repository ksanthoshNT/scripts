from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from PIL import Image, ImageDraw

app = FastAPI()



def draw_rectangle_on_image(image_path, coordinates):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    
    for coord in coordinates:
        x1, y1 = coord[0]
        x2, y2 = coord[1]
        draw.rectangle([x1, y1, x2, y2], outline="red", width=2)
    
    image.show()

@app.post('/structuredDocumentExtraction')
def structured_document_extraction(data: FormInput):
    try:
        form_name = data.formName
        form_image = data.formImage
        coordinates = data.coordinates

        # Assuming you have a function to get the image path based on form name
        image_path = get_image_path(form_name)

        draw_rectangle_on_image(image_path, coordinates)

        return {'message': 'Rectangle drawn successfully.'}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_image_path(form_name):
    # Implement logic to map form_name to the actual image path
    # Example: return "/home/ntlpt59/MAIN/TF_FINAL_TESTING/struct_docs/data_used/Export-Bill_filled_sample0.jpg"
    pass

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8088, log_level="info")
