from typing import Literal, cast
from type_definitions import Person


def parse(person: Person) -> Person:
    for key, value in person.items():
        value = cast(str, value)
        key = cast(Literal['Age', 'Income', 'Travel_Frequency', 'Vacation_Budget', 'Proximity_to_Mountains', 'Proximity_to_Beaches', 'Pets', 'Environmental_Concerns'], key)
        if isinstance(key, str):
            try:
                person[key] = int(value)
            except:
                continue
    
    return person