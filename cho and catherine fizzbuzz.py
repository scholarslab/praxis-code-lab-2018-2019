# pseudo code so we remember how it works in two weeks
# first line gives us a whole number for input to work with
# second line starts a loop and makes it stop when we get to the input number (+1)
# then provides variable a which we are going to define later
# then in loop: if number it's looping through is divisible by three
# (aka nothing left at the end), instead of assigning that nothing to a, assign fizz
# same thing for if divisible by five
# which means we don't have to tell it about fizzbuzz for both it'll do that bc it's looping both
# then if the above two things don't apply, a = whatever the number is
# print a

x = int(input("Enter a number for when the FizzBuzz game is reached: "))
for i in range(1,x+1):
    a = ""
    if i % 3 == 0:
        a = a + "fizz"
    if i % 5 == 0:
        a = a + "buzz"
    if a == "":
        a = i
    print (a)