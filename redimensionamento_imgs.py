from PIL import Image
import os

pasta_origem= r"C:\Users\Acer\Downloads\data_origem" 
pasta_final= r"c:\Users\Acer\Downloads\data_final"

for img in os.listdir(pasta_origem):
    caminho= os.path.join(pasta_origem,img)
    imagem=Image.open(caminho)
    imagem_redimensionada=imagem.resize((225,225))
    caminho_final=os.path.join(pasta_final,img)
    imagem_redimensionada.save(caminho_final)

