import tkinter as tk
from tkinter import filedialog
import cv2
import os

root = tk.Tk()
root.withdraw()

folder = filedialog.askdirectory(title="Wähle ein Probanden-Verzeichnis aus")

print("Chosen folder:", folder)



content = os.listdir(folder)
