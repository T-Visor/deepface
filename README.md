# Batch Face Recognition

Uses the Deepface library in Python to support batch facial recognition. Top-K accuracy is used to evaluate facial recognition performance.

## Installation

```bash
pip3 install -r requirements.txt
```

## Server Environment

```
conda activate deepface
```

## Usage

```bash
$ python3 run.py                                                                                 
usage: run.py [-h] -s SOURCE_DIRECTORY -d DATABASE_PATH -k K_VALUE -o OUTPUT_FILE

options:
  -h, --help            show this help message and exit
  -s SOURCE_DIRECTORY, --source_directory SOURCE_DIRECTORY
                        Directory with images of people to identify.
  -d DATABASE_PATH, --database_path DATABASE_PATH
                        Dataset of images containing known faces.
  -k K_VALUE, --k_value K_VALUE
                        Determines the value used for Top-K Accuracy.
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Output file to write accuracy results to (Ex. "output.txt")

```

## Sample Output

```
-------------------------------
TOP 5 ACCURACY
-------------------------------

1.
=============================================
source image: George_Clooney_40143._attacked.png
predicted: ['Ian_Holm', 'J.K._Simmons', 'Christopher_Lloyd', 'J.K._Simmons', 'Chazz_Palminteri'] 
true label: George_Clooney
Result: INCORRECT
=============================================

2.
=============================================
source image: George_Clooney_39923._attacked.png
predicted: ['Hugh_Jackman', 'Eric_Dane', 'Gerard_Butler', 'Freddy_Rodríguez', 'Billy_Boyd'] 
true label: George_Clooney
Result: INCORRECT
=============================================

3.
=============================================
source image: George_Clooney_40211._attacked.png
predicted: ['Jeremy_Irons', 'Bradley_Cooper', 'Christian_Bale', 'J.K._Simmons', 'George_Clooney'] 
true label: George_Clooney
Result: CORRECT
=============================================

Accuracy: 1/3 (33%)
```
