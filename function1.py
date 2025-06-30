def fibonaci(n,memo):
    if n in memo:
        return memo[n]
    if n<=1:
        return n
    memo[n]=fibonaci(n-1,memo) + fibonaci(n-2,memo)
    
    return memo[n]
memo={}
print(fibonaci(10,memo))



def add_dict(a,b=None):
    if b is None:
        b={}
    b[a]=a*a
    return b
print(add_dict(3))
print(add_dict(3,{1:1}))


def filter_integer(**karg):
    # for key,value in karg.items():
    #     if isinstance(value,int):
            
    return {k:v for k,v in karg.items() if isinstance(v,int)}

print(filter_integer(name="Rishi",value=4,c=5,d=5,e=0.5))


def outer_function():
    def inner_function(x):
        return x**2
    return inner_function

square=outer_function()
print(square(2))
