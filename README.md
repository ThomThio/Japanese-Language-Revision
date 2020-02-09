# Japanese-Language-Revision
Simple scripts to assist in revising my Japanese-English every morning, night (and commute, if an API layer is built)

Problem solved: Anki is not convenient to create cards, and input the meanings when switching in Japanese to English keyboard, whether on computers or mobile. I also want a program to run anywhere, by adding a simple API layer.

Solution: Allow convenient entry via Excel Macros, switching keyboards using Apple's input sources via a hotkey.


Usage:
Update Living Document with new Japanese words/phrases and its English meanings, vice-versa.
	Press the "New Learning" button, it is a convenience macro to add a new row (saving you a second per entry!)
<img
src="https://github.com/ThomThio/Japanese-Language-Revision/blob/master/Living%20Document%20Example.png"
raw=true
alt="Example"
/>

Run this program on Terminal/command prompt
	python3 LangRevision.py


1. Sampling with replacement so that revised words in a session do not appear again. We can save state of the last revised to give a spaced-repeition effect, but this involves having to save to a server/flat-file.
2. I can request this with an API call later on to push these to a server, serving revisions to different formats (On the go: Phone, at home: a portable android/tablet) or on a Dart/Flutter or website variant. Gunicorn does the trick.
