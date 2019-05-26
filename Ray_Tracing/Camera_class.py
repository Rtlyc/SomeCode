import math,random
from Vec3_class import Vec3
from Ray_class import Ray

def random_in_unit_disk():
    p = Vec3(random.random(),random.random(),0)*2 - Vec3(1,1,0)
    while p.dot(p) >= 1:
        p = Vec3(random.random(), random.random(), 0) * 2 - Vec3(1, 1, 0)
    return p

class Camera:
    def __init__(self,lookfrom,lookat,vup,vfov,aspect,aperture,focus_dist):
        self.lens_radius = aperture/2
        theta = vfov*math.pi/180
        half_height = math.tan(theta/2)
        half_width = aspect*half_height
        self.origin = lookfrom
        self.w = lookfrom - lookat
        self.w = self.w.unit_vector()
        self.u = vup.cross(self.w)
        self.u = self.u.unit_vector()
        self.v = self.w.cross(self.u)
        self.lower_left_corner = self.origin - self.u*half_width*focus_dist - self.v*half_height*focus_dist - self.w*focus_dist
        self.horizontal = self.u*2*half_width*focus_dist
        self.vertical = self.v*2*half_height*focus_dist

    def get_ray(self,s,t):
        rd = random_in_unit_disk()*self.lens_radius
        offset = self.u * rd.e0 + self.v * rd.e1
        return Ray(self.origin+offset,self.lower_left_corner+self.horizontal*s+self.vertical*t-self.origin-offset)