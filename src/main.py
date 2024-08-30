

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



table = Table(['fname', 'lname'],
              [['john', 'smith', '40'],
               ['jane', 'doe', '5'],
               ['joe', 'bloggs', '23']]).build()



#TODO: insert into table
#TODO: delete from table
#TODO: selectable border lines (e.g., =, -, ~)
#TODO: justify values in rows left/right/centre
#TODO: different types of tables (e.g., compact has no border in between rows)
#TODO: multiline values (i.e., wrapping)
#TODO: table -> json