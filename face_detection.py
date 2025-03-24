from PIL import Image
import pillow_heif
import cv2
import numpy as np
import face_recognition
import time

import sys
import os

# ------------- Just to know the environment
print("Benutzte Python-Version:", sys.version)
print("Python-Pfad:", sys.executable)


# --------------- read images from input folder + define the output folder
pictures = os.listdir("image")
print(f"Pics: {pictures}")

output = "output_image"

# --------------- Format Aligning: 
# .heic and .heif are not accepted by OpenCV, thats why check - and transform to .jpg
for i in range (len(pictures)):
    if pictures[i].lower().endswith((".heic", ".heif")):
     
     full_path = os.path.join("image", pictures[i])
     heif_pic= pillow_heif.open_heif(full_path)

     image = Image.frombytes(heif_pic.mode, heif_pic.size, heif_pic.data)
     image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

     # save the .heic as .png, delete the old one 
     new_name = os.path.splitext(pictures[i])[0] + ".jpg"
     new_path = os.path.join("image", new_name)
     cv2.imwrite(new_path, image_cv)
     os.remove(full_path)


     '''face = face_recognition.face_locations(image_cv, model="cnn")
     print(f"Gesichtserkennung abgeschlossen. {len(face)} Gesichter gefunden.")

     if not face:
        print(f"Picture {pictures[i]:s} muss manuell verarbeitet werden!")

     
     start = time.time()
     
     # Jedes erkannte Gesicht ausschneiden und skalieren
     for i, (top, right, bottom, left) in face:
      h, w, _ = image_cv.shape
    
      # Abstand um 20% vergrößern
      padding = int((bottom - top) * 0.3)  

      top = max(0, top - padding)
      bottom = min(h, bottom + padding)
      left = max(0, left - padding)
      right = min(w, right + padding)

      face = image_cv[top:bottom, left:right]
      face_resized = cv2.resize(face, (400, 400), interpolation=cv2.INTER_LINEAR)

      cv2.imwrite(f"gesichtus_{i}.jpg", face_resized)
      print(f"Gesicht {i} gespeichert mit vergrößertem Bereich.")

      ende = time.time()
      print(f"Time: {ende - start:.4f} seconds")'
      '''
   

    else:
       continue
      #sys.exit(0) 


pictures = os.listdir("image")
print(f"Pics: {pictures}")