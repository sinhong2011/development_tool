import sys,cv2
from os import listdir, getcwd, mkdir
from os.path import isfile, isdir
print(cv2.__version__)

def extractImages(pathIn, pathOut):
    print("Processing %s" % (pathIn))
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
      vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))    # added this line 
      success,image = vidcap.read()
      print ('Read a new frame: ', count)
      cv2.imwrite( pathOut + "/frame%d.jpg" % count, image)     # save frame as JPEG file
      count = count + 1
    print("The %s had output to %s\n" % (pathIn,pathOut))

if __name__=="__main__":

    e = '.mp4'
    for f in listdir(getcwd()):
        if f.endswith(e):
            output = f.replace(e,"")+"_output"
            if not isdir(output):
                mkdir(output)
            extractImages(f, output)
print("Done!")