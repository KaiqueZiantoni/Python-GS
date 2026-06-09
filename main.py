# ====================================================================
# GLOBAL SOLUTION - COMPUTATIONAL THINKING USING PYTHON
# Projeto: AstroPharma - Inteligência Espacial Preditiva B2B
# Aluno: Kaique Ziantoni Guedes Rosa (RM 570294) - Turma: 1TDSPV
# ====================================================================

def exibir_descricao():
    """
    Exibe a descrição do projeto. Limitado a no máximo 5 linhas.
    Sem parâmetros e sem retorno.
    """
    print("\n--- SOBRE O ASTROPHARMA ---")
    print("O AstroPharma cruza dados de microclima espacial e demografia")
    print("para calcular a 'Janela Biológica' de adoecimento da população.")
    print("O sistema atua de forma preditiva, alertando farmácias de 8 a 15")
    print("dias antes do pico de demanda para evitar ruptura de gôndola.")
    print("---------------------------\n")

def registrar_anomalia(dados_climaticos):
    """
    Cadastra um alerta climático microrregional no sistema.
    Usa if-elif-else para definir a classe do medicamento (ATC) sugerido.
    Parâmetro: dados_climaticos (list)
    """
    print("\n--- INGESTÃO DE DADOS: ANOMALIA CLIMÁTICA ---")
    regiao = input("Digite o CEP ou Microrregião: ")
    evento = input("Tipo de evento (Ex: Onda de Calor, Chuva Intensa, Queda de Temp): ")
    
    # Tratamento para aceitar tanto vírgula quanto ponto
    entrada_temp = input("Variação de Temperatura prevista (°C): ").strip()
    entrada_temp = entrada_temp.replace(',', '.')
    
    try:
        variacao_temp = float(entrada_temp)
    except ValueError:
        print("Erro: Digite apenas valores numéricos para a temperatura.\n")
        return

    # Estrutura de decisão para sugerir a classe terapêutica (ATC)
    evento_lower = evento.lower()
    if "calor" in evento_lower:
        sugestao_atc = "Respiratórios e Hidratação"
        latencia_dias = 8
    elif "chuva" in evento_lower or "enchente" in evento_lower:
        sugestao_atc = "Antibióticos e Gastrointestinais"
        latencia_dias = 15
    elif "queda" in evento_lower or "frio" in evento_lower:
        sugestao_atc = "Antitérmicos e Corticoides"
        latencia_dias = 10
    else:
        sugestao_atc = "Análise Manual Necessária"
        latencia_dias = 0

    # Armazenando como uma Tupla dentro da Lista
    novo_alerta = (regiao, evento, variacao_temp, sugestao_atc, latencia_dias)
    dados_climaticos.append(novo_alerta)
    
    print(f"\nAlerta registrado! Anomalia '{evento}' em '{regiao}'.")
    print(f"Gatilho ATC Sugerido: {sugestao_atc}\n")

def prever_janela_biologica(dados_climaticos):
    """
    Analisa os dados ingeridos e gera alertas de envio de estoque.
    Parâmetro: dados_climaticos (list)
    Retorno: lista de ações recomendadas (list)
    """
    print("\n--- MOTOR DE IA: CÁLCULO DA JANELA BIOLÓGICA ---")
    if not dados_climaticos:
        print("Nenhuma anomalia climática registrada para análise.\n")
        return []

    acoes_recomendadas = []
    
    # Estrutura de repetição (for) 
    for anomalia in dados_climaticos:
        regiao, evento, temp, atc, latencia = anomalia
        
        if latencia > 0:
            alerta = f"ENVIAR ESTOQUE: {atc} para {regiao.upper()} em até {latencia} dias (Motivo: {evento})."
            acoes_recomendadas.append(alerta)
            print(alerta)
        else:
            print(f"ATENÇÃO: Evento '{evento}' em {regiao} não possui padrão de latência mapeado.")
            
    print("------------------------------------------------\n")
    return acoes_recomendadas

def relatorio_supply_chain(dados_climaticos):
    """
    Gera estatísticas para os gestores de Supply Chain.
    Parâmetro: dados_climaticos (list)
    Retorno: tupla com total de alertas e variação térmica média (tuple)
    """
    print("\n--- DASHBOARD B2B: SUPPLY CHAIN ---")
    total_alertas = len(dados_climaticos)
    
    if total_alertas == 0:
        print("Sistema ocioso. Nenhum alerta no momento.\n")
        return 0, 0.0

    soma_variacao = 0.0
    for anomalia in dados_climaticos:
        soma_variacao += abs(anomalia[2]) 

    media_variacao = soma_variacao / total_alertas

    print(f"Total de Alertas Ativos: {total_alertas}")
    print(f"Variação Térmica Média Detectada: {media_variacao:.1f}°C")
    print("-----------------------------------\n")

    return total_alertas, media_variacao

def consultar_microrregiao(dados_climaticos, termo_busca):
    """
    Busca se há anomalias previstas para um CEP ou Microrregião específica.
    Parâmetros: dados_climaticos (list), termo_busca (string)
    Retorno: tupla com os dados ou None
    """
    for anomalia in dados_climaticos:
        if termo_busca.lower() in anomalia[0].lower():
            return anomalia
    return None

def painel_astropharma():
    """
    Função principal que controla o fluxo do sistema SaaS.
    """
    banco_anomalias = []

    # Estrutura de repetição
    while True:
        print("========================================")
        print(" 🚀 SaaS ASTROPHARMA - BI PREDITIVO 🚀")
        print("========================================")
        print("1 - Sobre a Solução")
        print("2 - Ingestão de Gatilho Climático (API)")
        print("3 - Calcular Janela Biológica (IA)")
        print("4 - Relatório Gerencial (Supply Chain)")
        print("5 - Consultar Hub/Microrregião")
        print("0 - Fazer Logout")
        print("========================================")

        # O .strip() aqui limpa os "enters" e espaços que o terminal do Linux joga sem você ver
        opcao = input("Selecione um módulo: ").strip()

        # Decisão em if-elif-else (funciona em qualquer versão do Python)
        if opcao == '1':
            exibir_descricao()
        elif opcao == '2':
            registrar_anomalia(banco_anomalias)
        elif opcao == '3':
            prever_janela_biologica(banco_anomalias)
        elif opcao == '4':
            relatorio_supply_chain(banco_anomalias)
        elif opcao == '5':
            print("\n--- CONSULTA DE DEMANDA REGIONAL ---")
            busca = input("Digite a região ou CEP do Centro de Distribuição: ").strip()
            
            resultado = consultar_microrregiao(banco_anomalias, busca)
            
            if resultado:
                print(f"\n[ALERTA LOCALIZADO] Região: {resultado[0].upper()}")
                print(f"Evento: {resultado[1]} | Variação: {resultado[2]}°C")
                print(f"Ação ATC: Enviar {resultado[3]} (Latência: {resultado[4]} dias)\n")
            else:
                print(f"\nNenhum alerta climático ativo para a região '{busca}'. Operação normal.\n")
        elif opcao == '0':
            print("\nEncerrando o BI Preditivo do AstroPharma. Até logo!")
            break
        else:
            print("\nMódulo inválido! Escolha uma opção de 0 a 5.\n")

# Inicia a execução do SaaS
if __name__ == "__main__":
    painel_astropharma()