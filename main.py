matrix =  [[1,5,8],#první řádek
          [5,6,6], #druhý řádek a změna druhého čísla na číslo 105
          [9,7,5]]#třetí řádek
          

#přidání čísla 105
matrix[1][1] = 105

#přídání nového řádku
matrix.append([0, 0, 0])
for row in matrix:
    row.append(0)


#vytisknutí řádků a sloupců
for x in matrix:
    print(x)

    
