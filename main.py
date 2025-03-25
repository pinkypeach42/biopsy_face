from face_detection import align_format, downsample, recognize_face

import tkinter as tk
from tkinter import filedialog
import os
import time

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
        
         #print (f'Folder "{item}" found: {full_path}') #debug
         pictures_of_person = os.listdir(full_path)

         start = time.time()   
        # Apple has .heic .heif format that cannot be proccessed with cv
        # this funktion translates every .heic (if there are any) into .jpg
         align_format (pictures_of_person, full_path) 
         pictures_of_person = os.listdir(full_path)

         print(f'Downsampling Folder "{item}" ...')
         downsample(pictures_of_person, full_path)
         recognize_face (pictures_of_person, participant_folder, item)
         ende = time.time() 
         print (f"Processing {ende - start} seconds")


        #print(images) #test the content of the folder


if __name__ == "__main__":
    main()