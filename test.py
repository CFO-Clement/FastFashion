
import pandas as pd
import spacy
import string
from sklearn.impute import KNNImputer
from sklearn.linear_model import LinearRegression
import numpy as np
from time import perf_counter


# Load
impacts_df = pd.read_csv('data.csv')
clothes_df = pd.read_csv('vetements copy.csv')


impacts_df.fillna(0, inplace=True)
clothes_df.fillna(0, inplace=True)


#print(impacts_df.info())
#print(clothes_df.info())


#NLP to convert materials into generic name
nlp = spacy.load('en_core_web_lg')

def convert_raw_material(raw_material):
    raw_material = raw_material.lower()
    raw_material = raw_material.strip()

    doc = nlp(raw_material)

    lemmas = [token.lemma_ for token in doc]

    best_match = None
    max_similarity = 0
    for material in impacts_df['Material']:
        similarity = nlp(material.lower()).similarity(doc)
        if similarity > max_similarity:
            best_match = material
            max_similarity = similarity

    if max_similarity > 0.6:
        #print(f"-- OK -- {raw_material} have been transform to {best_match}")
        return best_match
    else:
        #print(f"-- KO -- can't fine a better name for {raw_material}")
        return raw_material




def impute_missing_value(df, column_name, k=5):
    
    missing_values = df[column_name].values.reshape(-1,1)
    #print(f'missing -> {missing_values}')
    
    # KNNImputer
    knn_imputer = KNNImputer(n_neighbors=k)
    knn_imputed_values = knn_imputer.fit_transform(missing_values)
    
    # Linear Regression
    lr_imputer = LinearRegression()
    lr_imputed_values = missing_values.copy()
    lr_imputed_values[np.isnan(lr_imputed_values)] = 0 # set NaN values to 0
    non_missing_indices = np.where(~np.isnan(lr_imputed_values))[0] # get non-missing value indices
    X = non_missing_indices.reshape(-1,1)
    y = lr_imputed_values[non_missing_indices]
    lr_imputer.fit(X, y)
    lr_imputed_values[np.isnan(missing_values).ravel()] = lr_imputer.predict(np.isnan(missing_values).reshape(-1,1))
    
    # Mean imputation
    mean_imputed_values = missing_values.copy()
    mean = np.nanmean(mean_imputed_values)
    mean_imputed_values[np.isnan(mean_imputed_values)] = mean
    
    # Evaluate performance
    knn_mae = np.mean(abs(missing_values - knn_imputed_values))
    lr_mae = np.mean(abs(missing_values - lr_imputed_values))
    mean_mae = np.mean(abs(missing_values - mean_imputed_values))
    
    # Return imputed value with best performance
    if knn_mae <= lr_mae and knn_mae <= mean_mae:
        return knn_imputed_values[0][0]
    elif lr_mae <= mean_mae:
        return lr_imputed_values[0][0]
    else:
        return mean_imputed_values[0][0]




# define function to calculate KPIs
def calculate_kpis(row):

    impact_data = impacts_df.loc[impacts_df['Material'] == row]
    
    if impact_data.isnull().values.any():
        for col in impact_data.columns:
            if impact_data[col].isnull().values.any():
                imputed_value = impute_missing_value(impact_data, col)
                impact_data[col] = imputed_value
    
    
    env_score = (impact_data['Water_Use_kg/kg'] + impact_data['Fossil_Energy_kg/kg'] +
                 impact_data['Greenhouse_Gas_kgCO2eq/kg'] + impact_data['Land_use_m2/kg']) / 4
    
    animal_score = impact_data['Animal_Welfare_Score']
    
    
    human_score = impact_data['Human_Welfare_Score']
    
    
    social_score = (1 if impact_data['Labor_Conditions'].eq("unsafe").any() else 10+ 
                    impact_data['Human_Welfare_Score']) / 2

    try: 
        kpis = {'Environmental Impact Score': float(env_score),
            'Animal Welfare Score': float(animal_score),
            'Human Welfare Score': float(human_score),
            'Social Responsibility Score': float(social_score)}
    except:
        print(f'raw -> {raw}\nimpact_data -> {impact_data}\nenv_score -> {env_score}\nanimal_score -> {animal_score}')
        raise Exception("SHIT")
    return kpis




times = []
for idx, raw in clothes_df.iterrows():
    kpis_row = []
    final = {}
    start_time = perf_counter()
    for col, value in raw.items():
        if (value not in [0, 0.0]) and (col != "Type"):
            kpis = calculate_kpis(convert_raw_material(col))
            pond_kpis = {}
            for k, v in kpis.items():
                pond_kpis[k] = v * value
            kpis_row.append(pond_kpis)
    
    for i in kpis_row:
        for k, v in i.items():
            final[k] = final.get(k, 0) + (v/len(kpis_row))
    for k, v in final.items():
        if k not in clothes_df.columns:
            clothes_df[k] = 0
        clothes_df.loc[idx, k] = int(v)
    print(f'Index {idx} done. Total {len(clothes_df)}. Percentage -> {(idx / len(clothes_df)):.2%}')
    times.append(perf_counter() - start_time)
# print the updated clothes_df DataFrame
print(clothes_df)
print(f'mean time per row -> {(sum(times)/len(times)):.2f} s')
print(f'max time per row -> {max(times):.2f} s')
print(f'min time per row -> {min(times):.2f} s')
print(f'total time -> {sum(times):.2f} s')

clothes_df.to_csv('clothes_KPI.csv', index=False)