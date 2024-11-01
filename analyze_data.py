from matplotlib import pyplot as plt
import pandas as pd
from filter_data import filter_data
from kaggle_data import KaggleData
from type_definitions import PersonFilter
import seaborn as sns

kaggle = KaggleData('jahnavipaliwal/mountains-vs-beaches-preference')
data_file = kaggle.data

person_filter: PersonFilter = {
    # 'Age': (30, 39),
    'Proximity_to_Beaches': (0, 1000),
    'Favorite_Season': ['summer'],
    # 'Preferred_Activities': ['sunbathing', 'swimming']
}

persons = filter_data(data_file, person_filter)

# for person  in persons:
#     print(person.get('Preference'))

df = pd.DataFrame(list(persons))

# print(df.corr())

# df = df.sort_values('Income')

# print(df.corr(numeric_only=True))
# # df.plot(x=)

# plt.show()

# df['Travel_Frequency'] = pd.Categorical(df['Travel_Frequency'])
# df['Preferred_Activities'] = pd.Categorical(df['Preferred_Activities'], categories=['hiking', 'swimming', 'skiing', 'sunbathing'])
# df['Proximity_to_Mountains'] = pd.Categorical(df['Proximity_to_Mountains'])
# df['Proximity_to_Beaches'] = pd.Categorical(df['Proximity_to_Beaches'])

# # Set up the FacetGrid
# g = sns.FacetGrid(df, col='Travel_Frequency', hue='Proximity_to_Mountains', 
#                   row='Proximity_to_Beaches', margin_titles=True, height=3)

# # Map each subplot
# g.map(sns.countplot, 'Preferred_Activities', order=df['Preferred_Activities'].cat.categories)

# # Adjust layout
# g.add_legend()
# g.set_axis_labels("Preferred Activities", "Count")
# plt.xticks(rotation=45)
# plt.suptitle("Preferred Activities by Proximity to Mountains/Beaches and Travel Frequency", y=1.05)
# plt.tight_layout()
# plt.show()

# Prepare data for stacked bar chart
grouped_data = df.groupby(['Travel_Frequency','Proximity_to_Mountains', 'Proximity_to_Beaches', 'Preferred_Activities', ]).size().unstack(fill_value=0)

# Plotting
# grouped_data.plot(kind='bar', stacked=True, figsize=(12, 8), colormap='viridis')
grouped_data.plot(stacked=True)
# Labels and Title
plt.title("Stacked Bar Plot of Preferred Activities by Proximity and Travel Frequency")
plt.xlabel("Travel Frequency and Preferred Activities")
plt.ylabel("Count")
plt.legend(title="Proximity")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
