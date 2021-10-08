import paputalk as ppmd 
papumodule = ppmd.Module('example_module')
@papumodule.command(['help']) # usage: m/example_module help
async def help(message, cutted_text): # cutted_text is message.text cutted to be like this example: message.text - m/example_module help 1, cutted_text - 1
    await message.reply('This is an example module...')
papumodule.eof()
