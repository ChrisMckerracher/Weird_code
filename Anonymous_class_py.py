def create_anon_class(*args):
    #define arguments such as, function names are in some dictionary.
    #all attributes can be put into a dictionary, and thus their default values
    #can be assigned.
    #otherwise, just having a string of a attribute will set it's default value
    #to its own name

    return (lambda z,*y:type.__new__(type,z,(object,),(lambda f:apply(lambda\
    *d:map(lambda e:d[0].update(e) or d[0],d[1:])[0],f) if len(f)>1 else f[0])\
    (map(lambda b:b if type(b)==dict else{str(b):b},y))))(*args)


create_anon_class('test','spec',{'getspec':lambda self: print(self.spec)})().getspec()
