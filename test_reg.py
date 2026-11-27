from reg import calculate_registration


def test_student_registration():
    result = calculate_registration("Apeksha", "Student", 3)
    assert result["total_amount"] == 600


def test_faculty_registration():
    result = calculate_registration("Rahul", "Faculty", 2)
    assert result["total_amount"] == 1000


def test_industry_registration():
    result = calculate_registration("Priya", "Industry", 4)
    assert result["total_amount"] == 4000


def test_single_student_registration():
    result = calculate_registration("Amit", "Student", 1)
    assert result["total_amount"] == 200


def test_invalid_category():
    result = calculate_registration("John", "Other", 2)
    assert result == "Invalid registration category"
