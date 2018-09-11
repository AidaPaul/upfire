from evennia import create_object
from evennia.utils import lazy_property, inherits_from

from commands.planet import PlanetCommandSet
from objects import Object
from typeclasses.objects import NoStorageException
from typeclasses.storages import Landmass
from world.traits import TraitHandler


class Planet(Object):
    """
    Describes basic type for all the planets
    """

    def at_object_creation(self):
        self.cmdset.add_default(PlanetCommandSet, permanent=True)
        self.locks.add("puppet:all();call:false()")
        self.volume = float(10000000)
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
        self.allowed_types = [type(Landmass()), ]
        create_object("typeclasses.storages.Landmass", key="landmass",
                      location=self)

    def return_appearance(self, looker=None):
        desc_string = "Planet %s \n\n" % self.name
        desc_string += "Mass: %f\n" % self.mass
        desc_string += "Traits:\n"
        desc_string += "----------------\n"
        for trait in self.traits.all:
            trait = self.traits[trait]
            desc_string += str(trait.name) + ": " + str(trait.actual) + "\n"
        desc_string += "\nStorages:\n"
        desc_string += "----------------\n"
        desc_string += "\nFree/total: %s/%s" % (self.spare_capacity,
                                                self.capacity)
        return desc_string

    @property
    def storages(self):
        return self.contents

    @lazy_property
    def traits(self):
        return TraitHandler(self)

    @lazy_property
    def resources(self):
        return TraitHandler(self, db_attribute="resources")

    @property
    def capacity(self):
        capacity = 0.0
        for storage in self.storages:
            capacity = storage.capacity + capacity
        return capacity

    @property
    def spare_capacity(self):
        storage_free = 0.0
        for storage in self.storages:
            storage_free = storage_free + storage.spare_capacity
        return storage_free

    @storages.setter
    def storages(self, storages):
        self.db.storages = storages

    def announce_move_from(self, destination, msg=None, mapping=None, **kwargs):
        try:
            Object.announce_move_from(self, destination, msg=None,
                                      mapping=None, **kwargs)
        except NoStorageException:
            self.ndb.move_override = True

    def at_object_receive(self, moved_obj, source_location, **kwargs):
        if inherits_from(moved_obj, Landmass):
            moved_obj.location = self
            return
        super(Planet, self).at_object_receive(moved_obj, source_location,
                                              **kwargs)
