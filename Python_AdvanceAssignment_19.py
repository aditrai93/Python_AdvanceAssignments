"""1. Create a checker board generator, which takes as inputs n and 2 elements
to generate an n x n checkerboard with those two elements as alternating
squares."""
#%%

def checker_board(n,let1,let2):
    try:
        if let1==let2:
            board="Invalid"

        else:
            board=[[let1 if (i+j)%2==0 else let2 for j in range(n)]for i in range(n)]
        return board
    except Exception as e:
        print(e)

# %%
print(checker_board(4,"c","d"))
# %%
'''2. A string is an almost-palindrome if, by changing only one character, you
can make it a palindrome. Create a function that returns True if a string is an
almost-palindrome and False otherwise.'''

# %%
def almost_palindrome(string):
    try:
        s=string[::-1]
        c=0
        for i in range(len(string)):
            if s[i]==string[i] and c<=2:
                
                b=True
                continue
            else:
                
                if s[i]==string[len(string)-1-i] and i==len(string)-1 and c<=2:
                    b=True
                else:
                    b=False
                    c=c+1
        return b
    except Exception as e:
        print(e)
# %%
almost_palindrome("abccia")
# %%
'''3. Create a function that finds how many prime numbers there are, up to the
given integer.'''
def prime_num(n):
    li=[]
    for i in range(2,n):
        prime=True
        for j in range(2,n):
            if i%j==0 and i!=j:
                
                prime=False
                break
        if prime:
            li.append(i)
    return len(li)

# %%
prime_num(10)
# %%
'''4. If today was Monday, in two days, it would be Wednesday.
Create a function that takes in a list of days as input and the number of days
to increment by. Return a list of days after n number of days has passed.'''

def after_n_days(li,n):
    days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    l=[]
    for i in li:
        num=n
        print(i)
        ind=days.index(i)
        j=ind
        while num>0:
            # print(n)
            if j<=(len(days)-1):
                j=j+1
            if j>(len(days)-1):
                j=0
            num=num-1
        l.append(days[j])
    return l
                

# %%
after_n_days(["Monday","Sunday"],12)
# %%
'''5. You are in the process of creating a chat application and want to add an
anonymous name feature. This anonymous name feature will create an alias
that consists of two capitalized words beginning with the same letter as the
users first name.
Create a function that determines if the list of users is mapped to a list of
anonymous names correctly.'''

def is_correct_aliases(l1,l2):
    b=False
    for i,j in zip(l1,l2):

        s1=i.split(" ")
        let=s1[0][0]
        s2=j.split(" ")
        let2=s2[0][0]
        let3=s2[1][0]
        if let2==let and let3==let:
            b=True
    return b
        

# %%
is_correct_aliases(["Beth T."], ["Brandishing Mimosa"])
# %%
