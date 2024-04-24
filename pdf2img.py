from pdf2image import convert_from_path
import sys
 
 
# Store Pdf with convert_from_path function

if __name__ == "__main__":
    args = sys.argv
    print(args)
    src = args[1]
    dest = None
    print(len(args))
    if len(args)>2:
        dest = args[2]
    images = convert_from_path(src)
 
    for i in range(len(images)):
      # Save pages as images in the pdf
        if dest is  None:
            dest = src.rsplit(".",1)[0]
        print(src)
        print(dest)
        images[i].save(dest+"_" +str(i+1) +'.png', 'PNG')


