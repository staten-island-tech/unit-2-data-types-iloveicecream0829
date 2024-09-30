# write_a_sentence = input("write a sentence")
# if write_a_sentence == "Do you like icecream?":
#     print("correct")
# else:
#     print("incorrect")


# def evenodd():
#     evenodd = int(input("input a number: "))
#     if evenodd % 2 == 0:
#         print("even")
#     else:
#         print("odd")
# evenodd()




# def thing(): 
#         bill = int(input("Whats the bill?"))
#         print(int(bill))
#         quality = input("Whats the quality: bad, ok, good, great?")
#         if quality == "bad":
#                 print (bill)
#         if quality == "ok":
#                 print (bill * 1.15)
#         if quality == "good":
#                 print (bill * 1.2)
#         if quality == "great":
#                 print (bill * 1.25)

# thing()

def fac():
        num = int(input("Please enter the number you want the factor of."))
        












def fgcf(a, b):
        while b:
                a, b = b, a % b
        return a

def gcf():
        a = int(input("Input a number you want the gcf of: "))
        b = int(input("Input another number you want the gcf of: "))
        gcf_value = fgcf(a, b)
        print(f"The factor of {a} and {b} is {gcf_value}.")

gcf()
        