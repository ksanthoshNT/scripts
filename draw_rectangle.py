import cv2
import sys
import matplotlib.pyplot as plt


def parse_arg(arg):
    if isinstance(arg,list):
        return [int(_.translate(str.maketrans('', '', ',[{}]'))) for _ in arg ]
    return int(arg.translate(str.maketrans('', '', ',[{}]')))

if __name__ == "__main__":
    print(sys.argv)
    img_path = sys.argv[1]
    x1,y1,x2,y2 = parse_arg([sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]])
    print(f"x1,y1,x2,y2:{x1},{y1},{x2},{y2}")
    img = cv2.imread(img_path)
    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
    cv2.imwrite("output.png",img)
