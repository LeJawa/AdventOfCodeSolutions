from datetime import datetime

now = datetime.now()
LAST_YEAR = now.year if now.month >= 12 else now.year - 1