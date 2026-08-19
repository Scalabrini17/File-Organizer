import os 
import random
import string
import shutil
from  pathlib import Path

print('Inicinado o Script de Organização de Arquivos \n')
# Script para buscar o nome da pasta onde o arquivo .py está rondando (nesse caso 'Organizador_de_arquivos')
diretorio_projeto = os.path.dirname(os.path.abspath(__file__))
print(f'Diretório do projeto encontrado, nome do diretório principal é: {diretorio_projeto} \n')

# criando as subpastas dentro da própria pasta onde o script está rodando
print('Iniciando a Criação de Pastas e Subpastas \n')
pasta_principal = diretorio_projeto
subpastas = ['pasta_txt', 'pasta_pdf', 'pasta_jpeg', 'pasta_png', 'pasta_docx', 'pasta_csv', 'pasta_mp3', 'pasta_mp4']

# for para poder criar as subpastas para a separação dos arquivos por extensão
for sub in subpastas:
    # variavel que recebe a pasta principal e as subpastas 
    caminho = os.path.join(pasta_principal, sub)
    # Script com a biblioteca os para a criação da pasta com o makedirs e usando exist_ok = True para não para a execução
    os.makedirs(caminho, exist_ok = True)
    print(f'Criando {sub}... ')

# Organizando os arquivos 
print('\nIniciando a Organização dos Arquivos\n')
origem = Path(pasta_principal)
destinos = {
    '.txt': Path(pasta_principal) / 'pasta_txt',
    '.pdf': Path(pasta_principal) / 'pasta_pdf',
    '.jpeg': Path(pasta_principal) / 'pasta_jpeg',
    '.png': Path(pasta_principal) / 'pasta_png',
    '.docx': Path(pasta_principal) / 'pasta_docx',
    '.csv': Path(pasta_principal) / 'pasta_csv',
    '.mp3': Path(pasta_principal) / 'pasta_mp3',
    '.mp4': Path(pasta_principal) / 'pasta_mp4',
}

# Loop para percorrer os arquivos 
for arquivo in origem.iterdir():
    if arquivo.is_file():
        # Essa variavel é responsavel por pegar a extensão do arquivo 
        extc = arquivo.suffix.lower()

        if extc in destinos:
            pasta_destino = destinos[extc]
            shutil.move(str(arquivo), str(pasta_destino/ arquivo.name))

            print(f'O arquivo: {arquivo.name} foi adicionado a pasta: {pasta_destino.name}')