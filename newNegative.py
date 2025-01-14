import numpy as np
from pathlib import Path
import cv2 
from multiprocessing import Pool
import time

#Function: Creates negative image of the input image 
#Math: Negative color channel value = 255 - original color channel value 
def makeNegative(row):
    #Takes in a row of the image and iterate through the columns
    for i in range(len(row)):
        #Takes in the row AND column (pixel at (row,col)) of the image and iterate through the channels of the pixel 
        for j in range(3):
            #At each color channel in the pixel, replace original value with the negative value 
            #Negative value = 255 - Original value
            row[i][j] = 255 - row[i][j]
    return row

#Function: Creates greyscale image of the input image 
#Math: grey color channel value = the average of all the values in each color channel of pixel 
def makeGrey(row): 
    #Takes in a row of the image and iterate through the columns
    for i in range(len(row)): 
        #Grey value = average of all color channels at the pixel at (row, col)
        greyNum = np.average(row[i])
        #Takes in the row AND column (pixel at (row,col)) of the image and iterate through the channels of the pixel 
        for j in range(3):
            #At each color channel in the pixel, replace original value with the grey value 
            row[i][j] = int(greyNum)
    return row

#Function(s) only[Color]: Redirection functions that calls func onlyChannel to target specific channel
def onlyRed(row): 
    return onlyChannel(2, row) 
def onlyGreen(row): 
    return onlyChannel(1, row) 
def onlyBlue(row): 
    return onlyChannel(0, row) 

#Function: Creates [specific color]-scale image of the input image 
#           only a single channel (from RGB) will show up in the image, others are greyed out 
#Math: grey color channel value = the average of all the values in each color channel of pixel 
def onlyChannel(num, row):
    #Takes in a row of the image and iterate through the columns
    for i in range(len(row)): 
        #Grey value = average of all color channels at the pixel at (row, col)
        greyNum = np.average(row[i])
        #Takes in the row AND column (pixel at (row,col)) of the image and iterate through the channels of the pixel 
        for j in range(3): 
            if j == num: 
                #If the color channel is the targeted channel (num): 
                #       if the color is less than the grey val, it becomes the grey value
                #       otherwise it keeps the original value
                row[i][j] = row[i][j] if row[i][j] > int(greyNum) else int(greyNum)
            else: 
                #Else (color channel is not the targeted channel [num]): 
                #       it becomes the grey value
                row[i][j] = int(greyNum)
    return row 

#Function(s) no[Color]: Redirection functions that calls func noChannel to target specific channel
def noRed(row): 
    return noChannel(2, row) 
def noGreen(row): 
    return noChannel(1, row) 
def noBlue(row): 
    return noChannel(0, row) 

#Function: Creates image without targetted color of the input image 
#           only a single channel (from RGB) will be greyed out, others will show up in the image 
#Math: grey color channel value = the average of all the values in each color channel of pixel 
def noChannel(num, row): 
    #Takes in a row of the image and iterate through the columns 
    for i in range(len(row)): 
        #Grey value = average of all color channels at the pixel at (row, col)
        greyNum = np.average(row[i])
        #Takes in the row AND column (pixel at (row,col)) of the image and iterate through the channels of the pixel 
        for j in range(3): 
            if j == num: 
                #If the color channel is the targeted channel (num): 
                #       it becomes the grey value
                row[i][j] = int(greyNum)
            else: 
                #Else (color channel is not the targeted channel [num]): 
                #       if the color is less than the grey val, it becomes the grey value
                #       otherwise it keeps the original value
                row[i][j] = row[i][j] if row[i][j] > int(greyNum) else int(greyNum)
    return row

#TODO
#Functions for composite colors (not exclusion)
#Cyan, Magenta, Yellow: 
#       Excluded = Grey
#       Composite = Average of Non-excluded 
#                   compositeNum = (np.sum(row[i]) - row[i][num]) / 2 
#Full/Halves (Orange, Hot Pink, Lime, Cyan-Lime, Purple, Sky-Blue):
#       Excluded = Grey
#       Half = 1/3 of the total of Non-Excluded
#       Full = 2/3 of the total of Non-Excluded

#Dictionary of integers to strings that will be used for output file names
colorWords = {
    0 : "_negative", 
    1 : "_grey",
    2 : "_red", 
    3 : "_green", 
    4 : "_blue", 
    5 : "_no_red", 
    6 : "_no_green", 
    7 : "_no_blue" 
}

#Dictionary of integers to functions that will be used for image modification 
colorFuncs = {
    0 : makeNegative, 
    1 : makeGrey,
    2 : onlyRed, 
    3 : onlyGreen, 
    4 : onlyBlue, 
    5 : noRed, 
    6 : noGreen, 
    7 : noBlue 
}

png = ".png"
file_req = "Enter the name of the .png file (without the file type): "
choice_req = "Enter your choice (in numbers) of image modification: "
input_failed = "User input does not exist to the program, please try again " 

#Function: Takes in user input to get the image file for image modification
def requestFile(project_directory): 
    #notWorking represents failure of user input thus need to repeat query
    notWorking = True 
    #Intial return value settings
    inputImage = None
    inputName = None
    #Keep querying user until input is valid
    while(notWorking): 
        #Takes in user input of the file name
        inputName = input(file_req)
        #Combine inputName to get the actual file name
        inputFile = inputName + png
        #Gets the full path to the inputfile
        inputPath = project_directory / inputFile 
        #Attempts to read the inputFile in the inputPath
        inputImage = cv2.imread(inputPath) 
        #If read succeeds, we are able to get out of the loop 
        #Else: notify user that input failed
        if np.any(inputImage): notWorking = False
        else: print(input_failed)
    return inputName, inputImage

#Function: Takes in user input to select the image modification choice onto the image file
def requestChoice():
    #notWorking represents failure of user input thus need to repeat query
    notWorking = True
    #Intial return value settings
    inputChoice = None
    #Keep querying user until input is valid
    while(notWorking): 
        #Takes in user input for the modification choice
        inputChoice = input(choice_req)
        #Checks if user input is in available list of image modification
        if int(inputChoice) not in colorWords: 
            #If input is not in colorWords: notify user that input failed
            print(input_failed)
        else: 
            #Else: we are able to get out of the loop 
            notWorking = False
    return int(inputChoice)
            
if __name__ == '__main__':
    #Gets the path/directory that contains this code file
    projDir = Path(__file__).parent
    #Calls requestFile to get user file input
    inputName, inputImage = requestFile(projDir)
    #Calls requestChoice to get user image modification input
    inputChoice = requestChoice()

    #Starts timer
    start_time = round(time.time(), 2) 
    #Creates name of the outputFile 
    outputFile = inputName + colorWords[inputChoice] + png
    #Makes the location where outputFile is in 
    #   (puts outputFile in same directory as this code file)
    outputPath = projDir / outputFile
    
    #Starts parallel processing for faster image modification processing
    #Number of processes depends on user's number of cores on computer
    #EX: Author's computer has 10 cores thus processes=10
    #TODO: Make user input for dynamic processes/core to use
    pool = Pool(processes=10)
    #In parallel process, calls chosen image modification function onto the rows of each image. 
    #Each process takes on 1 row at a time. 
    outputImage = pool.map(colorFuncs[inputChoice], inputImage)
    pool.close

    #Reformats the outputImage from List to np.array for proper image creation 
    outputImage = np.array(outputImage)
    #Writes the outputImage and puts it in the same directory as this code file)
    cv2.imwrite(outputPath, outputImage)
    #Ends Timer 
    end_time = round(time.time(), 2)
    #Notify user how long program has taken
    print("Time elapsed for program is: ", end_time - start_time, " seconds")