# Python script to batch generate QR codes with 
# a url and sequential numbers
#
# Will generate a code for
# https://www.roots.uk/qr/001
# https://www.roots.uk/qr/002
# and so on.
#
#
# Written by Steve Root, https://www.steveroot.co.uk
# 
# Instructions:
#
# Copy this script into a new directory,
# I called it python-batch-qr-generator-script.py
#
# It uses https://pypi.org/project/qrcode/ which
# can be installed by:
#   pip install qrcode
# 
# Update the while loop to how many codes you
# want to generate and the url you want all 
# codes to start with
#
# To run the script;
# python3 python-batch-qr-generator-script.py


#How many codes do you want to generate?
gen = 5
#Enter the start of the URL
starturl = "https://www.roots.uk/qr/"


import qrcode


# to generate the last code, we need to incriment by 1
gen = gen + 1

i = 1
while i < gen:
    #pad the integer to 3 digits with leading zeros
    padi = f'{i:03}'
    #built the url from starturl and the current number
    url = starturl + "{}".format(padi)
    #create the image with qrcode
    img = qrcode.make(url)
    type(img) # qrcode.image.pil.PilImage
    #set a filename for the image
    filename = "{}.png".format(padi)
    #save the image
    img.save(filename)
    #increment the loop id
    i += 1
