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
        self.trim() # remove zeros in first

    def __add__(self, val):
        # Return self+val
        if isinstance(val, list):                          # add sequence
            x = self.coeffs
            x.reverse()
            val.reverse()
            res = [a+b for a,b in itertools.zip_longest(x, val, fillvalue=0)]
            res.reverse()
            x.reverse()
        elif isinstance(val, Polynomial):                    # add Polynomial
            x = self.coeffs
            x.reverse()
            y = val.coeffs
            y.reverse()
            res = [a+b for a,b in itertools.zip_longest(x, y, fillvalue=0)]
            res.reverse()
            y.reverse()
            x.reverse()
        else:                                              # add scalar
            if self.coeffs:
                res = self.coeffs
                res[len(self.coeffs)-1] += val
            else:
                res = [val]
        return self.__class__(res)

    def __eq__(self, val):
        # Test self==val
        if isinstance(val, Polynomial):
            return self.coeffs == val.coeffs        # check ceoffs is equal
        else:
            return len(self.coeffs)==1 and self.coeffs[0]==val      # check poly is equal to number

    def __mul__(self, val):
        # Return self*val
        """
        algorithm:
        every res[i] = 0
        for every i and j:
            res[i+j] = res[i][j] + poly1[i] * poly2[j]
        """
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
        _s.reverse()
        _v.reverse()
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
            Poly1.reverse() # we cant divide
            Poly2.reverse()
            return self.__class__([0]), self.__class__(Poly1)
        
        quot = []
        divisor = float(Poly2[-1])
        for i in range(shiftlen + 1):
            #Get the next coefficient of the quotient.
            mult = Poly1[-1] / divisor
            quot = [mult] + quot

            #Subtract mult * den from num, but don't bother if mult == 0
            if mult != 0:
                d = [mult * u for u in Poly2]
                Poly1 = [u - v for u, v in zip(Poly1, d)]

            Poly1.pop()
            Poly2.pop(0)
        
        quot.reverse()
        Poly1.reverse()
        Poly2.reverse()
        self.coeffs.reverse()
        return self.__class__(quot) , self.__class__(Poly1)

    def __rtruediv__(self, val):
        # same as __truediv__
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
            Poly2.reverse()
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
        Poly2.reverse()
        self.coeffs.reverse()
        return self.__class__(quot) , self.__class__(Poly1)

    def __neg__(self):
        # Return -self
        return self.__class__([-co for co in self.coeffs])

    def _radd__(self, val):
        # Return val+self
        return self+val

    def __repr__(self):
        return "{0}({1})".format(self.__class__.__name__, self.coeffs)

    def __rmul__(self, val):
        # Return val*self
        return self*val

    def __rsub__(self, val):
        # Return val-self
        return -self + val

    def __str__(self):
        # Return string formatted as aX^3 + bX^2 + c^X + d
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
        # Return self-val
        if isinstance(val, Polynomial):
            return self.__add__([-co for co in val.coeffs])
        return self.__add__([-co for co in val])

    def __call__(self, val):
        # return number if X==val
        po = len(self.coeffs)-1
        res = 0
        for i in self.coeffs:
            res += i * (val**po)
            po-=1
        return res

    def diff(self, val=1):
        # Derivative calculator
        poly = self.coeffs
        poly.reverse()
        for i in range(val):
            deriv_poly = [poly[i] * i for i in range(1, len(poly))]
            poly = deriv_poly
        poly.reverse()
        self.coeffs.reverse()
        return self.__class__(poly)

    def inl(self, val=1, c=0):
        # Integral calculator
        res = self.coeffs
        for j in range(val):
            res = [0] + res
            inl = len(res)-1
            for i in range(1 , len(res)):
                res[i-1] = res[i]/(inl)
                inl-=1
            res[-1] = c
        return self.__class__(res)

    def root(self, val=3):
        # Using Newton Raphson Method to find one root
        # for more info : https://www.geeksforgeeks.org/program-for-newton-raphson-method/
        dif = self.diff()
        f = self
        num = 0
        h = f.__call__(val) / dif.__call__(val)
        while abs(h) >= 0.0001 and num<=1e5:
            h = f.__call__(val) / dif.__call__(val)            
            val = val - h
            num+=1
        return val
 
    def trim(self):
        # Remove trailing 0-coefficients
        _co = self.coeffs
        if _co:
            offs = 0
            while len(_co)!=0 and _co[offs]==0:
                del _co[0]
    
    def fit1(Setx, Sety):
        if(len(Setx)!=len(Sety)):
            return 0
        
        mx = 1e20
        res = []
        for i in range(1 , 20):
            for j in range(0 , 20):
                f = Polynomial(i, j)
                distance = 0
                for k in range(len(Setx)):
                    fx = f(Setx[k])
                    distance += abs(fx-Sety[k])**2
                if(distance<mx):
                    mx = distance
                    res = [i, j]
        return Polynomial(res)
    
    def fit2(Setx, Sety):
        if(len(Setx)!=len(Sety)):
            return 0
        
        mx = 1e20
        res = []
        for i in range(1 , 20):
            for j in range(0 , 20):
                for h in range(0 , 20):
                    f = Polynomial(i, j, h)
                    distance = 0
                    for k in range(len(Setx)):
                        fx = f(Setx[k])
                        distance += abs(fx-Sety[k])**2
                    if(distance<mx):
                        mx = distance
                        res = [i, j, h]
        return Polynomial(res)

