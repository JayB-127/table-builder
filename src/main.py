

class Table:
    def __init__(self, cols: list, rows: list):
        self.cols = cols
        self.rows = rows
        self.colNo = len(cols)
        self.rowNo = len(rows)

    def build(self):
        # raise TypeError if not lists?
        # handle unmatching numbers of cols to rows

        colLens = []
        # append longest value length for each col
        for i in range(len(self.cols)):
            colLens.append(max([len(row[i]) for row in self.rows] + [len(self.cols[i])]))

        # create formattings
        border = "+" + "+".join("{borderType}"*(colLen + 2) for colLen in colLens) + "+"
        values = "|" + "|".join(" {:<%d} " % colLen for colLen in colLens) + "|"

        print(border.format(borderType="="))
        print(values.format(*self.cols))
        print(border.format(borderType="="))
        for row in self.rows:
            print(values.format(*row))
            print(border.format(borderType="-"))


    def addRow(self, row):
        #TODO: sanitisation to ensure it contains valid amount of cols
        #TODO: add as bottom row (further update to insert in middle)
        #TODO: update self.rowNo value
        pass

    def addColumn(self, col: str):
        #TODO: give empty values for in rows
        #TODO: update self.colNo value
        pass

    def removeRow(self, rowIndex: int):
        #TODO: remove row
        #TODO: update self.rowNo value
        pass

    def removeCol(self, colIndex: int):
        #TODO: remove col
        #TODO: update self.colNo value
        pass



table = Table(['fname', 'lname'],
              [['john', 'smith', '40'],
               ['jane', 'doe', '5'],
               ['joe', 'bloggs', '23']]).build()



#TODO: indexing specific cells (could operator overload [])
#TODO: selectable border lines (e.g., =, -, ~) - optional param in build()
#TODO: change border line of exisiting table
#TODO: justify values in rows left/right/centre
#TODO: different types of tables (e.g., compact has no border in between rows)
#TODO: multiline values (i.e., wrapping)
#TODO: table -> json