import math
import copy

class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

#instantiating
# jack = Point()
# print(type(jack))
# jack.x = 3
# jack.y = 4
# print(jack.x, jack.y)


# print('(%g, %g)' % (jack.x, jack.y))
# distance = math.sqrt(jack.x**2 + jack.y**2)
# print(distance)

def print_point(p):
    """Print a Point object in human-readable format."""
    print('({}, {}).'.format(p.x, p.y))

# print_point(jack)

# jonathan = Point()
# jonathan.x = 4
# jonathan.y = 5
# print_point(jonathan)

# print(hasattr(jack, 'x'))
# print(hasattr(jack, 'z'))

def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.

    p1: Point
    p2: Point

    returns: float
    """
    return math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)

# print(distance_between_points(jack, jonathan))

class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner.
    """

# angela = Rectangle()
# angela.width = 100
# angela.height = 200
# angela.corner = jack

def find_center(rect):
    """Returns a Point at the center of a Rectangle.

    rect: Rectangle

    returns: new Point
    """
    p = Point()
    p.x = rect.corner.x + rect.width / 2.0
    p.y = rect.corner.y + rect.height / 2.0
    return p

# sarah = find_center(angela)
# print_point(sarah)

def grow_rectangle(rect, dwidth, dheight):
    """Modifies the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight




def print_rectangle(rect):
    print('width:', rect.width, 'height:', rect.height)
    print('the lower-left corner:')
    print_point(rect.corner)

# print_rectangle(angela)
# grow_rectangle(angela, 50, 100)
# print('after growing')
# print_rectangle(angela)


'''Exercise 2'''
class Circle:
    """Represents a point in 2-D space.

    attributes: center, radius

    center is a Point object and radius is a number
    """    

def print_circle(circle):
    print('radius:', circle.radius)
    print('center:')
    print_point(circle.center)

'''Write a function named point_in_circle that takes a Circle and a Point and returns True if the Point lies in or on the boundary of the circle.'''

def point_in_circle(circle, point):
    return distance_between_points(point, circle.center) <= circle.radius


'''Write a function named rect_in_circle that takes a Circle and a Rectangle and returns True if the Rectangle lies entirely in or on the boundary of the circle.'''

def rect_in_circle(circle, rect):
    bot_right = copy.copy(rect.corner)
    bot_right.x += rect.width
    top_left = copy.copy(rect.corner)
    top_left.y += rect.height
    top_right = copy.copy(rect.corner)
    top_right.x += rect.width
    if point_in_circle(circle, rect.corner):
        if point_in_circle(circle, bot_right):
            if point_in_circle(circle, top_left):
                if point_in_circle(circle, top_right):
                    return True
    return False

'''Write a function named rect_circle_overlap that takes a Circle and a Rectangle and returns True if any of the corners of the Rectangle fall inside the circle.
Or as a more challenging version, return True if any part of the Rectangle falls inside the circle.'''

def rect_circle_overlap(circle, rect):
    bot_right = copy.copy(rect.corner)
    bot_right.x += rect.width
    top_left = copy.copy(rect.corner)
    top_left.y += rect.height
    top_right = copy.copy(rect.corner)
    top_right.x += rect.width
    if point_in_circle(circle, rect.corner):
        return True
    if point_in_circle(circle, bot_right):
        return True
    if point_in_circle(circle, top_left):
        return True
    if point_in_circle(circle, top_right):
        return True
    return False

def main():
    my_point = Point()
    print(Point.__doc__)
    my_point.x = 3
    my_point.y = 4
    print('My point', end=' ')
    print_point(my_point)

    print('Is my_point an instance of Point?', isinstance(my_point, Point))
    print('Is my_point an instance of Rectangle?',
          isinstance(my_point, Rectangle))
    print('Does my_point have an attribute x?', hasattr(my_point, 'x'))
    print('Does my_point have an attribute z?', hasattr(my_point, 'z'))

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    print('Does box have an attribute x?', hasattr(box, 'x'))

    print('Does box have an attribute corner?', hasattr(box, 'corner'))

    print('Rectangle has these:', dir(box))
    #dir is all the attributes. the double underscore is hidden.

    center = find_center(box)
    print('center', end=' ')
    print_point(center)

    print(box.width)
    print(box.height)
    print('grow')
    grow_rectangle(box, 50, 100)
    print(box.width)
    print(box.height)

    #Exercise 2
    '''Instantiate a Circle object that represents a circle with its center at (150, 100) and radius 75.'''
    cir = Circle()
    cir.center = Point()
    cir.center.x = 150
    cir.center.y = 100
    cir.radius = 75
    print_circle(cir)
    print(point_in_circle(cir, box.corner))
    print(rect_in_circle(cir, box))
    print(rect_circle_overlap(cir, box))




if __name__ == '__main__':
    main()

#why use main and hide the main using if?
    #when imported/called, the file will called will run first