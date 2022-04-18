name_list = ["Toyin", "Remi", "Bukky", "Femi", "Wale", "Kola"]
marks = [78, 48, 43, 62, 80, 95]

counter = 0

for students in name_list:
    if students == "Bukky":
        print(marks[counter])
        break
    counter += 1

