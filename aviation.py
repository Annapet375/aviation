days_per_year = 365.0
passengers_per_year = 5_000_000_000.0
seats_per_aircraft = 150.0
flights_per_aircraft_per_day = 2.0

passengers_per_day = passengers_per_year / days_per_year
required_global_flee = passengers_per_day / (seats_per_aircraft * flights_per_aircraft_per_day)
print(f"{required_global_flee=:.2f}")
