
import tkinter as tk
from tkinter import filedialog

import os


def process_folder (path, pics_ending):
   if if_pics_in_folder (path, pics_ending):
    rename_pictures (path, pics_ending)
   

def if_pics_in_folder (path, pics_ending):

    # if at least one picture found - directly return True and break
    return any(
        datei.lower().endswith(pics_ending)
        for datei in os.listdir(path)
        if os.path.isfile(os.path.join(path, datei))  
    )
    


def rename_pictures (path, pics_ending):
    folder_content = os.listdir(path) 
    folder_name = os.path.basename(path)

    print(f'------------------ FOLDER "{folder_name}" ------------------')
    name = input(f'PLEASE TIPP A NEW NAME FOR PICS IN "{folder_name}": '+"\n"+ 
                         "For example, 'person1' " + "\n" +
                         "The pics would then be renamed to 'person1_1', 'person1_2' " + "\n"+ 
                         'Enter the name without "  " ' + "\n"+ "\n" )
    print(f'Renaming pics to "{name}_n" ...')

    i = 0
    for item in folder_content:
     full_path = os.path.join(path, item)
     if os.path.isfile(full_path) and item.lower().endswith(pics_ending):
       extension = os.path.splitext(item)[1]
       os.rename(full_path, os.path.join(path, f"{name}_{i}{extension}"))
       i += 1



def main():
   
    root = tk.Tk()
    root.withdraw()

    participant_folder = filedialog.askdirectory(title="Please choose the participant Folder")
    root.destroy()
    print (participant_folder)
    
    pics_ending = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.heic', '.heif', '.cr2', '.raw')

    # if the folder itself has pictures inside
    process_folder (participant_folder, pics_ending)
     

    # if unterordner vorhanden
    for item in os.listdir(participant_folder):
        full_path = os.path.join(participant_folder, item)
        if os.path.isdir(full_path):
            print(f"📁 Gefundener Unterordner: {item}")
            process_folder (full_path, pics_ending)
       



if __name__ == "__main__":
    main()