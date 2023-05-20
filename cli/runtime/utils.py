import typing
import requests
import time

from datetime import datetime
from functools import singledispatch


def index(d:dict, parent_key:str='', sep:str='.', transform=str.lower) -> dict:
    """ Indexes the dict so it will be only one level deep.
    All values from nested dicts will be now available
    the base level of dict and their position in the 
    structure will be reflected in their key.
    
    >>> example = {'a': 1, 'c': {'a': 2, 'b': {'x': 5}, 'd': [1, 2, 3]}
    >>> index(example)
    >>> {'a': 1, 'c.a': 2, 'c.b': {'x': 5} ,'c.b.x': 5, 'd': [1, 2, 3]}
    """
    if not isinstance(d, dict):
        return d
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        new_key = transform(new_key)
        if isinstance(v, typing.MutableMapping):
            items.extend(index(v, new_key, sep=sep).items())
        items.append((new_key, v))
    return dict(items)


@singledispatch
def merge(x:dict, y:dict):
    x_keys, y_keys = x.keys(), y.keys()
    result = { k: merge(x[k], y[k]) for k in x_keys & y_keys }
    result.update({k: x[k] for k in x_keys - y_keys})
    result.update({k: y[k] for k in y_keys - x_keys})
    return result

@merge.register
def m(x:str, y:str):
    return x + y

@merge.register
def m(x: tuple, y:tuple):
    return x + y

@merge.register
def m(x: list, y:list):
    combined = set(x + y)
    return list(combined)

@merge.register
def m(x: int, y: int):
    raise ValueError("integer value conflict")

@merge.register
def m(x: bool, y: bool):
    return x or y


def url_ready(url: str, timeout: int=10, max_retry:int = 3):
    start = datetime.utcnow()
    response = requests.get(url=url)
    while not response.ok:
        delta = datetime.utcnow() - start
        if delta.seconds >= timeout:
            return
        time.sleep(timeout/max_retry)
        response = requests.get(url=url)
