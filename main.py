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
            elif isinstance(val, list):                    # from sequence
                self.coeffs = val
            else:                                          # from single scalar
                self.coeffs = [val]
        else:                                              # multiple scalars
            self.coeffs = [i+0 for i in args]
        self.trim()

    def __add__(self, val):
        "Return self+val"
        if isinstance(val, list):                          # add sequence
            x = self.coeffs
            x.reverse()
            val.reverse()
            res = [a+b for a,b in itertools.zip_longest(x, val, fillvalue=0)]
            res.reverse()
        elif isinstance(val, Polynomial):                    # add Polynomial
            x = self.coeffs
            x.reverse()
            y = val.coeffs
            y.reverse()
            res = [a+b for a,b in itertools.zip_longest(x, y, fillvalue=0)]
            res.reverse()
        else:                                              # add scalar
            if self.coeffs:
                res = self.coeffs
                res[len(self.coeffs)-1] += val
            else:
                res = [val]
        return self.__class__(res)

    def __eq__(self, val):
        "Test self==val"
        if isinstance(val, Polynomial):
            return self.coeffs == val.coeffs
        else:
            return len(self.coeffs)==1 and self.coeffs[0]==val

    def __mul__(self, val):
        "Return self*val"
        _s = self.coeffs
        _v = []
        if isinstance(val, Polynomial):
            _v = val.coeffs
        elif isinstance(val, list):
            _v = val
        else:
            _v = [val]
        _v.reverse()
        _s.reverse()
        res = [0]*(len(_v)+len(_s)-1)
        for i in range(len(_v)):
            for j in range(len(_s)):
                res[i+j] += _s[j]*_v[i]
        res.reverse()
        return self.__class__(res)

    def __truediv__(self, val):
        Poly1 = self.coeffs
        Poly2 = ( self.__class__(val) ).coeffs
        Poly1.reverse()
        Poly2.reverse()

        if len(Poly1) >= len(Poly2):
            #make them same size
            shiftlen = len(Poly1) - len(Poly2)
            Poly2 = [0] * shiftlen + Poly2
        else:
            Poly1.reverse()
            return self.__class__([0]), self.__class__(Poly1)
        
        quot = []
        divisor = float(Poly2[-1])
        for i in range(shiftlen + 1):
            mult = Poly1[-1] / divisor
            quot = [mult] + quot

            if mult != 0:
                d = [mult * u for u in Poly2]
                Poly1 = [u - v for u, v in zip(Poly1, d)]

            Poly1.pop()
            Poly2.pop(0)
        
        quot.reverse()
        Poly1.reverse()
        return self.__class__(quot) , self.__class__(Poly1)

    def __rtruediv__(self, val):
        Poly2 = self.coeffs
        Poly1 = ( self.__class__(val) ).coeffs
        Poly1.reverse()
        Poly2.reverse()

        if len(Poly1) >= len(Poly2):
            #make them same size
            shiftlen = len(Poly1) - len(Poly2)
            Poly2 = [0] * shiftlen + Poly2
        else:
            Poly1.reverse()
            return self.__class__([0]), self.__class__(Poly1)
        
        quot = []
        divisor = float(Poly2[-1])
        for i in range(shiftlen + 1):
            mult = Poly1[-1] / divisor
            quot = [mult] + quot

            if mult != 0:
                d = [mult * u for u in Poly2]
                Poly1 = [u - v for u, v in zip(Poly1, d)]

            Poly1.pop()
            Poly2.pop(0)
        
        quot.reverse()
        Poly1.reverse()
        return self.__class__(quot) , self.__class__(Poly1)

    def __neg__(self):
        "Return -self"
        return self.__class__([-co for co in self.coeffs])

    def _radd__(self, val):
        "Return val+self"
        return self+val

    def __repr__(self):
        return "{0}({1})".format(self.__class__.__name__, self.coeffs)

    def __rmul__(self, val):
        "Return val*self"
        return self*val

    def __rsub__(self, val):
        "Return val-self"
        return -self + val

    def __str__(self):
        "Return string formatted as aX^3 + bX^2 + c^X + d"
        res = []
        it = len(self.coeffs)-1
        for co in self.coeffs:
            if co:
                po = ''
                if it==0:
                    po = ''
                elif it==1:
                    po = 'X'
                else:
                    po = 'X^'+str(it)
                res.append(str(co)+po)
            it-=1
        if res:
            return ' + '.join(res)
        else:
            return "0"

    def __sub__(self, val):
        "Return self-val"
        return self.__add__([-co for co in val])

    def __call__(self, val):
        po = len(self.coeffs)-1
        res = 0
        for i in self.coeffs:
            res += i * (val**po)
            po-=1
        return res

    def trim(self):
        "Remove trailing 0-coefficients"
        _co = self.coeffs
        if _co:
            offs = 0
            while len(_co)!=0 and _co[offs]==0:
                del _co[0]
