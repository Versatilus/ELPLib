from __future__ import print_function, unicode_literals

from ctypes import windll

from win32con import (VK_CONTROL, VK_LCONTROL, VK_LMENU, VK_LSHIFT, VK_LWIN,
                      VK_MENU, VK_RCONTROL, VK_RMENU, VK_RSHIFT, VK_RWIN,
                      VK_SHIFT)

from dragonfly import Key


class KeyBind(Key):
    """Override default delay."""

    mod_vk = (VK_LCONTROL, VK_LMENU, VK_LSHIFT, VK_LWIN, VK_RCONTROL, VK_RMENU,
              VK_RSHIFT, VK_RWIN, VK_CONTROL, VK_MENU, VK_SHIFT)

    def __init__(self, spec, duration=5):
        super(KeyBind, self).__init__(spec, static=False)
        self.interval_default = duration

    def _execute_events(self, events):
        key_states = [
            k for k in self.mod_vk
            if (windll.user32.GetAsyncKeyState(k) & 0x8000) != 0
        ]
        modifiers = []
        for mod in key_states:
            modifiers.append((mod, False, .01))
        self._keyboard.send_keyboard_events(modifiers)
        return super(KeyBind, self)._execute_events(events)
