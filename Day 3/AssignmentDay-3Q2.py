def convert(data):
    if type(data) == str and data.startswith('(') and data.endswith(')'):
        res=[]
        a=data[1:-1].split(',')
        for i in a:
            res.append(int(i))
        return res
    if type(data)==list:
        res=[]
        for i in data:
            res.append(convert(i))
        return res
    return data
data=[[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
print(convert(data))