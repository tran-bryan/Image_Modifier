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

TODO List: 
* Make user input to tell program how many processes to use at a time for parallel processing. 
* Make function that creates an image for specific composite colors: Cyan, Magenta, Yellow, Orange, Hot Pink, Lime, Cyan-Lime, Purple, Sky-Blue. 