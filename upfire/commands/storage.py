from evennia import Command, CmdSet
from evennia.utils.evmenu import EvMenu


class CommandLoadIntoStorage(Command):
    """
    Sets planet production focus on specific sector

    Usage:
        set_prod_focus [civilian|naval]

    This will direct the planets economical focus in specified direction.
    """
    pass


class CommandRemoveFromStorage(Command):
    """
    Sets planet production focus on specific sector

    Usage:
        set_prod_focus [civilian|naval]

    This will direct the planets economical focus in specified direction.
    """
    pass


class StorageCommandSet(CmdSet):
    key = "storagecommandset"

    def at_cmdset_creation(self):
        self.add(CommandLoadIntoStorage())
        self.add(CommandRemoveFromStorage())
