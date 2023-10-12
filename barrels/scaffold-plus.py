from codemonkeys.entities.barrel import Barrel


class ScaffoldPlus(Barrel):

    def run(self):

        (self

         # Load a Monkey (omit name to prompt user)
         .with_monkey('scaffold')
         .run_automation('scaffold')

         .with_monkey('ide_documentation')
         .run_automation('default'))
