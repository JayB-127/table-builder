from typing import Self


class Table:
    
    # constructor -
    def __init__(self, cols: list, rows: list):
        self.cols = cols
        self.rows = rows
        self.num_cols = len(cols)
        self.num_rows = len(rows)


    # setters and getters -
    def __set_cols(self, cols: list) -> None:
        self.cols = cols
        self.num_cols += 1

    def __get_cols(self) -> list:
        return self.cols

    def __set_rows(self, rows: list):
        self.rows = rows
        self.num_rows = len(self.rows)

    def __get_rows(self):
        return self.rows
    
    def __get_num_rows():
        pass

    # instance methods -
    def show(self) -> Self:

        # find max cell width per column
        colWidths = []
        for i in range(self.num_cols):
            widths = []
            for row in self.__get_rows():
                widths.append(len(str(row[i])))
            widths.append(len(str(self.__get_cols())))
            colWidths.append(max(widths))

        # create formattings
        border = "+" + "+".join("{borderType}"*(colWidth + 2) for colWidth in colWidths) + "+"
        values = "|" + "|".join(" {:<%d} " % colWidth for colWidth in colWidths) + "|"

        # TODO: create table in one string using \n so we only print once
        print(border.format(borderType="="))
        print(values.format(*self.__get_cols())) # unpacking col values
        print(border.format(borderType="="))
        for row in self.rows:
            print(values.format(*row))
            print(border.format(borderType="-"))

        return self
 

    def add_column(self, col: str, values: list = []) -> Self:
        # empty values if none passed
        # TODO: if len(values) < len(self.cols), fill with empty values
        # TODO: should this be NaN?
        if values == []:
            values = [' ']*self.num_rows

        # update cols (append on right)
        # TODO: ability to add into certain index
        cols = self.__get_cols()
        cols.append(col)
        self.__set_cols(cols)

        for row in self.__get_rows():
            row.append('')

        #TODO: update self.colNo value
        return self

    def remove_col(self, colIndex: int) -> Self:
        #TODO: remove col
        #TODO: update self.colNo value
        return self


    def add_row(self, row: list) -> Self:
        #TODO: empty values if list len does not match self.colNo
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
        tableString = f'Table | shape: ({self.num_rows}, {self.cols}), rows: {self.rows}, cols: {self.cols}' # TODO: use getters and setters
        print(tableString)
        return tableString



table = Table(['fname', 'lname', 'age'],
              [['john', 'smith', 40],
               ['jane', 'doe', 5],
               ['joe', 'bloggs', 23]]).show().add_column('test')

table.show()

#TODO: build() sets cols and rows (and shows)
#TODO: show() actually prints the table


#TODO: what if data given is not square (num of cols doesnt match width of rows)
#TODO: indexing specific cells (could operator overload [])
#TODO: selectable border lines (e.g., =, -, ~) - optional param in build()
#TODO: change border line of exisiting table
#TODO: set default settings of class (e.g., border) through staticmethod decorator
#TODO: justify values in rows left/right/centre
#TODO: presets of different types of tables (e.g., compact has no border in between rows)
#TODO: multiline values (i.e., wrapping)
#TODO: table to/from json, csv, etc.
#TODO: documentation
#TODO: testing (especially chaining of functions)