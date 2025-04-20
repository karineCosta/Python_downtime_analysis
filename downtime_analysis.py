import pandas as pd

# List simulating production data from 2 different machines
dados = [
    # M2
    {"date": "2025-04-08", "machine": "M2", "produced_units": 390, "downtime_minutes": 45, "energy_kwh": 220},
    {"date": "2025-04-09", "machine": "M2", "produced_units": 350, "downtime_minutes": 60, "energy_kwh": 230},
    {"date": "2025-04-10", "machine": "M2", "produced_units": 410, "downtime_minutes": 15, "energy_kwh": 215},

     # M4
    {"date": "2025-04-08", "machine": "M4", "produced_units": 420, "downtime_minutes": 10, "energy_kwh": 200},
    {"date": "2025-04-09", "machine": "M4", "produced_units": 390, "downtime_minutes": 30, "energy_kwh": 210},
    {"date": "2025-04-10", "machine": "M4", "produced_units": 370, "downtime_minutes": 50, "energy_kwh": 225},
]

# Criating DataFrame
df = pd.DataFrame(dados)
print(df)

# Add a colunm indicating if the goal is achieved
df["met_goal"] = df["produced_units"] >= 400
print(df)

#Counting how many days the goal was not achieved
fail_meta = df[df["met_goal"] == False].groupby("machine").size()
print(fail_meta)

# Analyzing inactivity time during the days the goal was not achieved
downtime_failure = df[df["met_goal"] == False]["downtime_minutes"]

# Avarage of downtime during days of failure
media_downtime = downtime_failure.mean()
print(f"Avarage of downtime during days of failure: {media_downtime} minutes")

# Analyzing energy consume during days of failure
energy_failure = df[df["met_goal"] == False]["energy_kwh"]

# Avarage
average_energy = energy_failure.mean()

print(f"Average energy consumed on days of failure: {average_energy} kWh")

