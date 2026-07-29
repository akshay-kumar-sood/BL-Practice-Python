# PROG 2: Employee Data (MIS)

employees = [
    {
        'id': 1,
        'name': 'John Doe',
        'personal_information': {
            'gender': 'M',
            'age': 28,
            'mobile_number': '1234567890',
            'additional_mobile_number': None
        },
        'education_information': {
            'Degree': 'BE',
            'Degree_Stream': 'Computer Science',
            'Year_of_passout': 2017,
            'total_percentage': 72
        },
        'skills_information': {
            'languages': ['Python', 'Java'],
            'tools': ['Git', 'Docker']
        },
        'department_information': {
            'name_of_dept': 'Development',
            'role': 'Developer'
        }
    },

    # Employee 2, 3 ... up to 10
]

# print all employees
for emp in employees:
    print(emp)