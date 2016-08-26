
def create_anon_class(*args, **kwargs):
    #define arguments such as, function names are in some dictionary.
    #all attributes can be put into a dictionary, and thus their default values
    #can be assigned.
    #otherwise, just having a string of a attribute will set it's default value
    #to its own name

    return (lambda *y:type.__new__(type,"",(object,),(lambda f:[(lambda:(f[0].\
            update(f.pop())))() for x in range(len(f)-1)] and f if len(f)>0 \
            else f)([(lambda x:x if type(x)==dict else {str(x):x})(x) for x \
            in y])[0]))(*(args + (kwargs,)))


create_anon_class('spec',{'getspec':lambda self: print(self.spec)}, test='hello world', gettest=(lambda self: print(self.test)))().gettest()


    
