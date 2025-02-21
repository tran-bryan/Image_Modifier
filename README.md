# Image_Modifier
Summary: Takes in an image file inputted by user and then creates an output image file of the input file with a specific color modification. Uses parallel processing to quicken image modification. 

Notes: 
* Default Color Model is RGB. 
* Default input and output file type is ".png". 
* Default parallel processing is set to use 10 processes at once. 

List of modifications: 
* Create a negative of the image. 
* Create a greyscale of the image. 
* Create a red/green/blue (choose one) -scale of the image. 
* Create an image without red/green/blue (choose one). 
* Create a full/full composite (Cyan, Magenta, Yellow) - scale of the image. 
* Create a full/half composite (Orange, Hot Pink, Lime, Cyan-Lime, Purple, Sky-Blue) - scale of the image. 
* Create an image that has each pixel only show the highest value channel while other channels are 0 (black)
* Create an image that has each pixel only show the highest value channel while other channels are grey-value (average of channel values)

Instructions: 
1. After executing command, a request for file name input appears. 
2. On successful input for file, a request for choice of image modification appears. 
3. On successful input for choise, program proccess the image to output the modified image. 
4. Output image by default will be placed in the same folder/directory as program/code file. 