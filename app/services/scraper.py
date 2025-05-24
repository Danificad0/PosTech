import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO


def get_table_from_url(url: str) -> pd.DataFrame:
    """
    Faz scraping da tabela principal da página especificada.
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Erro ao acessar {url}: Status {response.status_code}")

    soup = BeautifulSoup(response.content, "html.parser")
    tabela = soup.find("table", {"class": "tb_base tb_dados"})

    if tabela is None:
        raise Exception("Nenhuma tabela encontrada na página.")

    df = pd.read_html(StringIO(str(tabela)), decimal=",", thousands=".")[0]

    return df


# 🔗 URLs de cada aba
URLS = {
    "producao": "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02",
    "processamento": "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03",
    "comercializacao": "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04",
    "importacao": "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05",
    "exportacao": "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06"
}


def get_data(tipo: str) -> pd.DataFrame:
    """
    Pega os dados da aba especificada.
    """
    if tipo not in URLS:
        raise ValueError(f"Tipo inválido: {tipo}")
    url = URLS[tipo]
    return get_table_from_url(url)
