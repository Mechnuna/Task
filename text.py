from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def ft_split(text):
    mass = []
    string = ""
    for i in text:
        if i in ', .\n\t\r':
            if string:
                mass.append(string)
                string = ""
        else:
            string += i
    if string:
        mass.append(string)
    return mass

def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    mass = ft_split(text)
    maxim = 0
    minim = 9999999
    t = [None, None]
    for i in mass:
        if len(i) > maxim:
            maxim = len(i)
            t[1] = i
        if len(i) < minim:
            minim = len(i)
            t[0] = i
    return (t[0],t[1])
