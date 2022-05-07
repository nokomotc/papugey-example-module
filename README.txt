papugey-example-module
Example module for telegram bot @papugeybeta_bot

nokomotc.github.io/papugey

papugey filters (only kwargs):

commands (list of str): m/name COMMAND args

fs (list of functions): filters

fs example (you can't check admin rights like that, but imagine you can)

await register_handler(self.command, fs=[self.filter])

async def filter(self, message):

  return message.from_user.is_chat_admin # bool
  
you can get aiogram.Bot via self.bot
