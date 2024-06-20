from functions import Rename_function 
from constants import _type, instruction_manual

_directory = input("Enter Your folder location:")
print("Enter your type of files you want to rename")
print("Options: a.Photo b.Video c.Text d.Code")
valid_inputs = ("a", "b", "c", "d")
while True:
  input_type = input("Enter in (a,b,c,d): ").lower()  # Convert input to lowercase
  if input_type in valid_inputs:
    break  # Exit the loop if input is valid
  else:
    print("Invalid input. Please enter a, b, c, or d.")

input_type = _type[input_type]

print(f"directory: {_directory}")
print(f"type: {input_type[1]}")
print(f"prompt: {input_type[0]}")



instruction = instruction_manual[input("Instruction : a. upper case  b. lower case  c.GEM: ")]
Rename_function(_directory, input_type[1], instruction)