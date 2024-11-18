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
mass = float(input("Enterthe mass (in kg): "))
velocity = float(input("Enter the velocity (in m/s): "))

# Output
print(f"The kinetic energy is {calculate_kinetic_energy(mass, velocity)} J (Joule).")


# Gravitational Force: F = G * (m1 * m2) / r^2
def gravitational_force(m1, m2, r):
    G = 6.67430e-11  # Gravitational constant
    return G * (m1 * m2) / r**2

# Coulomb’s Law: F = k * |q1 * q2| / r^2
def electrostatic_force(q1, q2, r):
    k = 8.9875e9  # Coulomb's constant (N·m²/C²)
    return k * abs(q1 * q2) / r**2






