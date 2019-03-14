from PIL import Image
import numpy as np
import cv2 as cv

def readImage():
    
    image = cv.imread("IMG.jpg")
    greyScaleArray = np.dot(image,[0.07,0.72,0.21])
    greyScaleArray[greyScaleArray > 127] = 255
    greyScaleArray[greyScaleArray <= 127] = 0

    image=Image.fromarray(greyScaleArray)
    #image.show()
    
    return greyScaleArray
def readCells():
    #reading file and converting to integer using map
    cells = [list(map(int, line.rstrip('\n').split(","))) for line in open("cellsinformation.txt","r")]
    return cells
    
def calcHeightWidthSize(cells):
    cellsHW = [[cell[3]-cell[2],cell[1]-cell[0]] for cell in cells]
    sizes = [hw[0]*hw[1] for hw in cellsHW]
    #print(sizes)
    return sizes, cellsHW;

def countBlack(image,cells):
    blackCount = [0 for i in range(0,64)]
    
    for i in range(0,len(cells)):
        for x in range(cells[i][0],cells[i][1]+1): #left
            for y in range(cells[i][2],cells[i][3]+1):
                if image[x,y] == 0:
                    blackCount[i]+=1;
    #print(blackCount)           
    return blackCount;

def main():
    image = readImage();

    #read cells left,right,top,bottom
    cells = readCells()

    #sizes and cells height and width
    sizes, cellsHW = calcHeightWidthSize(cells)

    #number of black count
    blackCount = countBlack(image, cells)
    
    #ratio of black with total size
    blackRatio = [ (bSize[0] * 1.0) / bSize[1] for bSize in zip(blackCount, sizes)]
    #print(blackRatio)
        
if __name__ == "__main__":
    main()
