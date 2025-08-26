def decimal_to_hours_minutes(hours_decimal):
    horas = int(hours_decimal)
    minutos = int(round((hours_decimal - horas) * 60))
    return f"{horas}h {minutos}m"

def generate_daily_schedule(subjects, available_hours):
    topic_list = []
    for subject in subjects:
        for topic in subject["topics"]:
            priority = topic["difficulty"] * (1 - topic["progress"])
            topic_list.append({**topic, "subject": subject["subject"], "priority": priority})

    total_priority = sum(t["priority"] for t in topic_list)
    schedule = []

    if total_priority == 0:
        return schedule

    for t in topic_list:
        hours_decimal = available_hours * (t["priority"] / total_priority)
        schedule.append({
            "subject": t["subject"],
            "topic": t["name"],
            "daily_hours": decimal_to_hours_minutes(hours_decimal)
        })

    return schedule
