import csv
import re
from telethon.sync import TelegramClient
from telethon.tl.types import MessageEntityUrl
import pyautogui
import time
import webbrowser
import asyncio



# Substitua os valores abaixo com suas próprias credenciais do Telegram
api_id = 'coloqye sua api_id'
api_hash = 'coloque sua apiHash'
phone_number = 'coloque aqui seu telefone'


# Crie um novo cliente Telegram
client = TelegramClient('session_name', api_id, api_hash)

# Substitua os valores abaixo com suas próprias credenciais do


async def main():
    # Conecte-se ao Telegram
    await client.start()
    group_id = -'coloque o id do grupo'


    # Expressão regular para encontrar links
    link_regex = r'https?://www\.(coloqueaqui o prefixo)\.\S+'

    # Lista para armazenar os links únicos
    unique_links = set()

    # Pegue as últimas 10 mensagens do grupo
    async for message in client.iter_messages(group_id, limit=8):
        # Verifica se a mensagem contém texto
        if hasattr(message, 'text') and message.text:
            # Encontre todos os links no texto da mensagem que começam com "www.seubet."
            links_encontrados = re.findall(link_regex, message.text)
            # Adicione os links únicos à lista
            for link in links_encontrados:
                unique_links.add(link)

    # Verifique se os links já existem no arquivo CSV antes de salvá-los
    existing_links = set()
    try:
        with open('links.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row:  # Verifica se a linha não está vazia
                    existing_links.add(row[0])
    except FileNotFoundError:
        pass

    # Adicione os links únicos ao arquivo CSV e use o Selenium para abrir os links no Firefox
    with open('links.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for link in unique_links:
            if link not in existing_links:
                writer.writerow([link])
                # Configure o WebDriver do Firefox
                webbrowser.open(link)
                time.sleep(10)
                pyautogui.click(x=986, y=715) # configurado para monitor fullhd com a tela cheia, caso mude a resolução devera mudar o x e y
                time.sleep(5)
                pyautogui.hotkey('1') #coloque o valor desejado
                time.sleep(1)
                pyautogui.hotkey('enter')
async def run_periodically(): #caso queira rodar apenas uma vez delete essa parte do codigo e deixe apenas o codigo loop principal 2
    while True:
        await main()
        await asyncio.sleep(60)  # Espera 60 segundos antes de rodar novamente

# Execute o loop principal
asyncio.run(run_periodically())




# Execute o loop principal 2 
#with client:
#    client.loop.run_until_complete(main())