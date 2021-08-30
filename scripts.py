import random

from datacenter.models import Schoolkid, Teacher, Subject, Lesson
from datacenter.models import Mark, Chastisement, Commendation


def find_schoolkid(name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
        return schoolkid
    except Schoolkid.MultipleObjectsReturned:
        print('Найдено больше одного ученика')
    except Schoolkid.DoesNotExist:
        print('Учеников не найдено')


def find_lesson(subject, kid_lessons):
    try:
        lesson = kid_lessons.filter(subject__title=subject).order_by('?')[0]
    except IndexError:
        print('Нет в программе такого предмета. Проверь название предмета')
        return
    return lesson


def fix_marks(name):
    schoolkid = find_schoolkid(name)
    if not schoolkid:
        return
    bad_kid_marks = Mark.objects.filter(schoolkid=schoolkid).filter(points__in=[2, 3])
    for mark in bad_kid_marks:
        mark.points = 5
        mark.save()


def remove_chastisements(name):
    schoolkid = find_schoolkid(name)
    if not schoolkid:
        return
    kid_chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    kid_chastisements.delete()


def create_commendation(name, subject):
    schoolkid = find_schoolkid(name)
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
    lesson = find_lesson(subject, kid_lessons)
    if not lesson:
        return
    text = random.choice(recommended_commendations)
    commendation = Commendation.objects.create(
        text=text,
        created=lesson.date,
        schoolkid=schoolkid,
        subject=lesson.subject,
        teacher=lesson.teacher,
    )
