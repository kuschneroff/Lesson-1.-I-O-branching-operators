import pandas as pd

data = pd.read_csv('Pokemon.csv')  # Загрузка данных из файла 'Pokemon.csv'

# Создание столбцов-индикаторов для столбца 'Type 1'
indicator_columns = pd.get_dummies(data['Type 1'], prefix='Type')

# Объединение столбцов-индикаторов с исходным DataFrame
data_encoded = pd.concat([data, indicator_columns], axis=1)

print(data_encoded)
