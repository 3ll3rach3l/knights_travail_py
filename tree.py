class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = list()

    
    @property
    def value(self):
        return self._value  

    @property
    def children(self):
        return self._children
    
    @property
    def parent(self):
        return self._parent
    
    def add_child(self, node):
        if node not in self._children:
            self._children.append(node)
            node.parent = self
    
    def remove_child(self, node):
        if node in self._children:
            self._children.remove(node)
            node.parent = None
    
    @parent.setter
    def parent(self, node):
        if self._parent is node:
            return
        if self._parent is not None:
            self._parent.remove_child(self)
        self._parent = node
        if node is not None:
            node.add_child(self)