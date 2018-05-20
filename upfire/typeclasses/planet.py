from commands.planet import PlanetCommandSet
from objects import Object


class Planet(Object):
    """
    Describes basic type for all the planets
    """

    def at_object_creation(self):
        self.cmdset.add_default(PlanetCommandSet, permanent=True)
        self.locks.add("puppet:all();call:false()")
        self.db.desc = "This is a planet still pending to be described."
        self.db.focus = "civilian"
