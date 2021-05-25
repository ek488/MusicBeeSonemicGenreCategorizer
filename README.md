Intended for those using MusicBee with tracks tagged with RateYourMusic genres.

RYM has hundreds of genres in its database, so it can be difficult to categorize them. By doing the steps below, you can easily categorize most of them in MusicBee!

# Genre categories

Label most genres with their parent genre.

> Alternative Rock: Rock

> Art Pop: Pop

> East Coast Hip Hop: Hip Hop

> Neo-Psychedelia: Psychedelia

> Trip Hop: Electronic

> Volkstümliche Musik: Pop

## How to (copy and paste)

1. Open "MusicBee Genre Categorisation Editor Input.txt".
2. Select all text, then copy it (ctrl + A, then ctrl + C.)
3. Open MusicBee.
4. Edit -> Edit Preferences -> Tags (2) -> group genres: Categorise....
5. Paste in the Genre Categorisation Editor.
6. Click save, then click save again.

# Virtual genre categories

Some genres belong to multiple different genre categories.

> Deconstructed Club : Dance & Electronic & Industrial Music

> Pop Rock: Pop & Rock

Unfortunately, we cannot assign a genre to more than one genre category in MusicBee. But by using a virtual tag, we can assign, for example, "Pop Rock" to separate "Pop" and "Rock" categories.

## How to (still copy and paste)

1. Open "Virtual Tag - Virtual Genre Category.txt".
2. Select all text, then copy it.
3. Open MusicBee.
4. Edit -> Edit Preferences -> Tags (1) -> group genres: Define New Tags....
5. Paste in the empty box right of "Virtual 1" and under "formula:".
6. Click save, then click save again.

# Other Genre Categories

MusicBee has a maximum limit on number of genres you can categorize, so I excluded the genre categories "Descriptors" and "Regional Music". You can edit the python file and add "Descriptors" and/or "Regional Music" in the set on line 90, then run it. It'll output a new "MusicBee Genre Categorisation Editor Input.txt" that has those genre categories too.
