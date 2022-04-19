#!/usr/bin/env python3
import iterm2

raw_commands = [
    'topgrade',
    'cd vogelbuch && ./get_current_tweets.sh',
    './gpncl_copy.sh',
    './backup.sh',
]

commands = ['zsh -c \'source ~/.env && {' + x + ' ; }\'' for x in raw_commands]

async def main(connection):
    window = await iterm2.Window.async_create(connection, command=commands.pop(0))
    for command in commands:
        try:
            await window.async_create_tab(command=command)
        except:
            # it throws because it wants to call
            # Window.delegate.window_delegate_get_tab_with_session_id
            # TODO: find a better workaround for that
            pass

iterm2.run_until_complete(main)
