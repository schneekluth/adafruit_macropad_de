# MACRO ..... :  Windows
# DESCRIPTION :  Basic Windows Functions

from keycode_win_de import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {
    'name' : 'WINDOWS',
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000020, 'Vol-', [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0x000020, 'Mute', [[ConsumerControlCode.MUTE]]),
        (0x000020, 'Vol+', [[ConsumerControlCode.VOLUME_INCREMENT]]),
        # 2nd row ----------
        (0x404000, 'TSKMGR', [Keycode.CONTROL, Keycode.SHIFT, Keycode.ESCAPE]),
        (0x02180B, 'DSKTP', [Keycode.WINDOWS, 'd']),
        (0x200000, 'CBHist', [Keycode.WINDOWS, 'v']),
        # 3rd row ----------
        (0x380e0e, 'Cut', [Keycode.CONTROL, 'x']),
        (0x02180B, 'FCKSKP', [Keycode.WINDOWS, Keycode.ESCAPE]),
        (0x663300, 'Lock', [Keycode.WINDOWS, 'l']),
        # 4th row ----------
        (0x380e0e, 'SelAll', [Keycode.CONTROL, 'a']),
        (0x380e0e, 'Copy', [Keycode.CONTROL, 'c']),
        (0x380e0e, 'Paste', [Keycode.CONTROL, 'v']),
        # Encoder button ---
        (0x000000, 'Quit', [Keycode.ALT, Keycode.F4])
    ]
}