from PIL import Image
import os
import PIL
import glob

filename = 'Logo_Android.png'

image = Image.open(filename)
parentDirectory = os.path.abspath(os.path.dirname(__file__)) + "/../android/app/src/"


sizes = {
    "main" : {
        "appstore.png" : (1024, 1024),
        "ic_playstore.png" : (512, 512), ##Change this to the playstore PNG Name
        "playstore.png" : (512, 512)
    },
    "main/res/mipmap-hdpi": {
        "ic_launcher_foreground.png": (162, 162),
        "ic_launcher_round.png": (72, 72),
        "ic_launcher.png": (72, 72)
    },
    "main/res/mipmap-mdpi": {
        "ic_launcher_foreground.png": (108, 108),
        "ic_launcher_round.png": (48, 48),
        "ic_launcher.png": (48, 48)
    },
    "main/res/mipmap-xhdpi": {
        "ic_launcher_foreground.png": (216, 216),
        "ic_launcher_round.png": (96, 96),
        "ic_launcher.png": (96, 96)
    },
    "main/res/mipmap-xxhdpi": {
        "ic_launcher_foreground.png": (324, 324),
        "ic_launcher_round.png": (144, 144),
        "ic_launcher.png": (144, 144)
    },
    "main/res/mipmap-xxxhdpi": {
        "ic_launcher_foreground.png": (432, 432),
        "ic_launcher_round.png": (192, 192),
        "ic_launcher.png": (192, 192)
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

