import papumodule as ppmd # api
papumodule = ppmd.Module('example_module') # here is the name of the module
@papumodule.command(['help']) # usage: m/example_module help
async def help(message, cutted_text): # cutted_text is message.text cutted to be like this example: message.text - m/example_module help 1, cutted_text - 1
    await message.reply('This is an example module...') # aiogram syntax
papumodule.eof() # end of file
