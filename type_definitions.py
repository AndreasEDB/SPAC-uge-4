from typing import Dict, Literal, TypedDict, Union, List, Tuple

gender = Literal['male', 'female', 'non-binary']
education_level = Literal['high_school', 'bachelor', 'master', 'doctorate']
preferred_activity = Literal['hiking', 'swimming', 'skiing', 'sunbathing']
location = Literal['urban', 'suburban', 'rural']
favourite_season = Literal['summer', 'winter', 'spring', 'fall']
preference = Literal['mountains', 'beaches']


class Person(TypedDict):
    Age: int
    Gender: gender
    Income: int
    Education_Level: education_level
    Travel_Frequency: int
    Preferred_Activities: preferred_activity  
    Vacation_Budget: int
    Location: location  
    Proximity_to_Mountains: int 
    Proximity_to_Beaches: int
    Favorite_Season: favourite_season  
    Pets: bool
    Environmental_Concerns: bool
    Preference: preference


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
    Preference: preference