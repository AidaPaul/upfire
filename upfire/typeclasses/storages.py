from commands.storage import StorageCommandSet
from typeclasses.objects import Object


class Storage(Object):
    """
    The abstract storage unit to be implemented into actually functioning ones
    """
    def at_object_creation(self):
        self.cmdset.add_default(StorageCommandSet, permanent=True)
        self.locks.add("puppet:all();call:false()")
        self.volume = 100.00
        self.efficiency = 1.5
        self.capacity = 1

    @property
    def capacity(self):
        if self.db.capacity:
            return float(self.db.capacity)

    @capacity.setter
    def capacity(self, capacity):
        self.db.capacity = capacity
        self._recalculate()

    @property
    def efficiency(self):
        return self.db.efficiency

    @efficiency.setter
    def efficiency(self, efficiency):
        self.db.efficiency = efficiency
        self._recalculate()

    def _recalculate(self):
        if self.capacity and self.efficiency:
            self.volume = float(self.capacity * self.efficiency)

    @property
    def spare_capacity(self):
        return (self.capacity + self.volume) - self.mass

    def at_object_receive(self, moved_obj, source_location, **kwargs):
        moved_obj.location = self

    def return_appearance(self, looker=None):
        desc_string = super(Storage, self).return_appearance()
        desc_string += "Spare capacity: %f\n" % self.spare_capacity
        return desc_string


class Landmass(Storage):
    """
    Representation of land masses where stuff can be dumped or buildings placed
    """

    def at_object_creation(self):
        super(Landmass, self).at_object_creation()
        self.capacity = 10000.00
        self.efficiency = 2


class CargoBay(Storage):
    """
    Basic cargo storage used for ships, forbids from storing planets
    """

    def at_object_creation(self):
        super(CargoBay, self).at_object_creation()
        self.capacity = 100.00
        self.db.forbidden_types = ['Planet']
