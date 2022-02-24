from enum import IntEnum


class Races(IntEnum):
    ELF = 1
    ORC = 2
    DWARF = 3
    HUMAN = 4


raceNames = { Races.ELF: "Elf", Races.HUMAN:"Human", Races.ORC:"Orc", Races.DWARF:"Dwarf"}
