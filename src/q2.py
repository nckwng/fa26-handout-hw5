"""HW5 Question 2: Slicing a list

Please see sample code below that uses a Building class you need to define.

Sample Building class usage:
b = Building("A", 3)
print(b.name)    # A
print(b.floors)  # 3

Two Buildings should be considered equal if they have the same name and number of floors.

After writing the Building class, please write a function takes a list of Building instances 
and returns the sum of the number of floors in the last n Buildings in the list, where n is 
specified as an argument to the function. If n is longer than the list of buildings, consider 
all buildings in the list. If n is zero, the function should return 0.

Example usage:
sum_last_n_floors([Building("A", 3), Building("B", 5), Building("C", 2)], 2) -> 7
sum_last_n_floors([Building("A", 3), Building("B", 5), Building("C", 2)], 1) -> 2
sum_last_n_floors([Building("A", 3), Building("B", 5), Building("C", 2)], 3) -> 10
sum_last_n_floors([Building("A", 3), Building("B", 5), Building("C", 2)], 0) -> 0
"""

class Building:
    """represents a building with a name and number of floors"""
    def __init__(self, name: str, floors: int) -> None: 
        self.name = name 
        self.floors = floors
        
def sum_last_n_floors(buildings: list[Building], n: int) -> int: 
    """returns the sum of the number of floors in the last n Buildings in the list"""
    if n == 0: 
        return 0
    return sum(building.floors for building in buildings[-n:])

