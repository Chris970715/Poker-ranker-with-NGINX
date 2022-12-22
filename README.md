# Poker-ranker-with-NGINX
A website tells users poker hands that you have randomly picked


ASSIGNMENT SPECIFICATIONS:
For this assignment in PRG550 this semester, you will use your Raspberry Pi
running Python 3.10.5 and the NGINX web server 1.22.1 and create an HTML form (client)
and a Python CGI (server) program that allows users to select 5 cards (from a deck of
52 cards) representing a "Poker" hand and determines whether the category of poker
that poker hands ranked in order from lowest to highest:
High card, 1 pair, 2 pair, 3 of a kind, straight, flush, full house,
4 of a kind, and straight flush (see below for category codes).
Please refer to this wikipedia page for a complete description and
explanation of poker hands:

http://en.wikipedia.org/wiki/Poker_hands

Here are the 52 (strings) your program MUST use to represent all 52 cards in the deck:

"2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "th", "jh", "qh", "kh", "ah"
"2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "tc", "jc", "qc", "kc", "ac"
"2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "ts", "js", "qs", "ks", "as"
"2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "td", "jd", "qd", "kd", "ad"

This card deck MUST be stored in a Python dictionary with the cards as values
and an index of 0 to 51 as the keys!

Your html form MUST allow the user to select EXACTLY 5 UNIQUE cards from ALL 52 cards in the deck
as a checkbox input type with card images displayed in place of the text (see below).
The images used in the sample below (as well as all images for all the other cards) can be
downloaded here: cards.zip


 ... 
 ... 


If the user does not select exactly 5 cards, then your server program will send back
an HTML reponse back to the client informing the user that they have made an error and
instructs the user to hit the "BACK" button and select again!

Once 5 cards have been selected, your program MUST determine what poker hand the 5 cards
represent and send back an HTML response consisting of the 5 cards (as images) selected
by the user (sorted in rank order from low to high) and a message indicating the hand category
(i.e. High card, 1 pair, 2 pair, 3 of a kind, etc).
In addition, the following function MUST be called and displayed as HTML output:

OUTPUT

    
Your Poker Hand represents a THREE OF A KIND!

Thu 17 Nov 2022 01:57:32 PM EST

19531 ?        Ss     0:00 nginx: master process /usr/local/nginx/nginx
19532 ?        S      0:00 nginx: worker process
29501 pts/0    S+     0:00 grep nginx

Linux piCM4devSSD 5.15.61-v8+ #1579 SMP PREEMPT Fri Aug 26 11:16:44 BST 2022 aarch64 GNU/Linux
