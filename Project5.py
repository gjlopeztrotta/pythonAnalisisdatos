import pandas as pd
import numpy as np     
import seaborn as sns   


#def main():
#    tips= pd.read_csv('tip.csv')
#    fligths=pd.read_csv('flights.csv')
#    merged_df=concatenar_dataframes(tips,fligths)
#    print("DataFrame concatenado:")
#    print(merged_df.tail(25))

def concatenar_dataframes(df1, df2):
    concatenated_df = pd.concat([df1, df2], axis=0)
    return concatenated_df

def main():
    tips= pd.read_csv('tip.csv')
    flights=pd.read_csv('flights.csv')
    #5-1
    concat_vertically = pd.concat([tips, flights], axis=0)
    print("#5-1:")
    print(concat_vertically.head())
    #5-2
    df_discount = pd.DataFrame({
    'total_bill': [16.99, 10.34, 21.01,23.68,23.75,17.92],
    'discount': [10, 5, 7,12,15,16]
    })
    merged_df = pd.merge(tips, df_discount, on='total_bill',
    how='inner')
    print("\n#5-2:")
    print(merged_df.head(10))
    #5-3
    
    df_feedback = pd.DataFrame({
    'total_bill': [16.99, 10.34, 21.01],
    'feedback': ['Good', 'Average', 'Excellent']
    })
    left_joined = pd.merge(tips, df_feedback, on='total_bill', how='left')
    print("\n#5-3:")
    print(left_joined.head(10))
    #5-4
    df_review = pd.DataFrame({
    'total_bill': [16.99, 10.34, 15.00],
    'restaurant_review': ['4 stars', '3 stars', '5 stars']
    })
    outer_joined = pd.merge(tips, df_review, on='total_bill', how='right')
    print("\n#5-4:")
    print(outer_joined.head(10))
    #5-5
    concat_horizontally = pd.concat([tips, flights], axis=1)
    print("\n#5-5:")
    print(concat_horizontally.head())
    #5-6
    df_experience = pd.DataFrame({
    'total_bill': [16.99, 10.34, 21.01],
    'tip': [1.01, 1.66, 3.50],
    'dining_experience': ['Casual', 'Formal', 'Casual']
    })
    merged_overlapping = pd.merge(tips, df_experience, on=['total_bill', 'tip'],
    how='inner')
    print("\n#5-6:")
    print(merged_overlapping.head())
    #5-7
    multi_index_df = pd.DataFrame({
    'total_bill': [16.99, 10.34, 21.01],
    'tip': [1.01, 1.66, 3.50],
    'meal_preference': ['Veg', 'Non-Veg', 'Non-Veg']
    }).set_index(['total_bill', 'tip'])
    merged_multiindex = pd.merge(tips.set_index(['total_bill', 'tip']),
    multi_index_df, left_index=True, right_index=True)
    print("\n#5-7:")
    print(merged_multiindex.head())

if __name__ == "__main__":
    main()