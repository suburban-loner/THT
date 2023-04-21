Space Complexity Analysis for ISBN13 Validator Code

Function: sum_13(isbn)
The sum_13 function takes an ISBN number as input and returns the sum of the product of each digit with 1 and 3 alternatively.

Function: isbn13(txt)
The isbn13 function takes an ISBN number as input and returns whether the number is valid or not. It also converts a 10-digit ISBN to a 13-digit one.

The worst-case space complexity of the isbn13 function depends on the length of the input txt and the number of memory allocations made. Let's break it down into smaller chunks:

txt = txt.replace("-", "").replace(" ", ""): This line replaces any hyphens or spaces with an empty string. The maximum length of the input is 13 digits, and the length of the output string will also be 13 digits. Therefore, the space complexity of this line is O(13).

if len(txt) == 13 and txt.isdigit() and int(txt[0:3]) == 978:: This line checks if the input string is valid according to the ISBN-13 format. It accesses the input string multiple times, and the maximum length of the input is 13 digits. Therefore, the space complexity of this line is O(13).

sum = 0: This line creates a new variable to store the sum of the product of each digit.

for i in range(0, 13):: This line creates a new range object with a length of 13.

if i % 2 == 0:: This line accesses the value of the variable i and performs a modulus operation. It does not allocate any new memory.

sum += int(txt[i]) and sum += int(txt[i]) * 3: These lines add new values to the variable sum based on the value of the input string. The maximum length of the input is 13 digits, and these lines are executed 13 times. Therefore, the space complexity of these lines is O(13).

if sum % 10 == 0:: This line performs a modulus operation on the value of the variable sum. It does not allocate any new memory.

return "Valid" or return "Invalid": These lines return a string. The length of the output string is constant, and it is not dependent on the length of the input. Therefore, the space complexity of these lines is O(1).

if len(txt) == 10:: This line checks if the input string is a 10-digit ISBN. It accesses the input string once, and the maximum length of the input is 13 digits. Therefore, the space complexity of this line is O(13).

sum = 0: This line creates a new variable to store the sum of the product of each digit.

for i in range(0, 10):: This line creates a new range object with a length of 10.

if i == 9 and txt[i] == "X":: This line accesses the value of the variable i and the input string. It does not allocate any new
