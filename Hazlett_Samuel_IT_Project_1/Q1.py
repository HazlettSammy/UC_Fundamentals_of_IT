Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def main():
...     # Asking for the cost of item1 and item2
...     cost_item1 = float(input("What is the cost of item1? "))
...     cost_item2 = float(input("What is the cost of item2? "))
... 
...     # Calculating the total cost including 8% sales tax
...     total_cost = cost_item1 + cost_item2 + (cost_item1 + cost_item2) * 0.08
... 
...     # Displaying the total cost
...     print("The total cost is:", round(total_cost, 2))
... 
... if __name__ == "__main__":
...     main()
... 
SyntaxError: invalid syntax
