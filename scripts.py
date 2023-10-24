from datacenter.models import Mark, Schoolkid, Chastisement, Lesson, Subject, Commendation, Teacher
import random



def change_marks(schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2,3])
    for mark in bad_marks:
        mark.points = 5
        mark.save()


def remove_chasts(schoolkid):
    chasts = Chastisement.objects.filter(schoolkid=schoolkid)
    for chast in chasts:
        chast.delete()


def create_commendation(kid, name_subject):
    commends = ['Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!']
    text = random.choice(commends)
    schoolkid = Schoolkid.objects.filter(full_name__contains=kid)
    if schoolkid.count() > 1:
        print('Учеников больше 1')
        return None
    elif not schoolkid.exists():
        print('Ученик не существует')
        return None
    else:
        schoolkid = schoolkid.first()
    year_of_study = schoolkid.year_of_study
    group_letter = schoolkid.group_letter
    lessons = Lesson.objects.filter(subject__title=name_subject, year_of_study=year_of_study, group_letter=group_letter)
    random_lesson = random.choice(lessons)
    teacher = random_lesson.teacher
    date = random_lesson.date
    subject = Subject.objects.filter(title=name_subject, year_of_study=year_of_study).first()
    Commendation.objects.create(schoolkid=schoolkid, subject=subject, teacher=teacher,created=date, text=text)