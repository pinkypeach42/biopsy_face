# 🧠 Biopsy Face Extraction 🧠 


**PLEASE READ THIS CAREFULLY**

Last version (29.03.2025):
- DOES NOT recognize the same person over images!
- so, if processing an image with SEVERAL faces, ALL the faces on the image will be saved to "x_output"-Folder
- you need to delete the pictures with other person faces from output-Folder manually or just use the pictures with only one face!

**Workflow:**
1. please install as listed in "Step 1: Installation"
2. run the main.py

**IF YOU USED PICTURES WITH SEVERAL FACES:**

When finished runnung the main.py:

(3.) delete the unnecessary images manually!

4. To rename the pictures run module "rename.py" (for details see "Step 4: Rename" below)
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

## Step 4: Rename the pictures

---

Tested on **Python 3.12** under macOS Sequoia
