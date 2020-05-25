temps = [223,336,225,350]

new_temps = [temp / 10 for temp in temps]

print(new_temps)


# Comprehension loop 

# -ve number is not valid data and we're not processing -ve integer
temps = [223,336,225,350, -9999, -235,225,-122]

new_temps = [temp / 10 for temp in temps if temp > 0]

print(new_temps)