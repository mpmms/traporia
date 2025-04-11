from traps import Spike, Void
from levels.level import Level
from thepalette import Color
def gotolvl3():
    import lvl3
lvl = Level((1200, 600), gotolvl3, Color(hex="#1B56FD"))
lvl.traps.append(Spike(lvl.display, 450, 364))
lvl.traps.append(Spike(lvl.display, 480, 364))
lvl.traps.append(Void(lvl.display, 9, (670, 600)))
lvl.run()