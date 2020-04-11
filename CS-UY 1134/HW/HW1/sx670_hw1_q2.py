def shift(lst,k,d='left'):
    if (d=='left'):
        for i in range(k):
            lst.append(lst.pop(0))
    else:
        for i in range(k):
            lst.insert(0,lst.pop())

