# Python-Global Solution - 1 Semestre

## Projeto desenvolvido para o projeto AstroPharma / Projeto desenvolvido para Global Solution com a intenção de utilizar técnologia espacial para resolver problemas na terra.

### Explicação das funcionalidades do sistema: 

**- Sobre a Solução**
  
Exibe uma breve descrição textual do sistema, seu objetivo e como ele atua na antecipação
da demanda de medicamentos.

**- Ingestão de Gatilho Climático (API):**

Permite ao usuário cadastrar uma nova anomalia climática informando região, evento e
temperatura. O algoritmo processa esses dados e define automaticamente a classe
terapêutica (ATC) sugerida e o tempo de latência.


**- Calcular Janela Biológica (IA):**
  
Analisa a lista de anomalias cadastradas e gera alertas logísticos precisos, indicando aos
centros de distribuição qual medicamento enviar, para qual região e o prazo limite (em dias)
para evitar a ruptura de gôndola.


**- Relatório Gerencial (Supply Chain):**

Realiza cálculos estatísticos com base nos dados armazenados, exibindo um painel com o
total de alertas ativos e a média global de variação térmica detectada no monitoramento.

**- Consultar Hub/Microrregião:**

Permite buscar o status de uma região ou CEP específico dentro do banco de dados,
retornando os detalhes da anomalia e a ação necessária caso a área esteja em risco.

**- Fazer Logout:**

Encerra o loop principal de execução e finaliza o programa de forma segura.

```
Execução:
Git clone -
cd\"""Pasta do arquivo"""

**Windows**
python main.py

**Linux**
python3 main.py
