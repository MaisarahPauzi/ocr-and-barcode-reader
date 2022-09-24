# Importing library
import cv2
from pyzbar.pyzbar import decode
import pytesseract
from pytesseract import Output

# Make one method to decode the barcode
def BarcodeReader(image):
     
    # read the image in numpy array using cv2
    img = cv2.imread(image)

    # read texts
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    n_boxes = len(d['text'])
      
    # Decode the barcode image
    detectedBarcodes = decode(img)
      
    # If not detected then print the message
    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:

      # detect texts
      for i in range(n_boxes):
            if int(d['conf'][i]) > 60:
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
       
      # Traverse through all the detected barcodes in image
      for barcode in detectedBarcodes: 
           
            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect
             
            # Put the rectangle in image using
            # cv2 to heighlight the barcode
            cv2.rectangle(img, (x-10, y-10),
                          (x + w+10, y + h+10),
                          (255, 0, 0), 2)
             
                 
    #Display the image
    # cv2.resizeWindow("Image", 300, 700)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
if __name__ == "__main__":
  # Take the image from user
    image="sample.jpg"
    BarcodeReader(image)