from PIL import Image
import os

# Ouvrir l'image
image = Image.open("camel.jpg") #pk il ne retrouve pas l'image camel.jpg??

# Récupérer les données Exif
exif_data = image._getexif()

# Vérifier si les données Exif sont présentes
if exif_data:
    print("L'image contient des données Exif.")
else:
    print("L'image ne contient pas de données Exif.")