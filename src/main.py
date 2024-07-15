

def build_table(cols: list, rows: list):
    # raise TypeError if not lists?

    colLens = []
    for i in range(len(cols)):
        colLens.append(max([len(row[i]) for row in rows] + [len(cols[i])])) #append longest value length for each col

    


table_data = [
    ['column1', 'column2'],
    [['value1', 'value2'],
     ['value1', 'value2'],
     ['value1', 'value2']]
]

build_table(table_data[0], table_data[1])

#TODO: insert into table
#TODO: delete from table
#TODO: mnake border characters constants that can be dependent on "style" of table (e.g., lines can be -, =, ~, etc.)