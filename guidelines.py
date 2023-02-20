#!/usr/bin/env python3

"""
This script serves at generating the many ``!editmessage`` commands
needed by Not a Bot to update the messages in the #guidelines channel.

This script can be used within the repository in which case it reads
the content of the ``guidelines.md`` file. It can also be used
standalone it which case it download the guidelines from the github
master branch.

By default all ``!editmessage`` commands are shown at once. In case you
want to print the messages one at a time (e.g. to run them manually) you
can run the script with the ``-i``/``--interactive`` option.

The script can be used as a library too:

    import guidelines

    rules = guidelines.load()
    assert len(rules) <= len(guidelines.slots), "Not enough slots"

    editmessages = [
        guidelines.format_editmessage(slot, color, title, content)
        for slot, color, (title, content)
        in zip(guidelines.slots, guidelines.colors, rules)
    ]
    print(editmessages)  # ['!editmessage...', '!editmessage...', ...]

"""

import argparse
import itertools
import json
import os
import sys
import urllib.request


download_url = 'https://raw.githubusercontent.com/NotANameServer/discord/main/guidelines.md'

channel_url = 'https://discord.com/channels/323076998576603137/860920579154772018/'
slots = [
    '860920639182077952', '860920736470663178', '860920938074079233',
    '860920994973745182', '860921064211873792', '860921120818987038',
    '860921172912111656', '860921226150412289', '860927662649114655',
    '860928557538476083', '860928670105600021', '860928737185234944',
    '860928788437925908', '860928835910762516', '860928879831941140',
    '957023249684914256', '1017117136621142066', '1017399866659442719',
    '1061681906434977802', '1061681934956249098',
]

colors = itertools.cycle([
    0x000000, 0x007f7f, 0x00fefe, 0x7f7f00, 0x7ffe7f, 0xfe00fe, 0x00007f,
    0x007ffe, 0x7f0000, 0x7f7f7f, 0x7ffefe, 0xfe7f00, 0x0000fe, 0x00fe00,
    0x7f007f, 0x7f7ffe, 0xfe0000, 0xfe7f7f, 0x007f00, 0x00fe7f, 0x7f00fe,
    0x7ffe00, 0xfe007f, 0xfe7ffe
])

server_url = 'https://discord.com/channels/323076998576603137/'
substitutions = {
    '#bots-discord':               f'[#bots-discord]({server_url}539809627987247135)',
    '#création-bots-discord':      f'[#création-bots-discord]({server_url}539809627987247135)',
    '#database':                   f'[#database]({server_url}389159935830654976)',
    '#discussions':                f'[#discussions]({server_url}323076998576603137)',
    '#detente':                    f'[#detente]({server_url}392444836441227274)',
    '#etudes-orientation':         f'[#etudes-orientation]({server_url}405326955458592770)',
    '#live':                       f'[#live]({server_url}706871523084075009)',
    '#offres':                     f'[#offres]({server_url}411544328717205504)',
    '#python':                     f'[#python]({server_url}358724995159031820)',
    '#questions-professionnelles': f'[#questions-professionnelles]({server_url}710846454549446698)',
    '#rejoindre-les-canaux':       f'[#rejoindre-les-canaux]({server_url}440592843489280011)',
    '#screenshots':                f'[#screenshots]({server_url}643835487903023104)',
    '#sciences':                   f'[#sciences]({server_url}434331479607083008)',
    '#sécurité':                   f'[#sécurité]({server_url}910211300313952336)',
    '#vos-projets':                f'[#vos-projets]({server_url}666594934278586368)',
    ':lourd:':                     '<:lourd:390149780896088074>',
    ':modo:':                      '<:modo:459352634038550529>',
}

def replace_all(string, substitutions):
    for source, dest in substitutions:
        string = string.replace(source, dest)
    return string


def load():
    try:
        file = open(__file__.replace('.py', '.md'), 'rb')
    except OSError:
        file = urllib.request.urlopen(download_url)
    with file:
        file_content = file.read().decode()

    return [
        (title, replace_all(content, substitutions.items()))
        for section in file_content.split('##')
        for title, _, content in (
            section.lstrip('#').strip().partition('\n\n'),
        )
        if content
    ]


def format_editmessage(slot, color, title, content):
    embed = json.dumps({"embed": {
        "color": color,
        "title": title,
        "description": content,
    }}, ensure_ascii=False)
    return f"!editmessage {channel_url}{slot}\n```\n{embed}\n```"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--interactive',
        dest='interactive', action='store_true',
        help="print each !editmessage one at a time on its own screen",
    )
    options = parser.parse_args()

    def printerr(*args, **kwargs):
        print(*args, **kwargs, file=sys.stderr)

    def pause():
        printerr("\nPress enter to continue...", end="")
        input()
        os.system('clear' if os.name == 'posix' else 'cls')


    guidelines = load()
    length = len(guidelines) + 1

    if options.interactive:
        printerr("Guidelines:")
        for i, (title, _) in enumerate(guidelines):
            printerr(f"{i+1:02d} {title}")
        printerr(f"\nThere are {len(slots)} slots available")
        pause()

    if len(guidelines) > len(slots):
        raise RuntimeError(
            "Not enough slots, you cannot use the message that "
            "contains the 'new ticket' button, please remove it "
            "and add an empty message"
        )

    iterable = enumerate(zip(slots, colors, guidelines))
    for i, (slot, color, (title, content)) in iterable:
        print(format_editmessage(slot, color, title, content))

        if options.interactive:
            printerr(f"\n[{i + 1}/{length}] {title!r}")
            pause()

    print("!createticketform <#860920579154772018>")
    if options.interactive:
        printerr(f"\n[{length}/{length}] In case the button is gone")
        pause()


if __name__ == '__main__':
    main()
