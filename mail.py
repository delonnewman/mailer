#!python
import os
import sys
import yaml
import win32com.client
from optparse import OptionParser

class Message:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def send(self, to, subject, body):
        app = win32com.client.gencache.EnsureDispatch("Outlook.Application")
        ns  = app.GetNamespace("MAPI")
        ns.Logon(self.username, self.password, False, False)

        ol = win32com.client.constants
        outbox = ns.GetDefaultFolder(ol.olFolderDrafts)

        memo = app.CreateItem(ol.olMailItem)
        memo.To = to
        memo.Subject = subject
        memo.HTMLBody = body
        memo.SaveSentMessageFolder = outbox
        memo.Send()

def parse_opts():
    parser = OptionParser()
    parser.add_option("-t", "--to",      dest="to",      help="specify recipient of message", metavar="TO")
    parser.add_option("-s", "--subject", dest="subject", help="specify subject of message",   metavar="SUBJECT")
    parser.add_option("-b", "--body",    dest="body",    help="specify body of message",      metavar="BODY")

    (opts, args) = parser.parse_args()
    return opts

def get_config(path):
    if not os.path.exists(path):
        f = open(path, 'w')
        f.write('')
        f.close()
    
    f = open(path, 'r')
    return yaml.load(f.read()) or {}


if __name__ == '__main__':

    opts    = parse_opts()
    homedir = os.environ['HOMEDRIVE'] + os.environ['HOMEPATH']
    config  = get_config(homedir + '/.mailrc')

    user, password = None, None
    if config.has_key('username') and config.has_key('password'):
        user, password = config['username'], config['password']
    else:
        user = raw_input("Username: ")
        password = raw_input("Password: ")
        

    try:
        if opts.to and opts.subject and opts.body:
            Message(user, password).send(opts.to, opts.subject, opts.body)
            print "message sent."
            sys.exit(0)
        else:
            print "USAGE: mail --to=RECIPIENT --subject=SUBJECT --body=BODY"
            sys.exit(1)
    except Exception, e:
        print e
        sys.exit(1)
