from commands.storage import StorageCommandSet
from typeclasses.objects import Object


class Building(Object):
    """
    The abstract building type, makes sure to be built on appropriate land.
    """

    def at_object_creation(self):
        self.cmdset.add_default(StorageCommandSet, permanent=True)
        self.locks.add("puppet:all();call:false()")
        self.volume = 100.00
