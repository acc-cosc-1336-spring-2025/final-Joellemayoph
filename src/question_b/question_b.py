#write functions here, don't add input('') statements here!
def create_multiplication_table(length, height):
    list = []

    for r in range(1,length+1):
        row = [] 
        for c in range(1,height+1):
            c = r * c 
            row.append(c)
        list.append(row)

    return list

def display_multiplication_table(length, height):
    list = create_multiplication_table(length,height)

    for row in list:
        for column in row: 
            print(column, ' ' , end='')
        print()

