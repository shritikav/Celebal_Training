
employees = [
    {
        'id': 1,
        'name': 'John Doe',
        'personal_information': {
            'gender': 'M', 'age': 28,
            'mobile_number': '1234567890',
            'additional_mobile_number': None
        },
        'education_information': {
            'Degree': 'BE', 'Degree_Stream': 'Computer Science',
            'Year_of_passout': 2017, 'total_percentage': 72
        },
        'skills_information': {
            'languages': ['Python', 'Java'],
            'tools': ['Git', 'Docker']
        },
        'department_information': {
            'name_of_dept': 'Development', 'role': 'Developer'
        }
    },
    {
        'id': 2,
        'name': 'Jane Smith',
        'personal_information': {
            'gender': 'F', 'age': 24,
            'mobile_number': '9876543210',
            'additional_mobile_number': None
        },
        'education_information': {
            'Degree': 'BE', 'Degree_Stream': 'IT',
            'Year_of_passout': 2018, 'total_percentage': 85
        },
        'skills_information': {
            'languages': ['Python'],
            'tools': ['Git', 'Kubernetes']
        },
        'department_information': {
            'name_of_dept': 'Development', 'role': 'Developer'
        }
    },
    {
        'id': 3,
        'name': 'Alice Brown',
        'personal_information': {
            'gender': 'F', 'age': 30,
            'mobile_number': '3456789012',
            'additional_mobile_number': '3456789013'
        },
        'education_information': {
            'Degree': 'ME', 'Degree_Stream': 'Electronics',
            'Year_of_passout': 2014, 'total_percentage': 88
        },
        'skills_information': {
            'languages': ['Java'],
            'tools': ['Jenkins', 'Docker']
        },
        'department_information': {
            'name_of_dept': 'QA', 'role': 'QA Engineer'
        }
    },
    {
        'id': 4,
        'name': 'Bob White',
        'personal_information': {
            'gender': 'M', 'age': 38,
            'mobile_number': '7654321098',
            'additional_mobile_number': None
        },
        'education_information': {
            'Degree': 'ME', 'Degree_Stream': 'Mechanical',
            'Year_of_passout': 2008, 'total_percentage': 75
        },
        'skills_information': {
            'languages': ['Python', 'Java'],
            'tools': ['Kubernetes', 'AWS']
        },
        'department_information': {
            'name_of_dept': 'DevOps', 'role': 'DevOps Engineer'
        }
    },
    {
        'id': 5,
        'name': 'Emma Green',
        'personal_information': {
            'gender': 'F', 'age': 23,
            'mobile_number': '5678901234',
            'additional_mobile_number': None
        },
        'education_information': {
            'Degree': 'BE', 'Degree_Stream': 'Computer Science',
            'Year_of_passout': 2021, 'total_percentage': 80
        },
        'skills_information': {
            'languages': ['Python'],
            'tools': ['AWS', 'Jenkins']
        },
        'department_information': {
            'name_of_dept': 'Development', 'role': 'Developer'
        }
    },
    {
        'id': 6,
        'name': 'Chris Blue',
        'personal_information': {
            'gender': 'M', 'age': 26,
            'mobile_number': '9876512340',
            'additional_mobile_number': None
        },
        'education_information': {
            'Degree': 'BE', 'Degree_Stream': 'Electronics',
            'Year_of_passout': 2019, 'total_percentage': 82
        },
        'skills_information': {
            'languages': ['Java'],
            'tools': ['AWS', 'Git']
        },
        'department_information': {
            'name_of_dept': 'Development', 'role': 'Developer'
        }
    },
    {
        'id': 7,
        'name': 'Diana King',
        'personal_information': {
            'gender': 'F', 'age': 34,
            'mobile_number': '7654873210',
            'additional_mobile_number': None
        },
        'education_information': {
            'Degree': 'ME', 'Degree_Stream': 'IT',
            'Year_of_passout': 2013, 'total_percentage': 90
        },
        'skills_information': {
            'languages': ['Python', 'Java'],
            'tools': ['Kubernetes', 'AWS']
        },
        'department_information': {
            'name_of_dept': 'DevOps', 'role': 'DevOps Engineer'
        }
    },
    {
        'id': 8,
        'name': 'Eve Lewis',
        'personal_information': {
            'gender': 'F', 'age': 22,
            'mobile_number': '6543219870',
            'additional_mobile_number': None
        },
        'education_information': {
            'Degree': 'BE', 'Degree_Stream': 'Computer Science',
            'Year_of_passout': 2023, 'total_percentage': 78
        },
        'skills_information': {
            'languages': ['Python'],
            'tools': ['Docker', 'AWS']
        },
        'department_information': {
            'name_of_dept': 'Development', 'role': 'Developer'
        }
    },
    {
        'id': 9,
        'name': 'Frank Woods',
        'personal_information': {
            'gender': 'M', 'age': 40,
            'mobile_number': '4567890123',
            'additional_mobile_number': None
        },
        'education_information': {
            'Degree': 'ME', 'Degree_Stream': 'Computer Science',
            'Year_of_passout': 2006, 'total_percentage': 70
        },
        'skills_information': {
            'languages': ['Python', 'Java'],
            'tools': ['Jenkins', 'Git']
        },
        'department_information': {
            'name_of_dept': 'Development', 'role': 'Developer'
        }
    },
    {
        'id': 10,
        'name': 'Grace Black',
        'personal_information': {
            'gender': 'F', 'age': 27,
            'mobile_number': '8765432109',
            'additional_mobile_number': None
        },
        'education_information': {
            'Degree': 'BE', 'Degree_Stream': 'Mechanical',
            'Year_of_passout': 2016, 'total_percentage': 74
        },
        'skills_information': {
            'languages': ['Python'],
            'tools': ['AWS', 'Docker']
        },
        'department_information': {
            'name_of_dept': 'QA', 'role': 'QA Engineer'
        }
    }
]

# 1. Gender distribution
male = 0
female = 0

# 2. Age distribution
less_25 = 0
age_25_35 = 0
above_35 = 0

# 3. Developer count
developers = 0

# 4. Employees by programming language
java_employees = []
python_employees = []
both_employees = []

for emp in employees:
    personal = emp['personal_information']
    age = personal['age']
    gender = personal['gender']

    # Count gender
    if gender == 'M':
        male += 1
    elif gender == 'F':
        female += 1

    # Count age groups
    if age < 25:
        less_25 += 1
    elif age <= 35:
        age_25_35 += 1
    else:
        above_35 += 1

    # Count developers
    if emp['department_information']['role'] == 'Developer':
        developers += 1

    # Check programming languages
    languages = emp['skills_information']['languages']
    name = emp['name']

    if 'Java' in languages:
        java_employees.append(name)

    if 'Python' in languages:
        python_employees.append(name)

    if 'Java' in languages and 'Python' in languages:
        both_employees.append(name)


# Display results
print("Gender Distribution Ratio:")
print("Male:", male)
print("Female:", female)

print("\nAge Distribution:")
print("Less than 25:", less_25)
print("25-35:", age_25_35)
print("Above 35:", above_35)

print("\nNumber of Developers:", developers)

print("\nNames of Employees who know Java:")
print(java_employees)

print("\nNames of Employees who know Python:")
print(python_employees)

print("\nNames of Employees who know both Java and Python:")
print(both_employees)
