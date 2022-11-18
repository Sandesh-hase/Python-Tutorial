
def div(a,b):
    return a/b

d= div(2,4)
print(d)   # Here whrn mu numerator is samlaar than denominator o/p is less than 1
            # what is  want o/p always >1

# Lets use decoratoe to decorate the div funcion

def smart_div(fun):

    def div_gt_1(a,b):
        if a<b:
            a,b = b,a
        return fun(a,b)
    return div_gt_1

div=smart_div(div)
d=div(2,4)

print(d)
