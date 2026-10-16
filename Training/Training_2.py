#Sets and dictionaries
dict = {
    "table" : ["a piece of furniture", "list of facts and figures"],
    "cat" : "a small animal"
}
print(dict)

subjects = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print("the no. of classroom required :", len(subjects))

marks = {}
chem = int(input("enter chem marks: "))
marks.update({"chem" : chem})
phy = int(input("enter phy marks: "))
marks.update({"phy" : phy})
bio = int(input("enter bio marks: "))
marks.update({"bio" : bio})
print(marks)

val = {
    ("float", 8.0),
    ("int", 8)
}
print(type(val))