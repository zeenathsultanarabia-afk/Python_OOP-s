class Hallticket:
  def __init__(self,name,roll_number,college_name,branch):
    self.name=name
    self.roll_number=roll_number
    self.college_name=college_name
    self.branch=branch

  def display_details(self):
    print(f"Name: {self.name}")
    print(f"Roll Number: {self.roll_number}")
    print(f"College Name: {self.college_name}")
    print(f"Branch: {self.branch}")

std1= Hallticket("Priya Yadav",1101,"Bright Future Institute of Technology","CSE")
std1.display_details()
