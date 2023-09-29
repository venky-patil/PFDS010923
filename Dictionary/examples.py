# Example of Creation of Dictionary
# ==================================

d = {}
print(type(d))

d=dict()
print(type(d))

d = {"name":"Pratyush","Batch":"Edyoda Digital University"}
print(type(d))

# Example of Adding an Element in Dictionary
# ============================================

d = {}
d["Employee Number"] = 100
d["Empoloyee Name"] = "Ansh Srivastava"
d["Employee Location"] = "Hyderabad"
print(d)

# Example of Accessing an Element in Dictionary
# ==============================================

d = {'Employee Number': 100, 'Empoloyee Name': 'Ansh Srivastava', 'Employee Location': 'Hyderabad'}
print(d['Empoloyee Name'])#Ansh Srivastava 
print(d['Employee Number'])#100
# print(d[10])# Key Error


# Example of Update the Value of a dictionary
# =============================================

d = {'Employee Number': 100, 'Empoloyee Name': 'Ansh Srivastava', 'Employee Location': 'Hyderabad'}
print(d)
d['Empoloyee Name'] = "Pratyush Srivastava"
d['Employee Number'] = 250
print(d)

# Example of Deletion of a Key Value Pair
# ========================================

d = {'Employee Number': 100, 'Empoloyee Name': 'Ansh Srivastava', 'Employee Location': 'Hyderabad'}
print(d)
del d['Employee Number']
print(d)


# Example of Deletion of Complete Dictionary
# ===========================================


d = {'Employee Number': 100, 'Empoloyee Name': 'Ansh Srivastava', 'Employee Location': 'Hyderabad'}
print(d)
del d
# print(d) #Error


# Example of Len() Function 
# ============================

d = {'Employee Number': 100, 'Empoloyee Name': 'Ansh Srivastava', 'Employee Location': 'Hyderabad'}
print(len(d))

# Example of Clear() Function
# =============================

d = {'Employee Number': 100, 'Empoloyee Name': 'Ansh Srivastava', 'Employee Location': 'Hyderabad'}
print(d)
d.clear()
print(d)


# Example of Pop() Function 
# ===========================

d = {'Employee Number': 100, 'Empoloyee Name': 'Ansh Srivastava', 'Employee Location': 'Hyderabad'}
print(d.pop('Employee Number'))#100
print(d)

d = {'Employee Number': 100, 'Empoloyee Name': 'Ansh Srivastava', 'Employee Location': 'Hyderabad'}
# print(d.pop('Employee Salary'))#Error
# print(d)

# d = {}
# print(d.pop('Employee Salary'))#Error
# print(d)


# Example of PopItem() Function 
# ==============================

d = {'Employee Number': 100, 'Empoloyee Name': 'Ansh Srivastava', 'Employee Location': 'Hyderabad'}
print(d)
print(d.popitem())#('Employee Location','Hyderabad')
print(d)


d = {}
# print(d)
# print(d.popitem())#Error


# Example of Get() Function 
# ==========================

d = {'Employee Number': 100, 'Empoloyee Name': 'Ansh Srivastava', 'Employee Location': 'Hyderabad'}
print(d.get('Employee Number'))#100
print(d.get('Empoloyee Name'))#Ansh Srivastava 
print(d.get('Employee Salary')) #None


# Example of Accessing Operator 
# =============================

d = {'Employee Number': 100, 'Empoloyee Name': 'Ansh Srivastava', 'Employee Location': 'Hyderabad'}
print(d['Employee Number'])#100
print(d['Empoloyee Name'])#Ansh Srivastava 
# print(d['Employee Salary']) #Error


# Example of update() Function 
# ==============================

d1 = {"name":"Ayush","Class":"12th","Roll No":56,"Address":"Delhi"}
d2 = {"Grade":"A","Rank":"5th","IsTopper":False}
d1.update(d2)
print(d1) #{'name': 'Ayush', 'Class': '12th', 'Roll No': 56, 'Address': 'Delhi', 'Grade': 'A', 'Rank': '5th', 'IsTopper': False}


# Iterations Over a Dictionaries 
# ===============================
d = {'name': 'Ayush', 'Class': '12th', 'Roll No': 56, 'Address': 'Delhi', 'Grade': 'A', 'Rank': '5th', 'IsTopper': False}
for i in d:
    print(i)

# Example of Keys() Function 
# ===========================

d = {'name': 'Ayush', 'Class': '12th', 'Roll No': 56, 'Address': 'Delhi', 'Grade': 'A', 'Rank': '5th', 'IsTopper': False}
print(d.keys())#
for i in d.keys():
    print(i)



# Example of Values() Function 
# ===========================

d = {'name': 'Ayush', 'Class': '12th', 'Roll No': 56, 'Address': 'Delhi', 'Grade': 'A', 'Rank': '5th', 'IsTopper': False}
print(d.values())#dict_values(['Ayush', '12th', 56, 'Delhi', 'A', '5th', False])
for i in d.values():
    print(i)

# Example of Items() Function 
# =============================

d = {'name': 'Ayush', 'Class': '12th', 'Roll No': 56, 'Address': 'Delhi', 'Grade': 'A', 'Rank': '5th', 'IsTopper': False}
print(d.items())#dict_items([('name', 'Ayush'), ('Class', '12th'), ('Roll No', 56), ('Address', 'Delhi'), ('Grade', 'A'), ('Rank', '5th'), ('IsTopper', False)])
for key,values in d.items():
    print(key,values)

# Example of Mutability in case of Dictionary.
# ==============================================
d = {'name': 'Ayush', 'Class': '12th', 'Roll No': 56, 'Address': 'Delhi', 'Grade': 'A', 'Rank': '5th', 'IsTopper': False}
print(d,id(d))
d['name'] = "Ravi"
d['Address'] = "Noida"
d['Class'] = 'Graduation'
print(d,id(d))

# Example of Operators with Dictionary:
# ======================================
d1 = {10:20,30:40}
d2 = {50:60,70:80}
print(d1+d2) #Error
print(d1*d2)#Error
