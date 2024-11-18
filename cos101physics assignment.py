# Program to calculate speed
def calculate_speed(distance, time):
    if time == 0:
        return "Time cannot be zero!"
    return distance / time

# User input
distance = float(input("Enter the distance (in meters): "))
time = float(input("Enter the time (in seconds): "))

# Output
print(f"The speeds is {calculate_speed(distance, time)} m/s.")


# Program to calculate force
def calculate_force(mass, accleration):
    return mass * accleration

# User input
mass = float(input("Enter the mass (in kg): "))
acceleration = float(input("Enter the acceleration (in m/s^2): "))

# Output
print(f"The force is {calculate_force(mass, acceleration)} N (Newton).")


# Program to calculate kinetic energy
def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

# User input
mass = float(input("Enter the mass (in kg): "))
velocity = float(input("Enter the velocity (in m/s): "))

# Output
print(f"The kinetic energy is {calculate_kinetic_energy(mass, velocity)} J (Joule).")


# Program to calculate gravitational potential energy
def calculate_potential_energy(mass, gravity, height):
    return mass * gravity * height

# User input
mass= float(input("Enter the mass (in kg): "))
height = float(input("Enter the height (in meters): "))
gravity = 9.81
# Standard gravitational acceleration (m/s^2)

#Output
print(f"The gravitational potential energy is {calculate_potential_energy(mass, gravity, height)} J (Joule).")


# Program to calculate the force between two charges using Coulomb's Law
def calculate_coulomb_force(q1, q2, r):
    k = 8.99e9
# Coulomb's constant in N.m^2 / C^2
    if r == 0:
        return  "Distance between charges cannot be zero!"
    return k * (q1 * q2) / (r ** 2)

# User input
q1 = float(input("Enter the magnitude of charge 1 (in Coulombs): "))
q2 = float(input("Enter the magnitude of charge 2 (in Coulumbs): "))
r = float(input("Enter the distance between the charges (in meters): "))

#Output
force = calculate_coulomb_force(q1, q2, r)
print(f"The force between the charges is {force:.2e} N (Newtons).")







