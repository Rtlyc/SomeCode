import math,random
from Vec3_class import Vec3
from Ray_class import Ray
from Camera_class import Camera

class Material:
    def __init__(self):
        self.mat = ""

class Hit_record:
    def __init__(self):
        self.t = ""
        self.p = 0
        self.normal = 0
        self.mat_ptr = Material()

class Sphere:
    def __init__(self,cen,r,material):
        self.center = cen
        self.radius = r
        self.mat_ptr = material

    def hit(self,ray,tmin,tmax,rec):
        oc = ray.origin - self.center #vec3
        a = ray.direction.dot(ray.direction)
        b = oc.dot(ray.direction)
        c = oc.dot(oc) - self.radius*self.radius
        discriminant = b*b - a*c
        if discriminant>0:
            temp = (-b-math.sqrt(discriminant))/a
            if tmin < temp < tmax:
                rec.t = temp
                rec.p = ray.point_at_parameter(rec.t)
                rec.normal = (rec.p - self.center)/self.radius
                rec.mat_ptr = self.mat_ptr
                return True
            temp = (-b+math.sqrt(discriminant))/a
            if tmin < temp < tmax:
                rec.t = temp
                rec.p = ray.point_at_parameter(rec.t)
                rec.normal = (rec.p - self.center)/self.radius
                rec.mat_ptr = self.mat_ptr
                return True
        return False

class Hitable_list:
    def __init__(self,lst,n):
        self.lst = lst
        self.lst_size = n

    def hit(self,ray,t_min,t_max,rec):#bool
        global rec0
        temp_rec = Hit_record()
        hit_anything = False
        closest_so_far =t_max
        for i in range(0,self.lst_size):
            if self.lst[i].hit(ray,t_min,closest_so_far,temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec0 = temp_rec


        return hit_anything

def random_in_unit_sphere():
    p = Vec3(random.random(),random.random(),random.random()) * 2.0 -Vec3(1,1,1)
    while p.squared_length() >= 1:
        p = Vec3(random.random(), random.random(), random.random()) * 2.0 - Vec3(1, 1, 1)
    return p

class Lambertian:
    def __init__(self,a):
        self.albedo = a

    def scatter(self,ray,rec,attenuation,scattered):
        global attenuation0, scattered0
        target = rec.p + rec.normal + random_in_unit_sphere()
        scattered0 = Ray(rec.p,target-rec.p)
        attenuation0 = self.albedo
        return True

def reflect(v,n):
    return v-n*(v.dot(n)*2)

def refract(v,n,ni_over_nt,refracted):
    global refracted0
    uv = v.unit_vector()
    dt = uv.dot(n)
    discriminant = 1.0-ni_over_nt*ni_over_nt*(1-dt*dt)
    if discriminant>0:
        refracted0 = (uv-n*dt)*ni_over_nt - n*math.sqrt(discriminant)
        return True
    return False

def schlick(cosine,ref_idx):
    r0 = (1-ref_idx)/(1+ref_idx)
    r0 *= r0
    return r0+(1-r0)*math.pow((1-cosine),5)


class Metal:
    def __init__(self,a,f):
        self.albedo = a
        if f < 1:
            self.fuzz = f
        else:
            self.fuzz = 1

    def scatter(self,ray,rec,attenuation,scattered):
        global attenuation0,scattered0
        reflected = reflect(ray.direction.unit_vector(),rec.normal)
        scattered0 = Ray(rec.p,reflected+random_in_unit_sphere()*self.fuzz)
        attenuation0 = self.albedo
        return (scattered0.direction.dot(rec.normal))>0

class Dielectric:
    def __init__(self,ri):
        self.ref_idx = ri

    def scatter(self,r_in,rec,attenuation,scattered):
        global attenuation0, scattered0,refracted0
        reflected = reflect(r_in.direction,rec.normal)
        attenuation0 = Vec3(1.0,1.0,1.0)
        refracted = Vec3(0,0,0)
        if r_in.direction.dot(rec.normal)>0:
            outward_normal = -rec.normal
            ni_over_nt = self.ref_idx
            cosine = self.ref_idx* r_in.direction.dot(rec.normal)/r_in.direction.length()
        else:
            outward_normal = rec.normal
            ni_over_nt = 1/self.ref_idx
            cosine = -r_in.direction.dot(rec.normal)/r_in.direction.length()

        if refract(r_in.direction,outward_normal,ni_over_nt,refracted):
            reflect_prob = schlick(cosine,self.ref_idx)
        else:
            scattered0 = Ray(rec.p,reflected)
            reflect_prob = 1.0

        if random.random() < reflect_prob:
            scattered0 = Ray(rec.p,reflected)
        else:
            scattered0 = Ray(rec.p,refracted0)
        return True


def color(ray,world,depth): #world: Hitable_list
    global rec0,attenuation0,scattered0
    rec0 = Hit_record()
    if world.hit(ray,0.001,3.40282e+38,rec0):
        scattered0 = Ray(Vec3(0,0,0),Vec3(0,0,0))
        attenuation0 = Vec3(0,0,0)
        if depth < 50 and rec0.mat_ptr.scatter(ray,rec0,attenuation0,scattered0):
            return attenuation0 * color(scattered0,world,depth+1)
        else:
            return Vec3(0,0,0)
    else:
        unit_direction = ray.direction.unit_vector()
        t = (unit_direction.e1+1.0)*0.5
        return Vec3(1.0,1.0,1.0)*(1-t)+Vec3(0.5,0.7,1.0)*t


def random_scene():
    lst = [Sphere(Vec3(0,-1000,0),1000,Lambertian(Vec3(0.5,0.5,0.5)))]
    for a in range(-11,11):
        for b in range(-11,11):
            choose_mat = random.random()
            center = Vec3(a+0.9*random.random(),0.2,b+0.9*random.random())
            if (center - Vec3(4,0.2,0)).length()>0.9:
                if choose_mat < 0.8:
                    lst.append(Sphere(center,0.2,Lambertian(Vec3(random.random(),random.random(),random.random()))))
                elif choose_mat < 0.95:
                    lst.append(Sphere(center,0.2,Metal(Vec3(0.5*(1+random.random()),0.5*(1+random.random()),0.5*(1+random.random())),0.5*random.random())))
                else:
                    lst.append(Sphere(center,0.2,Dielectric(1.5)))

    lst.append(Sphere(Vec3(0,1,0),1.0,Dielectric(1.5)))
    lst.append(Sphere(Vec3(-4,1,0),1.0,Lambertian(Vec3(0.4,0.2,0.1))))
    lst.append(Sphere(Vec3(4,1,0),1.0,Metal(Vec3(0.7,0.6,0.5),0.0)))
    return Hitable_list(lst,len(lst))


def main():
    nx = 1200
    ny = 800
    ns = 10
    f = open("Class15.pgm","w")
    f.write("P3\n"+str(nx)+" "+str(ny)+"\n255\n")
    lst0 = Sphere(Vec3(0,0,-1),0.5,Lambertian(Vec3(0.1,0.2,0.5)))
    lst1 = Sphere(Vec3(0,-100.5,-1),100,Lambertian(Vec3(0.8,0.8,0.0)))
    lst2 = Sphere(Vec3(1,0,-1),0.5,Metal(Vec3(0.8,0.6,0.2),0.0))
    lst3 = Sphere(Vec3(-1,0,-1),0.5,Dielectric(1.5))
    lst4 = Sphere(Vec3(-1,0,-1),-0.45,Dielectric(1.5))
    lst = [lst0, lst1, lst2, lst3, lst4]
    R = math.cos(math.pi/4)
    lookfrom = Vec3(13,2,3)
    lookat = Vec3(0,0,0)
    dist_to_focus = 10.0
    aperture = 0.1
    world = random_scene()
    cam = Camera(lookfrom,lookat,Vec3(0,1,0),20,nx/ny,aperture,dist_to_focus)

    for j in range(ny-1,-1,-1):
        for i in range(0,nx):
            col = Vec3(0,0,0)
            for s in range(0,ns):
                u = (i+random.random())/nx
                v = (j+random.random())/ny
                r = cam.get_ray(u,v)
                p = r.point_at_parameter(2.0)
                col += color(r,world,0)

            col /= ns
            col = Vec3(math.sqrt(col.e0),math.sqrt(col.e1),math.sqrt(col.e2))
            ir = int(255.99*col.e0)
            ig = int(255.99*col.e1)
            ib = int(255.99*col.e2)
            f.write(str(ir)+" "+str(ig)+" "+str(ib)+"\n")
    f.close()

main()

#rec
