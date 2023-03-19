from datetime import datetime
from sqlalchemy.inspection import inspect

class Serialiser(object):

    def serialise(self):
        return {c: self.getAttr(c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialise_list(l):
        return [m.serialise() for m in l]

    def getAttr(self, attr):
        value = getattr(self, attr)
        if type(value) == datetime:
            return datetime.strftime(value, '%d.%m.%y')
        else:
            return value 
            