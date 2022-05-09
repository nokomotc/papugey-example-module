from papumodule import register_handler
class Module:
    name = 'example_module' # m/example_module
    requirements = [] # if you need something from pypi, just type it here
    # requirements = ['numpy']
    
    def __init__(self):
        # first arg is function, which is going to be called, after getting a message
        # after first arg there are papu_filters. They're going to be described in readme
        register_handler(self.help, commands=['help'], fs=[self.homemade_filter]) # applying the filter
        register_handler(self.hello, commands=['hello'])
        register_handler(self.unknown) # no handlers = m/example_module
    async def homemade_filter(self, message):
        # The command with this filter won't work if user's first name starts with 'a' or 'A'
        return False if message.from_user.first_name.lower().startswith('a') else True 
    def import_requirements(self): # there are no requirements
        # but if they were:
        # global numpy # to make import be global
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

