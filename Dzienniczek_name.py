message = "Hi {},\n\nThis is a reminder that you have {} tasks left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

with open('name.txt', 'r') as name:
    students_from_file = name.readlines()

def make_student_dict(person):
    person = person.split()
    student_dict = {
        'name' : person[0],
        'task' : person[1],
        'grades' : person[2]
    }
    return student_dict

list_studenst = []
def add_students(counter):
    list_studenst.append(make_student_dict(students_from_file[counter]))

for i in range(4):
    add_students(i)
    prob = int(list_studenst[i]['grades'])
    print(message.format(list_studenst[i] ['name'], list_studenst[i] ['task'], list_studenst[i] ['grades'], prob + 1))












