from traps import Spike, Void, MSpike
from levels.level import Level
from thepalette import Color
def gotolvl5():
    import lvl5
lvl = Level((1200, 600), gotolvl5, Color(hex="#FEBA17"))
lvl.traps.append(Spike(lvl.display, 450, 364))
lvl.traps.append(Spike(lvl.display, 480, 364))
lvl.traps.append(Void(lvl.display, 7, (510, 600)))
lvl.traps.append(Void(lvl.display, 10, (720, 600)))
lvl.traps.append(MSpike(lvl.display, 732, 364, (550, 364)))
lvl.run()