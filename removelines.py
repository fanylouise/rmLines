import re

def remover_linhas_com_timestamp(texto):
    # Expressão regular para encontrar o padrão de timestamp
    padrao = r'\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}'
    
    # Dividindo o texto em linhas
    linhas = texto.splitlines()
    
    # Filtrando as linhas que não contêm o padrão de timestamp
    linhas_filtradas = [linha for linha in linhas if not re.search(padrao, linha)]
    
    # Unindo as linhas filtradas de volta em um único texto
    texto_filtrado = "\n".join(linhas_filtradas)
    
    return texto_filtrado

    texto =
    """
    """
    
