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




def thing(): 
        bill = int(input("Whats the bill?"))
        print(int(bill))
        quality = input("Whats the quality: bad, ok, good, great?")
        if quality == "bad":
                print (bill)
        if quality == "ok":
                print (bill * 1.1)
        if quality == "good":
                print (bill * 1.15)
        if quality == "great":
                print (bill * 1.2)

thing()