import cv2
import sys
import matplotlib.pyplot as plt


if __name__ == "__main__":
    img_path = sys.argv[1]
    x1 = int(sys.argv[2])
    y1 = int(sys.argv[3])
    x2 = int(sys.argv[4])
    y2 = int(sys.argv[5])
    print(f"x1,y1,x2,y2:{x1},{y1},{x2},{y2}")
    img = cv2.imread(img_path)
    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
    cv2.imwrite("output.png",img)
        
    #plt.imshow(img)
    #plt.show()
