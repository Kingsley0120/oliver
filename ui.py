import pygame

class UI:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.SysFont('Arial', 24)

    def display_title(self, title):
        title_surface = self.font.render(title, True, (255, 255, 255))
        self.screen.blit(title_surface, (self.width // 2 - title_surface.get_width() // 2, 20))

    def display_disciple(self, disciples):
        for index, disciple in enumerate(disciples):
            disciple_surface = self.font.render(f'Disciple: {disciple}', True, (255, 255, 255))
            self.screen.blit(disciple_surface, (50, 100 + index * 30))

    def display_realms(self, realms):
        for index, realm in enumerate(realms):
            realm_surface = self.font.render(f'Realm: {realm}', True, (255, 255, 255))
            self.screen.blit(realm_surface, (50, 100 + index * 30))

    def display_spirit_stones(self, spirit_stones):
        for index, stone in enumerate(spirit_stones):
            stone_surface = self.font.render(f'Spirit Stone: {stone}', True, (255, 255, 255))
            self.screen.blit(stone_surface, (50, 100 + index * 30))

    def display_treasure_pavilion(self, treasures):
        for index, treasure in enumerate(treasures):
            treasure_surface = self.font.render(f'Treasure: {treasure}', True, (255, 255, 255))
            self.screen.blit(treasure_surface, (50, 100 + index * 30))

    def update(self):
        pygame.display.flip()  

# Example usage
def main():
    pygame.init()
    ui = UI(800, 600)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ui.screen.fill((0, 0, 0))  # Clear the screen with black
        ui.display_title('Game UI')
        ui.display_disciple(['Disciple1', 'Disciple2'])
        ui.display_realms(['Realm1', 'Realm2'])
        ui.display_spirit_stones(['Stone1', 'Stone2'])
        ui.display_treasure_pavilion(['Treasure1', 'Treasure2'])
        ui.update()

    pygame.quit()

if __name__ == '__main__':
    main()