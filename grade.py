
def grade():
  try:
    marks = int(input("Enter Marks : "))
    if (marks <0) or (marks > 100):
      print("invalid marks")
      return grade()
    else:
      calculate(marks)
  except:
      print("invalid marks")

def calculate(marks):
  if (marks >= 90):
    print("Grade A+")
  elif (marks >= 80) and (marks <=89):
    print("Grade A")
  elif (marks >= 70) and (marks <=79):
    print("Grade B")
  elif (marks >= 60) and (marks <=69):
    print("Grade C")
  elif (marks >= 50) and (marks <=59):
    print("Grade D")
  else:
    print("Fail")

  return grade()

grade()