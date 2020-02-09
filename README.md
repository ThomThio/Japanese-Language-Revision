# Japanese-Language-Revision
Simple scripts to assist in revising my Japanese-English every morning, night (and commute, if an API layer is built)

Usage:
Update Living Document with new Japanese words/phrases and its English meanings, vice-versa.
	Press the "New Learning" button, it is a convenience macro to add a new row (saving you a second per entry!)
![Image description]Living Document Example.png


Run this program on Terminal/command prompt
	python3 LangRevision.py


1. Sampling with replacement so that revised words in a session do not appear again. We can save state of the last revised to give a spaced-repeition effect, but this involves having to save to a server/flat-file.
2. I can request this with an API call later on to push these to a server, serving revisions to different formats (On the go: Phone, at home: a portable android/tablet) or on a Dart/Flutter or website variant. Gunicorn does the trick.
