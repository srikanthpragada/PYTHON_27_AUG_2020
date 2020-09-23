f = open("students.txt", "rt")

students = {}
for line in f.readlines():
    parts = line.strip().split(',')
    if len(parts) < 2:  # Ignore line if it doesn't contain two values
        continue

    name = parts[0]
    marks = parts[1:]
    try:
        students[name] = sum(map(int, marks))
    except:
        # Write invalid line into errors.txt file
        pass

for name, total in sorted(students.items()):
    print(f"{name:20} {total:3}")
