#%%
"""3. Write a method that accepts two integer parameters rows and cols. The output is a 2d array of numbers displayed in column-major order,
 meaning the numbers shown increase sequentially down each column and wrap to the top of the next column to the right once the bottom of the current column is reached."""
def printGrid(row,col):
    num=1
    grid=[]
    for i in range(col):
        r=[]
        for j in range(row):
            r.append(num)
            num=num+1
        grid.append(r)
    return [[row[i] for row in grid] for i in range(len(grid[0]))]
# %%
printGrid(5,3)
# %%
"""4. Given a list of integers, return the smallest positive integer not present in
the list."""
def missint(li):
    s=min(li)
    e=max(li)
    for i in range(s,e):
        if i >0 and i not in li:
            print(i)
            break
        

# %%
missint([0, 4, 4, -1, 9, 4, 5, 2, 10, 7, 6, 3, 10, 9])
# %%
"""5. Google is launching a network of autonomous pizza delivery drones and wants you to create a flexible rewards system (Pizza Points™) that can be tweaked in the future.
 The rules are simple: if a customer has made at least N orders of at least Y price, they get a FREE pizza!

Create a function that takes a dictionary of customers, a minimum number of orders and a minimum order price. Return a list of customers that are eligible for a free pizza.
"""
def pizza_points(cust,min_ord,min_price):
    customer=[]
    for i in cust:
        if len([x for x in cust[i] if x>=min_price])>=min_ord:
            customer.append(i)
    return customer

# %%
customers = {
  "Batman": [22, 30, 11, 17, 15, 52, 27, 12],
  "Spider-Man": [5, 17, 30, 33, 40, 22, 26, 10, 11, 45]
}

# %%
pizza_points(customers,5,100)
# %%
