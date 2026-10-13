# create dictionary with student details
students = {
    101: {"Name": "Aditi", "Scores": [70, 85, 90]},
    102: {"Name": "Shruti", "Scores": [75, 88, 95]},
    103: {"Name": "Rahul", "Scores": [40, 40, 62]},
    104: {"Name": "Karan", "Scores": [55, 63, 72]},
    105: {"Name": "Priya", "Scores": [80, 89, 92]},
}

# calculate average score and flag pass/fail
for sid, details in students.items():
    avg = sum(details["Scores"]) / len(details["Scores"])
    details["Average"] = avg
    details["Passed"] = avg >= 50

# Print names of students who passed
print("Students who passed:")
for sid, details in students.items():
    if details["Passed"]:
        print(details["Name"])
