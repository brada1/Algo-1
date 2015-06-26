class PhoneBook:

  def __init__ (self):
    self.root = None

#inserts a new contact
  def insert(self, number, name):
    if self.root:
      return self.root.insert([name, number])
    else:
      self.root = Node([name, number])
      return True

#lookup a name and print its phone number
  def lookup(self, name):
    if self.root:
      return self.root.lookup(name)
    else:
      return False
    
#list all records in an alphabetical order
  def list(self):
    self.root.list()

#remove a record for a given name
  def remove(self, name):
    if self.root:
      return self.root.remove(name)
    else:
      return False

class Node:
  def __init__(self, val):
    self.value = val
    self.left = None
    self.right = None

  def insert(self, data):
      if self.value[0] == data[0]:
        return False
      elif self.value[0] > data[0]:
        if self.left:
          return self.left.insert(data)
        else:
          self.left = Node(data)
          return True
      else:
        if self.right:
          return self.right.insert(data)
        else:
          self.right = Node(data)
          return True

  def list(self):
    if self:
      if self.left:
        self.left.list()
      print (self.key, self.payload)
      if self.right:
        self.right.list()

  def lookup(self, name):
    if self.value[0] == name:
      return self.value[1]
    elif self.value[0] > name:
      if self.left:
        return self.left.lookup(name)
      else:
        return False
    else:
      if self.right:
        return self.right.lookup(name)
      else:
        return False

  def remove(self, name):
    if self.value[0] == name:
      if not self.left and not self.right:
        self.value = None
    elif self.value[0] > name:
      if self.left:
        return self.left.remove(name)
      else:
        return False
    else:
      if self.right:
        return self.right.remove(name)
      else:
        return False
      
pb = PhoneBook()
instr = ''
while True:
  instr = input('')

  if instr == 'exit':
    break
  else:
    if instr == 'list':
      pb.list()
    if ' ' in instr:
      split = instr.split()
      operation = split[0]
      if operation == 'insert':
        print(pb.insert(split[1], split[2]))
      elif operation == 'lookup':
        print (pb.lookup(split[1]))
      elif operation == 'remove':
        print (pb.remove(split[1]))
        
      
