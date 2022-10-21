class Planet:

    def __init__(self, id, name, description, mass):
        self.id = id
        self.name = name
        self.description = description
        self.mass = mass

planets = [
            {
                'id': 1,
                'name': 'Mercury',
                'description': 'Smallest planet',
                'mass': '3.301×1023 kg'
            },
            {
                'id': 2,
                'name': 'Venus',
                'description': 'Second planet from the sun',
                'mass': '4.867×10^24 kg'
            },
            {
                'id': 3,
                'name': 'Earth',
                'description': 'Our home',
                'mass': '5.972×10^24 kg'
            },
            {
                'id': 4,
                'name': 'Mars',
                'description': 'Some want to go there',
                'mass': '6.417×10^23 kg'
            },
            {
                'id': 5,
                'name': 'Jupiter',
                'description': 'Biggest planet',
                'mass': '1.899×10^27 kg'
            },
            {
                'id': 6,
                'name': 'Saturn',
                'description': 'Has nice rings',
                'mass': '5.685×10^26 kg'
            },
            {
                'id': 7,
                'name': 'Uranus',
                'description': 'Interesting name',
                'mass': '8.682×10^25 kg'
            },
            {
                'id': 8,
                'name': 'Neptune',
                'description': 'Last planet',
                'mass': '1.024×10^26 kg'
            }
]

planet_list = []
for p in planets:
    instance = Planet(p['id'], p['name'], p['description'], p['mass'])
    planet_list.append(instance)