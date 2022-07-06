imagem = open("imagem.png", "rb")
data = imagem.read()
imagem.close()

imagem = open("imagem_copia.png", "wb")
imagem.write(data)
imagem.close()
