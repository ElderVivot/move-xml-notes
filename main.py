import json
import os
from src.process import ProcessXmls

dataJson = {}
with open('configuracoes.json', 'r', encoding='utf-8') as f:
    dataJson = json.load(f)

ProcessXmls(dataJson['pasta_xml'], dataJson['somente_arquivo_que_contenha'], dataJson['pasta_substituir_nome']).process()

os.system('pause')
