from math import cos, sin, tan, degrees, radians


def component_from_magnitude(mag, angle):
    '''return the component vectore for magnitude, degree angle vector'''
    angle = radians(angle)
    return ( 
            mag * cos(angle),
            mag * sin(angle)
           )

def add_component_vectors(*args):
    x_total = sum(arg[0] for arg in args)
    y_total = sum(arg[1] for arg in args)
    return (x_total, y_total)

def add_magnitude_vectors(*args):
   '''returns magnitude vector'''
   pass


if __name__ == "__main__":
    # print(component_from_magnitude(5,40))
    assert [round(i, 2) for i in component_from_magnitude(5, 40)] == [3.83, 3.21]
    assert add_component_vectors((1,2), (1,2), (1,2)) == (3,6)


