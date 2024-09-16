# Albot
## AAU | CCT 24-27 Discord Bot
### Custom Discord Bot for AAU CCT 24-27 line with integrated moodle and O365 support

- - - - -

## Commands

### Admin commands
\# In order to access theese commands, you must be admin
- /admin ping - Pings the bot
- /admin embed - Creates an embed
- /admin echo {message} - Makes the bot say a message
- /admin purge {amount} - Deletes x amount of messages from current channel (default 1)

### Group commands (not implemented yet)
\# In order to use group commands, you must be member of the group (create is of course an exception to this)
- /group create {name} {members_list (comma seperated)} - creates a new group
- /group add {members_list (comma seperated)} - Adds members to group
- /group remove {members_list (comma seperated)} - Removes members from group
- /group delete {name} - Deletes a group

### Personal commands (not implemented yet)
- /personal sync - syncs with moodle and o365
- /personal login {account} - login to o365 or moodle
- /personal logout {account} - logout from o365 or moodle
- /personal notifications - notifications settings

### calendar commands (not implemented yet)
\# in order to access group features, you must be part of the group
- /calendar view {calendar} - displays specified calendar
- /calendar add {calendar} {event} {time} - adds event to specified calendar
- /calendar remove {event} - removes event from specified
- /calendar sync {calendar} - synchronises calendars (from groups and o365/moodle)

### mail commands (not implemented yet)
\# in order to access group features, you must be part of the group
- /mail create - creates a new mail (pops up as embed)
- /mail view - view mails
- /mail sync - synchronises mail (from groups and o365/moodle)
 