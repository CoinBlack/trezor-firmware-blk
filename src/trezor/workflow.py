from trezor import loop

started = []
default = None
default_handler = None
layouts = []


def onstart(w):
    started.append(w)


def onclose(w):
    started.remove(w)
    if not started and not layouts and default_handler:
        startdefault(default_handler)


def closedefault():
    global default

    if default:
        loop.close(default)
        default = None


def startdefault(handler):
    global default
    global default_handler

    if not default:
        default_handler = handler
        default = handler()
        loop.schedule(default)


def restartdefault():
    global default_handler
    d = default_handler
    closedefault()
    startdefault(d)


def onlayoutstart(l):
    closedefault()
    layouts.append(l)


def onlayoutclose(l):
    layouts.remove(l)
