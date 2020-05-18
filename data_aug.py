from PIL import Image 
from PIL import ImageFilter 
import os 
  
def main(): 
    # path of the folder containing the raw images 
    inPath ="/media/shivam-gupta/SHIVAM/images"
  
    # path of the folder that will contain the modified image 
    outPath ="/media/shivam-gupta/SHIVAM/images"


    count = 0
    for folderPath in os.listdir(inPath):
        inputPath = os.path.join(inPath, folderPath)

        for imagePath in os.listdir(inputPath): 
            # imagePath contains name of the image
             
            fullPath = os.path.join(inputPath, imagePath)

            img = Image.open(fullPath) 
  
            fullOutPath = os.path.join(inputPath, 'invert_'+imagePath) 
            # fullOutPath contains the path of the output 
            # image that needs to be generated 
            img.rotate(45).save(fullOutPath) 
      
            print(fullOutPath)  


  
# Driver Function 
if __name__ == '__main__': 
    main()