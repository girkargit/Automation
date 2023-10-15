item_in_cart = 0
# 2 item will be added in cart.
#
# if item_in_cart != 2:
#     raise Exception("Product count is not matching.")
#
# assert(item_in_cart == 2)

# try catch mechanism
try:
    with open('test1.txt' , 'r') as reader:
        data = reader.read()
except:
    print("File is not present. Failure in try block.")

# What actualy python show error
try:
    with open('test1.txt' , 'r') as reader:
        data = reader.read()
except Exception as e: # python error message stored in e variable.
    print(e)

# finally keyword
try:
    with open('test1.txt' , 'r') as reader:
        data = reader.read()
except Exception as e:
    print(e)
finally: # code will fail or not finally will definatly print.
    print("clearing up resources.")


