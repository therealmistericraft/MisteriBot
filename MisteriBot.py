# coding=utf-8

import discord
from discord.ext import commands
from discord.ext import tasks
import random
from time import sleep
from discord.utils import get
import json

#Dreistellige Fehlernummern: Fehler, die die Öffentlichkeit sehen können; Vierstellige Fehlernummern: interne Fehler

#TODO: *hier einfügen*

#clipboard
#1️⃣
#2️⃣
#3️⃣
#4️⃣
#5️⃣
#6️⃣
#7️⃣
#8️⃣
#9️⃣
#0️⃣
#❎
#⬅️
#➡️
#🎲
file = open('prefix.txt', 'r')
data = file.read()
data = data.split('\n')
prefix = data[0]
file.close()

client = commands.Bot(command_prefix=prefix)
client.remove_command('help')

helpmessage = 'Hier sind die Commands, die ich ausführen kann: \n\n `` '+prefix+'getID `` [Optional: `` channel `` oder `` [@MENTION] ``] - Zeigt deine eigene ID bzw. die des Textchannels oder des gewählten Nutzers an. (Aliases: `` '+prefix+'id `` )\n\n `` '+prefix+'clear `` - Löscht die in einer Zahl danach eingegebene Anzahl an Nachrichten, Pins sind ausgeschlossen. (Diese Funktion ist nicht für alle verfügbar.)\n\n `` '+prefix+'wuerfeln `` - Würfelt einen Würfel (Zahlen 1-6). Für andere Würfel bitte mit einem Leerzeichen getrennt die maximale Zahl eingeben.\n\n `` '+prefix+'entscheidung [Sache 1] [Sache 2] `` - Hilft euch, zwischen zwei nachfolgend angegebenen Sachen zu entscheiden.\n\n `` '+prefix+'ping `` - Zeigt die aktuelle Latenz zwischen deinem Client und dem Bot in Millisekunden an. Achtung: Die Zahl ist nicht wirklich aussagekräftig über deine Internetleitung.\n\n `` '+prefix+'pc [NAME] `` - Erstellt einen Privatchat-Kanal mit dem angegebenen Namen, zu dem weitere Mitglieder hinzugefügt werden können. Aliases: `` '+prefix+'privatchat `` \n     Mit `` '+prefix+'pc_add [@MENTION] `` können weitere Nutzer hinzugefügt werden.\n     Bitte beachte, dass alle Teammitglieder trotzdem euren Chatverlauf lesen können.\n\n``'+prefix+'embed`` - Stellt die angegebene Nachricht als Embed dar.\n\n``'+prefix+'google`` - Gibt einen Link zur Google-Suche, die nachfolgend angegeben wurde, aus.'


helpembed1 = discord.Embed(title='Hilfe - Seite 1', description='**Tools**\n*Wörter in* ``[eckigen Klammern]`` *müssen* ***ersetzt*** *werden*\n*Wörter in* ``(Klammern)`` *sind* ***optional***\n*Durch* ``/`` *getrennte Wörter sind* ***alternativ***\n-', colour=discord.Colour.from_rgb(r=255, g=127, b=0))
helpembed1 = helpembed1.add_field(name='**'+prefix+'clear [(Anzahl)]**', value='Dieser Command **löscht** die nachfolgend angegebene Anzahl an **Nachrichten** (standardgemäß eine). **Angepinnte Nachrichten** werden **ausgelassen**.\n\n*Dieser Command kann nur von Leuten ausgeführt werden, die Nachrichten verwalten dürfen.*', inline=True)
helpembed1 = helpembed1.add_field(name='**'+prefix+'clear pinned [(Anzahl)]**', value='Dieser Command **löscht** die nachfolgend angegebene Anzahl an **Nachrichten** (standardgemäß eine), **inklusive** der **angepinnten Nachrichten**\n\n*Dieser Command kann nur von Leuten ausgeführt werden, die Nachrichten verwalten dürfen.*', inline=True)
helpembed1 = helpembed1.add_field(name='**'+prefix+'getID (channel/[#CHANNEL]/[@MENTION])**', value='Gibt *deine eigene* (Wenn nachfolgend leer) ID / die ID des *Channels* / die ID des *ausgewählten Channels* / die ID der *ausgewählten Person* aus.\n``Alias: '+prefix+'id``', inline=False)
helpembed1 = helpembed1.add_field(name='**'+prefix+'ping**', value='Gibt die Latenz zum Bot im ``ms`` an.\n***Achtung:*** *Die Latenz kann auch durch die Internetleitung des Hosts beeinflusst werden.*', inline=False)
helpembed1 = helpembed1.add_field(name='**'+prefix+'embed [Nachricht]**', value='Stellt deine Nachricht als Embed dar.', inline=False)
helpembed1 = helpembed1.add_field(name='**'+prefix+'changeprefix [Prefix]**', value='Ändert das Prefix des Bots. \n\nDieser Command kann nur von Leuten ausgeführt werden, die Webhooks verwalten dürfen.')

helpembed2 = discord.Embed(title='Hilfe - Seite 2', description='**Misc (Miscellanineous)**\n*Wörter in* ``[eckigen Klammern]`` *müssen* ***ersetzt*** *werden*\n*Wörter in* ``(Klammern)`` *sind* ***optional***\n*Durch* ``/`` *getrennte Wörter sind* ***alternativ***\n-', colour=discord.Colour.from_rgb(r=255, g=127, b=0))
helpembed2 = helpembed2.add_field(name='**'+prefix+'wuerfeln [(max. Augenzahl)]**', value='Würfelt eine Zahl von 0 bis zur angegebenen Maximalzahl (wenn leer: 6)')
helpembed2 = helpembed2.add_field(name='**'+prefix+'entscheidung [Sache 1] [Sache 2]**', value='Hilft dir, dich zwischen den angegebenen Dingen zu entscheiden.')
helpembed2 = helpembed2.add_field(name='**'+prefix+'pc [Name]**', value='Eröffnet einen Textkanal, auf den nur du und die Admins zugriff haben. Mit '+prefix+'``pc_add [@MENTION]`` fügst du deine Freunde hinzu.')
helpembed2 = helpembed2.add_field(name='**'+prefix+'google [Suchtext]**', value='Gibt einen Link zur Google-Suche mit dem angegebenen Suchtext aus.')
helpembed2 = helpembed2.add_field(name='**'+prefix+'changelog**', value='Eine Übersicht aller Änderungen der jeweiligen Version. Die Versionen können durch Reaktionen durchgeschaltet werden, standartmäßig wird die aktuelle angezeigt.\n*Alias:* ``'+prefix+'cl``')
helpembed2 = helpembed2.add_field(name='**'+prefix+'howto**', value='Gibt von mir vorgefertigte Hilfen aus, die ich so nicht im Internet finden konnte.\n Verfügbare *how-tos:*\n-``'+prefix+'howto python save var to file`` - Wie man eine oder mehrere Python Variablen in einer Datei speichern kann, damit die Werte auch nach einem Neustart des Skripts gespeichert bleiben.')

clembed0 = discord.Embed(title='Es ist kein älterer Changelog verfügbar.', colour=discord.Colour.red())
clembed1 = discord.Embed(title='Changelog V4.0', colour=discord.Colour.from_rgb(r=255, g=229, b=196))
clembed1 = clembed1.add_field(name='Design', value='-Der ``'+prefix+'help`` -Command ist nun ordendlich in mehreren Embeds, nach Kategorien geordned, die mithilfe von Reaktionen durchgeschaltet und geschlossen werden können.')
clembed1 = clembed1.add_field(name='Bugfixes', value='-Beim ``'+prefix+'embed`` - Command wird nun nicht mehr der komplette eingegebene Text inklusive Command angezeigt, sondern nur der gewünschte Text. Dies war zwar schon vorher integriert, wurde aber durch einen Flüchtigkeitsfehler ausser Kraft gesetzt.\n-Beim Ausführen des ``'+prefix+'help`` -Commands wird nicht mehr unendlich Rückmeldung an mich gesendet.\n-Aufgrund eines Updates seitens Discord konnten zwar Privatchats erstellt werden, aber weder Mitglieder hinzugrfügt, noch wieder gelöscht werden. Das Script wurde dementsprechend an die Version angepasst.')
clembed1 = clembed1.add_field(name='Neue Funktionen', value='Diese Funktionen gibt es zwar schon, sollten aber eigentlich erst in dieser Version erscheinen.\n-``'+prefix+'google [Suchtext]``: Gibt einen Link zur Google-Suche nach dem angegebenen Suchtext aus.\n-Feedback: Wenn du eine Privatnachricht an diesen Bot sendest, wird diese nun an mich weiter geleitet. [open Alpha!!!]\n-``'+prefix+'changelog``: Das hast du ja schon herausgefunden.')
clembed1 = clembed1.add_field(name='Sonstiges', value='-In der Helpnachricht wurde angegeben, dass das Moderatorenteam in Privatchats schauen kann, das kann aber nur der Admin und die Nachricht wurde dementsprechend angepasst.\n-In der Willkommensnachricht wurde auf Funktionen des Bots "Member Count" hingewiesen, der wurde allerdings bereits durch unseren Navnlos ersetzt. Die Nachricht wurde dementsprechend angepasst.')
clembed2 = discord.Embed(title='Changelog V4.1', colour=discord.Colour.from_rgb(r=255, g=229, b=196))
clembed2 = clembed2.add_field(name='Bugfixes', value='-Die Changelog- und Helpnachrichten, die zum dauerhaften Verweil im Kanal gedacht sind, können nicht mehr durchgeschaltet oder entfernt werden.\n-Farbe im Changelog-Embed angepasst\n-Durch den Changelog kann jetzt fehlerfrei und intuitiv durchgeklickt werden.')
clembed2 = clembed2.add_field(name='Sonstiges', value='-``'+prefix+'changelog`` zu ``'+prefix+'help`` hinzugefügt')
clembed3 = discord.Embed(title='Changelog V4.2', colour=discord.Colour.from_rgb(r=255, g=229, b=196))
clembed3 = clembed3.add_field(name='Bugfixes', value='-Bei ``'+prefix+'help`` und ``'+prefix+'changelog`` wird nur noch ein "schliessen"-Button angezeigt.')
clembed3 = clembed3.add_field(name='Design', value='-Beim ``'+prefix+'ping``, ``'+prefix+'entscheidung`` und ``'+prefix+'wuerfeln`` -Command wird die Nachricht nun gelöscht und das Ergebnis in einem Embed dargestellt.\n-Commands, die nur von Moderatoren ausgeführt werden können, werden nun auch gelöscht')
clembed3 = clembed3.add_field(name='Sonstiges', value='-Nach ausführen des ``'+prefix+'wuerfeln`` -Commands kann man dank einer Reaktion ganz schnell erneut Würfeln.')
clembed4 = discord.Embed(title='Changelog V5.0', colour=discord.Colour.from_rgb(r=255, g=229, b=196))
clembed4 = clembed4.add_field(name='Sonstiges:', value='-Würfel-Emoji bei ``'+prefix+'wuerfeln`` zu Standard-Discord-Emoji gemacht\n-Bei ``'+prefix+'wiederruf`` wurde bisher die zuletzt gesendete Nachricht gelöscht, egal, wer diese gesendet hat. Jetzt wird das letzte Feedback des jeweiligen Authors gelöscht, durch erneute Eingabe des Commands kann weiteres Feedback gelöscht werden.\n-Rächtschraipfela koregirt\n-Leute mit der Berechtigung, Nachrichten zu verwalten, können bei bestimmten Commands das Output deaktivieren.\n-Bei ``'+prefix+'entscheidung`` kann nun zwischen unendlich vielen Sachen entschieden werden.')
clembed4 = clembed4.add_field(name='Generelles:', value='Am Namen der Version erkennt ihr, dass es ein großes Update ist. Viel davon merken werdet ihr aber nicht, da es eine Interne Umstellung ist. Viele Variablen werden nun in einer seperaten Textdatei gespeichert, was den Vorteil hat, dass z.B. bei dem ``'+prefix+'changelog`` -Command auch noch durchgeschaltet werden kann, wenn der Bot in der Zwischenzeit neu gestartet wurde.')
clembed4 = clembed4.add_field(name='Neue Funktionen', value='Der ``'+prefix+'howto``-Command gibt von mir vorgefertigte Hilfestellugnen aus, die ich so nicht im Internet finden konnte. Aktuell ist nur ``'+prefix+'howto python save var to file`` verfügbar.\n-Menschen mit kleinen Hammern aus dem Thor-DLC können nun das Prefix des Bots ändern')
clembed5 = discord.Embed(title='Es ist kein neuerer Changelog verfügbar.', colour=discord.Colour.red())


welcome0 = 'Herzlich Willkommen auf dem MisteriCraft Communityserver, '
welcome1 = '! Ich werde dich jetzt in den Server einführen. Das komplizierteste ist eigentlich unser Rollensystem. Wir haben zahlreiche Newsletter, viele auch mit themenspezifischen Chats, die man im Kanal ``#rollen-erhalten`` kostenfrei abonnieren kann. Probier es aus!'
welcome2 = 'Ich denke, die Zeit hat gereicht, um dir eine Rolle zu geben. Führe bitte '+prefix+'help in ``#bot-commands`` aus, um Infos über mich zu erhalten. Ich bin mir sicher, ich kann dir gut behilflich sein. Wenn du Fragen zu einem beliebigen Thema hast oder nicht weiter weißt, zögere nicht, der Anleitung in ``#help`` zu folgen!'

file = open('MisteriBotVars.txt', 'r')
data = file.read()
data = data.split('\n')
weiterleitung_id = data[0]
weiterleitung_id = json.loads(weiterleitung_id)
weiterleitung_author_id = data[1]
weiterleitung_author_id = json.loads(weiterleitung_author_id)
helpids = data[2]
helpids = json.loads(helpids)
helppages = data[3]
helppages = json.loads(helppages)
clids = data[4]
clids = json.loads(clids)
clpages = data[5]
clpages = json.loads(clpages)
diceids = data[6]
diceids = json.loads(diceids)
dicenums = data[7]
dicenums = json.loads(dicenums)
diceauthor = data[8]
diceauthor = json.loads(diceauthor)
file.close()

def refresh():
    datatowrite = str(weiterleitung_id) + '\n' + str(weiterleitung_author_id) + '\n' + str(helpids) + '\n' + str(helppages) + '\n' + str(clids) + '\n' + str(clpages) + '\n' + str(diceids) + '\n' + str(dicenums) + '\n' + str(diceauthor)
    file = open('MisteriBotVars.txt', 'w+')
    file.write(datatowrite)
    file.close()

@client.event
async def on_ready():
    print('Ready.')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=prefix+'help'))

@client.event
async def on_member_join(member):
    global welcome0
    global welcome1
    global welcome2
    await member.send(welcome0+member.mention+welcome1)
    sleep(90)
    await member.send(welcome2)

@client.event
async def on_raw_reaction_add(payload):
    if not payload.user_id == 707242307610476595 and not payload.user_id == 708584393555312690:
        print('Es wurde mit "'+payload.emoji.name+'" reagiert.')
        if payload.emoji.name == '➡️':
            global helpids
            global clids
            if payload.message_id in helpids:
                index = helpids.index(payload.message_id)
                if helppages[index] < 2:
                    helppages[index] += 1
                    refresh()
                channel = client.get_channel(payload.channel_id)
                message = await channel.fetch_message(payload.message_id)
                guild_id = payload.guild_id
                guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                await message.remove_reaction(payload.emoji, member)
                if helppages[index] == 2:
                    global helpembed2
                    await message.edit(content=None, embed=helpembed2)
            if payload.message_id in clids:
                index = clids.index(payload.message_id)
                if clpages[index] < 5:
                    clpages[index] += 1
                    refresh()
                channel = client.get_channel(payload.channel_id)
                message = await channel.fetch_message(payload.message_id)
                guild_id = payload.guild_id
                guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                await message.remove_reaction(payload.emoji, member)
                if clpages[index] == 1:
                    await message.edit(content=None, embed=clembed1)
                if clpages[index] == 2:
                    global clembed2
                    await message.edit(content=None, embed=clembed2)
                if clpages[index] == 3:
                    global clembed3
                    await message.edit(content=None, embed=clembed3)
                if clpages[index] == 4:
                    global clembed4
                    await message.edit(content=None, embed=clembed4)
                if clpages[index] == 5:
                    global clembed5
                    await message.edit(content=None, embed=clembed5)
        if payload.emoji.name == '⬅️':
            if payload.message_id in helpids:
                index = helpids.index(payload.message_id)
                if helppages[index] > 1:
                    helppages[index] -= 1
                    refresh()
                channel = client.get_channel(payload.channel_id)
                message = await channel.fetch_message(payload.message_id)
                guild_id = payload.guild_id
                guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                await message.remove_reaction(payload.emoji, member)
                if helppages[index] == 1:
                    global helpembed1
                    await message.edit(content=None, embed=helpembed1)
                if helppages[index] == 2:
                    await message.edit(content=None, embed=helpembed2)
            if payload.message_id in clids:
                index = clids.index(payload.message_id)
                if clpages[index] > 0:
                    clpages[index] -= 1
                    refresh()
                channel = client.get_channel(payload.channel_id)
                message = await channel.fetch_message(payload.message_id)
                guild_id = payload.guild_id
                guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                await message.remove_reaction(payload.emoji, member)
                if clpages[index] == 0:
                    global clembed0
                    await message.edit(content=None, embed=clembed0)
                if clpages[index] == 1:
                    await message.edit(content=None, embed=clembed1)
                if clpages[index] == 2:
                    await message.edit(content=None, embed=clembed2)
                if clpages[index] == 3:
                    await message.edit(content=None, embed=clembed3)
                if clpages[index] == 4:
                    await message.edit(content=None, embed=clembed4)
        if payload.emoji.name == '🎲':
            global diceids
            global dicenums
            global diceauthor
            if payload.message_id in diceids:
                channel = client.get_channel(payload.channel_id)
                message = await channel.fetch_message(payload.message_id)
                guild_id = payload.guild_id
                guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                await message.remove_reaction(payload.emoji, member)
                index = diceids.index(payload.message_id)
                dice = random.randint(1, dicenums[index])
                embed = discord.Embed(title='Du hast eine ``' + str(dice) + '`` gewürfelt.', colour=discord.Colour.blue())
                embed.set_author(name=diceauthor[index], icon_url=diceauthor[index].avatar_url)
                await message.edit(content=None, embed=embed)
        if payload.emoji.name == '❎' or payload.emoji.name == 'schliessen':
            if payload.message_id in helpids or payload.message_id in clids or payload.message_id in diceids:
                channel = client.get_channel(payload.channel_id)
                message = await channel.fetch_message(payload.message_id)
                await message.delete()

@client.event
async def on_message(message):
    global prefix
    if isinstance(message.channel, discord.DMChannel) and not message.author.id == 708584393555312690 and not message.author.id == 707242307610476595 and not message.content.startswith(prefix):
        global weiterleitung_id
        global weiterleitung_author_id
        weiterleitung_author_id.append(message.author.id)
        refresh()
        await message.channel.send('Deine Nachricht wird an meinen Programmierer weitergeleitet. Nutze '+prefix+'wiederruf, um die Nachricht wieder zu löschen.')
        user = client.get_user(303166734557380608)
        embed = discord.Embed(title='Feedback von '+str(message.author)+':', description=message.content, colour=discord.Colour.blue())
        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
        weiterleitung = await user.send(content=None, embed=embed)
        weiterleitung_id.append(weiterleitung.id)
        refresh()
    await client.process_commands(message)

@client.command()
@commands.has_permissions(manage_webhooks=True)
async def changeprefix(ctx, arg):
    file = open('prefix.txt', 'w')
    file.write(arg)
    file.close()
    global prefix
    prefix = arg
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=prefix + 'help'))
    await ctx.send(content=None, embed=discord.Embed(title='Das Prefix wurde erfolgreich zu ``'+prefix+'`` geändert.', colour=discord.Colour.orange()))

@client.command()
async def howto(ctx, *, arg):
    if arg == "python save var to file":
        backslashn = repr("\n")
        await ctx.send("**Variablen in Datei Speichern**\n\n1.: `Variablen lesen`\n```python\nfile = open('DATEINAME', 'r')\ndata = file.read()\ndata = data.split('\n')\nvar1 = data[0]\nvar2 = data[1]\n...\n```***Problem:***\nAlle Variablen werden zu einem *string*. Zu einem *integer* kann der wert durch ```python\nint(data[x])\n``` umgewandelt werden, aber bei mir ist es der Fall, dass es sich ausschließlich um *Listen* handelt. Dafür braucht man Spezialwerkzeug: ```python\nimport json\n\nfile = open('DATEINAME', 'r')\ndata = file.read()\ndata = data.split('\n')\nvar1 = data[0]\nprint(type(var1))\n``` ```python\nvar1 = json.loads(var1)\nprint(type(var1))\n``` Durch die *print* Ausdrücke wird die Umwandlung bestätigt/kontrolliert.")
        await ctx.send("-\n2.: ``Variablen schreiben``\nDamit dies wie gewollt funktioniert, brauchen wir zwei Dinge: `Die Variablen müssen wie oben gelesen werden und in den richtigen Objekttypen umgewandelt werden` und: `Wir brauchen ein Programm, dass die im Skript geänderten Variablen auch in der Datei ändert. Das sieht dann bei mir so aus:` ```python\ndef refresh():\n    datatowrite = str(var1) + "+backslashn+" + str(var2) + "+backslashn+" + str(var3) + "+backslashn+" + str(var4)\n    file = open('DATEINAME.DATEITYP', 'w+')\n    file.write(datatowrite)\n    file.close()\n```")
        await ctx.send("3.: `Neue Variablen hinzufügen`\n```python\nfile = open('DATEINAME.DATEITYP', 'a')\nvar5 = 'test'\nfile.write(var5)\n```")
        await ctx.send("**Beachte: Die Datei darf nicht leer sein, sondern muss bereits vor Verwendung je Zeile einen Wert des jeweiligen Typs beinhalten. Die präparierte `.txt` Datei kann dann z.B. so aussehen:** ```python\n#*dateiname.txt*\n[1] #z.B. var1\n1 #z.B. var2\nA #z.B. var3\n[2] #z.B. var4\n``` Die Reihenfolge dieser Werte wird von der Reihenfolge der Variablen in der Variablen `datatowrite` bestimmt; wenn `var1` eine Liste sein soll, muss auch in der `.txt`-Datei in der ersten Zeile ein Wert des Typs `list` stehen.")

@client.command()
async def help(ctx):
    await ctx.channel.purge(limit=1)
    global helpembed1
    global helpids
    message = await ctx.send(content=None, embed=helpembed1)
    helpids.append(message.id)
    refresh()
    helppages.append(1)
    refresh()
    await message.add_reaction('⬅️')
    await message.add_reaction('➡️')
    try:
        await message.add_reaction(':schliessen:732960097344684113')
    except:
        await message.add_reaction('❎')

@client.command()
@commands.has_permissions(manage_messages=True)
async def globalhelp(ctx):
    await ctx.channel.purge(limit=1)
    global helpembed1
    global helpembed2
    await ctx.send(content=None, embed=helpembed1)
    await ctx.send(content=None, embed=helpembed2)

@client.command(aliases=['cl'])
async def changelog(ctx):
    await ctx.channel.purge(limit=1)
    global clembed4
    global clids
    message = await ctx.send(content=None, embed=clembed4)
    clids.append(message.id)
    refresh()
    clpages.append(4)
    refresh()
    await message.add_reaction('⬅️')
    await message.add_reaction('➡️')
    try:
        await message.add_reaction(':schliessen:732960097344684113')
    except:
        await message.add_reaction('❎')

@client.command()
@commands.has_permissions(manage_messages=True)
async def globalchangelog(ctx):
    await ctx.channelk.purge(limit=1)
    global clembed4
    await ctx.send(content=None, embed=clembed4)

@client.command(aliases=['widerruf'])
async def wiederruf(ctx):
    global weiterleitung_id
    global weiterleitung_author_id
    i = len(weiterleitung_author_id)-1
    try:
        while not weiterleitung_author_id[i] == ctx.message.author.id:
            i = i-1
        else:
            msg = await ctx.message.channel.fetch_message(weiterleitung_id[i])
            await msg.edit(content=None, embed=discord.Embed(title='Fehler 0001', colour=discord.Colour.red(), description='Die Nachricht wurde auf Wunsch des Verfassers gelöscht.'))
            weiterleitung_author_id.pop(i)
            refresh()
            weiterleitung_id.pop(i)
            refresh()
    except:
        error = discord.Embed(title='Fehler 001', colour=discord.Colour.red(), description='Ich konnte kein Feedback von dir finden.')
        await ctx.send(content=None, embed=error)

#Dieser Command löscht die ausgewählte Anzahl an Nachrichten.
@client.command(aliases=['c'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, arg=''):
    if arg == '' or arg == '-nogui' or arg == 'pinned':
        num = 1
    else:
        num = int(arg)
    if 'pinned' in ctx.message.content:
        await ctx.channel.purge(limit=num+1)
        if '-nogui' not in ctx.message.content:
            embed = discord.Embed(title='Es wurden ``'+str(num)+'`` Nachrichten inklusive der angepinnten Nachrichten gelöscht.', colour=discord.Colour.orange())
            embed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
            msg = await ctx.send(content=None, embed=embed)
            sleep(5)
            await msg.delete()
    else:
        await ctx.channel.purge(limit=num+1, check=lambda msg: not msg.pinned)
        if '-nogui' not in ctx.message.content:
            embed = discord.Embed(title='Es wurden ``'+str(num)+'`` Nachrichten exklusive der angepinnten Nachrichten gelöscht.', colour=discord.Colour.orange())
            embed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
            msg = await ctx.send(content=None, embed=embed)
            sleep(5)
            await msg.delete()

@client.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def pc_delete(ctx, name):
    if str(discord.utils.get(ctx.message.author.guild.roles, name=name)) == 'None':
        await ctx.send('Dieser Privatchat wurde nicht gefunden.')
    else:
        guild = ctx.message.guild
        await discord.CategoryChannel.delete(get(guild.channels, name=name), reason='Der Kanal (Ein Privatchat) wurde durch den Nutzer gelöscht, offensichtlich wurde er nicht mehr benötigt.')
        await discord.Role.delete(get(guild.roles, name=name),reason='Die Rolle zu einem Privatchat wurde durch den Nutzer gelöscht, offensichtlich wurde sie nicht mehr benötigt.')
        await discord.Role.delete(get(guild.roles, name='{}-admin'.format(name)),reason='Die Rolle zu einem Privatchat wurde durch den Nutzer gelöscht, offensichtlich wurde sie nicht mehr benötigt.')

@client.command(aliases=['personal_channel', 'private_chat', 'privatchat'])
async def pc(ctx, name):
    if isinstance(ctx.message.channel, discord.DMChannel):
        await ctx.send('Dieser Bot ist nicht in einem Privatchat verfügbar.')
    else:
        if '*' in name:
            message = await ctx.send('Der Name darf keine Sonderzeichen enthalten.')
            message_id = message.id
            sleep(5)
            msg = await ctx.message.channel.fetch_message(message_id)
            msg1 = await ctx.message.channel.fetch_message(ctx.message.id)
            await msg.delete()
            await msg1.delete()
        else:
            if name.islower():
                if str(discord.utils.get(ctx.message.author.guild.roles, name=name)) == 'None':
                    guild = ctx.message.guild
                    await guild.create_role(name=name)
                    await guild.create_role(name='{}-admin'.format(name))
                    sleep(0.5)
                    await ctx.message.author.add_roles(get(guild.roles, name=name))
                    await ctx.message.author.add_roles(get(guild.roles, name='{}-admin'.format(name)))
                    name1 = str(name)
                    name1admin = str('{}-admin'.format(name))
                    await guild.create_text_channel(name)
                    channel = get(guild.channels, name=name)
                    await channel.set_permissions(ctx.guild.default_role, read_messages=False)
                    await channel.set_permissions(ctx.guild.me, read_messages=True)
                    await channel.set_permissions(get(guild.roles, name=name1), attach_files=True, embed_links=True, send_messages=True, read_messages=True)
                    await channel.set_permissions(get(guild.roles, name=name1admin), manage_messages=True)
                    await channel.send('Willkommen in deinem privaten Textkanal.\nMit `` '+prefix+'pc_add [UserID] `` kannst du deine Freunde hinzufügen. Falls du die ID nicht weißt, benutze gerne ``'+prefix+'getID [@MENTION]`` Bitte beachte, dass Admins auch Nachrichten aus einem privaten Kanal lesen können!\nWenn der Kanal nicht mehr benötigt wird, schreibe bitte einen unserer Moderatoren (@Mod/TEAM) an.')
                else:
                    await ctx.send('Dieser Name ist leider bereits Vergeben.')
            else:
                message = await ctx.send('Der Name darf keine Großbuchstaben enthalten.')
                message_id = message.id
                sleep(5)
                msg = await ctx.message.channel.fetch_message(message_id)
                msg1 = await ctx.message.channel.fetch_message(ctx.message.id)
                await msg.delete()
                await msg1.delete()

@client.command()
async def pc_add(ctx, p: discord.Member):
    if isinstance(ctx.message.channel, discord.DMChannel):
        await ctx.send('Dieser Bot ist nicht in einem Privatchat verfügbar.')
    else:
        name = ctx.message.channel.name
        guild=ctx.message.guild
        role=get(guild.roles, name=name)
        await p.add_roles(role)
        await ctx.send(str(p)+' hat nun Zugriff auf diesen Kanal.')

#Dieser Command würfelt eine Zahl von 1-6
@client.command(aliases=['roll','dice'])
async def wuerfeln(ctx, arg=6):
    await ctx.channel.purge(limit=1)
    if isinstance(ctx.message.channel, discord.DMChannel):
        await ctx.send('Dieser Bot ist nicht in einem Privatchat verfügbar.')
    else:
        dice = random.randint(1, arg)
        embed = discord.Embed(title='Du hast eine ``'+str(dice)+'`` gewürfelt.', colour=discord.Colour.blue())
        embed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
        msg = await ctx.send(content=None, embed=embed)
        global diceids
        global dicenums
        global diceauthor
        diceauthor.append(ctx.message.author)
        refresh()
        diceids.append(msg.id)
        refresh()
        dicenums.append(arg)
        refresh()
        await msg.add_reaction('🎲')
        try:
            await msg.add_reaction(':schliessen:732960097344684113')
        except:
            await msg.add_reaction('❎')

@client.command()
@commands.has_permissions(manage_messages=True)
async def spam(ctx, arg, arg1='', arg2='', arg3='', arg4=''):
    await ctx.channel.purge(limit=1)
    sleep(10)
    message = arg+''+arg1+''+arg2+''+arg3+''+arg4
    await ctx.send(message)
    await ctx.send(message)
    await ctx.send(message)
    await ctx.send(message)
    await ctx.send(message)
    await ctx.send(message)
    await ctx.send(message)
    await ctx.send(message)
    await ctx.send(message)
    await ctx.send(message)

@client.command()
async def fish(ctx):
    if isinstance(ctx.message.channel, discord.DMChannel):
        await ctx.send('Dieser Bot ist nicht in einem Privatchat verfügbar.')
    else:
        embed = discord.Embed(title='´Blub.´ :tropical_fish:', colour=discord.Colour.dark_blue())
        await ctx.channel.purge(limit=1)
        await ctx.send(content=None, embed=embed)

@client.command(aliases=['zufall','zufallsgenerator'])
async def entscheidung(ctx, *, arg):
    await ctx.channel.purge(limit=1)
    if isinstance(ctx.message.channel, discord.DMChannel):
        await ctx.send('Dieser Bot ist nicht in einem Privatchat verfügbar.')
    else:
        arg = arg.split(' ')
        zufall = random.randint(0, len(arg)-1)
        embed = discord.Embed(title='Der MisteriBot hat sich für ``'+arg[zufall]+'`` entschieden.', colour=discord.Colour.light_grey())
        embed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
        await ctx.send(content=None, embed=embed)

@client.command(aliases=['id','getid','gid'])
async def getID(ctx, arg=' '):
    await ctx.channel.purge(limit=1)
    if isinstance(ctx.message.channel, discord.DMChannel):
        await ctx.send('Dieser Bot ist nicht in einem Privatchat verfügbar.')
    else:
        if arg == ' ':
            id = ctx.author.id
            embed = discord.Embed(title='Deine ID ist: ``'+str(id)+'``.', colour=discord.Colour.purple())
        if arg == 'channel':
            id = ctx.channel.id
            embed = discord.Embed(title='Die ID des Channels ist ``'+str(id)+'``.', colour=discord.Colour.purple())
        if arg.startswith('<@'):
            arg = arg.replace('<', '')
            arg = arg.replace('>', '')
            arg = arg.replace('@', '')
            arg = arg.replace('!', '')
            arg = arg.replace('&', '')
            id = arg
            embed = discord.Embed(title='Die ID des ausgewählten Members ist ``'+str(id)+ '``.', colour=discord.Colour.purple())
        if arg.startswith('<#'):
            arg = arg.replace('<', '')
            arg = arg.replace('#', '')
            arg = arg.replace('#', '')
            arg = arg.replace('>', '')
            id = arg
            embed = discord.Embed(title='Die ID des ausgewählten Channels ist ``'+str(id)+'``.', colour=discord.Colour.purple())
        embed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
        await ctx.send(content=None, embed=embed)

@client.command()
async def ping(ctx):
    await ctx.channel.purge(limit=1)
    if isinstance(ctx.message.channel, discord.DMChannel):
        await ctx.send('Dieser Bot ist nicht in einem Privatchat verfügbar.')
    else:
        ping = round(client.latency*1000)
        embed = discord.Embed(title='Der aktuelle Ping beträgt ``'+str(ping)+'``ms.')
        embed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
        await ctx.send(content=None, embed=embed)

@client.command()
async def write(ctx):
    await ctx.channel.purge(limit=1)
    if ctx.message.author.id == 303166734557380608:
        msg=ctx.message.content
        msg1=msg.replace('*write', '')
        await ctx.send(msg1)

@client.command()
async def embed(ctx):
    await ctx.channel.purge(limit=1)
    msg=ctx.message.content
    msg1=msg.replace(prefix+'embed', '')
    embed= discord.Embed(description=msg1, colour=discord.Colour.dark_grey())
    embed.set_author(name=ctx.message.author,icon_url=ctx.author.avatar_url)
    await ctx.send(content=None, embed=embed)

@client.command()
async def google(ctx):
    message = ctx.message.content
    message = message.replace(prefix, '')
    message = message.replace('google', '')
    msg = message
    test = True
    while test == True:
        message = message.replace(' ', '+')
        if ' ' in message.lower():
            test = True
        else:
            test = False
    link = 'https://www.google.com/search?&q='+message
    embed = discord.Embed(title='Google-Suche: '+msg, description=link)
    await ctx.send(content=None, embed=embed)


client.run('#TODO: Add TOKEN')
