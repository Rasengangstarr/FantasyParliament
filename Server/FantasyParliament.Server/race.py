from enum import IntEnum


class Races(IntEnum):
    NONE = 0 
    ELF = 1
    ORC = 2
    DWARF = 3
    HUMAN = 4


raceNames = {Races.NONE: "N/A", Races.ELF: "Elf", Races.HUMAN:"Human", Races.ORC:"Orc", Races.DWARF:"Dwarf"}

