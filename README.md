NAME
====

Mailer - A command line tool for sending mail via Outlook

USAGE
=====

Mailer can be used from the command line like so:

    python mail --to=receiver@example.com --subject="This is a test" --body="this is a message"

CONFIGURATION
=============

Mailer configuration is simple, it exists in a file called `.mailrc` in your
home directory and is formatted in the YAML format.  Here is an example file:

    # C:\Users\Peter\.mailrc
    username: Peter
    password: Peter'sPassword

To use Mailer you'll need to set it's `username` and `password` fields to your
username and password, and that's it.

KNOWN ISSUES
============

At the moment Mailer is being used in Ant build scripts to send automated emails
from my Outlook account.  One issue we have is that Ant scripts won't allow me
to embed XML/HTML syntax in an attribute (I think it violates XML validation).
So I'd like to extend Mailer to support some sort of markup (or encoding) for
formatting the body particularly for new lines.

AUTHOR
======

If you have any questions feel free to contact me.

Delon Newman
Email: delon.newman@gmail.com
Phone: 808-561-3617
