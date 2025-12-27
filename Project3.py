import pandas as pd
import seaborn as sns
iris = sns.load_dataset('iris')




def main():
    print("#3-1:\n",headerX(iris, 5))
    print("#3-2:\n",get_description(iris))
    print("#3-3:\n",get_info_aggrupated(iris, 'species'))
    print("#3-4:\n",get_highest_sepal_length(iris))
    print("#3-5:\n",get_species(iris, 'setosa') )
    print("#3-6:\n",get_max_petalwidth(iris) )
    print("#3-7:\n",get_pivot_table(iris) ) 
    
def get_description(iris):
    #auxiliary_iris = iris
    return iris.describe()

def get_info_aggrupated(iris, filter_column):
    return iris.groupby(filter_column).mean()

def get_highest_sepal_length(iris):
    return iris[iris['sepal_length'] == iris['sepal_length'].max()]

def get_species(iris, species_name):
    auxiliary_iris=iris[iris['species'] == species_name].filter(items=['petal_width']).value_counts()
    
    return auxiliary_iris

def headerX(iris, x=5):
    return iris.head(x)

def get_max_petalwidth(iris):
    agg_data = iris.groupby('species').agg({'petal_width': 'max','sepal_width': 'mean'})
    
    return agg_data[agg_data['petal_width'] == agg_data['petal_width'].max()]

def get_pivot_table(iris):
    pivot_table = pd.pivot_table(iris, values=['sepal_length','petal_length'], index='species',  aggfunc='mean')
    return pivot_table
    
if __name__ == "__main__":
    main()