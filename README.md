# Image_Modifier
Summary: Takes in an image file inputted by user and then creates an output image file of the input file with a specific color modification. Uses parallel processing to quicken image modification. 

Notes: 
* Only works for RGB files. 
* Currently will only output .png files. 
* Currently parallel processing is set to use 10 processes at once. 

List of modifications: 
* Create a negative of the image. 
* Create a greyscale of the image. 
* Create a red/green/blue (choose one) -scale of the image. 
* Create an image without red/green/blue (choose one). 
* Create a full/full composite (Cyan, Magenta, Yellow) - scale of the image. 
* Create a full/half composite (Orange, Hot Pink, Lime, Cyan-Lime, Purple, Sky-Blue) - scale of the image. 
* Create an image that has each pixel only show the highest value channel while other channels are 0 (black)
* Create an image that has each pixel only show the highest value channel while other channels are grey-value (average of channel values)

TODO List: 
* Make user input to tell program how many processes to use at a time for parallel processing. 