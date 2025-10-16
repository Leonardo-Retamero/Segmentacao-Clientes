### Dashboard de Segmentação do Cliente para a Área de Marketing

[🔗 Acesse o Dashboard pelo Streamlit](https://segmentacao-clientes.streamlit.app/)

---

### 🧠 Descrição do Projeto

Este projeto apresenta um dashboard interativo desenvolvido em Python e Streamlit, com o objetivo de segmentar clientes em grupos distintos (clusters) a partir de suas características de idade, renda anual e pontuação de gastos.

A segmentação permite que a área de marketing entenda melhor o perfil de cada grupo e direcione estratégias personalizadas de comunicação, fidelização e ofertas.

---

### 💼 Problema de Negócio:

Dado o histórico de clientes que realizaram compras na empresa, realize o agrupamento (segmentação) por similaridade de características em 3 grupos.

O objetivo é identificar padrões de comportamento e ajustar as estratégias de marketing para cada segmento de forma mais eficaz e direcionada.

---

### ⚙️ Metodologia: Segmentação com K-Means

A técnica de K-Means Clustering foi utilizada para agrupar os clientes em 3 segmentos distintos com base em suas variáveis numéricas.

### 🔹 Passos executados:

1. Importação das bibliotecas:
```python
  import pandas as pd
  from sklearn.cluster import KMeans
  from sklearn.preprocessing import StandardScaler
```

2. Carregamento dos dados:
```python
df_dsa = pd.read_csv('dados_clientes.csv')
```

3. Padronização das variáveis numéricas:

Antes de aplicar o K-Means, os dados de idade, renda anual e pontuação de gastos foram padronizados com StandardScaler() para que todas as variáveis tivessem a mesma escala.
```python
padronizador = StandardScaler()
dados_padronizados = padronizador.fit_transform(
  df_dsa[['idade', 'renda_anual', 'pontuacao_gastos']]
)
```

4. Definição do número de clusters (k=3):

Após testes e análise exploratória (como o método do cotovelo), foi definido k = 3.
```python
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(dados_padronizados)
```

5. Atribuição dos clusters ao dataset:
```python
df_dsa['cluster'] = kmeans.labels_
```

O resultado foi uma base segmentada em três grupos (Cluster 0, 1 e 2), que representam perfis distintos de clientes — por exemplo:

- Cluster 0: Clientes jovens com renda média e alta pontuação de gastos.

- Cluster 1: Clientes de renda mais alta com gastos equilibrados.

- Cluster 2: Clientes com menor renda e baixa pontuação de gastos.

---

### 📈 Princípais Indicadores:

- Média de Pontuação de Gastos
- Média de Idade
- Média de Renda Anual
- Total de Clientes

### 📊 Gráficos:

- Distribuição da Renda Médial Anual por Faixa de Idade
- Média de Pontuação de Gastos por Segmento
- Média de Renda Anual por Segmento
- Total de Clientes por Segmento
- Média de Idade por Segmento

---

### 💻 Tecnologias Utilizadas

| Categoria            | Ferramenta     |
| -------------------- | -------------- |
| Linguagem            | Python         |
| Framework Web        | Streamlit      |
| Visualização         | Plotly Express |
| Machine Learning     | Scikit-learn   |
| Manipulação de Dados | Pandas         |
