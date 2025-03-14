import pygame

class DragDrop:
    def __init__(self):
        self.dragging = None  # Track which object is being dragged

    def handle_event(self, event, game_objects):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for obj in game_objects:
                if obj.rect.collidepoint(event.pos):
                    self.dragging = obj

        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self.dragging.rect.move_ip(event.rel)

        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = None
