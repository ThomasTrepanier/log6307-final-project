def calc_base_area(base_length, base_width):
    return base_length * base_width
    
def calc_pyramid_volume(base_area, pyramid_heigth):
    return calc_base_area * pyramid_heigth 
    
length = float(input())
width = float(input())
height = float(input())
base = calc_base_area(length, width)
print('Volume for', length, width, height, "is:", calc_pyramid_volume(base, height))
