import pygame

from animation import Animation
from forest.forest_resources import ForestResources
from game_data import GameData
from null_state import NullState
from render_type import RenderType
from state import State


class WinTalking(State):
    def __init__(self, context: GameData):
        super().__init__(context)
        self.needs_background = RenderType.PRE
        self.needs_bottom = RenderType.PRE

    def process_events(self, events):
        if self.get_frame_index() >= len(ForestResources.sync_levelcompleted):
            return NullState
        return None

    def on_enter(self) -> None:
        super().on_enter()
        pygame.mixer.Sound.play(ForestResources.speak_levelcompleted)

    def render(self, screen):
        screen.blit(Animation.get_sync_frame(ForestResources.hugo_telllives, ForestResources.sync_levelcompleted, self.get_frame_index()), (128, -16))
