from matplotlib import pyplot as plt
import pandas as pd
from filter_data import filter_data
from kaggle_data import KaggleData
from type_definitions import PersonFilter
import seaborn as sns # type: ignore

kaggle = KaggleData('jahnavipaliwal/mountains-vs-beaches-preference')
data_file = kaggle.data

person_filter: PersonFilter = {
    # 'Age': (30, 39),
    # 'Proximity_to_Beaches': (0, 1000),
    # 'Favorite_Season': ['summer'],
    # 'Preferred_Activities': ['sunbathing', 'swimming'],
    # 'Preference': 'mountains'
}

persons = filter_data(data_file, person_filter)

# for person  in persons:
#     print(person.get('Preference'))

df = pd.DataFrame(list(persons))




# print(df)


# sns.pairplot(df, hue='Preference', diag_kind='kde')
# plt.show()

sns.barplot(x='Vacation_Budget', y='Travel_Frequency', data=df, hue='Preference')

# sns.stripplot(x='Age', y='Proximity_to_Beaches', data=df, hue='Preference', jitter=True)

plt.show()