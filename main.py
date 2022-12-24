# Operation: runs in ".reserved" of the master dir of the usb
# When ran, this script will backup the contents of the usb to the backup folder
import os
from shutil import make_archive
import init

# CONST BACKUP_DIR
# Get desktop path
BACKUP_DIR = os.environ['USERPROFILE'] + "\\OneDrive\\Desktop\\" # I'm using OneDrive as my backup folder
# Get the disk master dir
master_dir = os.getcwd().split(".reserved")[0] + "\\store\\"
# Get the id of the usb
id = init.id()
# Get the name of the backup folder
backup_loc = BACKUP_DIR + id + "_TG"
print(backup_loc)
# If the backup folder doesn't exist, create it
if not os.path.exists(backup_loc):
    os.mkdir(backup_loc)
    os.mkdir(backup_loc + "\\data")
    os.mkdir(backup_loc + "\\.backup")
else:
    # Store previous backup in zip file
    if not os.path.exists(backup_loc + "//.backup"):
        os.mkdir(backup_loc + "//.backup")
# Zip the backup folder
make_archive(backup_loc + "\\.backup\\", "zip", backup_loc + "\\data")
# Delete everything in the backup\\data folder
os.system("del /s /q " + backup_loc + "\\data")
# Copy everything from the master dir to the backup\\data folder
os.system("xcopy /s /e /y " + master_dir + " " + backup_loc + "\\data")
