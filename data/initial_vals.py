import numpy as np

G = 6.67430e-11     # gravitational constant, m^3 kg^-1 s^-2

m_sun = 1.989e30    # mass of the Sun, kg

# EARTH
m_earth = 5.972e24  # mass of the Earth, kg

earth_perihelion = 1.471e8    # perihelion distance of the Earth, meters
earth_aphelion = 1.521e8        # aphelion distance of the Earth, meters
earth_semi_major = (earth_perihelion + earth_aphelion) / 2   # semi-major axis of the Earth

earth_period = 365.256 * 24 * 3600         # period of the Earth, seconds

x_earth = earth_perihelion
y_earth = 0.0
vx_earth = 0.0
vy_earth = np.sqrt(G * m_sun * ((2 / earth_perihelion) - (1 / earth_semi_major)))


# JUPITER
m_jupiter = 1.898e27            # mass of Jupiter, kg

jupiter_perihelion = 7.4059e8   # perihelion distance of Jupiter, meters
jupiter_aphelion = 8.1636e8     # aphelion distance of Jupiter, meters
jupiter_semi_major = (jupiter_perihelion + jupiter_perihelion) / 2  # semi-major axis of Jupiter

jupiter_period = 4332.589 * 24 * 3600        # period of Jupiter, seconds

x_jupiter = jupiter_perihelion
y_jupiter = 0.0
vx_jupiter = 0.0
vy_jupiter = np.sqrt(G * m_sun * ((2 / jupiter_perihelion) - (1 / jupiter_semi_major)))


