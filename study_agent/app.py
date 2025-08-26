import json
from modules.human_input import ask_difficulty
from modules.progress import update_progress
from modules.scheduler import generate_daily_schedule
from modules.reminders import send_daily_reminder

available_hours_per_day = 3
DAYS_OF_WEEK = ["Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"]

with open("data/topics.json", "r", encoding="utf-8") as f:
    subjects = json.load(f)

subjects = ask_difficulty(subjects)

for i, day in enumerate(DAYS_OF_WEEK):
    day_subjects = subjects[i::len(DAYS_OF_WEEK)] 
    schedule = generate_daily_schedule(day_subjects, available_hours_per_day)
    print(f"\n📅 {day}")
    send_daily_reminder(schedule)

subjects = update_progress(subjects)

for i, day in enumerate(DAYS_OF_WEEK):
    day_subjects = subjects[i::len(DAYS_OF_WEEK)]
    schedule = generate_daily_schedule(day_subjects, available_hours_per_day)
    print(f"\n📅 {day} - Atualizado")
    send_daily_reminder(schedule)

with open("data/topics.json", "w", encoding="utf-8") as f:
    json.dump(subjects, f, indent=2, ensure_ascii=False)
