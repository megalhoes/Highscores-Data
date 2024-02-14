import re
import os
import shutil

def corrigir_lista(match):
    try:
        lista = eval(match.group(0))
        nova_lista = [f"{{\"DATA\": \"{key}\", \"XP\": {value}}}" for key, value in lista.items()]
        return ',\n'.join(nova_lista)
    except Exception as e:
        raise RuntimeError(f"Erro ao processar a lista: {e}")

def adicionar_virgula(match):
    dicionario = match.group(0)
    if dicionario[-1] != ',':
        return dicionario[:-1] + ',]'
    return dicionario

def corrigir_arquivo(arquivo_path):
    with open(arquivo_path, 'r') as file:
        content = file.read()

    # Adicionando uma vírgula ao final de cada ocorrência de dicionário, se necessário
    pattern_virgula = re.compile(r'\{[^}]*\}(?!\s*])')
    content = re.sub(pattern_virgula, adicionar_virgula, content)

    # Usando uma expressão regular para encontrar listas de dicionários no formato anterior
    pattern_lista = re.compile(r'\{[^}]*\}')
    novo_conteudo = re.sub(pattern_lista, corrigir_lista, content)

    with open(arquivo_path, 'w') as file:
        file.write(novo_conteudo)

    print(f"Correções aplicadas com sucesso no arquivo: {arquivo_path}")

def corrigir_todos_arquivos():
    diretorio = "Data"

    for filename in os.listdir(diretorio):
        if filename.endswith(".py"):
            arquivo_path = os.path.join(diretorio, filename)
            corrigir_arquivo(arquivo_path)

if __name__ == "__main__":
    corrigir_todos_arquivos()
