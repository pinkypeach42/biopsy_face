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
pictures = os.listdir("input")
print(f"Pics: {pictures}")

output_folder = "output"

# --------------- Format Aligning: 
# .heic and .heif (usual by Apple) are not accepted by OpenCV, 
# thats why check - and transform to .jpg
for pic in pictures:
    if pic.lower().endswith((".heic", ".heif")):
     
     full_path = os.path.join("input", pic)
     heif_pic= pillow_heif.open_heif(full_path)

     image = Image.frombytes(heif_pic.mode, heif_pic.size, heif_pic.data)
     image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

     # save the .heic as .png, delete the old one 
     new_name = os.path.splitext(pic)[0] + ".jpg"
     new_path = os.path.join("input", new_name)
     cv2.imwrite(new_path, image_cv)
     os.remove(full_path)

pictures = os.listdir("input")
print(f"Pics: {pictures}")


# -------------- Face Recognition
# "pic" ist just the name of the picture
for i, pic in enumerate(pictures):
     print (f"Picture {pic} processing...")

     full_path = os.path.join("input", pic)
     image = cv2.imread(full_path)
     
     start = time.time()
     face = face_recognition.face_locations(image, model="cnn")
     print(f"Gesichtserkennung abgeschlossen. {len(face)} Gesichter gefunden.")

     # HIER AM BESTEN IN DEBUG FILE SCHREIBEN!!!!!!!!!!!!!!
     if not face:
        print(f"Picture {pic} muss manuell verarbeitet werden!")

     ende = time.time()
     print(f"Gesichtserkennng Time: {ende - start:.4f} seconds")
     
     start = time.time()
     
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

      cv2.imwrite(os.path.join(output_folder, pic), face_resized)
      print(f"Gesicht {i} gespeichert mit vergrößertem Bereich.")

      ende = time.time()
      print(f"Ausschneiden Time: {ende - start:.4f} seconds")
      
   


