import os
from PIL import Image
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\fqcancado\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Defina o caminho da pasta que contém as imagens
pasta_imagens = r'C:\Users\fqcancado\Downloads\loja'

# Dicionário para mapear meses por extenso para seus números
meses = {
    'Janeiro': '01',
    'Fevereiro': '02',
    'Março': '03',
    'Abril': '04',
    'Maio': '05',
    'Junho': '06',
    'Julho': '07',
    'Agosto': '08',
    'Setembro': '09',
    'Outubro': '10',
    'Novembro': '11',
    'Dezembro': '12'
}

# Variáveis para armazenar resultados
datas_incorretas = []
contador_incorretas = 0

# Listar todos os arquivos na pasta
for nome_arquivo in os.listdir(pasta_imagens):
    if nome_arquivo.endswith('.jpg'):
        # Montar o caminho completo do arquivo
        imagem_path = os.path.join(pasta_imagens, nome_arquivo)
        
        # Carregar a imagem
        imagem = Image.open(imagem_path)

        # Usar pytesseract para extrair texto
        texto = pytesseract.image_to_string(imagem)

        # Mostrar o texto extraído
        #print(f"\nTexto extraído da imagem {nome_arquivo}:")
        #print(texto)

        # Extrair mês e ano do nome do arquivo
        mes_ano = nome_arquivo.replace('Loja - ', '').replace('.jpg', '')
        mes, ano = mes_ano.split(' - ')

        # Verificar as datas no texto extraído
        data_pattern = r'(\d{2}/\d{2}/\d{4})'  # Padrão para buscar a data no formato DD/MM/AAAA
        datas_encontradas = re.findall(data_pattern, texto)

        mes_numero = meses.get(mes)

        for data in datas_encontradas:  
            dia, mes_data, ano_data = data.split('/')
            if mes_data == mes_numero and ano_data == ano:
                print(f"A data {data} no texto corresponde ao mês e ano do arquivo: {mes} - {ano}")
            else:
                print(f"A data {data} no texto NÃO corresponde ao mês e ano do arquivo: {mes} - {ano}")
                # Armazenar a data incorreta
                datas_incorretas.append(data)
                contador_incorretas += 1

# Exibir resultados finais
print(f"\nTotal de datas incorretas encontradas: {contador_incorretas}")
if contador_incorretas > 0:
    print("Datas incorretas:")
    for data in datas_incorretas:
        print(data)
