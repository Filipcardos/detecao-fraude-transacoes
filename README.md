<img width="1700" height="460" alt="github-header-banner" src="https://github.com/user-attachments/assets/01df8399-f63c-4424-844c-67d9e83a1c08" />

---

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python">
  <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--learn-orange">
  <img src="https://img.shields.io/badge/Data%20Analysis-Pandas-yellow">
  <img src="https://img.shields.io/badge/Status-Concluído-success">
</p>

---

##  Sobre o projeto

Este projeto foi desenvolvido com o objetivo de identificar possíveis fraudes em transações financeiras utilizando técnicas de Machine Learning.

A proposta simula um cenário comum em fintechs e sistemas bancários, onde é essencial detectar padrões anômalos que possam indicar atividades suspeitas.

---

## 🧠 Contexto do problema

Fraudes financeiras representam um grande desafio para empresas que lidam com transações digitais.  

Neste projeto, foi explorado um conjunto de dados contendo informações como valor da transação, tipo e localização, buscando identificar padrões que diferenciem transações normais de fraudulentas.

---

## ⚙️ Tecnologias e ferramentas

- Python  
- Pandas  
- Scikit-learn  
- Seaborn  
- Matplotlib  

---

## 🔬 Etapas do desenvolvimento

###  1. Análise exploratória (EDA)
- Visualização inicial dos dados
- Estatísticas descritivas
- Identificação da distribuição de fraudes

###  2. Pré-processamento
- Transformação de variáveis categóricas em numéricas
- Preparação do dataset para modelagem

###  3. Modelagem
Foram utilizados dois modelos:

- **Isolation Forest**  
  → Identificação de anomalias diretamente nos dados  

- **Random Forest**  
  → Classificação supervisionada para detecção de fraudes  

---

## 📊 Avaliação do modelo

Os modelos foram avaliados utilizando métricas padrão de classificação:

- Precision  
- Recall  
- F1-score  
- Matriz de confusão  

Essas métricas são essenciais em problemas de fraude, onde identificar corretamente os casos positivos é mais importante do que apenas ter alta acurácia.

---

## 📈 Resultados e insights

Durante a análise, foi possível observar que:

- Transações com valores elevados apresentam maior risco
- Transações realizadas de forma online tendem a concentrar mais anomalias
- Algumas localizações aparecem com maior frequência em casos suspeitos

---

## ⭐ Considerações finais

Este projeto representa um passo importante na evolução prática em Python e Machine Learning, focando não apenas na implementação, mas também na organização e clareza do processo.
