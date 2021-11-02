import argparse

class ArgParser(argparse.ArgumentParser):
    # Reference: https://github.com/crocollins/pyOS
    def __init__(self, program, name=None, *args, **kwargs):
        argparse.ArgumentParser.__init__(prog=program, *args, **kwargs)
        if name is None:
            self.name = program
        else:
            self.name = name
        self.help = False

    def add_shell(self, shell):
        self.shell = shell

    def print_usage(self, *args, **kwargs):
        try:
            self.shell.stderr.write(self.format_usage())
            self.help = True
        except AttributeError: pass

    def print_help(self, *args, **kwargs):
        try:
            self.shell.stdout.write(self.help_msg())
            self.help = True
        except AttributeError: pass

    def help_msg(self):
        return f"{self.name}{self.format_help()}"