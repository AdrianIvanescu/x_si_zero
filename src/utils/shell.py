'''
creates a shell
'''
from cmd import Cmd

from src.services.database.create_table import CreateTable
from src.services.database.display_table import DisplayTable
from . import version

toolversion = f"v{version.__version__}"


class Shell(Cmd):
    prompt = 'x si zero > '
    intro = f" {toolversion} Type (?) or (help) - to list commands"

    def do_new_game(self):
        pass

    def help_new_game(self) -> str:
        message = ('Start a new game')
        print(message)
        print()
        return message    

    def do_create_table(self, inp):
        table = CreateTable('x_si_zero', 'current_game')
        table.create_table()

    def help_create_table(self):
        print('create a sqlite3 table: x_si_zero.current_game')

    def do_display_current_game(self, inp):
        table = DisplayTable('x_si_zero', 'current_game')
        table.show_table()

    def help_display_current_game(self):
        print('read and display from table: x_si_zero.current_game')    

    def do_exit(self, inp):
        print("bye")
        return True

    def help_exit(self):
        print('exit the application. Shorthand: x q Ctrl-D.')

    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
        print(self.intro)

    def emptyline(self):
        pass

    do_EOF = do_exit
    help_EOF = help_exit


if __name__ == '__main__':
    Shell().cmdloop()
