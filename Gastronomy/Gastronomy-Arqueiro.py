# Importando as bibliotecas necessárias
from bs4 import BeautifulSoup # Biblioteca para fazer o parsing do HTML
from datetime import date # Biblioteca para obter a data atual
import json # Biblioteca para trabalhar com JSON
import requests # Biblioteca para fazer requests HTTP
import os # Biblioteca para manipular o sistema de arquivos do sistema operacional

# Função para salvar os highscores do mês em um arquivo JSON
def save_monthly_highscores(output):
    today = date.today() # Obtém a data atual
    directory_name = today.strftime('%Y-%m-%d') # Cria o nome do diretório a partir da data atual
    if not os.path.exists(directory_name): # Verifica se o diretório já existe
        os.mkdir(directory_name) # Se não existir, cria o diretório
    file_name = 'Gastronomy-Arqueiro-' + today.strftime('%Y-%m') + '.json' # Cria o nome do arquivo a partir da data atual
    file_path = os.path.join(directory_name, file_name) # Cria o caminho completo do arquivo
    with open(file_path, 'w', encoding='utf-8') as json_file: # Abre o arquivo em modo de escrita
        json.dump(output, json_file, indent=4, ensure_ascii=False) # Salva os dados no arquivo no formato JSON

# URL da página com os highscores
page = 'https://www.bloodstoneonline.com/pt/pontuacao/'

output = [] # Lista para armazenar os dados dos highscores
counter = 1 # Contador para numerar os registros

# Loop entre todos os servidores
for world in range(1, 6):
    
    # Dados para enviar no POST request
    data = {'server': world,
            'vocation': '5', # 0 = Todas, 1 = Cavaleiro, 2 = Bárbaro, 3 = Mago, 4 = Xamã, 5 = Arqueiro
            'category': '16', # 0 = Experiência, 1 = Skill Ataque, 2 = Skill Escudo, 3 = Arena, 4 = Mineração, 5 = Forja
            'submit': 'Filtrar'}
    
    # Fazendo o POST request na URL
    r = requests.post(url = page, data = data)

    # Parsing do HTML da página
    page_source = BeautifulSoup(r.content, 'html.parser') # Código fonte da página
    highscore = page_source.find_all('td') # Buscando todos os resultados com a tag <td> no código fonte
    
    # Mapeamento de servidores
    if world == 1:
        server = 'Onix'
    elif world == 2:
        server = 'Ruby'
    elif world == 3:
        server = 'Jasper'

    # Loop entre todos os <td> encontrados.
    # O loop é feito com passo 6 pois cada personagem possui 6 colunas de conteúdo
    for i in range(0, len(highscore), 6):
        # Adicionando os dados dos highscores à lista de output
        output.append({'id': counter, 'name': highscore[i + 1].text, 'vocation': highscore[i + 2].text, 'level': int(highscore[i + 4].text), 'experience': int(highscore[i + 5].text), 'server': server})
        counter += 1

# Chamando a função para salvar os highscores do mês em um arquivo JSON
save_monthly_highscores(output)



categoryType = {'Todas': 0, 'Cavaleiro': 1, 'Bárbaro': 2, 'Mago': 3, 'Xamã': 4, 'Arqueiro': 5}

