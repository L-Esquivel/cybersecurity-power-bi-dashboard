import pandas as pd
from datetime import datetime, timedelta
import random

# Configuración
num_rows = 300
start_date = datetime(2026, 4, 1)

# Listas de datos ficticios
countries = ["Russia", "China", "USA", "Brazil", "Colombia", "India", "Nigeria"]
event_types = ["Failed Login", "Successful Login", "Port Scan", "Brute Force Attempt"]
statuses = ["Failed", "Success", "Detected"]
usernames = ["admin", "root", "guest", "luis", "alejandro", "carlos", "user", "administrator"]

data = []

for i in range(num_rows):
    date = start_date + timedelta(days=random.randint(0, 30), hours=random.randint(0, 23))
    ip = f"{random.randint(1,223)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"
    
    row = {
        "Date": date.strftime("%Y-%m-%d"),
        "Time": date.strftime("%H:%M:%S"),
        "EventType": random.choice(event_types),
        "IP_Address": ip,
        "UserName": random.choice(usernames) if random.random() > 0.3 else "-",
        "Status": random.choice(statuses),
        "Country": random.choice(countries),
        "ResponseTime": random.randint(30, 1500)
    }
    data.append(row)

# Crear DataFrame y guardar
df = pd.DataFrame(data)
df.to_csv("data/security_logs.csv", index=False)
print("✅ Archivo security_logs.csv generado con", num_rows, "filas.")