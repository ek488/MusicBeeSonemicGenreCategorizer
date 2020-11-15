from html.parser import HTMLParser
import io


class SonemicGenreHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        # TODO: If unclosedDivTags > 0, sectionSubgenres == True, else False
        self.sectionSubgenres = False
        self.subgenreListLevel = -1
        self.subgenreListItem = False
        self.subgenreLink = False
        self.unclosedDivTags = 0
        self.genres = []

    def handle_starttag(self, tag, attrs):
        # If this is not already the subgenre section, then check whether this
        # is the subgenre section.
        if self.sectionSubgenres == False and tag == "div":
            for name, value in attrs:
                if name == "class" and value == "page_object_section page_object_section_subgenres":
                    self.sectionSubgenres = True
                    self.unclosedDivTags += 1
        elif tag == "ul":
            for name, value in attrs:
                if name == "class" and value == "subgenre_list":
                    self.subgenreListLevel += 1
        elif tag == "div":
            for name, value in attrs:
                if name == "class" and value == "subgenre_list_item ":
                    self.subgenreListItem = True
                    self.unclosedDivTags += 1
                elif self.subgenreListItem == True:
                    self.unclosedDivTags += 1
        elif tag == "a":
            if self.subgenreListItem == True:
                self.subgenreLink = True

    def handle_endtag(self, tag):
        if self.sectionSubgenres == True:
            if tag == "ul":
                self.subgenreListLevel -= 1
            if self.subgenreListItem == True and tag == "div":
                self.unclosedDivTags -= 1
                if self.unclosedDivTags == 1:
                    self.subgenreListItem = False
                if self.unclosedDivTags == 0:
                    self.sectionSubgenres = False
            if self.subgenreLink == True and tag == "a":
                self.subgenreLink = False

    def handle_data(self, data):
        if self.subgenreLink == True:
            self.genres.append(data)


def generate_rym_html_name(genre):
    if genre == "Singer/Songwriter":
        return "Singer_Songwriter - Sonemic _ Rate Your Music music database.html"
    return genre + " - Sonemic _ Rate Your Music music database.html"


# TODO: musicbee_genre category and output are the same thing
def musicbee_genre_categorize(output, genre_category):
    parser = SonemicGenreHTMLParser()
    file_path = "html\\" + generate_rym_html_name(genre_category)
    f = open(file_path, "r", encoding="utf8")
    parser.feed(f.read())

    musicbee_genre_category = output
    musicbee_genre_category.append(
        {"genre": genre_category, "genre_category": [genre_category]})

    for genre in parser.genres:
        newGenre = True
        for dic in musicbee_genre_category:
            if dic["genre"] == genre:
                if not genre_category in dic["genre_category"]:
                    dic["genre_category"].append(genre_category)
                newGenre = False
        if newGenre == True:
            musicbee_genre_category.append(
                {"genre": genre, "genre_category": [genre_category]})

    f.close()
    return musicbee_genre_category


# "Descriptor" and "Regional Music" are not included.
genre_categories = {"Ambient", "Blues", "Classical Music", "Comedy", "Dance",
                    "Darkwave", "Electronic", "Experimental", "Folk",
                    "Hip Hop", "Industrial Music", "Jazz",
                    "Musical Theatre and Entertainment", "New Age", "Pop",
                    "Psychedelia", "Punk", "R&B", "Rock", "Singer/Songwriter",
                    "Ska", "Sounds and Effects", "Spoken Word"}

output = list()


for genre_category in genre_categories:
    output = musicbee_genre_categorize(output, genre_category)


outputString = ""

for dic in output:
    words = dic["genre"].split(" ")
    for i in range(len(words)):
        if words[i].lower() == words[i] and words[i] != "and":
            words[i] = words[i].title()

    genre = ""
    # Un-split the genre name.
    for word in words:
        genre += word + " "

    if genre == "Classical Marches ":
        genre = "Classical March "
    elif genre == "J-pop ":
        genre = "J-Pop "
    elif genre == "K-pop ":
        genre = "K-Pop "
    elif genre == "Lo-Fi Indie ":
        genre = "Lo-Fi / Slacker Rock "
    elif genre == "Trap ":
        genre = "Trap [EDM] "
    elif genre == "Trap Rap ":
        genre = "Trap "

    outputString += genre + ": "
    isFirst = True
    dic["genre_category"].sort()
    for genre_category in dic["genre_category"]:
        if not isFirst:
            outputString += " & "
        else:
            isFirst = False
        outputString += genre_category
    outputString += '\n'


# Add some genres that are in the RateYourMusic database, but not the Sonemic
# database.
outputString += "Cinematic Classical : Classical Music\nDarksynth : Electronic\nDeconstructed Club : Dance & Electronic & Industrial Music\nFuture Bass : Dance & Electronic\nSpaghetti Western : Classical Music\n"


# Write to file.
with io.open("MusicBee Genre Categorisation Editor Input.txt", 'w', encoding="utf-8") as file:
    file.write(outputString)
