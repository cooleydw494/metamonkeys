from codemonkeys.entities.barrel import Barrel
from codemonkeys.utils.monk.theme_functions import print_t


class IdeImprove(Barrel):

    def run(self):

        (self

         # Load a monkey config (omit name to prompt user)
         .with_monkey('signature-monkey')
         .run_automation('default')

         .with_monkey('ide-documentation-monkey')
         .run_automation('default'))
