import collections
import itertools

class Polynomial(object):
    def __init__(self, *args):
        """
        Create a polynomial in one of three ways:

        p = Polynomial(poly)           # copy constructor
        p = Polynomial([1,2,3 ...])    # from sequence
        p = Polynomial(1, 2, 3 ...)    # from scalars
        """
        if len(args)==1:
            val = args[0]
            if isinstance(val, Polynomial):                # copy constructor
                self.coeffs = val.coeffs[:]
            elif isinstance(val, collections.Iterable):    # from sequence
                self.coeffs = list(val)
            else:                                          # from single scalar
                self.coeffs = [val+0]
        else:                                              # multiple scalars
            self.coeffs = [i+0 for i in args]
        self.trim()
    
    def trim(self):
        "Remove trailing 0-coefficients"
        _co = self.coeffs
        if _co:
            offs = len(_co)-1
            if _co[offs]==0:
                offs -= 1
                while offs >= 0 and _co[offs]==0:
                    offs -= 1
                del _co[offs+1:]