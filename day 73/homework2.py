#შექმენით პროგრამა, რომელიც აფასებს სესხის განაცხადს და ადგენს, შეიძლება თუ არა მომხმარებელს სესხის მიღება.


name = input("შეიყვანეთ თქვენი სახელი: ")
age = input("შეიყვანეთ თქვენი ასაკი: ")
income = input("შეიყვანეთ თქვენი წლიური შემოსავალი: ")
status = input("შეიყვანეთ თქვენი ისტორია (კარგი, საშუალო ცუდი): ")
loan = input("შეიყვანეთ რამხელა სესხი გნებავთ: ")


if age < "18":
    print("You can't have the loan")
else:
    print("You can have the loan")

if income < "50000":
    print("You can't have the loan")
else:
    print("You can have the loan")

if status < "საშუალო":
    print("You can't have the loan")
else:
    print("You can have the loan")

if income > "30000":
    print("You can't have the loan")
else:
    print("You can have the loan")