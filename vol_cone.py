#calculate the volume of a right circular cone

def vol_cone(r,h):
    PI = 3.141592653589793
    v = (PI*r**2*h)/3
    return v


print(vol_cone(4,6))


radius = int(input())
height = int(input())
PI = 3.141592653589793
volume = (PI * radius**2 * height)/3 

print(volume)