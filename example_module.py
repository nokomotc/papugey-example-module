from papumodule import register_handler, stop_registering
class Module:
    name = 'example_module' # m/example_module
    requirements = [] # if you need something from pypi, just type it here
    # requirements = ['numpy']
    # but don't import the module via python's default import
    
    async def init_module(self): # not __init__, cause it needs to be async
        # first arg is function, which is going to be called, after getting a message
        # after first arg there are aiogram filters, BUT
        # you cannot use command_prefix
        await register_handler(self.help, commands=['help'])
        await register_handler(self.hello, commands=['hello'])
        await register_handler(self.unknown) # no handlers = m/example_module
        await stop_registering() # end of init_module
    async def help(self, message): # usage: m/example_module help
        await message.reply('nope.') # aiogram
    async def hello(self, message): 
        await message.reply('Hello!')
    async def unknown(self, message):
        await message.reply('You sent me "m/example_module". What did you mean?')

# and the structure of the command is:
# m/{name} {command_name} {arguments}
# like:
# m/example_module hello_name Mike
