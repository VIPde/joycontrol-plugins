import logging
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from TimeSkipBasePlugin import TimeSkipBasePlugin

logger = logging.getLogger(__name__)

class AutoLotoID(TimeSkipBasePlugin):
    async def run(self):
        logger.info('Auto Loto-ID Plugin loaded!')

        '''
        Reference:
          https://github.com/watagi/AutoWatt
        '''

        while True:
            # Talk to Rotomi
            await self.button_push('a')
            await self.wait(0.3)
            await self.button_push('a')
            await self.wait(0.3)
            await self.button_push('down')
            await self.wait(0.3)
            await self.button_push('a') # Select the try loto-ID
            await self.wait(0.8)

            await self.button_push('a')
            await self.wait(0.3)
            await self.button_push('a')
            await self.wait(0.3)
            await self.button_push('a')
            await self.wait(0.8)
            await self.button_push('a') # Save
            await self.wait(0.3)

            # Close the all messages
            for _ in range(32):
                await self.button_push('b')
                await self.wait(0.3)

            await self.change_year()