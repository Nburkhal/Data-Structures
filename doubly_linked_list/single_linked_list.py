# Head     First Node      Last Node
# 0 ---> node10 ----> node20 ----> None

# llist.head        second              third 
#          |                |                  | 
#          |                |                  | 
#     +----+------+     +----+------+     +----+------+ 
#     | 1  |  o-------->| 2  |  o-------->|  3 | null | 
#     +----+------+     +----+------+     +----+------+ 

class Node():
  def __init__(self, d, n=None):
    self.data = d
    self.next_node = n

class LinkedList():
  def __init__(self, r=None):
    self.head = r
    self.size = 0

  def get_size(self):
    # Return size of linked list
    return self.size

  def append(self, d):
    new_node = Node(d)
    
    # If the list is empty
    if self.head == None:
      self.head = new_node
      self.size += 1
      return

    # Find node that points to None
    # Iterate until next node is None
    current = self.head
    while current.next_node != None:
      current = current.next_node
    
    current.next_node = new_node
    
    self.count += 1

  def prepend(self, d):
    insert_node = Node(d)

    # Point insert_node's next to current node
    insert_node.next_node = self.head
    # Head of insert_node needs to point to first node
    self.head = insert_node

    self.count += 1

  def find_element(self, d):
    # Check first node
    current = self.head

    # If found, return the data
    while current:
      if current.data == d:
        return current
    # If not found, go to next node
      else:
        current = current.next_node

    # If you get to end of list and next == None
    # return None
    return False

  def remove(self, d):
    # Find previous node of node we wish to delete
    # Point next of previous node to the node after
    # the node we're deleting
    # delete the next of the node you're deleting
    current = self.head

    if current.next_node == None:
      if current.data == d:
        self.head = None
        return True

      else:
        return False

    while current.next_node != None:
      if current.next_node.data == d:
        current.next_node = current.next_node.next_node
        return True
      else:
        return False

  def print_list(self):
    tmp = self.head
    while tmp:
      print(tmp.data)
      tmp = tmp.next_node
