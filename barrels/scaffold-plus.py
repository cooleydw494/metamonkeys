from codemonkeys.entities.barrel import Barrel


class ScaffoldPlus(Barrel):

    def run(self):

        (self

         .with_monkey('scaffold')
         .run_automation('scaffold')

         .with_monkey('signature')
         .run_automation('default')

         .with_monkey('ide_documentation')
         .run_automation('default'))
