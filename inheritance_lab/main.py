# class Father:
#     def __init__(self):
#         self.father_name = 'Taylor Evans'
#
#
# class Mother:
#     def __init__(self):
#         self.mother_name = 'Bet Williams'
#
#
# class Daughter(Father, Mother):
#     def __init__(self):
#         Father.__init__(self)
#         Mother.__init__(self)
#
#     def get_parent_info(self):
#         return f'Father: {self.father_name}, Mother: {self.mother_name}'

class Parent:
   def __init__(self, name):
      self.name = name

   def get_name(self):
      return self.name

class Child(Parent):
   def __init__(self, name, age):
      super().__init__(name)
      self.age = age

   def get_age(self):
      return self.age


class GrandChild(Child):
   def __init__(self, name, age, address):
      super().__init__(name, age)
      self.address = address

   def get_address(self):
      return self.address

grand_child = GrandChild("Grand Name", 19, "Address 15-17")
print(grand_child.name)     # Grand Name
print(grand_child.age)      # 19
print(grand_child.address)  # Address 15-17
