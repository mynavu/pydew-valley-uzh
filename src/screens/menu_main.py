from collections.abc import Callable

import pygame

from src.enums import GameState
from src.gui.menu.general_menu import GeneralMenu


class MainMenu(GeneralMenu):
    def __init__(self, switch_screen: Callable[[GameState], None], set_token_status: Callable[[bool], None]):
        options = ["Play", "Quit","Enter a Token to Play"]
        title = "Main Menu"
        size = (400, 400)
        super().__init__(title, options, switch_screen, size, set_token_status)
        self.input_active = False
        self.token_input = ""
        self.token_entered = False
        self.play_button_enabled = False  # Initialize as False
    def button_action(self, text):
        if text == "Play" and self.play_button_enabled:
            self.switch_screen(GameState.PLAY)  # Only allow playing if the token is valid
        elif text == "Enter a Token to Play":
            self.input_active = True
            self.token_input = ""
        elif text == "Quit":
            self.quit_game()

    def handle_event(self, event: pygame.event.Event) -> bool:
        if super().handle_event(event):
            return True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.quit_game()
                return True

            if self.input_active and event.key == pygame.K_RETURN:
                if self.validate_token(self.token_input):
                    self.play_button_enabled = True 
                    self.set_token_status(True)
                    self.input_active = False  # Deactivate token input mode
                    print("Token is valid, Play button enabled.")
                else:
                    print("Invalid Token, try again!")
                return True

        return False
