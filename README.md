# life-automator

This is an ongoing project of mine that started with another repository. There's alot of time we waste on mundane,
repetetive tasks that can pretty easily be automated away. My goal with this project is to eliminate as much of this
as possible, so that I can spend my time working on things that actually matter.

This is basically a flask api to help easily automate basic tasks. I've specifically built it in a way that allows it to be easily extensible with 
Siri, Apple's default personal assistant software, and Athena, an alternative I developed for myself last year.

Currently, functionality is limited. Functions are seperated into protocols, which allow for more precise vocal commands that
are less system dependent.

-Bustime Protocol: functions that estimate the number of minutes until the next bus reaches the desired stop.
-Wolf Protocol: uses the Wolfram Alpha API to calculate or get information on basically anything.
