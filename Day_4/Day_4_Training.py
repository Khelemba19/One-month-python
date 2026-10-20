#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
str1 = ['Thirty', 'Days', 'Of', 'Python']
new_str1 = " ".join(str1)
print(new_str1)


#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
str2 = "Coding"
str3 = "For"
str4 = "All"
new_str2 = str2 + " " + str3 + " " + str4
print(new_str2)


#Declare a variable named company and assign it to an initial value "Coding For All".Print the variable company using print(). Print the length of the company string using len() method and print(). Change all the characters to uppercase letters using upper() method. Change all the characters to lowercase letters using lower() method.Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All. Cut(slice) out the first word of Coding For All string. Check if Coding For All string contains a word Coding using the method index, find or other methods.Replace the word coding in the string 'Coding For All' to Python.Change "Python for Everyone" to "Python for All" using the replace method or other methods.Split the string 'Coding For All' using space as the separator (split()). "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma. What is the character at index 0 in the string Coding For All. What is the last index of the string Coding For All. What character is at index 10 in "Coding For All" string. Create an acronym or an abbreviation for the name 'Python For Everyone'. Create an acronym or an abbreviation for the name 'Coding For All'. Use index to determine the position of the first occurrence of C in Coding For All.Use index to determine the position of the first occurrence of F in Coding For All. Use rfind to determine the position of the last occurrence of l in Coding For All People. 

company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[0: 6])
print("The word 'Coding' is in index: ",company.find("Coding"))
print(company.startswith("Coding"))
new_company = company.replace("Coding", "Python")
company2 = "Python for Everyone"
print(company2.replace("Everyone", "All"))
print(company.split())
company3 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(company3.split(", "))
print("The first character at the string 'Coding for All' is: ", company[0])
print("The 10th character at the string 'Coding for All' is: ", company[9])
py4e = "Python For Everyone"
c4a = "Coding For All"
print(c4a.find("C"))
print(c4a.find("F"))
print(c4a.rfind("l"))


#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

word = "You cannot end a sentence with because because because is a conjunction"
print(word.find("because"))
print(word.index("because"))
print(word.rfind("because"))
print(word.rindex("because"))
slice_word = word[31:54]
print(slice_word)


#Does 'Coding For All' start with a substring Coding?
#Does 'Coding For All' end with a substring coding?
#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
#Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python

print(company.startswith("Coding"))
print(company.endswith("coding"))

company4 = '   Coding For All      '
print(company.strip())

var1 = "30DaysOfPython"
var2 = "thirty_days_of_python"
print(var1.isidentifier())
print(var2.isidentifier())


#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
company5 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
new_company5 = "# ".join(company5)
print(new_company5)

print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\ Age\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, area))

a = 8
b = 6
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a-b))
print("{} * {} = {}".format(a, b, a*b))
print("{} / {} = {}".format(a, b, a*b))
print("{} % {} = {}".format(a, b, a%b))
print("{} // {} = {}".format(a, b, a//b))
print("{} ** {} = {}".format(a, b, a**b))