from PIL import Image
import pillow_heif
import cv2
import numpy as np
import face_recognition
import time

import sys
import os


# --------------- Format Aligning: 
# .heic and .heif (usual by Apple) are not accepted by OpenCV, 
# thats why check - and transform to .jpg

# THE FUNCTION DEALS WITH IMAGES IN PERSON'S FOLDER
def align_format (folder_content, full_path):
 for pic in folder_content:
    if pic.lower().endswith((".heic", ".heif")):
     
     path_pic = os.path.join(full_path, pic)
     heif_pic= pillow_heif.open_heif(path_pic)

     image = Image.frombytes(heif_pic.mode, heif_pic.size, heif_pic.data)
     image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

     # save the .heic as .png, delete the old one 
     new_name = os.path.splitext(pic)[0] + ".jpg"
     new_path = os.path.join(full_path, new_name)
     cv2.imwrite(new_path, image_cv)
     os.remove(path_pic)
    elif pic.lower().endswith(".ds_store"): # ignore git .ds_store
       os.remove(os.path.join(full_path, pic))


def downsample(folder_content, full_path):

    # ----------- DOWNSAMPLING THE PICTURES
    # separate loop just for debugging reasons
   
    for pic in folder_content:
        #print(f"pic {pic} start")  
        
        path_pic = os.path.join(full_path, pic)
        image = cv2.imread(path_pic)
        h, w = image.shape [:2]
        #print( h,w)

        if min(h,w) > 1000:
            #print(f"Downsampling the image {pic}")
            downsample_factor = 1000/min(h,w)
            new_h, new_w = int(h*downsample_factor), int(w*downsample_factor)
            new_image = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_LINEAR)
            cv2.imwrite(path_pic, new_image)
    

# -------------- Face Recognition
    # "pic" ist just the name of the picture
def recognize_face (folder_content, participant_folder, item):   

    # create an output folder 
    output_folder = os.path.join (participant_folder, item + "_output")
    os.makedirs(output_folder, exist_ok=True)
   
    

    for i, pic in enumerate(folder_content):
        #print (f"Picture {pic} processing...")

        full_path = os.path.join(participant_folder,item, pic)
       
        image = cv2.imread(full_path)
        
        face = face_recognition.face_locations(image, model="cnn")
        #print(f"Gesichtserkennung abgeschlossen. {len(face)} Gesichter gefunden.")

        # HIER AM BESTEN IN DEBUG FILE SCHREIBEN!!!!!!!!!!!!!!
        if not face:
            print(f"Picture {pic} muss manuell verarbeitet werden!")
        
        
        # Jedes erkannte Gesicht ausschneiden und skalieren
        for (top, right, bottom, left) in face:
            h, w, _ = image.shape
            
            # Abstand um 20% vergrößern
            padding = int((bottom - top) * 0.3)  

            top = max(0, top - padding)
            bottom = min(h, bottom + padding)
            left = max(0, left - padding)
            right = min(w, right + padding)

            face = image[top:bottom, left:right]
            face_resized = cv2.resize(face, (400, 400), interpolation=cv2.INTER_LINEAR)
            #print (os.path.join(output_folder, pic))
            new_name = f"{item}_{i}.jpg"
            cv2.imwrite(os.path.join(output_folder, new_name), face_resized)
        

        
    




def main():
    print("la-la-la")


    
   
if __name__ == "__main__":
    main()
