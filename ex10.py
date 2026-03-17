import pandas as pd
import numpy as np

# Exercise 10.1

# See notebook10ex1.txt for the solution.
with open("notebook10ex1.txt", "r") as ex101:
    print(ex101.read())
    ex101.close()

# Exercise 10.2

dates = pd.date_range(start="2026-03-01", end="2026-03-31")

temp_data = np.random.uniform(5, 15, size=len(dates))
march_temps = pd.Series(data=temp_data, index=dates, name="Noon Temperature")

print(march_temps.head())

# Exercise 10.3

elements_data = {
    "Name": [
        "Hydrogen",
        "Helium",
        "Lithium",
        "Beryllium",
        "Boron",
        "Carbon",
        "Nitrogen",
        "Oxygen",
        "Fluorine",
        "Neon",
    ],
    "Symbol": ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne"],
    "Weight": [
        1.008,
        4.0026,
        6.94,
        9.0122,
        10.81,
        12.011,
        14.007,
        15.999,
        18.998,
        20.180,
    ],
}

periodic_table = pd.DataFrame(elements_data, index=range(1, 11))
periodic_table.index.name = "Atomic Number"

print(periodic_table)
