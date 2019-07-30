import time
import os
import subprocess
from subprocess import call

h264_ext = -5
debug = True
data_dir = os.getcwd()

def convert(path_to_data):
    # move into data dir
    os.chdir(path_to_data)

    for file_name in os.listdir(path_to_data):
        # we want to check if the file is an .mp4 or h264 and convert if needed
        if ".h264" in file_name:
            # now we convert this file to .mp4
            f = file_name[:h264_ext]
            if debug: print("about to convert %s.h264 to %s.mp4") % (f, f)
            # now use bash to convert files
            return_val = call(["MP4Box", "-add", (f+".h264"), (f+".mp4")])
            # check bash cmd return val to see if it worked
            if return_val == 0:
                # conversion was successful!
                if debug: print("Conversion Successful!")
            else:
                if debug: print("Conversion %s Failed!") % file_name
                    
        elif ".mp4" in file_name:
            # if it has a .mp4 ext
            if debug: print("Previosuly converted file: %s") % file_name

        else:
            if debug: print("Unsupported file type: %s") % file_name

    # go back to previous dir
    if debug: print("inside data dir %s") % os.getcwd()
    os.chdir("../../")
    if debug: print("after os.chdir() dir %s") % os.getcwd()

def main():
    if debug: print("transforming videos from .h264 >> .mp4")
    # convert front camera videos
    convert(data_dir+"/tag_data/front")
    # convert back camera videos
    convert(data_dir+"/tag_data/back")
    
    
if __name__== "__main__":
    main()