from evennia import default_cmds
from evennia.utils import spawner

from objects import Object
from world.resources import MINERAL_TYPES


class Resource(Object):
    """
    Describes basic type for all the resources
    """

    def at_object_creation(self):
        self.db.desc = "A generic resource yet to be described."
        self.db.amount = 0
        self.db.volume = 0
        self.cmdset.add_default(default_cmds.CharacterCmdSet)


class Ore(Resource):
    """
    Base class for all the ores
    """

    def populate_with_minerals(self, seed=None):
        for mineral in MINERAL_TYPES:
            prototype = spawner.spawn(return_prototypes=True)[mineral]
            prototype['location'] = self
            spawner.spawn(prototype)


class Mineral(Resource):
    """
    Base class for all the minerals
    """
    pass
