def recite(start_verse, end_verse):
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

    for i in range(start_verse-1, end_verse):
        if i == 0:
            music.append(f"On the {day[i]} day of Christmas my true love gave to me: a Partridge in a Pear Tree.")
            continue
        
        day_verse = f"On the {day[i]} day of Christmas my true love gave to me: "
        gift_verse = "".join(gift[:i+1][::-1])
        full_verse = day_verse + gift_verse
        music.append(full_verse)

    return music

print(recite(1, 2))