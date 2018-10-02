import time
from telnetlib import Telnet

from django.conf import settings


def search_buffer(message_buffer, phrase):
    if message_buffer.find(phrase) == -1:
        return False
    else:
        return True


class MudClient(Telnet):
    message_buffer = ''

    def command_and_store(self, command, sleep_time=2):
        raw = ("%s\n" % command).encode()
        self.write(raw)
        time.sleep(sleep_time)
        result = self.read_very_eager().decode()
        self.message_buffer += result
        return result

    def get_and_clear_buffer(self):
        message_buffer = self.message_buffer
        self.message_buffer = ''
        return message_buffer

    def login(self, name, password):
        self.command_and_store('connect %s %s' % (name, password))

    def set_prompt(self):
        self.command_and_store('prompt Room name: %r')

    def __del__(self):
        self.command_and_store('quit')
        super(MudClient, self).__del__()
        return self.get_and_clear_buffer()


def before_scenario(context, scenario):
    context.search_buffer = search_buffer
    context.config.setup_logging()
    context.connection = MudClient(**settings.TEST_HOST)
    context.connection.login(**settings.TEST_USER)
    context.buffers = {
        'login': context.connection.get_and_clear_buffer()
    }
