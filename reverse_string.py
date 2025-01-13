#Reverse a string in Python without using any module/function
name = "Ankit Aggarwal"
rev_name_list = []
count = -1
for i in name:
    rev_name_list.insert(count,i)
    count = count - 1
    print(rev_name_list)

rev_name=''.join(rev_name_list)
print(type(rev_name))
print(rev_name)
