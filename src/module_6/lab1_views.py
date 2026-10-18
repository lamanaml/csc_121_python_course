import csv
import numpy as np
from PIL import Image

def main():
   with open("views.csv", "r", encoding="utf-8") as views, open ("analysis.csv", "w",  encoding="utf-8") as analysis:
       reader = csv.DictReader(views)
       writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
       writer.writeheader()
       
       for row in reader:
           row["brightness"] = calculate_brightness(f"{row['id']}.jpeg")
           writer.writerow(row)
    
    
def calculate_brightness (filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness

main()                           