import os
from tqdm import tqdm

# listar todos os diretórios no diretório atual
diretorios = [diretorio for diretorio in os.listdir() if os.path.isdir(diretorio)]

# ordene os diretórios alfabeticamente
diretorios.sort()

# loop através de cada diretório e executar os scripts Python dentro deles
for diretorio in diretorios:
    # mudar para o diretório atual
    os.chdir(diretorio)
    print('Executando scripts no diretório: ', os.getcwd())
    
    # listar todos os arquivos no diretório atual com a extensão .py
    arquivos_py = [arquivo for arquivo in os.listdir() if arquivo.endswith('.py')]
    
    # ordene os arquivos alfabeticamente
    arquivos_py.sort()
    
    # execute cada arquivo em ordem
    for arquivo in tqdm(arquivos_py, desc="Executando scripts", unit=" script", leave=False):
        os.system('python3 {}'.format(arquivo))
        tqdm.write(arquivo)
        
    # voltar para o diretório anterior
    os.chdir('..')

