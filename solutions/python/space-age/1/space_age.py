class SpaceAge:
    orbital_period_in_earth_years = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1.0,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132
    }

    def __init__(self, seconds):
        self.age_seconds = seconds

    def on_earth(self):
        orbital_period_earth = (self.orbital_period_in_earth_years["earth"] * 365.25) * 86400
        return round(self.age_seconds / orbital_period_earth, 2)

    def on_mercury(self):
        orbital_period_mercury = (self.orbital_period_in_earth_years["mercury"] * 365.25) * 86400
        return round(self.age_seconds / orbital_period_mercury, 2)

    def on_venus(self):
        orbital_period_venus = self.orbital_period_in_earth_years["venus"] * 365.25 * 86400
        return round(self.age_seconds / orbital_period_venus, 2)

    def on_mars(self):
        orbital_period_mars = self.orbital_period_in_earth_years["mars"] * 365.25 * 86400
        return round(self.age_seconds / orbital_period_mars, 2)

    def on_jupiter(self):
        orbital_period_mars = self.orbital_period_in_earth_years["jupiter"] * 365.25 * 86400
        return round(self.age_seconds / orbital_period_mars, 2)

    def on_saturn(self):
        orbital_period_saturn = self.orbital_period_in_earth_years["saturn"] * 365.25 * 86400
        return round(self.age_seconds / orbital_period_saturn, 2)

    def on_uranus(self):
        orbital_period_uranus = self.orbital_period_in_earth_years["uranus"] * 365.25 * 86400
        return round(self.age_seconds / orbital_period_uranus, 2)

    def on_neptune(self):
        orbital_period_neptune = self.orbital_period_in_earth_years["neptune"] * 365.25 * 86400
        return round(self.age_seconds/ orbital_period_neptune, 2)
