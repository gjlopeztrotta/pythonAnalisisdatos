import pandas as pd



titanic = pd.read_csv('titanic.csv', sep=',')
cotizacion =pd.read_csv('titanic.csv', sep=';')
print(titanic.Survived.value_counts())
print(titanic['Survived'].isin([1]).sum())
print(titanic.describe())
print(titanic.columns)


# Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas.
print('Dimensiones:', titanic.shape)
print('Número de elemntos:', titanic.size)
print('Nombres de columnas:', titanic.columns)
print('Nombres de filas:', titanic.index)
print('Tipos de datos:\n', titanic.dtypes)
print('Primeras 10 filas:\n', titanic.head(10))
print('Últimas 10 filas:\n', titanic.tail(10))
print(titanic.loc[148,'Ticket'])

# Mostrar por pantalla las filas pares del DataFrame.
print(titanic.iloc[range(0,titanic.shape[0],2)])
print(titanic.shape[0],2)

# Mostrar los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
print(titanic[titanic["Pclass"]==1]['Name'].sort_values())
print(titanic[titanic["Pclass"]==1]['Name'].sort_values())
print(titanic.groupby('Survived').count())
print('--------------------------')
print(titanic['Survived'].mean()*100)
print(titanic['Survived'].value_counts(normalize=True) * 100)
print(titanic.Name[325] )

num_var = [c for c in titanic if pd.api.types.is_numeric_dtype(titanic[c])]
cat_var = [c for c in titanic if pd.api.types.is_categorical_dtype(titanic[c])]
non_num_var = [c for c in titanic if not pd.api.types.is_numeric_dtype(titanic[c])]
print("Lista de colunmas numericas \n", num_var)
print("Lista de colunmas categoricas \n", cat_var)
print("Lista de colunmas no numericas \n",non_num_var)

y_objetivo = titanic.Survived
x_modelo = titanic.drop("Survived", axis = 1)
print(pd.get_dummies(x_modelo).shape)
t = titanic["Sex"]. astype("category")
print(t.head)
print(t.cat.codes.head())
print({i:e for i,e in enumerate(t.cat.categories)})