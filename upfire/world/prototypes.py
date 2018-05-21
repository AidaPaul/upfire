from random import randint

RESOURCE = {
    "key": "Nondescript resource",
    "typeclass": "typeclasses.resources.Resource",
    "volume": 1,
    "amount": 0,
}

ORE = {
    "prototype": "RESOURCE",
    "key": "Nondescript ore",
    "desc": "A generic ore yet to be described.",
    "typeclass": "typeclasses.resources.Ore",
    "amount": lambda: randint(0, 500000000),
    "volume": 10,
    "exec": "obj.populate_with_minerals()",
}

MINERAL = {
    "prototype": "RESOURCE",
    "key": "Nondescript mineral",
    "desc": "A generic mineral yet to be described.",
    "typeclass": "typeclasses.resources.Mineral",
    "volume": 2,
    "amount": lambda: randint(0, 5000),
}

BORONIDE = {
    "prototype": "MINERAL",
    "key": "Boronide",
    "desc": "The primary material used in the construction of power systems "
            "and capacitors and also for the creation of Terraforming "
            "facilities.",
}

CORBOMITE = {
    "prototype": "MINERAL",
    "key": "Corbomite",
    "desc": "Used for advanced shields, stealth systems and electronic "
            "warfare systems.",
}

CORUNDIUM = {
    "prototype": "MINERAL",
    "key": "Corundium",
    "desc": "The primary material used in almost all energy weapons.",
}

DURANIUM = {
    "prototype": "MINERAL",
    "key": "Duranium",
    "desc": "Most common mineral. Due to its abundance, duranium is the basic "
            "construction material, and is used for nearly everything e.g. "
            "construction of factories, mines and ship structures. ",
}

GALLICITE = {
    "prototype": "MINERAL",
    "key": "Gallicite",
    "desc": "Used in the construction of engines, including missile and "
            "fighter engines.",
}

MERCASSIUM = {
    "prototype": "MINERAL",
    "key": "Mercassium",
    "desc": "Used for Research Facilities, life support systems and tractor "
            "beams.",
}

NEUTRONIUM = {
    "prototype": "MINERAL",
    "key": "Neutronium",
    "desc": "Very dense material used for shipyards, advanced armors and "
            "kinetic weapons such as railguns or orbital bombardment systems.",
}

SORIUM = {
    "prototype": "MINERAL",
    "key": "Sorium",
    "desc": "Refined into Fuel, which is consumed by the engines to propel "
            "ships and missiles. Also used for construction of jump drives "
            "and jump gates. Sorium Harvester modules can extract Sorium from "
            "gas giants.",
}

TRITANIUM = {
    "prototype": "MINERAL",
    "key": "Tritanium",
    "desc": "The primary material used in many missile technologies and in "
            "the construction of ordnance factories.",
}

URIDIUM = {
    "prototype": "MINERAL",
    "key": "Uridium",
    "desc": "Used in sensors and fire control systems.",
}

VENDARITE = {
    "prototype": "MINERAL",
    "key": "Vendarite",
    "desc": "Used in the construction of fighters, fighter factories and "
            "fighter bases.",
}
