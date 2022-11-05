import requests
import json

groups_url = "https://ruz.hse.ru/api/search?term={}&type=group"
schedule_url = "https://ruz.hse.ru/api/schedule/group/{}?start={}&finish={}&lng={}"


def getting_group_id(group_name: str):
    response = requests.get(groups_url.format(group_name)).json()

    return int(response[0]['id'])


def updating_schedule(group_name: str, date_start: str, date_finish: str, datalength: int):
    group_id = getting_group_id(group_name)

    response = requests.get(schedule_url.format(group_id, date_start, date_finish, datalength))
    content = response.json()
    for lesson in content:
        data_used = {
            "discipline" : lesson.get("discipline"),
            "auditorium" : lesson.get("auditorium"),
            "dayOfWeekString" : lesson.get("dayOfWeekString"),
            "date" : lesson.get("date"),
            "beginLesson" : lesson.get("beginLesson"),
            "endLesson" : lesson.get("endLesson"),
            "kindOfWork" : lesson.get("kindOfWork"),
            "lecturer" : lesson.get("lecturer_title"),
            "lecturer_email" : lesson.get("lecturerEmail"),
            "zoom_url" : lesson.get("url1")
        }
        print(lesson)


def updating_group_info():
    pass


updating_schedule("БПАД222", "2022.11.05", "2022.11.08", 1)
