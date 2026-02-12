class CultivationSystem:
    def __init__(self):
        self.realms = {
            'Novice': 0,
            'Adept': 1,
            'Expert': 2,
            'Master': 3,
            'Grandmaster': 4,
            'Sage': 5,
            'Immortal': 6,
            'Ascended': 7,
            'Legendary': 8
        }
        self.cultivators = {}

    def add_cultivator(self, name):
        if name not in self.cultivators:
            self.cultivators[name] = {'realm': 'Novice', 'level': 1}

    def cultivate(self, name):
        if name in self.cultivators:
            current_realm = self.cultivators[name]['realm']
            current_level = self.cultivators[name]['level']
            if current_level < 9:
                self.cultivators[name]['level'] += 1
            else:
                # Level up to the next realm
                next_realm = self.level_up_realm(current_realm)
                if next_realm:
                    self.cultivators[name]['realm'] = next_realm
                    self.cultivators[name]['level'] = 1

    def level_up_realm(self, current_realm):
        realms_list = list(self.realms.keys())
        current_index = realms_list.index(current_realm)
        if current_index < len(realms_list) - 1:
            return realms_list[current_index + 1]
        return None

    def get_cultivator_info(self, name):
        return self.cultivators.get(name, 'Cultivator not found')

# Example usage:
sys = CultivationSystem()
sys.add_cultivator('Warrior1')
sys.cultivate('Warrior1')
print(sys.get_cultivator_info('Warrior1'))  
