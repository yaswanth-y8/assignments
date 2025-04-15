lst = [1,2,3,[1,2,3,[3,4],2]]

def flatten(lst):
    res = []
    for i in lst:
        if type(i) == list:
            res+=flatten(i)
        else:
            res.append(i)
    return res
print(flatten(lst))