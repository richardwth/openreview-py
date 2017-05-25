# openreview-py
A python package for interacting with the [OpenReview](https://openreview.net) API.

## Installation
You can install openreview-py from pip:

```
pip install openreview-py
```

You can also clone this repository and install it locally:

```
pip install <cloned_directory>
```

## Getting Started
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

**Detailed API coming soon**
