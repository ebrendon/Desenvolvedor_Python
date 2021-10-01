import os                                                                               #Importação do módulo os para poder trabalhar no sistema operacional
from PIL import Image                                                                   #Importação do módulo Pillow para trabalhar com imagens


def eh_imagem(nome_arquivo):                                                            #Função para verificar se o arquivo no diretório é uma imagem
    if nome_arquivo.endswith('png') or nome_arquivo.endswith('jpg'):
        return True
    else:
        return False


def reduzir_imagens(input_dir, output_dir, ext='.jpg'):                                 #Função para fazer a compressão das imagens recebendo um diretório origem e um diretório destino
    lista_de_arquivos = [nome for nome in os.listdir(input_dir) if eh_imagem(nome)]     #Lista a partir da lista inicial que só será considerada se for uma imagem 
    for nome in lista_de_arquivos:
        imagem = Image.open(os.path.join(input_dir, nome)).convert('RGB')               #Utilizando a função Image.open para abrir a imagem no diretório e convertendo de RGBA para RGB
        redimensionada = imagem.resize((1280, 720))                                     #Criando uma cópia redimensionada para as proporções 1280X720
        nome_sem_ext = os.path.splitext(nome)[0]                                        #Separando o nome do arquivo da extensão para poder converter de PNG para JPG
        redimensionada.save(os.path.join(output_dir, nome_sem_ext + ext))               #Salvando a cópia no diretório destino


if __name__ == "__main__":
    diretorio = '/Users/ebren/Pictures/entrada'                                         #Declarando o diretório de origem
    output = '/Users/ebren/Pictures/saída/'                                             #declarando o diretório destino
    reduzir_imagens(diretorio, output)
