"""In a given list of elements, all elements are equal except the one.Write a code to find the odd man out (Stray number)"""

element_list = list(map(int, input().split()))
element_dict = {}
count = 0
for i in element_list:
    if i in element_dict.keys():
        element_dict[i] += 1
    else:
        element_dict[i] = 1
for key, value in element_dict.items():
    if value == 1:
        print(key)
