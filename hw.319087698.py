def my_func(x1, x2, x3):
    try:
        if x1+x2+x3==0:
           return print('Not a number – denominator equals zero')
        if type(x1)!=float or type(x2)!=float or type(x3)!=float:
               return print('Error: parameters should be float')
        m=(x1 + x2 + x3) * (x2 + x3) *x3
        c=(x1 + x2 + x3)
        value=float(m / c)
        return value
    except:
        return "none"


def convert(hours, minutes) :
            if hours<0 or minutes<0:
                return print("Input error!")
            else:
                t=60*60*hours+60*minutes
                return t





