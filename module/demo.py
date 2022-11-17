from calc import add

def fun1():

    print("in fun 1 of demo")

def fun2():
    add()
    print("in fun 2 of demo")

def main():
    fun1()
    fun2()

if __name__=="__main__":
    main()