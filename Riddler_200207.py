## Riddler Express

# Riddler Classic
# How many different values can the expression
# |-1|-2|-3|-4|-5|-6|-7|-8|-9| have?

# This list will contain bracket_arrs of all possible inner/outer bracket_arr possibilities
# 1 signifies an inner bracket
# 0 signifies an outer bracket
num_ints = 9
num_bracket = num_ints+1
bracket_mat = [[]]

while(len(bracket_mat[0]) < num_bracket):
   
   for bracket_arr in bracket_mat:
      
      if len(bracket_arr) < num_bracket:
         
         nInner = bracket_arr.count(1)
         nOuter = bracket_arr.count(0)
   
         if(nOuter == nInner):                                                                            
            bracket_arr.append(1)                    
            
         elif(nInner == num_bracket/2):                                                                                  
            bracket_arr.append(0)
            
         elif((nOuter != nInner) and (nInner != num_bracket/2)):
            # The list() function is necessary to avoid temp_bracket_arr referencing the
            # same memory location as bracket_arr. This is a unique behavior of python.
            temp_bracket_arr = list(bracket_arr)
            
            bracket_arr.append(1)
            temp_bracket_arr.append(0)
            
            bracket_mat.append(temp_bracket_arr)
            

print("There are",len(bracket_mat),"unique expressions")

# Number before an inner implies multiplication is next operation
# Number before an outer implies subtraction is next operation

numbers = ['-1','-2','-3','-4','-5','-6','-7','-8','-9']
first = 'abs('
inner = '*abs('
outer = ')'
expr_values = []

for bracket_arr in bracket_mat:
   
   bracket_strings = []
   
   for ii in range(len(bracket_arr)):
      if ii == 0:
         bracket_strings.append(first)
      elif bracket_arr[ii] == 1:
         bracket_strings.append(inner)
      elif bracket_arr[ii] == 0:
         bracket_strings.append(outer)
         
   
   expression = bracket_strings[0]
   
   for ii in range(num_ints):
      
      expression = expression + numbers[ii] + bracket_strings[ii+1]
   
   expr_value = eval(expression)
   expr_values.append(expr_value)

expr_set = set(expr_values)   
print("There are",len(expr_set),"unique values")
print(expr_set)