def column_converter(column): 
    conversion = 0
    for i in range(0, len(column)):
        conversion += (ord(column[i])-64) *26**i
    print(column)
    print(conversion)

column_converter("ZZZZZZZZZZZZZZZ")
column_converter("A")
column_converter("D")
column_converter("AA")
column_converter("ZZ")
column_converter("AAA")
