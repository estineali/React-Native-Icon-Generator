# Using the icon Generator 

## Tl;dr
0. Place these **in a folder** in the root directory of your React Native project 
1. Put the picture for Android and/or iOS
2. Rename the picture `Logo_Android.png` or `Logo_iOS.png`
2. Run the script for Android/iOS `python3 iconGeneratorAndroid.py` or `python3 iconGeneratoriOS.py`
3. Everything else is taken care of. 

### For Android 

Since android manages the masking of icons to round icons and otherwise itself, the icons need to have extra padding. Therefore the parent file for android icons is `Logo_Android.png`. The script bellow only depends on this file. 

To generate icons for android, open a terminal window in this folder and run `python3 iconGeneratorAndroid.py`

All files will be generated and placed in the right folder.


### For iOS 

The logo for iOS must not have any transparency. Curved edges are generated automatically. Therefore the parent file for iOS is a sharp square with no transparency (alpha channel) called `Logo_iOS.png`. The script bellow only depends on this file. 

To generate icons for iOS, open a terminal window in this folder and run `python3 iconGeneratoriOS.py`. 

All files will be generated and placed in the right folder. 


####  In the event that doesn't work: 

1. Make sure you have PIL installed for python. 
2. Make sure the right way to invoke python for your system is `python3`. It could just be `python`. 