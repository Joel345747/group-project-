def set_labels(self):
    big_font = pygame.font.SysFont('monospcae',24, bold=True)
    small_font = pygame.font.SysFont('monospace',18)
    self.big_lbl = big_font.render(f'G A M E O V E R', 1,(0, 0, 0))
    self.smal_lbl = small_font.render(f'press r to restart', 1, (0, 0, 0))


def over(self):
    screen.blit(self.big_lbl, (WIDTH // 2 - self.big._lbl.get_width() // 2, HEIGHT // 4))
    screen.blit(self.small_lbl, (WIDTH // 2 - self.small_lbl.get_width() // 2, HEIGHT // 2)
