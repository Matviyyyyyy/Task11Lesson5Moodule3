import setup
from timetable_app.models import Subject, Student, Schedule, Class, Teacher, Grade

while True:
    print("\n1. Операції над таблицею вчителів")
    print("2. Операції над таблицею студентів")
    print("3. Операції над таблицею класів")
    print("4. Операції над таблицею предметів")
    print("5. Операції над таблицею розкладу")
    print("6. Операції над таблицею оцінок")
    print("7. Вийти")

    choice = input("Оберіть опцію (1-7): ")

    if choice == "1":
        teacher_choice = input("1 - Додати вчителя\n2 - Видалити вчителя\n")
        if teacher_choice == "1":
            teacher_first_name = input("Ім'я вчителя")
            teacher_last_name = input("Прізвище вчителя")
            teacher_subject_id = int(input("Id предмета,який вчтель викладає"))
            teacher_subject = Subject.objects.get(id = teacher_subject_id)
            if teacher_subject:
                new_teacher = Teacher(
                    first_name = teacher_first_name,
                    last_name = teacher_last_name,
                    subject = teacher_subject
                )
                new_teacher.save()
                print("Вчителя додано!")
            else:
                print("Некоректний id предмета")
        if teacher_choice == "2":
            deleted_teacher_id = int(input("Вкажи id вчителя, якого потрібно видалити"))
            deleted_teacher = Teacher.objects.get(id = deleted_teacher_id)
            if deleted_teacher:
                deleted_teacher.delete()
                print("Вчителя видалено")
            else:
                print("Некоректний id вчителя")
        else:
            print("Некоректна відповідь")
    if choice == "2":
        student_choice = input("1 - Додати студента\n2 - Видалити студента\n")
        if student_choice == "1":
            student_first_name = input("Ім'я вчителя")
            student_last_name = input("Прізвище вчителя")
            student_class_id = int(input("Id предмета,який вчтель викладає"))
            student_class = Class.objects.get(id=student_class_id)
            if student_class:
                new_student = Student(
                    first_name=student_first_name,
                    last_name=student_last_name,
                    class_s=student_class
                )
                new_student.save()
                print("Студента додано!")
            else:
                print("Некоректний id класу")
        if student_choice == "2":
            deleted_student_id = int(input("Вкажи id студента, якого потрібно видалити"))
            deleted_student = Student.objects.get(id=deleted_student_id)
            if deleted_student:
                deleted_student.delete()
                print("Студента видалено")
            else:
                print("Некоректний id студента")
        else:
            print("Некоректна відповідь")
    if choice == "3":
        class_choice = input("1 - Додати клас\n2 - Видалити клас\n3 - Змінити клас")
        if class_choice == "1":
            class_name = input("Вкажи назву класу")
            class_year = int(input("Вкажи рік класу"))
            new_class = Class(
                name = class_name,
                year = class_year
            )
            new_class.save()
            print("Студента додано!")
        if class_choice == "2":
            deleted_class_id = int(input("Вкажи id класу, який потрібно видалити"))
            deleted_class = Class.objects.get(id=deleted_class_id)
            if deleted_class:
                deleted_class.delete()
                print("Клас видалено")
            else:
                print("Некоректний id студента")
        if class_choice == "3":
            class_changed_id = int(input("Вкажи id класу"))
            class_changed = Class.objects.get(id = class_changed_id)
            if class_changed:
                class_choice_change = input("Що ти хочеш змінити?(1 - назву, 2 - рік)")
                if class_choice_change == "1":
                    new_class_name = input("Вкажи нову назву")
                    class_changed.name = new_class_name
                    class_changed.save()
                if class_choice_change == "2":
                    new_class_year = int(input("Вкажи новий рік класу"))
                    class_changed.year = new_class_year
                    class_changed.save()
                else:
                    print("Некоректна відповідь")
            else:
                print("Некоректний id")
        else:
            print("Некоректна відповідь")

    if choice == "4":
        subject_choice = input("1 - Додати предмет\n2 - Видалити предмет\n3 - Змінити предмет")
        if subject_choice == "1":
            subject_name = input("Вкажи назву предмета")
            subject_description = input("Вкажи опис предмету")
            new_subject = Subject(
                name = subject_name,
                description = subject_description
            )
            new_subject.save()
            print("Предмет додано!")
        if subject_choice == "2":
            deleted_subject_id = int(input("Вкажи id предмета, який потрібно видалити"))
            deleted_subject = Subject.objects.get(id=deleted_subject_id)
            if deleted_subject:
                deleted_subject.delete()
                print("Предмет видалено")
            else:
                print("Некоректний id предмета")
        if subject_choice == "3":
            subject_changed_id = int(input("Вкажи id предмета"))
            subject_changed = Subject.objects.get(id=subject_changed_id)
            if subject_changed:
                subject_choice_change = input("Що ти хочеш змінити?(1 - назву, 2 - опис)")
                if subject_choice_change == "1":
                    new_subject_name = input("Вкажи нову назву")
                    subject_changed.name = new_subject_name
                    subject_changed.save()
                if subject_choice_change == "2":
                    new_subject_des = input("Вкажи новий опис предмета")
                    subject_changed.description = new_subject_des
                    subject_changed.save()
                else:
                    print("Некоректна відповідь")
            else:
                print("Некоректний id")
        else:
            print("Некоректна відповід")

    if choice == "5":
        shedule_choice = input("1 - Додати заняття\n2 - Видалити заняття\n3 - Змінити заняття")
        if shedule_choice == "1":
            shedule_day_of_week = input("Вкажи день тижня")
            shedule_start_time = input("Час початку")
            shedule_subject_id = int(input("Id предмету"))
            shedule_class_id = int(input("Id класу"))
            shedule_teacher_id = int(input("Id вчителя"))
            shedule_teacher = Teacher.objects.get(id = shedule_teacher_id)
            shedule_class = Class.objects.get(id = shedule_class_id)
            shedule_subject = Subject.objects.get(id = shedule_class_id)
            if shedule_class and shedule_subject and shedule_teacher:
                new_shedule = Schedule(
                    day_of_week = shedule_day_of_week,
                    start_time = shedule_start_time,
                    subject = shedule_subject,
                    class_s = shedule_class,
                    teacher = shedule_teacher
                )
                new_shedule.save()
                print("Заняття додано додано!")
            else:
                print("Некоректний id")
        if shedule_choice == "2":
            deleted_shedule_id = int(input("Вкажи id заняття, яке потрібно видалити"))
            deleted_shedule = Subject.objects.get(id=deleted_shedule_id)
            if deleted_shedule:
                deleted_shedule.delete()
                print("Заняття видалено")
            else:
                print("Некоректний id заняття")
        if shedule_choice == "3":
            shedule_changed_id = int(input("Вкажи id заняття"))
            shedule_changed = Schedule.objects.get(id=shedule_changed_id)
            if shedule_changed:
                shedule_choice_change = input("Що ти хочеш змінити?(1 - день тижня, 2 - час початку)")
                if shedule_choice_change == "1":
                    new_shedule_day_of_week = input("Вкажи новий день тижня")
                    shedule_changed.day_of_week = new_shedule_day_of_week
                    shedule_changed.save()
                if shedule_choice_change == "2":
                    new_subject_start_time = input("Вкажи новий час початку")
                    shedule_changed.start_time = new_subject_start_time
                    shedule_changed.save()
                else:
                    print("Некоректна відповідь")
            else:
                print("Некоректний id")
        else:
            print("Некоректна відповідь")

    if choice == "6":
        grade_choice = input("1 - Додати оцінку\n2 - Видалити оцінку\n3 - Змінити оцінку")
        if grade_choice == "1":
            grade_student_id = int(input("Id студента"))
            grade_subject_id = int(input("Id предмета"))
            grade_mark = int(input("Оцінка"))
            grade_subject = Subject.objects.get(id = grade_subject_id)
            grade_student = Student.objects.get(id = grade_student_id)
            if grade_student and grade_subject:
                new_grade = Grade(
                    student = grade_student,
                    subject = grade_subject,
                    mark = grade_mark
                )
                new_grade.save()
                print("Оцінку додано")
            else:
                print("Некоректний id")
        if grade_choice == "2":
            deleted_grade_id = int(input("Вкажи id оцінки, яку потрібно видалити"))
            deleted_grade = Grade.objects.get(id=deleted_grade_id)
            if deleted_grade:
                deleted_grade.delete()
                print("Оцінку видалено")
            else:
                print("Некоректний id оцінки")
        if grade_choice == "3":
            grade_changed_id = int(input("Вкажи id заняття"))
            grade_changed =  Grade.objects.get(id = grade_changed_id)
            if grade_changed:
                new_grade_mark = int(input("Вкажи нову оцінку"))
                grade_changed.mark = new_grade_mark
                grade_changed.save()
            else:
                print("Некоректний id")
        else:
            print("Некоректна відповідь")
    if choice == "7":
        break


