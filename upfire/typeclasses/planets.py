from evennia import create_object
from evennia.utils import lazy_property

from commands.planet import PlanetCommandSet
from objects import Object
from world.traits import TraitHandler


class NoStorageException(Exception):
    pass


class FindingStorageFailedException(Exception):
    pass


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
        self.storages.append(create_object("typeclasses.storages.Landmass",
                                           key="landmass"))

    def return_appearance(self, looker=None):
        desc_string = "Planet %s \n\n" % self.name
        desc_string += "Mass: %f\n" % self.mass
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
        desc_string += "\nStorages:\n"
        desc_string += "----------------\n"
        storage_free = 0.0
        storage_total = 0.0
        for storage in self.storages:
            storage_free = storage_free + storage.spare_capacity
            storage_total = storage_total + storage.capacity
            desc_string += "%s: %s" % (str(storage), str(storage.capacity))
        desc_string += "\nFree/total: %s/%s" % (storage_free, storage_total)
        return desc_string

    @lazy_property
    def traits(self):
        return TraitHandler(self)

    @lazy_property
    def resources(self):
        return TraitHandler(self, db_attribute="resources")

    @property
    def capacity(self):
        capacity = float(0)
        for storage in self.storages:
            capacity = storage.capacity + capacity
        return capacity

    @property
    def storages(self):
        if not self.db.storages:
            self.db.storages = []
        return self.db.storages

    @storages.setter
    def storages(self, storages):
        self.db.storages = storages

    def at_object_receive(self, moved_obj, source_location, **kwargs):
        if not self.storages:
            moved_obj.location = source_location
            raise NoStorageException("A move to a planet with no storage was"
                                     "allowed!")
        success = False
        for storage in self.storages:
            if storage.spare_capacity >= moved_obj.volume:
                moved_obj.location = storage
                success = True
                break
        if not success:
            raise FindingStorageFailedException
