dimensions = input("Please input the layer size (N M): ")

dimensions_list = dimensions.split()

rows = int(dimensions_list[0])
cols = int(dimensions_list[1])

if cols and rows > 100:
   print("The size must be smaller than 100.")
   exit()

if cols % 2 != 0 and rows % 2 != 0:
   print("You should input even numbers")
   exit()
   
first_layer = []
   
for i in range(rows):
   numbers = input().split()
   if len(numbers) != cols:
      print("Invalid input")
      exit()
   first_layer.append(numbers)

second_layer = [[0 for i in range(cols)] for j in range(rows)]

current_number = 1

for n in range(rows):
   for m in range(cols - 1):
      if second_layer[n][m] != 0:
         continue
      if first_layer[n][m] != first_layer[n][m + 1]:
         # Placing horizontal brick
         second_layer[n][m] = current_number
         second_layer[n][m + 1] = current_number
      else:
         # Placing vertical brick
         second_layer[n][m] = current_number
         second_layer[n + 1][m] = current_number
      current_number += 1
   # If we don't have a brick on the last column because we couldn't place a horizontal brick there,
   # place a vertical brick on it
   if second_layer[n][cols - 1] == 0:
      second_layer[n][cols - 1] = current_number
      second_layer[n + 1][cols - 1] = current_number
      current_number += 1

for n in range(rows):
   if n == 0:
      print('-' * cols * 2)
   row_string = ""
   for m in range(cols - 1):
      row_string += str(second_layer[n][m])
      if second_layer[n][m] != second_layer[n][m + 1]:
         row_string += "-"
      else:
         row_string += " "
   row_string += str(second_layer[n][cols - 1])
   print(row_string)
   if n % 2 != 0:
      print('-' * cols * 2)