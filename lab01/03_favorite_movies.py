def first(movies_str):
    """Первый фильм"""
    return movies_str[0:10]

def last(movies_str):
    """Последний фильм"""
    return movies_str[-15:]

def second(movies_str):
    """Второй фильм"""
    return movies_str[12:24]

def second_last(movies_str):
    """Второй с конца"""
    return movies_str[-22:-17]

def get_movies(movies_str):
    """Вернуть все фильмы в виде списка (инкапсулированная логика)"""
    return [
        first(movies_str),
        last(movies_str),
        second(movies_str),
        second_last(movies_str)
    ]
