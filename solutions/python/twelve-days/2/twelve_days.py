"""This modulo solved the Twelve Days exercism"""
def recite(start_verse, end_verse):
    """This fuction recite especifide verses of the Song: The Twelve Days of Christmas."""
    day = (
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth",
    )
    
    gift = (
        "and a Partridge in a Pear Tree.",
        "two Turtle Doves, ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ",
        "twelve Drummers Drumming, "
    )

    music = []

    for counter in range(start_verse-1, end_verse):
        if counter == 0:
            music.append(f"On the {day[counter]} day of Christmas my true love gave to me: a Partridge in a Pear Tree.")
            continue
        
        day_verse = f"On the {day[counter]} day of Christmas my true love gave to me: "
        gift_verse = "".join(gift[:counter+1][::-1])
        full_verse = day_verse + gift_verse
        music.append(full_verse)

    return music

print(recite(1, 2))