# 🧠 Biopsy Face Extraction 🧠 


### **PLEASE READ THIS CAREFULLY**

Last version (29.03.2025):
- DOES NOT recognize the same person over images!
- so, if processing an image with SEVERAL faces, ALL the faces on the image will be saved to "x_output"-Folder
- you need to delete the pictures with other person faces from output-Folder manually or just use the pictures with only one face!

**Workflow:**
1. please install as listed in "Step 1: Installation"
2. run the main.py

**If you use pictures with several faces:**

When finished runnung the main.py:

(3.) delete the unnecessary images manually!

4. To rename the pictures run module "rename.py" (for details see "Step 4: Rename" below)


### **PREPARE:**

You should have the Participant Folder with following structure (the names are not important:
```bash
ParticipantName
--- Pics_1_person
------ pictures_person1.jpg
------ pictures_person1.png
--- Pics_2_person
etc.
```

---

## Step 1: Installation (Recommended) 

### 1. Clone the Repository (old-school download of main branch is also ok :) )

```bash
git clone https://github.com/pinkypeach42/biopsy_face.git
cd biopsy_face
```

### 2. Check your Python Version

```bash
python3.12 --version
```

if not installed, get it!

### 3. Create a venv (for macOS)

```bash
python3.12 -m venv biopsy_face
source biopsy_face/bin/activate
```

### 4. Install the required packages

```bash
pip install -r requirements.txt
```

### 5. RUNNING THE MAIN.PY

When running the main.py please choose in poping-up-window the Participant Folder!

## Step 4: if you want to rename the pictures (rename.py)

Imagine having Participant Folder "ParticipantName" with following structure:
```bash
ParticipantName
--- Marie
------ IMG91.jpg
------ marie1.png
--- Johnatan
------ j123.jpg
------ weqweq.png
```

Choose the main folder "ParticipantName"

You will be asked to give a name for pictures in the folders:

```bash
------------------ FOLDER "Marie" ------------------
PLEASE TIPP A NEW NAME FOR PICS IN "Marie": 
For example, 'person1' 
The pics would then be renamed to 'person1_1', 'person1_2' 
Enter the name without "  "
```

For example you entered "face1", then the pictures in "Marie" Folder will be renamed as:
```bash
ParticipantName
--- Marie
------ face1_0.jpg
------ face1_1.png
--- Johnatan
------ j123.jpg
------ weqweq.png
```

Then the same question will be asked for other folders (e.g. Johnatan). 

If you want to rename the pictures just in one folder, you can choose it from the beginning

---

Tested on **Python 3.12** under macOS Sequoia
