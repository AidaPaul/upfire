from objects import Object


class Resource(Object):
    """
    Describes basic type for all the resources
    """

    def at_object_creation(self):
        self.db.desc = "A generic resource yet to be described."
        self.db.amount = 0
        self.db.volume = 0


class Ore(Resource):
    """
    Base class for all the ores
    """

    def populate_with_minerals(self, seed=None):
        pass


class Mineral(Resource):
    """
    Base class for all the minerals
    """
    pass
