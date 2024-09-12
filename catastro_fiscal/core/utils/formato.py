

class Format:

    @staticmethod
    def isNoneOrBlank(value):
        result = False
        if value is None or value.strip()!='':
            result = True
        return result 

