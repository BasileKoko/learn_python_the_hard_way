class School:
  def __init__(self, student, teacher):
      self.student = student
      self.teacher = teacher

  def exam(self):
    return 'exam day is soon'


class AngelSchool(School):
  def __init__(self, student, teacher, director):
      School.__init__(self, student, teacher)
      self.director = director

angelschool1 = AngelSchool('Chris', 'Mr Leon', 'Mrs Juliette')
print(angelschool1.director)
