from csv import DictReader
from typing import Any, Generator, Iterable, List, Union, cast

from type_definitions import Person, PersonFilter


def compare_data(person: Person, filter: PersonFilter) -> bool:
            is_match: bool = True        

            for key, condition in filter.items():
                if is_match == False:
                    break

                if condition == None:
                    continue

                elif isinstance(condition, tuple):
                    is_match = bool(condition[0] <= int(cast(str, person.get(key))) <= condition[1])
                    continue
                    
                elif isinstance(condition, bool):
                    bool_value = bool(person.get(key) == '1')
                    is_match = bool_value == condition
                    continue

                elif isinstance(condition, int):
                    is_match = bool(condition == int(cast(int, person.get(key))))
                    continue
                
                elif isinstance(condition, list):
                    is_match = bool(person.get(key) in condition)
                    continue
                         
                elif isinstance(condition, str):
                    str_value: str = cast(str, person.get(key))
                    is_match = bool(str_value in condition)
                    continue
                

            return is_match