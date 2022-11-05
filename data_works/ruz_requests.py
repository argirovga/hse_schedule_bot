import requests
import json

from data_works.working_with_db import inserting_new_value_schedule

groups_url = "https://ruz.hse.ru/api/search?term={}&type=group"
schedule_url = "https://ruz.hse.ru/api/schedule/group/{}?start={}&finish={}&lng={}"


def getting_group_id(group_name: str):
    response = requests.get(groups_url.format(group_name)).json()

    return int(response[0]["id"])


def updating_schedule(
    group_name: str, date_start: str, date_finish: str, datalength: int
):
    group_id = getting_group_id(group_name)

    response = requests.get(
        schedule_url.format(group_id, date_start, date_finish, datalength)
    )
    content = response.json()
    for lesson in content:
        inserting_new_value_schedule(
            lesson.get("discipline"),
            lesson.get("date"),
            lesson.get("auditorium"),
            lesson.get("dayOfWeekString"),
            lesson.get("beginLesson"),
            lesson.get("endLesson"),
            lesson.get("kindOfWork"),
            lesson.get("lecturer_title"),
            lesson.get("lecturerEmail"),
            lesson.get("url1")
        )
