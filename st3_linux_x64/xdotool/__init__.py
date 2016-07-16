import subprocess
import os


XDOTOOL = os.path.join(os.path.dirname(__file__), "xdotool")


def xdotool(*args):
    return subprocess.check_output([XDOTOOL] + list(args))
