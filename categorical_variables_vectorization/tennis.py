import pandas as pd

dados = {
    "Dia": ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "D11", "D12", "D13", "D14"],
    "Aspecto": ["Sol", "Sol", "Nuvens", "Chuva", "Chuva", "Chuva", "Nuvens", "Sol", "Fresco", "Chuva", "Sol", "Nuvens", "Nuvens", "Chuva"],
    "Temperatura": ["Quente", "Quente", "Quente", "Ameno", "Fresco", "Fresco", "Fresco", "Ameno", "Fresco", "Ameno", "Ameno", "Ameno", "Quente", "Ameno"],
    "Umidade": ["Elevada", "Elevada", "Elevada", "Elevada", "Normal", "Normal", "Normal", "Elevada", "Normal", "Normal", "Normal", "Elevada", "Normal", "Elevada"],
    "Vento": ["Fraco", "Forte", "Fraco", "Fraco", "Fraco", "Forte", "Fraco", "Fraco", "Fraco", "Fraco", "Forte", "Forte", "Fraco", "Forte"],
    "Jogar_Tenis": ["Não", "Não", "Sim", "Sim", "Sim", "Não", "Sim", "Não", "Sim", "Sim", "Sim", "Sim", "Sim", "Não"]
}

df = pd.DataFrame(dados)