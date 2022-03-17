def basicDemo():
    tup = (30, 40)
    x, y = tup
    print(f"{tup} split into x={x} and y={y}")
basicDemo()

def attendanceExample():
    student_attendance = {"Rolf":96, "Bob":80, "Anne":100}
    for student, attendance in student_attendance.items():
        print(f"{student}: {attendance}")
attendanceExample()

def headAndTail():
    nums = [1,2,3,4,5]
    head, *tail = nums
    print(f"list={nums}, head={head} and tail={tail}")
headAndTail()

def reverseHeadAndTail():
    nums = [1,2,3,4,5]
    *head, tail = nums
    print(f"list={nums}, head={head} and tail={tail}")
reverseHeadAndTail()