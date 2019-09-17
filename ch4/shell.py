#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
  # make a duplicate of an existing file
  fileName = "textfile.txt"

  if path.exists(fileName):
    # get the path to the file in the current directory
    src = path.realpath(fileName)
        
    # # let's make a backup copy by appending "bak" to the name
    dst = src + ".bak"
    # # now use the shell to make a copy of the file
    shutil.copy(src,dst)
    
    # # copy over the permissions, modification times, and other info
    shutil.copystat(src, dst)
    
    # # rename the original file
    fileName2 = "newfile.txt"
    os.rename(fileName, fileName2)
        
     
    # now put things into a ZIP archive
    root_dir,tail = path.split(src)
    shutil.make_archive("archive", "zip", root_dir)

    # more fine-grained control over ZIP files
    with ZipFile("testzip.zip","w") as newzip:
      newzip.write("newfile.txt")
      newzip.write("textfile.txt.bak")

    print("Reverting back the backup copy.")
    shutil.copy(dst, src)
    shutil.copystat(dst, src)

if __name__ == "__main__":
  main()
