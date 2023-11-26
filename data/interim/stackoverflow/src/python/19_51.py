class Queue:

    def __init__(self):
     self.items = []

 
    def push(self, e):
      self.items.append(e)
 
    def pop(self):
      head = self.items[0]
      self.items = self.item[1:]
      return head

    def print(self):
      for e in self.items:
          print(e)
q = Queue()
q.push(1)
q.push(23)
q.print()

