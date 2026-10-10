#project1
import datetime
import time
name=input("enter your name:")
presentHour=int(input("tell the time:"))
presentHour=datetime.datetime.now().hour
if 5<=presentHour<=11:
    print("Good morning",name)
elif 11<=presentHour<=17:
    print("Good afternoon",name)
elif 17<=presentHour<=20:
    print("Good evening",name)
else:
    print("Good night",name)
print("Namaste!Welcome to your chatbot")
print("you can ask me basic questions, Type 'bye' to exit from the bot")
responses={
    "hello":"Hi! How can i help you?",
    "how are you":"I am very fine. How can i help you?",
    "who are you?":"I am smart AI chatbot",
    "motivate me":"Keep going.The fire within you must not stop.Every bug of your project makes you a better developer.",
    "happy":"great to hear that",
    "where to study functions?":"Go study lecture 7 and solve DPP-3",
    "what programming languages to learn?":"Study c++,python,c mostly."

}
def getresponseofBot(userquestion):
    userquestion=userquestion.lower()
    for eachkey in responses:
        if eachkey in userquestion:
             return responses[eachkey]
    return "sorry i still dont know that"

while True:
    userinput=input("please tell your question:")
    reply=getresponseofBot(userinput)
    print("Bot response:",reply)


    if "bye" in userinput.lower():
        break




#project2
def employee_analysis(employees):
    highest=employees[0]
    total=0
    departments={}
    for employee in employees:
        name=employee[0]
        department=employee[1]
        salary=employee[2]
        if salary>highest[2]:
            highest=employee
            total=total+salary
        if department in departments:
            departments[department]+=1
        else:
            departments[department]=1
    average = total / len(employees)

    return highest, average, departments


employees = [
    ("Rahul", "IT", 65000),
    ("Priya", "HR", 50000),
    ("Aman", "IT", 72000),
    ("Neha", "Finance", 60000),
    ("Ravi", "HR", 45000)
]

highest, average, departments = employee_analysis(employees)

print("Highest Salary:", highest[0], highest[2])
print("Average Salary:", average)
print("Department Count:", departments)






#project3
import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Ghanshyam", "Dhanshyam", "Aditi",
             "Jagdish", "Raj", "Simran", "Neha", "Karan"],

    "Department": ["IT", "HR", "IT", "Finance", "HR",
                    "IT", "Finance", "IT", "HR", "Finance"],

    "Age": [28, 34, 22, 30, 29, 40, 25, 32, 27, 35],

    "Salary": [50000, 60000, 45000, 52000, 49000,
               70000, 48000, 58000, 55000, 65000],

    "Performance": [85, 90, 78, 92, 88, 95, 80, 89, 91, 87],

    "Experience": [3, 7, 1, 5, 4, 12, 2, 8, 3, 10]
}

df = pd.DataFrame(data)
print("Complete DataFrame:")
print(df)
print("\nName, Salary and Performance:")
print(df[["Name","Salary","Performance"]])
high_salary=df[df["Salary"]>50000]
print("\nEmployees with salary > 50000:")
print(high_salary)
high_performers=df[(df["Salary"]>50000)&(df["Performance"]>85)]
print("\nSalary > 50000 AND Performance > 85:")
print(high_performers)
it_hr=df[(df["Department"]=="IT")|(df["Department"]=="HR")]
print("\nEmployees from IT or HR:")
print(it_hr)
sorted_salary = df.sort_values("Salary", ascending=False)
print("\nEmployees sorted by salary:")
print(sorted_salary)
df["Bonus"] = df["Salary"] * 0.10
print("\nDataFrame with Bonus:")
print(df)
df["Final Salary"] = df["Salary"] + df["Bonus"]
print("\nDataFrame with Final Salary:")
print(df)
highest_performance = df.loc[df["Performance"].idxmax()]
print("\nEmployee with highest performance:")
print(highest_performance)
worst_performance=df.loc[df["Performance"].idxmin()]
print("\nEmployee with worst performance:")
print(worst_performance)

#project4
import pandas as pd
data = {
    "Name":["Aman","Priya","Rahul","Neha","Arjun"],
    "Python":[78,65,88,55,92],
    "Maths":[85,70,92,60,89],
    "AI":[90,72,95,58,94]
}
df = pd.DataFrame(data)
print(df["Python"])
print(df[["Name","Python"]])
print(df[df["Python"] > 80])
print(df[(df["Python"] > 80) & (df["Maths"] > 80)])
print(df[(df["Python"] > 80) | (df["Maths"] > 80)])
df["Total"] = df["Python"] + df["Maths"] + df["AI"]
print(df["Total"])
df["Percentage"] = df["Total"] / 3
print(df["Percentage"])
df["average"]=df[["Python","Maths","AI"]].mean(axis=1)
print(df["average"])
print("Students:", df.shape[0])
print("Subjects:", df.shape[1]-1)
print("Columns:", list(df.columns))
print("\nData types:\n", df.dtypes)


#project5
import pandas as pd

df = pd.DataFrame({
    "Name": ["Aman", "Riya", "Karan", "Simran", "Arjun", "Neha", "Dev"],
    "Age": [21, 24, 19, 26, 23, 20, 28],
    "City": ["Delhi", "Mumbai", "Delhi", "Chandigarh", "Mumbai", "Delhi", "Chandigarh"],
    "Marks": [82, 91, 67, 88, 76, 95, 72],
    "Attendance": [85, 92, 78, 89, 81, 96, 74],
    "Department": ["CS", "IT", "CS", "ECE", "IT", "CS", "ECE"]
})
result=df[
    (df["Marks"]>75)&
    ((df["Attendance"]>=90)|(df["City"]=="Delhi"))&
    (df["Department"]!="ECE")&
    (df["Age"].between(20,25))
][["Name","City","Marks"]]
print(result)



#project6
import pandas as pd
df = pd.DataFrame({
    "Name": ["Aman", "Riya", "Karan", "Simran", "Arjun", "Neha", "Dev", "Tanya"],
    "Age": [21, 24, 19, 26, 23, 20, 28, 22],
    "City": ["Delhi", "Mumbai", "Delhi", "Chandigarh", "Mumbai", "Delhi", "Chandigarh", "Mumbai"],
    "Marks": [82, 91, 67, 88, 76, 95, 72, 84],
    "Attendance": [85, 92, 78, 89, 81, 96, 74, 87],
    "Department": ["CS", "IT", "CS", "ECE", "IT", "CS", "ECE", "IT"]
})
result = df[
    (df["Marks"] >= 80) &
    (df["Age"] < 25) &
    (df["City"].isin(["Delhi", "Mumbai"])) &
    ((df["Attendance"] > 85) | (df["Marks"] > 90)) &
    (df["Department"] != "ECE")
][["Name", "Age", "Department"]].sort_values("Age", ascending=False)

print(result)


#project7
import pandas as pd
data = {
    "Name": ["Riya", "Karan", "Simran", "Mohit", "Anjali", "Rohit", "Pooja", "Dev"],
    "Marks": [88, 67, 92, 74, 81, 59, 95, 72],
    "Attendance": [91, 78, 96, 82, 88, 65, 94, 76],
    "Course": ["Python", "Java", "Python", "Data Science", "Python", "Java", "Data Science", "Python"],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Chandigarh", "Delhi", "Mumbai", "Chandigarh"]
}
df = pd.DataFrame(data)
result=df[(df["Course"].isin(["Python","Data Science"]))&
          (df["Marks"]>=75)&
          (df["Attendance"]>=80)&
          (df["City"]!="Delhi")
          ]
result=result[["Name","Marks","Attendance","Course","City"]]
result = result.sort_values(
    "Marks",
    ascending=False
)
print(result)



#project8
import pandas as pd
data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor",
                "Printer", "Webcam", "Tablet", "Headphones"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics",
                 "Electronics", "Accessories", "Electronics", "Accessories"],
    "Price": [65000, 800, 1500, 18000, 12000, 3500, 28000, 2200],
    "Stock": [8, 45, 12, 6, 15, 25, 10, 4],
    "Rating": [4.5, 4.2, 4.0, 4.6, 3.8, 4.3, 4.7, 4.1]
}
products = pd.DataFrame(data)
result = products[
    (products["Category"] == "Electronics") &
    (products["Price"].between(10000, 70000)) &
    (products["Stock"] < 15) &
    (products["Rating"] >= 4.5)
]
result = result[
    ["Product", "Price", "Stock", "Rating"]
]
result = result.sort_values(
    "Price",
    ascending=False
)

print(result)



#project9
import pandas as pd
df = pd.DataFrame({
    "Employee": ["Aman", "Priya", "Rahul", "Sneha", "Aman", "Rahul"],
    "Department": ["IT", "HR", "IT", "Finance", "IT", "IT"],
    "Region": ["North", "West", "North", "South", "North", "East"],
    "Sales": [75000, 45000, 62000, 55000, 18000, 25000]
})
dept=df.groupby("Department")["Sales"].agg(["sum","mean"])
dept = dept[dept["sum"] > 100000].sort_values("sum", ascending=False)
print(dept)


#project10
import pandas as pd
df = pd.DataFrame({
    "Name": ["Aman", "Riya", "Karan", "Simran", "Vivek", "Neha", "Arjun", "Pooja"],
    "Email": ["aman@gmail.com", "riya@yahoo.com", "karan@gmail.com",
              "simran@hotmail.com", "vivek@gmail.com", "neha@yahoo.com",
              "arjun@gmail.com", "pooja@hotmail.com"],
    "Salary": [55000, 48000, 72000, 65000, 52000, 80000, 61000, 45000]
})
result=df[(df["Email"].str.contains("gmail"))&
          (df["Salary"]>60000)]
result = result[["Name", "Email", "Salary"]]
result = result.sort_values("Salary", ascending=False)
print(result)



#project11
import pandas as pd
df = pd.DataFrame({
    "Employee": ["Aman", "Riya", "Karan", "Simran", "Vivek", "Neha", "Arjun", "Pooja"],
    "Region": ["North", "South", "North", "West", "South", "North", "West", "South"],
    "Sales": [50000, 65000, 72000, 45000, 58000, 90000, 62000, 40000]
})
df["Bonus"]=df["Sales"]*0.10
df["Total"]=df["Sales"]+df["Bonus"]
result=df[df["Total"]>70000]
result=result[["Employee","Region","Sales","Bonus","Total"]]
result=result.sort_values("Total",ascending=False)
print(result)


#project12
import  numpy as np
marks = np.array([
    [78, 85, 90],
    [65, 70, 72],
    [88, 92, 95],
    [55, 60, 58],
    [92, 89, 94]
])

# Task 1 — Understand Dataset

print("\nMini Project 1 — Task 1")
print("Number of students:", marks.shape[0])
print("Number of subjects:", marks.shape[1])
print("Total number of marks:", marks.size)


# Task 2 — Subject-wise Analysis

subject_avg = marks.mean(axis=0)

print("\nTask 2")
print("Average Python marks:", subject_avg[0])
print("Average Maths marks:", subject_avg[1])
print("Average AI marks:", subject_avg[2])


# Task 3 — Student-wise Analysis

student_avg = marks.mean(axis=1)

print("\nTask 3")
for i, avg in enumerate(student_avg, start=1):
    print(f"Student {i}: {avg:.2f}")


# Task 4 — Top Performer

top_index = np.argmax(student_avg)

print("\nTask 4")
print("Top performer: Student", top_index + 1)
print("Average:", student_avg[top_index])


# Task 5 — Weakest Performer

weak_index = np.argmin(student_avg)

print("\nTask 5")
print("Weakest performer: Student", weak_index + 1)
print("Average:", student_avg[weak_index])


# Task 6 — Students Who Performed Well
# Marks greater than 75

print("\nTask 6")
print(marks[marks > 75])


# Task 7 — Subject-wise Highest Marks

print("\nTask 7")
print("Highest Python mark:", marks[:, 0].max())
print("Highest Maths mark:", marks[:, 1].max())
print("Highest AI mark:", marks[:, 2].max())


# Task 8 — Add Grace Marks

updated_marks = marks + 5

print("\nTask 8")
print(updated_marks)
print("Original marks remain unchanged:")
print(marks)


# Task 9 — Grace Marks with Maximum 100

updated_marks_100 = np.minimum(marks + 5, 100)

print("\nTask 9")
print(updated_marks_100)


# Task 10 — Pass/Fail Analysis

passed = student_avg >= 60
failed = student_avg < 60

print("\nTask 10")
print("Student averages:", student_avg)
print("Students who passed:", np.where(passed)[0] + 1)
print("Students who failed:", np.where(failed)[0] + 1)
print("Number passed:", np.sum(passed))
print("Number failed:", np.sum(failed))

best_subject_index=np.argmax(student_avg)
subjects=np.array(["Python", "Maths", "AI"])
print("Best performing subject:", subjects[best_subject_index])
print("Average marks:", subject_avg[best_subject_index])

condition = (student_avg > 75) & (marks[:, 2] > 90)
print("Students satisfying both conditions:", marks[condition])

total_marks=marks.sum(axis=1)
percentage = total_marks / 300 * 100
for i,p in enumerate(percentage,start=1):
    print(f"Student{i}:{p}")

performance = np.select(
    [student_avg >= 85,(student_avg >= 70) & (student_avg < 85)],
    ["Excellent", "Good"],
    default="Needs Improvement")

for i,result in enumerate(performance,start=1):
    print(f"Student{i}:{result}")





#project13
import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D", "E", "F"],
    "Department": ["IT", "HR", "IT", "Sales", "HR", "Sales"],
    "Salary": [50000, 45000, 65000, 55000, 48000, 70000],
    "Experience": [2, 3, 5, 4, 2, 6]
})
result=df[(df["Experience"]>3)&
          (df["Salary"]>50000)]
print(result)
it_salary=df[df["Department"]=="IT"]["Salary"].mean()
hr_salary=df[df["Department"]=="HR"]["Salary"].mean()
sales_salary=df[df["Department"]=="Sales"]["Salary"].mean()
print("IT:", it_salary)
print("HR:", hr_salary)
print("Sales:", sales_salary)
if it_salary > 55000:
    print("IT:", it_salary)

if hr_salary > 55000:
    print("HR:", hr_salary)

if sales_salary > 55000:
    print("Sales:", sales_salary) 





#project14
import pandas as pd
df = pd.DataFrame({
    "Movie": ["A", "B", "C", "D", "E", "F", "G"],
    "Genre": ["Action", "Comedy", "Action", "Drama", "Comedy", "Drama", "Action"],
    "Rating": [8.2, 7.5, 9.0, 8.1, None, 7.8, 8.7],
    "Votes": [1200, 800, 2000, 1500, 600, 900, 1800],
    "Budget": [100, 50, 150, 80, 40, 70, 130]
})
average_rating=df["Rating"].mean()
df["Rating"] = df["Rating"].fillna(average_rating)
df["Popularity"]=df["Rating"]*df["Votes"]
action=df[df["Genre"]=="Action"]["Rating"].mean()
comedy=df[df["Genre"]=="Comedy"]["Rating"].mean()
drama=df[df["Genre"]=="Drama"]["Rating"].mean()
print("Action:", action)
print("Comedy:", comedy)
print("Drama:", drama)
result = df[
    (df["Rating"] > 8) &
    (df["Votes"] > 1000)
]
print(result)
df = df.sort_values("Popularity", ascending=False)
top3 = df.head(3)
print(top3)
df=df.sort_values("Popularity",ascending=True)
worst3=df.head(3)
print(worst3)







#project15
import pandas as pd

# 1. Raw sales records
sales_data = [
    {"Rep": "Alice", "Total_Sales": 12000, "Region": "North"},
    {"Rep": "Bob", "Total_Sales": 45000, "Region": "East"},
    {"Rep": "Charlie", "Total_Sales": 8000, "Region": "South"},
    {"Rep": "David", "Total_Sales": 27000, "Region": "West"}
]
df = pd.DataFrame(sales_data)
def calculate_commission(sales):
    if sales >= 30000:
        return 0.10  # 10%
    elif sales >= 10000:
        return 0.05  # 5%
    else:
        return 0.02  # 2%
df["Commission_Rate"] = df["Total_Sales"].apply(calculate_commission)
df["Payout"] = df["Total_Sales"] * df["Commission_Rate"]
final_shape = df.shape
print("Final DataFrame:")
print(df)
print(f"\nFinal Shape (Rows, Columns): {final_shape}")



#project16
import pandas as pd
data = {
    "Name": ["Aman", "Priya", "Rahul", "Neha", "Arjun",
             "Simran", "Karan", "Meena"],
    "Python": [78, 65, 88, 55, 92, 74, 61, 85],
    "Maths": [85, 70, 92, 60, 89, 80, 67, 90],
    "AI": [90, 72, 95, 58, 94, 82, 70, 88]
}
df = pd.DataFrame(data)
print(df)
print("Number of students:", df.shape[0])
print("Total number of subjects:", df.shape[1]-1)
print("Column names:", df.columns.tolist())
print("\nFirst 5 students:")
print(df.head())
print("\nLast 3 students:")
print(df.tail(3))
python_top=df.loc[df["Python"].idxmax()]
maths_top=df.loc[df["Maths"].idxmax()]
ai_top=df.loc[df["AI"].idxmax()]
print(python_top)
print(maths_top)
print(ai_top)
print("\n--- Top Performers ---")
print("Python:", python_top["Name"], "-", python_top["Python"])
print("Maths:", maths_top["Name"], "-", maths_top["Maths"])
print("AI:", ai_top["Name"], "-", ai_top["AI"])



#project17
import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance_Score": [85, 90, 78, 92, 88, 95, 80, 89]
}
df=pd.DataFrame(data)
df.loc[0,'Salary']=55000
print(df)
df["Salary"]=df["Salary"]*1.05
print(df)
df.drop(columns="Performance_Score",inplace=True)
df.drop(columns="Age",inplace=True)
print(df)


#project18
import numpy as np
import matplotlib.pyplot as plt

temperature = np.array([32, 35, 31, 29, 36, 38, 34])

# 1. Average temperature
average = np.mean(temperature)
print("Average temperature:", average)

# 2. Highest and lowest
print("Highest:", np.max(temperature))
print("Lowest:", np.min(temperature))

# 3. Difference
difference = np.max(temperature) - np.min(temperature)
print("Difference:", difference)

# 4. Temperatures above average
print("Above average:", temperature[temperature > average])

# 5. Line plot
days = np.arange(1, 8)

plt.plot(days, temperature, marker="o")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("Weekly Temperature")
plt.show()
highest = np.max(temperature)
highest_day = np.argmax(temperature) + 1

plt.plot(days, temperature, marker="o")
plt.scatter(highest_day, highest, color="red", s=100)

plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("Highest Temperature")
plt.show()



#project19
import numpy as np
marks=np.array([
    [78, 85, 90],
    [65, 70, 72],
    [88, 92, 95],
    [55, 60, 58],
    [92, 89, 94]
])
print("Number of Students=",marks.shape[0])
print("Number of Subjects=",marks.shape[1])
print("Total number of marks=",marks.size)
subject_average=np.mean(marks,axis=0)
print("Average Python marks:", subject_average[0])
print("Average Maths marks:", subject_average[1])
print("Average AI marks:", subject_average[2])
student_average=np.mean(marks,axis=1)
print("Average 1st student marks:", student_average[0])
print("Average 2nd student marks:", student_average[1])
print("Average 3rd student marks:", student_average[2])
print("Average 4th student marks:", student_average[3])
print("Average 5th student marks:", student_average[4])
highest=max(student_average[0],student_average[1],student_average[2],student_average[3],student_average[4])
print(highest)
for i in range(0,5):
    if student_average[i]==highest:
        print("Top performer: Student",i+1)
lowest=min(student_average[0],student_average[1],student_average[2],student_average[3],student_average[4])
print(lowest)
for i in range(0,5):
    if student_average[i]==lowest:
        print("Worst performer: Student",i+1)
well_performed=np.all(marks>75,axis=1)
for i in np.where(well_performed)[0]:
    print('Student who scored more than 75:',i+1)
grace_marks = marks + 5
print("Marks after adding 5 grace marks:",grace_marks)
updated_marks=np.minimum(marks+5,100)
print("Updated marks with maximum limit of 100:",updated_marks)
print(updated_marks)
print("Average 1st student marks:", student_average[0])
print("Average 2nd student marks:", student_average[1])
print("Average 3rd student marks:", student_average[2])
print("Average 4th student marks:", student_average[3])
print("Average 5th student marks:", student_average[4])
passed=student_average>=60
failed=student_average<60
for i in np.where(passed)[0]:
    print("Students who passed: Student",i+1)
for i in np.where(failed)[0]:
    print("Students who passed: Student",i+1)
print("\nNumber of students passed:", np.sum(passed))
print("Number of students failed:", np.sum(failed))
best_subject_index=np.argmax(subject_average)
subjects = ["Python", "Maths", "AI"]
print("Best performing subject:", subjects[best_subject_index])
print("Average marks:", subject_average[best_subject_index])
condition = (student_average > 75) & (marks[:, 2] > 90)
for i in np.where(condition)[0]:
    print("Student", i + 1)
total_marks=np.sum(marks,axis=1)
percentage=((total_marks)/300)*100
for i in range(5):
    print("Student", i + 1, "Percentage:", percentage[i])
for i in range(5):
    print("Student", i + 1, "Total Marks:", total_marks[i])
condition=marks[:,2]>=90
for i in np.where(condition)[0]:
    print("Student:",i+1)




#project20
import random

print("===== NUMBER GUESSING GAME =====")

name = input("Enter your name: ")

while True:

    number = random.randint(1, 100)
    max_attempts = 8
    won = False

    print("\nHello", name + "!")
    print("I have selected a number between 1 and 100.")
    print("You have", max_attempts, "attempts.")

    for attempt in range(1, max_attempts + 1):

        guess = int(input("\nAttempt " + str(attempt) + ": Enter your guess: "))

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        if guess == number:
            print("\nCorrect!")
            print("You guessed the number in", attempt, "attempts.")
            won = True

            if attempt <= 2:
                score = 100
            elif attempt <= 4:
                score = 75
            elif attempt <= 6:
                score = 50
            else:
                score = 25

            print("Your score:", score)
            break

        elif guess < number:
            print("Too low!")

        else:
            print("Too high!")

        remaining = max_attempts - attempt

        if remaining > 0:
            print("Attempts remaining:", remaining)

    if won == False:
        print("\nGame over!")
        print("The correct number was:", number)
        print("Your score: 0")

    again = input("\nDo you want to play again? (yes/no): ")

    if again.lower() != "yes":
        print("\nThanks for playing,", name + "!")
        break