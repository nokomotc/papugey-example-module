from papumodule import register_handler
class Module:
    name = 'example_module' # m/example_module
    requirements = [] # if you need something from pypi, just type it here
    # requirements = ['numpy']
    
    def __init__(self):
        # first arg is function, which is going to be called, after getting a message
        # after first arg there are papu_filters. They're going to be described in readme
        register_handler(self.help, commands=['help'])
        register_handler(self.hello, commands=['hello'])
        register_handler(self.unknown) # no handlers = m/example_module
    def import_requirements(self): # there are no requirements
        # but if they were:
        # import numpy
        pass
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

