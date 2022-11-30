from PIL import Image
import os
import PIL
import glob

filename = 'Logo_iOS.png'

image = Image.open(filename)
parentDirectory = os.path.abspath(os.path.dirname(__file__)) + "/../ios/APP_NAME_HERE/Images.xcassets/"


sizes = {
    "AppIcon.appiconset" : {
        "ItunesArtwork@2x.png" : (1024, 1024),
        "App-Icon-20x20@1x.png" : (20, 20),
        "App-Icon-20x20@2x.png" : (40, 40),
        "App-Icon-20x20@3x.png" : (60, 60),
        "App-Icon-29x29@1x.png" : (29, 29),
        "App-Icon-29x29@2x.png" : (58, 58),
        "App-Icon-29x29@3x.png" : (87, 87),
        "App-Icon-40x40@1x.png" : (40, 40),
        "App-Icon-40x40@2x.png" : (80, 80),
        "App-Icon-40x40@3x.png" : (120, 120),
        "App-Icon-60x60@2x.png" : (120, 120),
        "App-Icon-60x60@3x.png" : (180, 180),
        "App-Icon-76x76@1x.png" : (76, 76),
        "App-Icon-76x76@2x.png" : (152, 152),
        "App-Icon-83.5x83.5@2x.png" : (167, 167)
    }
}

for folder in sizes:
    newDirectory = parentDirectory + folder + "/"
    
    if not os.path.exists(newDirectory):
        os.mkdir(newDirectory)

    for size in sizes[folder]:
        newfileName = newDirectory + size
        if not os.path.exists(newfileName):
            image.resize(sizes[folder][size]).save(newfileName)
        else:
            os.remove(newfileName)
            image.resize(sizes[folder][size]).save(newfileName)

