from graphics import *

class node():
    """
    A class that stores the information of a single node in the graph
    """

    ############################################################### CONSTRUCTOR

    def __init__(self,num:int,info:dict={}):
        """
        Creates a node object. prev id a list of previous nodes (optional),
        next is a list of following nodes
        (also optional). **kwagrs is a dictionary between variable name and value, like a=0.
        This may be used for special search algorithms and storing information along the way
        """
        self._num = int(num)
        self._next = []
        self._info = info
        self._circle = None
        self._connections = []
        self._switch = True

    ############################################################### DUNDER

    #Adds a dependant
    def __iadd__(self,n):
        if not isinstance(n,node):
            raise ValueError("NODE ADD - not a node")
        if n not in self._next:
            self._next.append(n)
        return self

    #Iterates over the dependants (_next)
    def __iter__(self):
        self._iterator = 0
        return self

    #Iterates over the dependants (_next)
    def __next__(self):
        if self._iterator < len(self._next):
            result = self._next[self._iterator]
            self._iterator+=1
            return result
        raise StopIteration

    #Prints out node information
    def __str__(self):
        return f"Node {self._num} :: Dependants{[str(i) for i in self._next]}, Info{self._info}"

    ############################################################### MODIFY

    #Adds/replaces information
    def add_info(self,key,value):
        self._info[key] = value
    
    #Assigns a circle to the node
    def assign_circle(self,circle:Circle):
        self._circle = circle
        self._circle.setFill("white")

    #Assigns line connection to the node
    def assign_connection(self,second_node):
        self._connections.append(Line(self.get_circle_pos(),second_node.get_circle_pos()))
        self._connections[-1].setFill("white")
        self._connections[-1].setWidth(2)

    #Switches colour white->green->white->...
    def switch_colour(self,colour:str):
        self._circle.setFill(colour)

    ############################################################### GETTERS

    #Returns node number
    def get_num(self):
        return self._num

    #Returns circle center
    def get_circle_pos(self):
        return self._circle.getCenter()

    #Returns a splash text of the number
    def get_splash(self):
        result = Text(self.get_circle_pos(),str(self._num))
        result.setTextColor('black')
        return result

    #Returns list of connections
    def get_connections(self):
        return self._connections

    #Returns node circle
    def get_circle(self):
        return self._circle
    
    #Get dictionary of object information
    def get_info(self): return self._info.items()
    