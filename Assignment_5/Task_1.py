
def student_rec(student_name):
    if student_name in student_record.keys():
        score = student_record[student_name]
        print(f'{student_name}\'s Marks : {score}')
    else:
        print('Student not found.')


if __name__ == "__main__":
    student_record = {'Alice' : 85, 'Bob' : 75, 'Carl' : 75, 'David' : 75}
    student_rec(input("Enter Student's Name: "))
