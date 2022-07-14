class Column
# this is the map representation of several Units
    def __init__(self, columnName):
        self.columnName = columnName
        self.attachedUnits = {}
        self.attachedUnitsCount = 0

    def assignUnit(self, unit):


    def detachUnit(self, unit):
