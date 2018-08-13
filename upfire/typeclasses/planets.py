from evennia.utils import lazy_property

from commands.planet import PlanetCommandSet
from objects import Object
from world.traits import TraitHandler


class Planet(Object):
    """
    Describes basic type for all the planets
    """

    def at_object_creation(self):
        self.cmdset.add_default(PlanetCommandSet, permanent=True)
        self.locks.add("puppet:all();call:false()")
        self.volume = 10000000
        self.traits.add(
            name="Population",
            key="population",
            type="counter",
            base=0,
        )
        self.traits.add(
            name="Temperature",
            key="temperature",
            type="static",
            base=0,
            mod=0,
        )
        self.resources.add(
            name="Various metals",
            key="metals",
            type="counter",
            base=0,
        )
        self.resources.add(
            name="Various minerals",
            key="minerals",
            type="counter",
            base=0,
        )

    def return_appearance(self, looker=None):
        desc_string = "Planet %s \n\n" % self.name
        desc_string += "Mass: %i\n" % self.mass
        desc_string += "Traits:\n"
        desc_string += "----------------\n"
        for trait in self.traits.all:
            trait = self.traits[trait]
            desc_string += str(trait.name) + ": " + str(trait.actual) + "\n"
        desc_string += "\nResources:\n"
        desc_string += "----------------\n"
        for resource in self.resources.all:
            resource = self.resources[resource]
            desc_string += str(resource.name) + ": " + str(
                resource.actual) + "\n"
        return desc_string

    @lazy_property
    def traits(self):
        return TraitHandler(self)

    @lazy_property
    def resources(self):
        return TraitHandler(self, db_attribute="resources")
