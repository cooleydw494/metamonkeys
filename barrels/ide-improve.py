from codemonkeys.base_entities.barrel_class import Barrel


class IdeImprove(Barrel):

    def run(self):

        (self

         # Load a monkey config (omit name to prompt user)
         .with_monkey('signature-monkey')
         .run_automation('default')

         .with_monkey('ide-documentation-monkey')
         .run_automation('default'))
