def create_anon_class(*args):
    #define arguments such as, function names are in some dictionary.
    #all attributes can be put into a dictionary, and thus their default values
    #can be assigned.
    #otherwise, just having a string of a attribute will set it's default value
    #to its own name

    return (lambda *y:type.__new__(type,"",(object,),(lambda f:apply(lambda\
    *d:map(lambda e:d[0].update(e) or d[0],d[1:])[0],f) if len(f)>1 else f[0])\
    (map(lambda b:b if type(b)==dict else{str(b):b},y))))(*(args + (kwargs,)))


create_anon_class('spec',{'getspec':lambda self: print(self.spec)}, test='hello world', gettest=(lambda self: print(self.test)))().gettest()
