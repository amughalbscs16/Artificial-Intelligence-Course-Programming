from PIL import Image
import numpy as np
import cv2 as cv
import math
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

def findCentres(cells):
    centres = [[0,0] for i in range(64)]
    for i in range(0,len(cells)):
        for x in range(cells[i][0],cells[i][1]+1): #left
            centres[i][0] += x;
        for y in range(cells[i][2],cells[i][3]+1):        
            centres[i][1] += y;
        
        centres[i][0] = int(centres[i][0]/(cells[i][1]-cells[i][0]))
        centres[i][1] = int(centres[i][1]/(cells[i][3]-cells[i][2]))
    return centres

def findAngleofIncline(centres,cells):
    angles = [0.00]*64
    for i in range(0,len(cells)):
        perp = cells[i][3] - centres[i][1]
        base = centres[i][0] - cells[i][0]
        angles[i] = math.atan( (perp * 1.0) / base )
    return angles;
    
def main():
    image = readImage();

    #read cells left,right,top,bottom
    cells = readCells()
    print("\n\ncells: ",cells)
    #sizes and cells height and width
    sizes, cellsHW = calcHeightWidthSize(cells)
    print("sizes:",sizes,end="\n\n\n")

    #number of black count
    blackCount = countBlack(image, cells)
    print("blackCount:", blackCount,end="\n\n\n")
    
    #ratio of black with total size
    blackRatio = [ (bSize[0] * 1.0) / bSize[1] for bSize in zip(blackCount, sizes)]
    
    print("Black ratio:", blackRatio,end="\n\n\n")
    centres = findCentres(cells)

    print("centres: ", centres,end="\n\n\n")
    angles = findAngleofIncline(centres,cells)
    print("angles:", angles,end="\n\n\n")
    
       
if __name__ == "__main__":
    main()
