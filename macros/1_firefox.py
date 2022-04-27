# MACRO ..... : Firefox
# DESCRIPTION : Firefox Hotkeys incl. Bitwarden Add-On

from keycode_win_de import Keycode

app = {
    'name' : 'FIREFOX',
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x02180B, '+ TAB', [Keycode.CONTROL, 't']),
        (0x380e0e, '+ WDW', [Keycode.CONTROL, 'n']),
        (0x000020, 'BW PW', [Keycode.CONTROL, Keycode.SHIFT, 'l']),
        # 2nd row ----------
        (0x02180B, '- TAB', [Keycode.CONTROL, 'w']),
        (0x380e0e, '- WDW', [Keycode.CONTROL, Keycode.SHIFT, 'w']),
        (0x000020, 'BW 2F', [Keycode.CONTROL, Keycode.SHIFT, 'l', 1.0, -Keycode.SHIFT, 'v', Keycode.ENTER]),
        # 3rd row ----------
        (0x404000, '< Back', [Keycode.ALT, Keycode.LEFT_ARROW]),
        (0x404000, 'Reload', [Keycode.F5]),
        (0x404000, 'Forw >', [Keycode.ALT, Keycode.RIGHT_ARROW]),
        # 4th row ----------
        (0x121212, '< Tab', [Keycode.CONTROL, Keycode.PAGE_UP]),
        (0x121212, 'Tab >', [Keycode.CONTROL, Keycode.PAGE_DOWN]),
        (0x002000, 'DL', [Keycode.CONTROL, 'j']),
        # Encoder button ---
        (0x000000, 'Quit', [Keycode.ALT, Keycode.F4])
    ]
}
