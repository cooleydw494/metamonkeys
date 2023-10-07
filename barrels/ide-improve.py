from codemonkeys.entities.barrel import Barrel


class IdeImprove(Barrel):

    def run(self):

        (self

         # Load a Monkey (omit name to prompt user)
         .with_monkey('signature')
         .run_automation('default')

         .with_monkey('ide_documentation')
         .run_automation('default'))
