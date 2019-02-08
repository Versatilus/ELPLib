from __future__ import print_function

import subprocess
from builtins import str
from time import sleep

from psutil import process_iter

from dragonfly import Function, Pause


def create_hidden_window(arguments):
    si = subprocess.STARTUPINFO()
    si.dwFlags = subprocess.STARTF_USESHOWWINDOW
    si.wShowWindow = subprocess.SW_HIDE
    return subprocess.Popen(
        arguments,
        close_fds=True,
        startupinfo=si,
        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)


def eyemouse_launcher(kill=False):
    for process in process_iter(attrs=['name']):
        if process.info['name'] == "EyeXMouse.exe":
            process.kill()
            process.wait()
    if not kill:
        create_hidden_window(
            "C:\\Users\\User\\GitHub\\Versatilus\\ELPLib\\ELPLib\\utilities\\EyeXMouse.exe"
        )


def pause_mouse(action_object, delay=1):
    return Function(
        eyemouse_launcher, kill=True) + Pause(
            str(delay)) + action_object + Function(eyemouse_launcher)


class MousePauseFunction(Function):
    def __init__(self, function, execution_delay=1, **defaults):
        self.delay = execution_delay
        super(MousePauseFunction, self).__init__(function, **defaults)

    def _execute(self, data=None):
        eyemouse_launcher(kill=True)
        sleep(self.delay * .01)
        super(MousePauseFunction, self)._execute(data)
        sleep(self.delay * .01)
        eyemouse_launcher()
