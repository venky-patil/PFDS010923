# Write a Python Program  which will return all the Different unique 
# vowels and its count that are present in the given String.

# Sample Cases:

# 1.String May be in Either Upper or Lower Case.
# 2.Result must give unique Vowels and its count.
# 3.If any string is having n repeating characters then only one character will be considered.
# 4. If the string is empty then return -1 and 0.

# Test Case:

# string1 = "edyoda"
# output = "eoa",3

# string2 = ""
# output = -1, 0

# Solution 
# =========

# 1st Approach 
# ============

# string1 = input("Enter String : ").lower()
# if len(string1)==0:
#     output = -1
#     count = 0

# else:
#     set1 = set(string1)#{'e","d",'y','o','a'}
#     vowels = {"a","e","i","o","u"} 
#     set3 = set1.intersection(vowels) #{'e','o','a'}
#     list1 = list(set3)#['e','o','a']
#     output = "".join(list1)#eoa
#     count = len(list1)
# print(output,count)

# 2nd Approach 
# =============

string1 = input("Enter String : ").lower()
if len(string1)==0:
    output = -1
    count = 0

else:
    list1 =set(string1)#{'e","d",'y','o','a'}
    vowels = ["a","e","i","o","u"] 
    list2 = []
    for i in list1: # e d y o a
        if i in vowels:
            list2.append(i) #[e,o,a]
    output = "".join(list2)#eoa
    count = len(list2)
print(output,count)




