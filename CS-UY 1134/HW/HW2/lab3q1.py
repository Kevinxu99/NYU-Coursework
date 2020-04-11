def reverse_vowels(input_str):
    input_lst=[]
    for i in input_str:
        input_lst.append(i)
    reverse_lst=input_lst[::-1]
    for i in range(len(input_lst)):
        if(input_lst[i]=='o' or input_lst[i]=='i' or input_lst[i]=='a' or input_lst[i]=='e' or input_lst[i]=='u'):
             input_lst[i]=reverse_lst[i]
    return ''.join(input_lst)

print(reverse_vowels('tandon'))
