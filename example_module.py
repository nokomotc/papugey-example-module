import papumodule as ppmd # api
papumodule = ppmd.Module('example_module') # here is the name of the module
@papumodule.command(['help']) # usage: m/example_module help
async def help(message): # please note, that command structure is like this - m/{mod_name} {func_name} {args}
    await message.reply('This is an example module...') # aiogram syntax
papumodule.eof() # end of file
