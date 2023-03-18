
I created this dataset because i can't  found on online
I tryed webscraping and data mining without sucess so i did it by hand.
Ref:
- "Environmental impacts of textile production and use" by T.E. Graedel et al. (2009)
- "Environmental performance of textile fibres using life cycle assessment" by S. Azadi et al. (2014)
- "Sustainability in the textile industry" by K. Mishra and K. Jha (2019)
- "Sustainability in the Textile and Fashion Industry" by Subramanian Senthilkannan Muthu (2017)
- The Higg Materials Sustainability Index (MSI) database
- The Textile Exchange Preferred Fiber and Materials Market Report (2019)

KPI:
 - Environmental Impact Score: This KPI measures the overall environmental impact of a textile based on its
 composition. It can be calculated as follows:
Environmental Impact Score = (Water_Use_kg/kg + Fossil_Energy_kg/kg + Greenhouse_Gas_kgCO2eq/kg + Land_use_m2/kg) / 4
This KPI takes into account the water usage, fossil energy usage, greenhouse gas emissions, and land usage associated with producing one kilogram of the textile. The higher the score, the greater the environmental impact.

- Animal Welfare Score: This KPI measures the animal welfare standards associated with a textile based on its composition. It can be calculated as follows:
Animal Welfare Score = Animal_Welfare_Score
This KPI takes into account the animal welfare score associated with producing one kilogram of the textile. The higher the score, the better the animal welfare standards.

- Human Welfare Score: This KPI measures the human welfare standards associated with a textile based on its composition. It can be calculated as follows:
Human Welfare Score = Human_Welfare_Score
This KPI takes into account the human welfare score associated with producing one kilogram of the textile. The higher the score, the better the human welfare standards.

- Biodegradability Score: This KPI measures how biodegradable a textile is. It can be calculated as follows:
Biodegradability Score = Biodegradability
This KPI takes into account the biodegradability score associated with the textile. The higher the score, the more biodegradable the textile is.

- Social Responsibility Score: This KPI measures the social responsibility standards associated with a textile based on its composition. It can be calculated as follows:
Social Responsibility Score = (Employee_Conditions_Score + Community_Impact_Score) / 2
This KPI takes into account the employee conditions score and community impact score associated with producing one kilogram of the textile. The higher the score, the better the social responsibility standards. The scores can be subjective and may vary depending on the organization or standard used to evaluate them.

- Energy Efficiency Score: This KPI measures how efficiently energy is used in the production of a textile. It can be calculated as follows:
Energy Efficiency Score = (Energy_Output_kWh/kg / Energy_Input_kWh/kg) x 100
This KPI takes into account the amount of energy required to produce one kilogram of the textile and compares it to the amount of energy produced. The higher the score, the more energy-efficient the production process.

- Recyclability Score: This KPI measures how recyclable a textile is. It can be calculated as follows:
Recyclability Score = Recyclability
This KPI takes into account the recyclability score associated with the textile. The higher the score, the more recyclable the textile is.

- Water Pollution Score: This KPI measures the potential for water pollution associated with the production of a textile. It can be calculated as follows:
Water Pollution Score = Water_Pollution_Score
This KPI takes into account the water pollution score associated with producing one kilogram of the textile. The higher the score, the greater the potential for water pollution.


I want you to give me the code of a function that allows to find a missing value in a dataframe based on the other values of this column.
This function will use a ML approach with a K-NN and a regression and a statistical approach.
Then this function will determine which of the 3 values seems to be the best and return it.

I also want you to modify the following code so that just after calculating the "average_impact_data" variable it looks if there are any missing values. If there are, it will use the new function to find the values
def calculate_kpis(row):

    impact_data = impacts_df.loc[impacts_df['Material'] == row]
    average_impact_data = impact_data.mean()
    
    env_score = (average_impact_data['Water_Use_kg/kg'] + average_impact_data['Fossil_Energy_kg/kg'] +
                 average_impact_data['Greenhouse_Gas_kgCO2eq/kg'] + average_impact_data['Land_use_m2/kg']) / 4
    
    animal_score = average_impact_data['Animal_Welfare_Score']
    
    human_score = average_impact_data['Human_Welfare_Score']
    
    social_score = (average_impact_data['Labor_Conditions'] + 
                    average_impact_data['Human_Welfare_Score']) / 2

    
    
    kpis = {'Environmental Impact Score': env_score,
            'Animal Welfare Score': animal_score,
            'Human Welfare Score': human_score,
            'Social Responsibility Score': social_score}
    
    return kpis
