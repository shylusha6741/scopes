gvar="global"
def outer():
    evar="enclosed"
    def  middle():
        midvar="middlevar"
        def inner():
            ivar="local"
            print("------Data Access from local scopes")
            print(ivar)
            print(midvar)
            print(evar)
            print(gvar)
        inner()
        print("--------Data Access From middle Scopes")
        print(ivar)
        print(midvar)
        print(evar)
        print(gvar)
    middle()
    print("-------Data Access From Enclose scopes")
    print(ivar)
    print(midvar)
    print(evar)
    print(gvar)
outer()
print("------Data Access From Global Scopes")
print(ivar)
print(midvar)
print(evar)
print(gvar)
