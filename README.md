# image-resizer-microservice
Microservice to resize images.

IMAGE RESIZER
Microservice to resize images

deployed at: https://image-resizer-microservice.herokuapp.com/


Request Parameters:
img: [required] image to be resized (base64 string)
width: desired width in pixels
height: desired height in pixels


You must specify either a width or height in the request parameters.
If width is specified & height is not: returns img with specified width; height is calculated to preserve aspect ratio.
If height is specified & width is not: returns img with specified height; width is calculated to preserve aspect ratio.
If both width & height are specified: returns largest possible img (not to exceed specified dimensions) that preserves aspect ratio.


Response:
base64: resized image (base64 string)
