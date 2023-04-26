import typing

def index(d:dict, parent_key:str='', sep:str='.', transform=str.lower) -> dict:
    """ Indexes the dict so it will be only one level deep.
    All values from nested dicts will be now available
    the base level of dict and their position in the 
    structure will be reflected in their key.
    
    >>> example = {'a': 1, 'c': {'a': 2, 'b': {'x': 5}, 'd': [1, 2, 3]}
    >>> flatten(example)
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
