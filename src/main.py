

def build_table(cols: list, rows: list):
    # raise TypeError if not lists?
    # handle unmatching numbers of cols to rows

    colLens = []
    # append longest value length for each col
    for i in range(len(cols)):
        colLens.append(max([len(row[i]) for row in rows] + [len(cols[i])]))

    # create formattings
    border = "+" + "+".join("{borderType}"*(colLen + 2) for colLen in colLens) + "+"
    values = "|" + "|".join(" {:<%d} " % colLen for colLen in colLens) + "|"

    print(border.format(borderType="="))
    print(values.format(*cols))
    print(border.format(borderType="="))
    for row in rows:
        print(values.format(*row))
        print(border.format(borderType="-"))


build_table(['fname', 'lname', 'age'],
            [['john', 'smith', '40'],
             ['jane', 'doe', '5'],
             ['joe', 'bloggs', '23']])

#TODO: insert into table
#TODO: delete from table
#TODO: make border characters constants that can be dependent on "style" of table (e.g., lines can be -, =, ~, etc.)
#TODO: justify values in rows left/right/centre
#TODO: different types of tables (e.g., compact has no border in between rows)
#TODO: multiline values (i.e., wrapping)