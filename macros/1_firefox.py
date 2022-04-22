# MACRO ..... : Firefox
# DESCRIPTION : Firefox Hotkeys incl. Bitwarden Add-On

from keycode_win_de import Keycode

app = {
    'name' : 'FIREFOX',
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000020, '+ TAB', [Keycode.CONTROL, 't']),
        (0x200000, '+ WDW', [Keycode.CONTROL, 'n']),
        (0x000020, 'BW PW', [Keycode.CONTROL, Keycode.SHIFT, 'l']),
        # 2nd row ----------
        (0x770de0, '- TAB', [Keycode.CONTROL, 'w']),
        (0x770de0, '- WDW', [Keycode.CONTROL, Keycode.SHIFT, 'w']),
        (0x000000, 'BW 2F', [Keycode.CONTROL, Keycode.SHIFT, 'l', 1.0, -Keycode.SHIFT, 'v', Keycode.ENTER]),
        # 3rd row ----------
        (0x0de05e, '< Back', [Keycode.ALT, Keycode.LEFT_ARROW]),
        (0x000000, 'Forw >', [Keycode.ALT, Keycode.RIGHT_ARROW]),
        (0x000000, 'Reload', [Keycode.F5]),
        # 4th row ----------
        (0x0de05e, '< Tab', [Keycode.CONTROL, Keycode.PAGE_UP]),
        (0x0de05e, 'Tab >', [Keycode.CONTROL, Keycode.PAGE_DOWN]),
        (0x0de05e, 'DL', [Keycode.CONTROL, 'j']),
        # Encoder button ---
        (0x000000, 'Quit', [Keycode.ALT, Keycode.F4])
    ]
}