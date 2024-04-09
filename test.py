name = "Kory"

print(name)

def say_hello():
    print("Hello")
    print("I'm inside")


print("I'm inside")

# call the fn
say_hello()

# array js -> list python
prices = [1,3,4,5,6,7]

# add
prices.append(9)

print(prices)

# sum all the prices 
total= 0
for price in prices:
    total += price
    
print(total)

# dictionary 
me = {
    "name": "Kory",
    "age": 31,
    "hobbies": [],
    "address": {
        "street": "Daffodil",
        "city": "Oceanside"
    }
    
}

print(me)

# read 
print(me["name"])

# warning: reading a ket that does not exist 

if "last" in me:
    print(me["last"])

# modify

me["age"] = 99

# add keys
me ["last"] ="Plotts"

print("THE END!!!")