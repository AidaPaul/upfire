from objects import Object
from collections import OrderedDict
import numpy
import random


class Resource(Object):
    """
    Describes basic type for all the resources
    """

    def at_object_creation(self):
        self.db.desc = self.__str__()
        self.locks.add("puppet:all();call:false()")

    def __str__(self):
        return self.__class__.__name__


class Mineral(Resource):
    """
    Base class for all the minerals
    """
    pass


class Boronide(Mineral):
    """
    A mineral called Boronide
    """

    def at_object_creation(self):
        self.db.desc = "The primary material used in the construction of " \
                       "power systems and capacitors and also for the " \
                       "creation of Terraforming facilities."


class Corbomite(Mineral):
    """
    A mineral called Corbomite
    """

    def at_object_creation(self):
        self.db.desc = "Used for advanced shields, stealth systems and " \
                       "electronic warfare systems . "


class Corundium(Mineral):
    """
    A mineral called Corundium
    """

    def at_object_creation(self):
        self.db.desc = "The primary material used in almost all energy weapons."


class Duranium(Mineral):
    """
    A mineral called Duranium
    """

    def at_object_creation(self):
        self.db.desc = "Most common ore and used to build factories, mines " \
                       "and ship structures. "


class Gallicite(Mineral):
    """
    A mineral called Gallicite
    """

    def at_object_creation(self):
        self.db.desc = "Used in the construction of engines, including " \
                       "missile and fighter engines. "


class Mercassium(Mineral):
    """
    A mineral called Mercassium
    """

    def at_object_creation(self):
        self.db.desc = "Used for Research Facilities, life support systems " \
                       "and tractor beams. "


class Neutronium(Mineral):
    """
    A mineral called Neutronium
    """

    def at_object_creation(self):
        self.db.desc = "Very dense material used for shipyards, advanced " \
                       "armors and kinetic weapons such as railguns or " \
                       "orbital bombardment systems. "


class Sorium(Mineral):
    """
    A mineral called Sorium
    """

    def at_object_creation(self):
        self.db.desc = "Used for construction of jump drives and jump gates."


class Tritanium(Mineral):
    """
    A mineral called Tritanium
    """

    def at_object_creation(self):
        self.db.desc = "The primary material used in many missile " \
                       "technologies and in the construction of ordnance " \
                       "factories. "


class Uridium(Mineral):
    """
    A mineral called Uridium
    """

    def at_object_creation(self):
        self.db.desc = "Used in sensors and fire control systems."


class Vendarite(Mineral):
    """
    A mineral called Vendarite
    """

    def at_object_creation(self):
        self.db.desc = "Used in the construction of fighters, fighter " \
                       "factories and fighter bases. "


AVAILABLE_MINERALS = [
    Boronide,
    Corbomite,
    Corundium,
    Duranium,
    Gallicite,
    Mercassium,
    Neutronium,
    Sorium,
    Tritanium,
    Uridium,
    Vendarite,
]


class Ore(Resource):
    """
    Base class for all the ores
    """

    def at_object_creation(self):
        super(Ore, self).at_object_creation()
        self.populate_with_minerals()
        self.db.volume = 4

    def populate_with_minerals(self, seed=None, minerals=None):
        if minerals is None:
            minerals = AVAILABLE_MINERALS

        numpy.random.seed(seed)
        random.seed(seed)
        minerals_count = len(minerals)
        split = numpy.random.dirichlet(numpy.ones(minerals_count), size=1)[0]
        composition = OrderedDict()
        iteration = 0
        for mineral in minerals:
            composition[str(mineral)] = split[iteration]
            iteration += 1
        self.db.composition = composition

    def return_appearance(self, looker=None):
        desc_string = "Ore %s \n\n" % self.name
        desc_string += "Volume: %i\n\n" % self.db.volume
        desc_string += "Composition: \n"
        for mineral, content in self.db.composition.iteritems():
            desc_string += "%s: %f\n" % (mineral, content)
        return desc_string
