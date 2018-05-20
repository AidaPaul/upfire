from evennia import Command, CmdSet


class CommandSetProductionFocus(Command):
    """
    Sets planet production focus on specific sector

    Usage:
        set_prod_focus [civilian|naval]

    This will direct the planets economical focus in specified direction.
    """
    key = "set_prod_focus"
    aliases = ["spf"]

    def func(self):
        caller = self.caller
        location = caller.location
        self.args = self.args[1:]

        if not self.args:
            message = "You must specify production focus for it to work!"
            location.msg_contents(message)
            return

        if self.args not in ["civilian", "naval"]:
            message = "Focus must be either civilian or naval! %s provided" % \
                      self.args[0]
            location.msg_contents(message)
            return

        message = "Great, planet focus set to %s" % self.args
        location.msg_contents(message)


class PlanetCommandSet(CmdSet):
    key = "planetcommandset"

    def at_cmdset_creation(self):
        self.add(CommandSetProductionFocus())
