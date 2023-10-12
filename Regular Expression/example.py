# Example of Regular Expression 
# ==============================

import re 
matcher = re.finditer('abc','abcabcabcabc')
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())


import re 
matcher = re.finditer('ab','123@abaer@hdifu')
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())



# 1.[abc] --> either a,b,c 
# =========================

import re 
matcher = re.finditer("[abc]","a7b@9xbs")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())


# 2. [^abc] --> except a,b,c
# =============================

import re 
matcher = re.finditer("[^abc]","a7b@9xbs")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())



# 3. [a-z] --> any lower case Alphabets characters
# ======================================================


import re 
matcher = re.finditer("[a-z]","aABBCCDDx")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())


# 4. [A-Z] --> any upper case Alphabets characters
# ======================================================

import re 
matcher = re.finditer("[A-Z]","ABCxabhsZ")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())

    
# 5. [a-zA-z] --> Any alphabet either in upper case of in lower case.
# =====================================================================

import re 
matcher = re.finditer("[a-zA-Z]","123a@$#A*B^s")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())


# 6.[0-9] --> Any Digit 0 to 9
# ==============================

import re 
matcher = re.finditer("[0-9]","123a@$#A*B^s")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())


# 7. [a-zA-Z0-9] --> Any uppercase alphabet/Lower case alphabet and Digits.
# ============================================================================

import re 
matcher = re.finditer("[a-zA-Z0-9]","123a@$#A*B^s")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())

# 8. [^a-zA-Z0-9] --> Except uppercase alphabet/Lower case alphabet and Digits --> Special Character.
# ===================================================================================================

import re 
matcher = re.finditer("[^a-zA-Z0-9]","123a@$#A*B^s")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())

# Example of Customization Of Character Classes:
# ==============================


import re 
matcher = re.finditer("[a-d]","123a@bxe$#A*B^s") #Only a to d
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())


import re 
matcher = re.finditer("[xyz]","123a@bxe$#A*B^s") #Either x,y,z
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())


import re 
matcher = re.finditer("[^xyz]","123a@bxe$#A*B^s") #except x,y,z
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())

import re 
matcher = re.finditer("[A-D]","123a@bxe$#A*B^s") #Only Upper Alphabets between A-D
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())


import re 
matcher = re.finditer("[0-2]","123a@bxe$#A*B^s") #Only digits between 0-2
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())



import re 
matcher = re.finditer("[a-kA-C]","123a@bxe$#A*B^s") #lower case between a-k and upper case A-C
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())



import re 
matcher = re.finditer("[^a-kA-C0-2]","123a@bxe$#A*B^s") #except (lower case between a-k and upper case A-C digits between 0-2)
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())


# Example of re.match() Function 
# ================================

import re 
m = re.match('ab','abcabcxyz')
print(m)
if m!=None:
    print('Match Found')
else:
    print('Match not Found')

import re 
m = re.match('ab','xyzabcxyz')
print(m)
if m!=None:
    print('Match Found')
else:
    print('Match not Found')


# Example of re.search() Function 
# ================================

import re 
m = re.search('xy','abcabcxyz')
if m!=None:
    print('Match Found')
else:
    print('Match not Found')


# Example of re.fullmatch() Function 
# ==================================

import re 
m = re.fullmatch('abc','abcabcxyz')
if m!=None:
    print('Match Found')
else:
    print('Match not Found')

import re 
m = re.fullmatch('abcabcxyz','abcabcxyz')
if m!=None:
    print('Match Found')
else:
    print('Match not Found')


# Example of re.search() Function 
# ================================

import re 
m = re.search('xy','abcabcxyz')
if m!=None:
    print('Match Found')
else:
    print('Match not Found')


import re 
m = re.search('xya','abcabcxyz')
if m!=None:
    print('Match Found')
else:
    print('Match not Found')

# Example of re.findall() Function 
# ================================

import re 
m = re.findall('[a-z0-9]','a786AbcAZa@#')
print(m)#['a','7','8','6','b','c','a']


import re 
m = re.findall('[0-9]','a786AbcAZa@#')
print(m)#['7','8','6']


# Example of re.sub() Function 
# ==============================

import re
s = re.sub('[a-z]',"%","aA$$**bxAOP@@")
print(s)

s = re.sub('[0-9]',"&&@@","1ABCDEF991")
print(s)


# Example of re.subn() Function 
# ==============================

import re
s = re.subn('[a-z]',"%","aA$$**bxAOP@@")
print(s)

s = re.subn('[0-9]',"&&@@","1ABCDEF991")
print(s)

s = re.subn('[a-kA-C0-5]','ta','A99# aM**L')
print(s)

# Example of ^ Symbol 
# ====================

import re 

res = re.search("^Easy","Learning Python is Easy")
if res!=None:
    print("Target string started with the given pattern")
else:
    print("Target string not started with the given pattern")


import re 

res = re.search("^Learning","Learning Python is Easy")
if res!=None:
    print("Target string started with the given pattern")
else:
    print("Target string not started with the given pattern")


# Example of $ Symbol 
# ====================

import re 

res = re.search("Easy$","Learning Python is Easy")
if res!=None:
    print("Target string ended with the given pattern")
else:
    print("Target string not ended with the given pattern")


import re 

res = re.search("Learning$","Learning Python is Easy")
if res!=None:
    print("Target string ended with the given pattern")
else:
    print("Target string not ended with the given pattern")


# Example of Predefined Character Classes 
# =========================================

# 1. \s  --> Space Character
# ===========================


import re 
matcher = re.finditer("\s","aAB BC CDD x")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())




# 2. \S  --> Any Character except space characters
# ==================================================


import re 
matcher = re.finditer("\S","a C C x")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())



# 3. \d  --> Any digits from 0 to 9
# ====================================

import re 
matcher = re.finditer("\d","a9C5C8x")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())

# 4. \D  --> Except Any digits from 0 to 9
# ============================================

import re 
matcher = re.finditer("\D","a9C5C8x")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())




# 5. \w  --> Any word Character[a-zA-Z0-9]
# ===========================================

import re 
matcher = re.finditer("\w","a@@&&9C5%%C8@@x")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())



# 6. \W  --> Except Any word Character[a-zA-Z0-9]
# ===========================================

import re 
matcher = re.finditer("\W","a@@&&9C5%%C8@@x")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())


# 7. '.' --> Any Character including all space character.
# =========================================================


import re 
matcher = re.finditer(".","a@@&&9C5%%C8@@x")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())


# 1. a --> exactly one a 
# ========================

import re 
matcher = re.finditer("a","abbaa")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())



# 2. a+ -->  atleast one a 
# ===========================

import re 
matcher = re.finditer("a+","abbaaaa")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())


import re 
matcher = re.finditer("a+","abbaaxaabaaa")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())



import re 
matcher = re.finditer("x+","abbaaxaabxxa")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())

import re 
matcher = re.finditer("x+","abcxxabxxxxxxxxxlix")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())

import re 
matcher = re.finditer("b+","DDBBbbb@b@@bbbb")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())


# 3. a* --> any number of a  including 0
# ========================================

import re 
matcher = re.finditer("a*","abbaa")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())


import re 
matcher = re.finditer("b*","abbabab")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group()) 
                #    0              0              ""
                #    1              3              bb
                #    3              3               ""
                #    4              5               b 
                #    5              5              "" 
                #    6              7               b
                #    7              7              ""

import re 
matcher = re.finditer("b*","abbaab")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group())
                # 0                   0             ""
                # 1                   3             bb
                # 3                   3             ""
                # 4                   4             ""
                # 5                   6             b 
                # 6                   6             ""
           
# 4. a? --> atmost one a (Either 0 times a or one time a)
# ==========================================================

import re 
matcher = re.finditer("a?","abbaa")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group()) 
            # 0                      1               a 
            # 1                      1               ""
            # 2                      2               ""
            # 3                      4               a 
            # 4                      5               a


         
# 5. a{m} --> exactly m number of a 
# ==================================

import re 
matcher = re.finditer("a{5}","abbaaaaaaaaa")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group()) 


import re 
matcher = re.finditer("a{3}","abbaaaaaaaaa")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group()) 

import re 
matcher = re.finditer("a{2}","abbaaaaaaaaa")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group()) 

# 6. a{m,n} --> minimum m number of a and maximum n number of a.
# ================================================================

import re 
matcher = re.finditer("a{2,5}","abbaaaaaaaaaxxaa")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group()) 


import re 
matcher = re.finditer("a{3,8}","abbaaaaaaaaaxxaa")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group()) 

import re 
matcher = re.finditer("a{3,8}","abbaabaaaaxxaa")
for i in matcher:
    print(str(i.start())+"  "+str(i.end())+" "+i.group()) 



# Mobile Number Validation 
# =========================

import re 

mobile_no = int(input('Enter a Number : '))
mobile_no = str(mobile_no)
m=re.fullmatch('[6-9][0-9]{9}',mobile_no)
if m!=None:
    print("Mobile Number is Valid")
else:
    print("Mobile Number is not Valid")
