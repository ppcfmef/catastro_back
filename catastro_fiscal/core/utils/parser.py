import re


class CamelCaseToSnake:

    @staticmethod
    def exec(value):
        value = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', value)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', value).lower()
