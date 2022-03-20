name_list = ["Toyin", "Remi", "Bukky", "Femi"]
marks = [95, 48, 59, 75]

counter = 0

for students in name_list:
    if students == "Bukky":
        print(marks[counter])
        break
    counter += 1

