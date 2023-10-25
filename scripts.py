from datacenter.models import Mark, Schoolkid, Chastisement, Lesson, Subject, Commendation, Teacher
import random

COMMENDATION = ['Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!']


def schoolkid_name(schoolkid):
    schoolkid = Schoolkid.objects.filter(full_name__contains=schoolkid)
    if schoolkid.count() > 1:
        print('Учеников больше 1')
        return None
    elif not schoolkid.exists():
        print('Ученик не существует')
        return None
    else:
        return schoolkid.first()


def change_marks(schoolkid):
    schoolkid = schoolkid_name(schoolkid)
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2,3])
    bad_marks.update(points=5)


def remove_chastisements(schoolkid):
    schoolkid = schoolkid_name(schoolkid)
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def create_commendation(schoolkid, name_subject):
    text = random.choice(COMMENDATION)
    schoolkid = schoolkid_name(schoolkid)
    year_of_study = schoolkid.year_of_study
    group_letter = schoolkid.group_letter
    lesson = Lesson.objects.filter(subject__title=name_subject, year_of_study=year_of_study, group_letter=group_letter).order_by('?').first()
    teacher = lesson.teacher
    date = lesson.date
    subject = Subject.objects.filter(title=name_subject, year_of_study=year_of_study).first()
    Commendation.objects.create(schoolkid=schoolkid, subject=subject, teacher=teacher,created=date, text=text)


