from Vec3_class import Vec3

class Ray:
    def __init__(self,v1,v2):#由vec3组成
        self.origin = v1
        self.direction = v2

    def point_at_parameter(self,t):
        return self.origin + self.direction*t
