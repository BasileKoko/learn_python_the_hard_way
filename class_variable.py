#Python class variable

class Company:
  number_of_meeting = 0

  def __init__(self, meeting):
    self.meeting = meeting
    Company.number_of_meeting += 1



meeting1 = Company('meeting1')
meeting2 = Company('meeting2')
print(Company.number_of_meeting)
