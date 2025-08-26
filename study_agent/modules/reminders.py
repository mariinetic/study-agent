def send_daily_reminder(schedule):
    print("\nLembrete diario de estudo:")
    for item in schedule:
        print(f"- {item['daily_hours']} -> {item['subject']}: {item['topic']}")
