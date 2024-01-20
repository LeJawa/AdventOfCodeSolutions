from importlib import import_module

def import_function(year, day, part, function):
    return eval(f'import_module("src.{year}.{day:02d}.part{part}").{function}')