OpenReview Python library
=========================


[![CircleCI](https://circleci.com/gh/iesl/openreview-py.svg?style=svg)](https://circleci.com/gh/iesl/openreview-py)

Classes:

Client(username=None, password=None, baseurl=None)



Examples:

initialize the client and get a group
```
>>> import openreview
>>> client = openreview.Client(username='johnsmith@mail.com', password='12345', baseurl='https://openreview.net')
>>> iclr_group = client.get_group('ICLR.cc/2017/pcs')
```

get all notes submitted via a given invitation
```
>>> notes = client.get_notes(invitation='ICLR.cc/2017/conference/-/submission')
>>> first_note = notes[0]
>>> second_note = notes[1]
```

list of functions:
```
get_group(self, id):

get_invitation(self, id):

get_note(self, id):

get_groups(self, prefix=None, regex=None, member=None, host=None, signatory=None):

get_invitations(self, id=None, invitee=None, replytoNote=None, replyForum=None, signature=None, note=None):

get_notes(self, id=None, forum=None, invitation=None, replyto=None, tauthor=None, signature=None, writer=None, includeTrash=None, number=None):

post_group(self, group, overwrite=True):

post_invitation(self, invitation):

post_note(self, note):

send_mail(self, subject, recipients, message):

add_members_to_group(self, group, members):

remove_members_from_group(self, group, members):
```

[Link](http://openreview-py.readthedocs.io/en/latest/) to full Documentation


Run tests
----------

To run the tests of the library you need to have the OpenReview backend running in your localhost.

Checkout the code and run

```bash
NODE_ENV=test node scripts/clean_start_app.js
```
