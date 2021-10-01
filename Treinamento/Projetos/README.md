<h1 align="center">
Compressor de Imagens
</h1>

## Configuração
Para desenvolver este projeto, é necessário utilizar a biblioteca do Python para trabalhar com imagens, a Pillow. Para instalar esta biblioteca no windows, basta utilizar o **pip**, com a seguinte linha de comando no terminal:
```shell
pip install Pillow
```
Esta é a única configuração neecssária para darmos início. Mas recomendamos a leitura da documentação da biblioteca para entender as funções que utilizaremos, tanto da **Pillow** quanto do módulo **os** que utilizaremos para trabalhar com o sistema operacional e na construção dos caminhos.

## Codificação
### Importação dos Módulos
Para iniciar, precisamos importar nossas duas bibliotecas. No caso da **Pillow** trabalharemos apenas com o modulo **Image**, para fazermos as configurações necessárias. Assim vamos importar ambas:
```python
import os
from PIL import Image
```
### Verificando se é uma imagem
A primeira coisa que precisamos é verificar se os arquivos no diretório são imagens. Logo, na primeira função vamos verificar se a extensão dos arquivos são PNG e JPG, se forem retornamos verdadeiro, senão retornamos falso.
```python
def eh_imagem(nome_arquivo):                                                            
    if nome_arquivo.endswith('png') or nome_arquivo.endswith('jpg'):
        return True
    else:
        return False
```
### Comprimindo e movendo as imagens
Com isso, o que precisamos agora é fazer a compressão das imagens e move-las para o novo diretório. Nesta função, por tratar das questões de caminhos nos arquivos, vamos trabalhar linha por linha.
Na declaração precisamos receber um diretório de origem e um diretório de destino. Além disso vamos passar também a extensão JPG como default para obtermos uma compressão ainda maior.
```python
def reduzir_imagens(input_dir, output_dir, ext='.jpg'):
```
Em seguida precisamos captar todos os arquivos do diretório, armazenando-os numa lista apenas se forem imagens. E isso pode ser feito pelo  recurso de **list comprehension (compressão de lista)** do python.
```python
lista_de_arquivos = [nome for nome in os.listdir(input_dir) if eh_imagem(nome)]
```
Agora vamos percorrer todas as imagens da lista, pegando seu comando completo. E além disso precisamos converter de PNG pra JPG, logo precisamos eliminar o fator alpha, assim passaremos de RGBA para RGB.
```python
for nome in lista_de_arquivos:
        imagem = Image.open(os.path.join(input_dir, nome)).convert('RGB')
````
Em seguida, vamos fazer a compressão reduzindo o tamanho das imagens para o formato 1280X720. O método resize cria uma cópia da imagem original, logo a imagem original ainda permanecerá no diretório origem.
```python
redimensionada = imagem.resize((1280, 720))
```
Para fazer a conversão de PNG para JPG, podemos separar o nome da sua extensão usando a função **splittext()** do módulo **os**. Como esta função retorna uma lista, pegaremos a primeira posição da lista, que se trata do nome do arquivo.
```python
nome_sem_ext = os.path.splitext(nome)[0]
```
E por fim enviaremos a cópia para o diretório destino juntando a extensão JPG ao seu nome.
```python
redimensionada.save(os.path.join(output_dir, nome_sem_ext + ext))
```
Com isso temos um compressor de imagens. Resta enfatizar que dependendo da proporção da imagem original podem existir deformações na imagem de saída.

