import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from student import student_details
def teacher():
    print("This is teacher details")
student_details.student()
