from typing import Literal, cast
from type_definitions import Person


def parse_person(person: Person) -> Person:
    for key, value in person.items():
        value = cast(str, value)
        key = cast(Literal['Age', 'Income', 'Travel_Frequency', 'Vacation_Budget', 'Proximity_to_Mountains', 'Proximity_to_Beaches', 'Pets', 'Environmental_Concerns', 'Preference'], key)
        if isinstance(key, str):
            try:
                if key == 'Pets' or key == 'Environmental_Concerns':
                    person[key] = bool(value == '1')
                elif key == 'Preference':
                    person[key] = 'beaches' if value == '0' else 'mountains'
                else:
                    person[key] = int(value)
            except:
                continue
    
    return person