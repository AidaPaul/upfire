from evennia.utils import lazy_property
from objects import Object
from commands.storage import StorageCommandSet


class Storage(Object):
    """
    The abstract storage unit to be implemented into actually functioning ones.
    """

    def at_object_creation(self):
        self.cmdset.add_default(StorageCommandSet, permanent=True)
        self.locks.add("puppet:all();call:false()")
        self.db.allowed_types = []
        self.db.forbidden_types = []
