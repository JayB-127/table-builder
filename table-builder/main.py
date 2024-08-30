from typing import Self


class Table:
    def __init__(self, cols: list, rows: list):
        self.cols = cols
        self.rows = rows
        self.colNo = len(cols)
        self.rowNo = len(rows)
        

    def show(self) -> Self:

        # find max cell width per column
        colWidths = []
        for i in range(self.colNo):
            widths = []
            for row in self.rows:
                widths.append(len(str(row[i])))
            widths.append(len(str(self.cols[i])))
            colWidths.append(max(widths))

        # create formattings
        border = "+" + "+".join("{borderType}"*(colWidth + 2) for colWidth in colWidths) + "+"
        values = "|" + "|".join(" {:<%d} " % colWidth for colWidth in colWidths) + "|"

        print(border.format(borderType="="))
        print(values.format(*self.cols))
        print(border.format(borderType="="))
        for row in self.rows:
            print(values.format(*row))
            print(border.format(borderType="-"))

        return self
    

    def add_column(self, col: str) -> Self:
        #TODO: give empty values for in rows
        #TODO: add as right column (further update to insert in middle)
        #TODO: update self.colNo value
        return self

    def remove_col(self, colIndex: int) -> Self:
        #TODO: remove col
        #TODO: update self.colNo value
        return self


    def add_row(self, row: list) -> Self:
        #TODO: sanitisation to ensure it contains valid amount of cols
        #TODO: add as bottom row (further update to insert in middle)
        #TODO: update self.rowNo value
        return self
    
    def remove_row(self, rowIndex: int) -> Self:
        #TODO: remove row
        #TODO: update self.rowNo value
        return self


    def edit_cell(self, colIndex: int, rowIndex: int, newValue) -> Self:
        #TODO: index rows and cols, replacing value with new value
        #TODO: would have to recalculate cell widths
        return self
    

    def set_border_line(self, border_type: str) -> Self:
        pass

    def justify_values(self, justification: str) -> Self:
        pass
    

    def to_string(self) -> str:
        #TODO: print out string stating colNo, rowNo, and data
        tableString = ""
        return tableString


table = Table(['fname', 'lname', 'age'],
              [['john', 'smith', 40],
               ['jane', 'doe', 5],
               ['joe', 'bloggs', 23]]).show()


#TODO: what if data given is square (num of cols doesnt match width of rows)
#TODO: indexing specific cells (could operator overload [])
#TODO: selectable border lines (e.g., =, -, ~) - optional param in build()
#TODO: change border line of exisiting table
#TODO: set default settings of class (e.g., border) through staticmethod decorator
#TODO: justify values in rows left/right/centre
#TODO: different types of tables (e.g., compact has no border in between rows)
#TODO: multiline values (i.e., wrapping)
#TODO: table from json, csv, etc.
#TODO: table to json, csv, etc.
#TODO: documentation :(
#TODO: testing (even worse than doc)