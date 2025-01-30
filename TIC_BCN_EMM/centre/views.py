from django.shortcuts import render
from .models import student, teacher
# Create your views here.

def students(request):
    students = []
    for student in data["students"]:
        students.append(student)
    return render(request, 'students.html', {'students': students})

def teachers(request):
    teachers = teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})

data = {
    "students": [
        {
            "id": 1,
            "first_name": "Hugo",
            "last_name_1": "Sansegundo",
            "last_name_2": "Costantini",
            "email": "2023_hugo.sansegundo@iticbcn.cat",
            "course": "DAW2A",
            "enrolled_modules": ["M06", "M07", "M08", "Big Data"]
        },
        {
            "id": 2,
            "first_name": "Adrián",
            "last_name_1": "Navarro",
            "last_name_2": "Pérez",
            "email": "2023_adrian.navarro@iticbcn.cat",
            "course": "DAW2A",
            "enrolled_modules": ["M06", "M07", "M08"]
        },
        {
            "id": 3,
            "first_name": "Xavi",
            "last_name_1": "Porras",
            "last_name_2": "del Pino",
            "email": "2023_xavier.porras@iticbcn.cat",
            "course": "DAW2A",
            "enrolled_modules": ["M06", "M07", "M08"]
        },
        {
            "id": 4,
            "first_name": "Javier",
            "last_name_1": "Giménez",
            "last_name_2": "Sánchez",
            "email": "2023_javier.gimenez@iticbcn.cat",
            "course": "DAW2A",
            "enrolled_modules": ["M06", "M07", "M08"]
        },
        {
            "id": 5,
            "first_name": "Milena",
            "last_name_1": "Vardumyan",
            "last_name_2": "Aleksanyan",
            "email": "2023_milena.vardumyan@iticbcn.cat",
            "course": "DAW2A",
            "enrolled_modules": ["M06", "M07", "M013", "Big Data"]
        },
        {
            "id": 6,
            "first_name": "Daniel",
            "last_name_1": "Vallespin",
            "last_name_2": "Mellado",
            "email": "2023_daniel.vallespin@iticbcn.cat",
            "course": "DAW2A",
            "enrolled_modules": ["M06", "M07", "M08"]
        },
        {
            "id": 7,
            "first_name": "Félix Bequet",
            "last_name_1": "Balbin",
            "last_name_2": "Silva",
            "email": "2023_felix.balbin@iticbcn.cat",
            "course": "DAW2A",
            "enrolled_modules": ["M06", "M07", "M08"]
        },
        {
            "id": 8,
            "first_name": "Victor Andrés",
            "last_name_1": "Fernández",
            "last_name_2": "Álvarez",
            "email": "2023_victor.fernandez@iticbcn.cat",
            "course": "DAW2A",
            "enrolled_modules": ["M06", "M07", "M08", "IA"]
        },
        {
            "id": 9,
            "first_name": "Lila",
            "last_name_1": "Díez",
            "last_name_2": "Zhou",
            "email": "2023_lila.diez@iticbcn.cat",
            "course": "DAW2A",
            "enrolled_modules": ["M06", "M07", "M08", "ML"]
        }
    ],
    "teachers": [
        {
            "id": 1,
            "first_name": "Roger",
            "last_name_1": "Sobrino",
            "last_name_2": "Gil",
            "email": "roger.sobrino@iticbcn.cat",
            "course": "DAW2A",
            "tutor": True,
            "teaching_modules": ["M07"]
        }
    ]
}