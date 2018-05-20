def _change_temperature(caller, raw_string):
    new_temperature = int(raw_string.strip())
    if not new_temperature:
        caller.msg("Aborted!")
    else:
        caller.traits.temperature.mod = new_temperature
        caller.msg("You've set temperature of planet to %i." % new_temperature)


def _set_attribute_to_change(caller, raw_string):
    selected_attribute = raw_string.strip()
    if selected_attribute not in caller.traits:
        caller.msg("Selected trait doesn't exist!")
        return
    caller.ndb._menutree.selected_attribute = selected_attribute


def get_user_input(caller):
    text = \
        """
        Please provide the new value for the attribute
        """
    new_value = yield ("Enter value: ")
    caller.msg("Okay, setting attribute as %s" % new_value)


def main_menu(caller):
    text = \
        """
        What planetary trait do you want to change?
        """
    options = ({"desc": "Change the temperature",
                "goto": "get_user_input"},
               )
    return text, options
