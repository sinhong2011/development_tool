import sys,time,cv2
from os import listdir, getcwd, mkdir
from os.path import isfile, isdir
print(cv2.__version__)

def extractImages(pathIn, pathOut):
    print("Processing %s" % (pathIn))
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    vidfps = vidcap.get(cv2.CAP_PROP_FPS)
    video_length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT)/vidfps)
    # print("video: ",video_length*30)
    success,image = vidcap.read()
    success = True
    while success:
        if count <= video_length:
            vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))    # added this line 
            success,image = vidcap.read()
            cv2.imwrite( pathOut + "/frame%d.jpg" % count, image)     # save frame as JPEG file
        
            #print("【Progress: %.2f%%】" %  (float(count/(video_length))*100) + '\r')
            sys.stdout.write("【Progress: %.2f%%】" %  (float(count/(video_length))*100) + '\r')
            sys.stdout.flush()
            count = count + 1
        else:
            break
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
        elif f.endswith(".py"):
            pass
        else: 
            print("%s is not support."% (f))