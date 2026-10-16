#WAF to print the length of a list
def len_list(var):
    print(len(var))

anime = ["Your Name", "Weathering with you", "Suzume"]
movies = ["Infinity war", "End game", "Far from home", "Brand New Day"]

len_list(anime)
len_list(movies)


#WAF to print the elements of a list
el1 = [1,3 ,2,3,4,6,4]
el3 = ["a", "b", "c", "d"]

def el_print(el):
    for i in el:
        print(i, end=", ")

el_print(el3)
print()


#WAF to find the factorial of n.
n = int(input("Enter the number: "))

def facto(n):
    fac = 1

    for i in range(1, n+1):
        fac *= i
    print(fac)

    #while fac <= n:
    #    sum *= fac  
    #    fac += 1
    #print(sum)

facto(n)  


#WAF to convert USD to INR
usd_sum = float(input("Enter USD amount: ",))

def conv(a):
    sum = a * 96.73
    print(sum, "INR")

conv(usd_sum)


#WAF to find even or odds
num = int(input("enter numbers: "))

def ev_odd(var):
    if (var/2 == 0):
        print(var, "is even")
    else:
        print("is odd")

ev_odd(num)

#Write a recursive function to calculate the sum of first n natural numbers
a = int(input("Enter natural number: "))

def re(n):
    if (n == 0):
        return 0
    else:
        return n + re(n-1)

print(re(a))


#Write a recursive function to print all elements in a list

def re1(n, idx=0):
    if (len(n) == idx):
        return
    else:
        print(n[idx])
        re1(n, idx + 1)

re1(anime)