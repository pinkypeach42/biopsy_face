from face_detection import align_format

import tkinter as tk
from tkinter import filedialog
import cv2
import os

# participant_folder  - PATH of participant Folder
# folder_content - ARRAY with all Data in Participant folder (NOT A PATH!)


def main():
   
    root = tk.Tk()
    root.withdraw()

    participant_folder = filedialog.askdirectory(title="Wähle ein Probanden-Verzeichnis aus")

    print("Chosen folder:", participant_folder)

    # ARRAY with all Data (folders, pictures), NOT A PATH ANYMORE!
    folder_content = os.listdir(participant_folder) 
    print (folder_content)

# PROCESSING OF SEPARATE FOLDERS (mom, dad etc.) in Participant Folder
    for item in folder_content:
        full_path = os.path.join(participant_folder, item)
        if os.path.isdir(full_path):
        
         print (f'Folder "{item}" found: {full_path}')
         images = os.listdir(full_path)

         align_format (images, full_path) #must be resaved!

        #print(images) #test the content of the folder


if __name__ == "__main__":
    main()