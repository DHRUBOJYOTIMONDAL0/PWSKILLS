import sys
from os.path import dirname, join, abspath
# Add the parent directory to the system path
parent_dir_path = abspath(join(dirname(__file__), '..'))
sys.path.insert(0, parent_dir_path)

# Import student_details first before using it
from student import student_details

def teacher():
    print("This is teacher details")

# Call functions in the correct order
teacher()
student_details.student()