import math
class Vec3:
    def __init__(self,e0,e1,e2):
        self.lst = [e0,e1,e2]
        self.e0 = e0
        self.e1 = e1
        self.e2 = e2

    def __repr__(self):
        return str(self.e0)+" "+ str(self.e1)+" "+str(self.e2)
    #索引[]
    def __pos__(self):
        return Vec3(self.e0,self.e1,self.e2)

    def __neg__(self):
        return Vec3(-self.e0,-self.e1,-self.e2)

    def length(self):
        return math.sqrt(self.e0**2 + self.e1**2 + self.e2**2)

    def squared_length(self):
        return self.e0**2 + self.e1**2 + self.e2**2

    def make_unit_vector(self):
        k = 1.0/self.length()
        return Vec3(self.e0*k,self.e1*k,self.e2*k)

    def __add__(self, other):
        return Vec3(self.e0+other.e0,self.e1+other.e1,self.e2+other.e2)

    def __sub__(self, other):
        return Vec3(self.e0-other.e0,self.e1-other.e1,self.e2-other.e2)

    def __mul__(self, other):
        try:
            return Vec3(self.e0*other.e0,self.e1*other.e1,self.e2*other.e2)
        except:
            return Vec3(self.e0*other,self.e1*other,self.e2*other)

    def __truediv__(self, other):
        try:
            return Vec3(self.e0/other.e0,self.e1/other.e1,self.e2/other.e2)
        except:
            return Vec3(self.e0/other,self.e1/other,self.e2/other)

    def dot(self,other):
        return self.e0*other.e0 + self.e1*other.e1 + self.e2*other.e2

    def cross(self,other):
        return Vec3((self.e1*other.e2-self.e2*other.e1),
                    (-(self.e0*other.e2-self.e2*other.e0)),
                    (self.e0*other.e1 - self.e1*other.e0))

    def __iadd__(self, other):
        self.e0 += other.e0
        self.e1 += other.e1
        self.e2 += other.e2
        return self

    def __isub__(self, other):
        self.e0 -= other.e0
        self.e1 -= other.e1
        self.e2 -= other.e2
        return self

    def __imul__(self, other):
        try:
            self.e0 *= other.e0
            self.e1 *= other.e1
            self.e2 *= other.e2
        except:
            self.e0 *= other
            self.e1 *= other
            self.e2 *= other
        return self

    def __idiv__(self, other):
        try:
            self.e0 /= other.e0
            self.e1 /= other.e1
            self.e2 /= other.e2
        except:
            self.e0 /= other
            self.e1 /= other
            self.e2 /= other
        return self

    def unit_vector(self):
        return self/self.length()



