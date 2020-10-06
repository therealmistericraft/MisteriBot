> Files named after the guild id save every custom thing, except the prefix for now (should be added later, but never change a running system).

> Final file should be a ``.txt``-File!

> Changelog is not saved here, it will be only avaiable in english!

---

### Line 1:
Guild owner id as int. If he reacts with language flag to a setup message (have to be saved in ``MisteriBotVars.txt``!)

### Line 2:
Welcome message as python list, user input split at ingredients (e.g. ``&member_name&``), but it should be saved in the list anyway, so you can exchange it when the message is sent.

### Line 3:
Help embeds. It cannot be custom set, but it should be avaiable in different languages. Saved as List too, it is easier to change the embeds with the code (no if clauses anymore, but list counter as embed pages), but has to be changed (***TODO***)!

### Line 4:
Warnings as a dict (warning id - warning content) in a dict (user id - dict)

### Line 5:
Message that is warned in a dict (warning id - message content)
