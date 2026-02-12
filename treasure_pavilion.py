class TreasurePavilion:
    def __init__(self):
        self.treasures = {}

    def add_treasure(self, treasure_name, spirit_stone_cost, reward):
        self.treasures[treasure_name] = (spirit_stone_cost, reward)
        print(f"Added {treasure_name} for {spirit_stone_cost} spirit stones as reward: {reward}")

    def trade(self, treasure_name, spirit_stones):
        if treasure_name in self.treasures:
            cost, reward = self.treasures[treasure_name]
            if spirit_stones >= cost:
                print(f"Exchanging {cost} spirit stones for {reward}")
                return reward
            else:
                print(f"Not enough spirit stones for {treasure_name}. Needed: {cost}, Available: {spirit_stones}")
        else:
            print(f"Treasure {treasure_name} does not exist.")

    def list_treasures(self):
        return list(self.treasures.keys())

    def get_reward_info(self, treasure_name):
        if treasure_name in self.treasures:
            return self.treasures[treasure_name]
        else:
            return None
