import csv
from typing import Any, Generator, List, Literal, Tuple, Union, cast
from compare_data import compare_data
from kaggle_data import KaggleData
from type_definitions import Person, PersonFilter
from parse_person import parse


def filter_data(data: Union[Generator[Person, Any, None], List[Person], str], filter: PersonFilter) -> Generator[Person, Any, None]:
    if isinstance(data, str):
        with open(data, newline='', encoding='utf-8') as data_in:
            persons = csv.DictReader(data_in)
            for _person in persons:
                person: Person = cast(Person, _person)

                if compare_data(person, filter):
                    yield parse(person)
    else:
        for person in data:
            if compare_data(person, filter):
                    yield parse(person)


if __name__=='__main__':
    kaggle = KaggleData('jahnavipaliwal/mountains-vs-beaches-preference')
    data_file = kaggle.data

    filter: PersonFilter = {
        'Age': (18, 34),
        'Education_Level': ['bachelor', 'master', 'doctorate'],
        'Gender': 'non-binary',
        'Favorite_Season': ['winter', 'fall'],
        'Pets': True,
        'Proximity_to_Beaches': (0, 100)
    }

    persons = filter_data(data_file, filter)
    print(len(list(persons)))
