# CPE 101 Lab 4
# Name:

def main():
   table_size = get_table_size()
   while table_size != 0:
      first = get_first()
      incr = get_increment()
      show_table(table_size, first, incr)
      table_size = get_table_size()

# Obtain a valid table size from the user
def get_table_size():
   size = int(input("Enter number of rows in table (0 to end): "))

   while size < 0:
      print("Size must be non-negative.")
      size = int(input("Enter number of rows in table (0 to end): "))
      
   return size;

# Obtain the first table entry from the user 
def get_first():
   first = int(input("Enter the value of the first number in the table: "))

   while first < 0:
      print("First numer must be non-negative.")
      first = int(input("Enter the value of the first number in the table: "))

   return first;

def get_increment():
   incr = int(input("Enter the increment between rows: "))

   while incr < 0:
      print("Increment must be non-negative.")
      incr = int(input("Enter the increment between rows: "))

   return incr;

# Display the table of cubes
def show_table(size, first, incr):
   print("Number  Cube")
   i = 0
   total = 0
   for i in range(first, size):
      print("%-6d   %d" % (first + incr * i, (first + incr * i)**3))
      total = total + (first + incr * i)**3
   print("\nThe sum of the cubes is: ", total,"\n")
   #print("A cube table of size %d will appear here starting with %d." % (size, first))
   
   
   # Insert Loop Here
   

if __name__ == "__main__":
   main()
