from django.core.exceptions import MultipleObjectsReturned


def find_schoolkid(name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
        return schoolkid
    except MultipleObjectsReturned:
        print('Найдено больше одного ученика')
    except Schoolkid.DoesNotExist:
        print('Учеников не найдено')


def fix_marks(name):
    schoolkid = find_kid(name)
    if not schoolkid:
        return
    bad_kid_marks = Mark.objects.filter(schoolkid=schoolkid).filter(points__in=[2, 3])
    for mark in bad_kid_marks:
        mark.points = 5
        mark.save()


def remove_chastisements(name):
    schoolkid = find_kid(name)
    if not schoolkid:
        return
    kid_chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    kid_chastisements.delete()


def create_commendation(name, subject):
    schoolkid = find_kid(name)
    if not schoolkid:
        return
    recommended_commendations = [
        'Молодец',
        'Отлично',
        'Хорошо',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты - гений!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже гораздо лучше',
    ]
    year_of_study = schoolkid.year_of_study
    group_letter = schoolkid.group_letter
    kid_lessons = Lesson.objects.filter(year_of_study=year_of_study, group_letter=group_letter)
    subject_lessons = kid_lessons.filter(subject__title=subject)
    num_subject_lessons = subject_lessons.count()
    lesson = subject_lessons[random.randint(0, num_subject_lessons-1)]
    text = random.choice(recommended_commendations)
    commendation = Commendation.objects.create(
        text=text,
        created=lesson.date,
        schoolkid=schoolkid,
        subject=lesson.subject,
        teacher=lesson.teacher,
    )
