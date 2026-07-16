file_names = ["1.raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]
for index, file in enumerate(file_names):
    file_names[index] = file.replace(".", "-")
print(file_names)
