def outer_function(x):
    def inner_function(y):
        return x+y
    return inner_function
#함수 중첩 선언 : 클로저 현상 발생
closure_instance = outer_function(10)
print(closure_instance)
result=closure_instance(5)
print(result)