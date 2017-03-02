library(pixmap)
secretencoder <- function(imgfilename,msg,startpix,stride,consec=NULL){
# encodes the secret message into an image
# Returns a 'pixmapGrey' object
	image <- read.pnm(imgfilename)
}

secretdecoder <- function(imgfilename, startpix, stride, consec=NULL){
# Returns the decoded message string
}