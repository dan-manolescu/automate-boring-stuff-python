#! python3
# tablePrinter.py - Take a list of strings and display it in a
# well-organized table with each column right-justified.

tableData = [
                ['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'moose', 'goose']
            ]

def printTable(tableData):

    # First let's figure out for each column what is the widest string.
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        colWidth = 0
        for row in tableData[i]:
            colWidth = max(colWidth, len(row))
        colWidths[i] = colWidth

    # Then let's justify each string based on the column max width.
    for i in range(len(tableData[0])):
        for j in range(len(colWidths)):
            print(tableData[j][i].rjust(colWidths[j]), end=' ')
        print()


printTable(tableData)
