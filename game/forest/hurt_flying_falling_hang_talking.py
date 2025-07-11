import pygame

from animation import Animation
from forest.forest_resources import ForestResources
from forest.forest_utils import ForestUtils
from state import State


class HurtFlyingFallingHangTalking(State):
    def process_events(self, events):
        if self.get_frame_index() >= len(ForestResources.sync_catapult_hang):
            return ForestUtils.reduce_lives(self.context)
        return None

    def on_enter(self) -> None:
        super().on_enter()
        pygame.mixer.Sound.play(ForestResources.speak_catapult_hang)
        pygame.mixer.Sound.play(ForestResources.sfx_hugo_hang)

    def render(self, screen):
        screen.blit(ForestResources.catapult_hang[12], (0, 0))
        screen.blit(Animation.get_sync_frame(ForestResources.catapult_hangspeak, ForestResources.sync_catapult_hang, self.get_frame_index()), (115, 117))


