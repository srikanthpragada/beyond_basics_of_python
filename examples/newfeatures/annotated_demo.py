from typing import Annotated, get_type_hints

LENGTH = Annotated[int, 'Length of object']  # Alias to annotation


def rect_area(length: Annotated[int, 'Length of rectangle'],
              breadth: Annotated[int, 'Breadth of rectangle']) -> Annotated[int, 'Area of rectangle']:
    return length * breadth


def square_area(length: LENGTH) -> Annotated[int, 'Area of Square']:
    return length * length


print(rect_area.__annotations__)  # Provides metadata
print(rect_area.__annotations__['length'].__metadata__)  # Provides only metadata
print(get_type_hints(rect_area))  # Ignores metadata
