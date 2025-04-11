from traps import Spike, Void, MSpike
from levels.level import Level
from thepalette import Color
def gotolvl5():
    import lvl1
lvl = Level((1200, 600), gotolvl5, Color(rgb=(30, 30, 30)))
lvl.traps.append(MSpike(lvl.display, 450, 364, (300, 364)))
lvl.traps.append(MSpike(lvl.display, 465, 364, (315, 364)))
lvl.traps.append(MSpike(lvl.display, 480, 364, (330, 364)))
lvl.traps.append(MSpike(lvl.display, 495, 364, (345, 364)))
lvl.traps.append(Void(lvl.display, 7, (510, 600)))
lvl.traps.append(Void(lvl.display, 10, (720, 600)))
lvl.traps.append(MSpike(lvl.display, 732, 364, (550, 364)))
lvl.traps.append(MSpike(lvl.display, 764, 364, (700, 364)))
lvl.run()