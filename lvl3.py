from traps import Spike, Void, MSpike
from levels.level import Level
from thepalette import Color
def gotolvl4():
    import lvl4
lvl = Level((1200, 600), gotolvl4, Color(hex="#F7374F"))
lvl.traps.append(Spike(lvl.display, 450, 364))
lvl.traps.append(Spike(lvl.display, 480, 364))
lvl.traps.append(Void(lvl.display, 9, (630, 600)))
lvl.traps.append(MSpike(lvl.display, 700, 364, (550, 364)))
lvl.run()