# Ni-a
Willing to learn something new

customer_name = str(input("Enter Customer Name: "))
contact_no = str(input("Enter your Contact No. : "))
address = str(input("Enter your Address: "))

print("========================================")

# Product 1
product1_name = str(input("Enter product name: "))
price1 = float(input("Enter price: "))
quantity1 = int(input("Enter quantity: "))
discount1 = float(input("Enter discount: "))

subtotal1 = price1 * quantity1
receipt1 = subtotal1 - discount1

print("========================================")

# Product 2
product2_name = str(input("Enter product name: "))
price2 = float(input("Enter price: "))
quantity2 = int(input("Enter quantity: "))
discount2 = float(input("Enter discount: "))

subtotal2 = price2 * quantity2
receipt2 = subtotal2 - discount2

print("========================================")

# Product 3
product3_name = str(input("Enter product name: "))
price3 = float(input("Enter price: "))
quantity3 = int(input("Enter quantity: "))
discount3 = float(input("Enter discount: "))

subtotal3 = price3 * quantity3
receipt3 = subtotal3 - discount3

# Total
total = receipt1 + receipt2 + receipt3

print("========================================")
print("Customer Name:", customer_name)
print("Contact No.:", contact_no)
print("Address:", address)
print("----------------------------------------")

print("Product 1:", product1_name)
print("Price:", price1)
print("Quantity:", quantity1)
print("Discount:", discount1)
print("Subtotal:", subtotal1)
print("Total:", receipt1)

print("----------------------------------------")

print("Product 2:", product2_name)
print("Price:", price2)
print("Quantity:", quantity2)
print("Discount:", discount2)
print("Subtotal:", subtotal2)
print("Total:", receipt2)

print("----------------------------------------")

print("Product 3:", product3_name)
print("Price:", price3)
print("Quantity:", quantity3)
print("Discount:", discount3)
print("Subtotal:", subtotal3)
print("Total:", receipt3)

print("----------------------------------------")
print("TOTAL:", total)
print("========================================")
