from traps import Void
from levels.level import Level
from thepalette import Color
def gotolvl2():
    import lvl2
lvl = Level((1200, 600), gotolvl2, Color(hex="#CBA35C"))
lvl.traps.append(Void(lvl.display, 9, (670, 600)))
lvl.run()