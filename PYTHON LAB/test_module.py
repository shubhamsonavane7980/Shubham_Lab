from university_package.result import Result
from university_package.college.exam import Exam

def test_function():
    # Access University package
    university_result = Result()
    result_data = university_result.get_data()
    university_result.display(result_data)

    # Access College package
    college_exam = Exam()
    exam_data = college_exam.get_data()
    college_exam.display(exam_data)

# Test the functionality
test_function()
