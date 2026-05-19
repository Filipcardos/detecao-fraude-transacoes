# =========================
# 📊 Detecção de Fraude em Transações
# =========================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix

# =========================
# 1. Carregar dados
# =========================
df = pd.read_csv("../data/transacoes.csv")

print("\n📊 Pré-visualização dos dados:")
print(df.head())

print("\n📌 Informações:")
print(df.info())

# =========================
# 2. Análise exploratória
# =========================
print("\n📈 Estatísticas:")
print(df.describe())

# Gráfico de distribuição
sns.countplot(x='classe', data=df)
plt.title('Distribuição de Fraudes (0 = Normal, 1 = Fraude)')
plt.show()

# =========================
# 3. Pré-processamento
# =========================
le = LabelEncoder()
df['tipo'] = le.fit_transform(df['tipo'])
df['localizacao'] = le.fit_transform(df['localizacao'])

# Separar dados
X = df.drop('classe', axis=1)
y = df['classe']

# Divisão treino/teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# 4. Modelo 1 - Isolation Forest
# =========================
print("\n🌲 Modelo: Isolation Forest")

iso = IsolationForest(contamination=0.3, random_state=42)
iso.fit(X_train)

y_pred_iso = iso.predict(X_test)

# Converter (-1 = anomalia → 1 fraude)
y_pred_iso = [1 if x == -1 else 0 for x in y_pred_iso]

print("\n📈 Relatório:")
print(classification_report(y_test, y_pred_iso))

print("\n📉 Matriz de Confusão:")
print(confusion_matrix(y_test, y_pred_iso))

# =========================
# 5. Modelo 2 - Random Forest
# =========================
print("\n🌲 Modelo: Random Forest")

rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)

y_pred_rf = rf.predict(X_test)

print("\n📈 Relatório:")
print(classification_report(y_test, y_pred_rf))

print("\n📉 Matriz de Confusão:")
print(confusion_matrix(y_test, y_pred_rf))

# =========================
# 6. Explicabilidade (Feature Importance)
# =========================
print("\n🔍 Importância das variáveis:")

importances = rf.feature_importances_

for feature, importance in zip(X.columns, importances):
    print(f"{feature}: {importance:.4f}")