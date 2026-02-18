import datetime

subjects = input("Enter subjects (using comma) : ").split(",")
days = int(input("Days left for exam: "))

today = datetime.date.today()

print("\n Smart Preparation Plan:\n")

for i in range(days):
    date = today + datetime.timedelta(days=i)
    subject = subjects[i % len(subjects)]
    print(date, "-> Study", subject.strip())