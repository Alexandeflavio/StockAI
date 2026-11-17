# StockAI — Inteligência aplicada à gestão de estoques

**Projeto de portfólio | Python • Pandas • Machine Learning • Power BI • Logística**

## Visão geral

O StockAI é um projeto educacional de análise de dados e previsão de demanda para um **centro de distribuição fictício**. O objetivo é apoiar a identificação de riscos de ruptura, a priorização de SKUs e o planejamento de reposição de materiais.

> **Aviso:** todos os dados são sintéticos e não representam operações, custos ou resultados de uma empresa real. As simulações são simplificadas e não contemplam integralmente pedidos em trânsito, perdas operacionais e outras restrições reais de abastecimento.

## Problema de negócio

Em um centro de distribuição com centenas de produtos, decisões de reposição exigem visibilidade sobre saldo disponível, consumo, cobertura de estoque e prazo de fornecimento. O StockAI combina indicadores operacionais e previsão de demanda para organizar uma fila de atenção para a equipe de planejamento.

## Dados

- **500 SKUs** e **25 fornecedores** fictícios.
- **365 dias** de histórico sintético.
- Arquivos-base: `produtos.csv`, `fornecedores.csv`, `movimentacoes.csv` e `estoques.csv`.
- Arquivos de saída: `prioridades_estoque.csv`, `planejamento_reposicao.csv`, `qualidade_previsoes.csv` e `impacto_fornecedores.csv`.

## Metodologia

1. Exploração e validação de dados com Python e Pandas.
2. Análise de movimentações, cobertura de estoque, indicadores financeiros e classificação ABC.
3. Classificação de prioridades de reposição com base em indicadores de estoque.
4. Previsão de demanda com **Random Forest**, comparada a uma referência de média móvel de sete dias.
5. Simulações retrospectivas (*backtesting*) e planejamento de reposição considerando lotes mínimos.
6. Visualização de indicadores e produtos prioritários em **Power BI**.

## Resultados obtidos na simulação

| Indicador | Resultado |
|---|---:|
| Produtos analisados | 500 |
| Prioridade crítica | 21 |
| Prioridade alta | 66 |
| Produtos em risco (alta + crítica) | 87 (17,4%) |
| MAE do Random Forest | 2,76 unidades |
| RMSE do Random Forest | 3,63 unidades |
| WAPE do Random Forest | 24,87% |
| MAE da referência de média móvel | 3,49 unidades |
| Reposição estimada antes dos lotes | 2.641 unidades |
| Reposição ajustada aos lotes | 4.110 unidades |
| Custo adicional estimado pelos lotes | R$ 132.714,12 |

Esses resultados são **experimentais**, calculados sobre dados sintéticos. A comparação com a média móvel não comprova desempenho em produção. As simulações retrospectivas devem ser interpretadas com cautela, pois nem todas utilizam um modelo retreinado exclusivamente com informações disponíveis até cada data simulada.

## Dashboard Power BI

O painel apresenta seis indicadores principais (total de produtos, críticos, prioridade alta, cobertura média, margem média de cobertura e produtos em risco), um gráfico de distribuição por prioridade e uma tabela gerencial filtrada para SKUs de prioridade **Alta** e **Crítica**.

O arquivo editável está em `Dashboard/StockAI_Dashboard_Logistico.pbix`.

## Estrutura do repositório

```text
Projeto Ifood AI/
├── Dados/
│   ├── produtos.csv
│   ├── fornecedores.csv
│   ├── movimentacoes.csv
│   └── estoques.csv
├── Notebooks/
│   ├── primeira_analise.py
│   └── StockAI_Analise_de_Estoques.ipynb
├── Dashboard/
│   └── StockAI_Dashboard_Logistico.pbix
├── Imagens/
├── StockAI_Resultados/
│   ├── prioridades_estoque.csv
│   ├── planejamento_reposicao.csv
│   ├── qualidade_previsoes.csv
│   └── impacto_fornecedores.csv
├── requirements.txt
└── README.md
```

## Como explorar

1. Instale Python e as dependências indicadas em `requirements.txt` (revise esse arquivo antes de executar).
2. Abra `Notebooks/StockAI_Analise_de_Estoques.ipynb` no Google Colab ou em ambiente Jupyter.
3. Disponibilize os arquivos de `Dados/` no ambiente de execução e ajuste os caminhos de leitura dos CSVs, se necessário.
4. Execute as células em sequência, verificando as saídas e os arquivos gerados.
5. Abra o relatório `.pbix` no Power BI Desktop. Se os arquivos CSV tiverem mudado de pasta, atualize os caminhos da fonte de dados no Power BI.

**Nota de reprodutibilidade:** os caminhos de arquivos e as dependências ainda precisam ser verificados em uma execução limpa antes de considerar o projeto totalmente reproduzível.

## Próximas melhorias

- Implementar validação temporal estrita com retreinamento em janelas históricas.
- Automatizar a leitura dos arquivos por caminhos relativos ou configuração centralizada.
- Acrescentar testes, instruções de instalação verificadas e capturas de tela do dashboard.
- Explorar cenários de reposição com restrições operacionais adicionais.

## Tecnologias

Python, Pandas, Scikit-learn (Random Forest), Google Colab/Jupyter, Power BI e GitHub.
