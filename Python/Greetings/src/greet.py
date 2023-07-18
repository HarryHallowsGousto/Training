# create greet method
import dataclasses
import re
from typing import Union


@dataclasses.dataclass
class People:
    names: Union[list[str], str, None]


class Greetings:
    def __init__(self, people: Union[People]):
        self.people = people

    def split_names(self) -> tuple[list[str], list[str]]:
        """
        Iterate over list of names passed into `people.name`
        Store each name to a temporary variable which slices all but the last one provided
        If there's a capitalised name then shout hello to that/those individuals
        :return: normal_names, shouted_names
        """
        shouted_names = []
        normal_names = []
        for name in self.people.names:
            if name == name.upper():
                shouted_names.append(name)
            else:
                if "," in name and "\"" not in name:
                    split_names = name.split(', ')
                    normal_names.extend(split_names)
                else:
                    if "\"" in name:
                        temporary_name = name.strip("\"")
                        name = f'and {temporary_name}'
                    normal_names.append(name)
        return normal_names, shouted_names

    def greet(self) -> str:
        """
        Handles generating the different types of greeting responses
        This considers the capitalisation of the names provided
        IF no name is provided then use a generic response
        :return:
        """
        if not self.people.names:
            return "Hello, my friend."

        if isinstance(self.people.names, str):
            if self.people.names == self.people.names.upper():
                return f"HELLO {self.people.names}!".upper()
            else:
                return f"Hello, {self.people.names}."
        else:
            normal_names, shouted_names = self.split_names()
            normal_greeting = f"Hello, {', '.join(normal_names[:-1])} and {normal_names[-1]}."
            # Using regex to check for recurring "and" then reducing them to a single "and
            fixed_greeting = re.sub(r'(?<=and) and', '', normal_greeting)
            normal_greeting = fixed_greeting

            if shouted_names:
                shouted_greeting = f"and hello {', '.join(shouted_names)}.".upper()
                return f"{normal_greeting} {shouted_greeting}"
            else:
                return normal_greeting

    def format_greetings(self):
        pass
