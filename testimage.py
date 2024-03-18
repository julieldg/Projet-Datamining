from PIL import Image
import os

#afficher les noms des images du dossier images
dossier_images = "C:\\Users\\vpica\\Documents\\CLBD S1\\Data Mining\\Projet-Datamining\\images"
for i in os.listdir(dossier_images):
    image_path = os.path.join(dossier_images, i)
    print(image_path)
    image = Image.open(image_path)
    exif_data = image._getexif()
    if exif_data:
        print("L'image contient des données Exif.")
    else:
        print("L'image ne contient pas de données Exif.")

