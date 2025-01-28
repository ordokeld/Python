from plyer import notification

notification.notify(
    title="Reminder",
    message="Take a break and stretch!",
    app_name="Python Notifier",  # Исправлено "Pyton" на "Python"
    timeout=10
)
