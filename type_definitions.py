from typing import Dict, Literal, TypedDict, Union, List, Tuple

gender = Literal['male', 'female', 'non-binary']
education_level = Literal['high_school', 'bachelor', 'master', 'doctorate']
preferred_activity = Literal['hiking', 'swimming', 'skiing', 'sunbathing']
location = Literal['urban', 'suburban', 'rural']
favourite_season = Literal['summer', 'winter', 'spring', 'fall']


class Person(TypedDict):
    Age: str | int
    Gender: gender
    Income: str | int
    Education_Level: education_level
    Travel_Frequency: str | int
    Preferred_Activities: preferred_activity  
    Vacation_Budget: str | int
    Location: location  
    Proximity_to_Mountains: str | int 
    Proximity_to_Beaches: str | int
    Favorite_Season: favourite_season  
    Pets: Literal['0', '1'] | int
    Environmental_Concerns: Literal['0', '1'] | Literal[0, 1]
    Preference: Literal['0', '1'] | Literal[0, 1]


class PersonFilter(TypedDict, total=False):
    Age: Union[int, Tuple[int, int]]
    Gender: Union[gender, List[gender]]
    Income: Union[int, Tuple[int, int]]
    Education_Level: Union[education_level, List[education_level]]
    Travel_Frequency: Union[int, Tuple[int, int]]
    Preferred_Activities: Union[preferred_activity, List[preferred_activity]]
    Vacation_Budget: Union[int, Tuple[int, int]]
    Location: Union[location, List[location]]
    Proximity_to_Mountains: Union[int, Tuple[int, int]]
    Proximity_to_Beaches: Union[int, Tuple[int, int]]
    Favorite_Season: Union[favourite_season, List[favourite_season]]
    Pets: bool
    Environmental_Concerns: bool
    Preference: Literal['0', '1'] | Literal[0, 1]