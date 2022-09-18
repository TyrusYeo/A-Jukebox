import lyricsgenius as lg

file = open(r"C:\Users\Tyrus Yeo\Desktop\Coding\Lyric generator\lyrics.txt", "w")

genius = lg.Genius('-lgbBbLxKVAdN311MF18o5fyAUZbKi0O2C6xeXbdehUvGMc8ET6nmVkUD3XJpxpw',
                   skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)


def getLyrics(arr, m):
    c = 0
    for name in arr:
        try:
            songs = (genius.search_artist(
                name, max_songs=m, sort='popularity')).songs
            s = [song.lyrics for song in songs]
            file.write("\n \n   <|endoftext|>   \n \n".join(s))
            c += 1
            print(f"Songs grabbed:{len(s)}")
        except:
            print(f"Some exception at {name}: {c}")


artistName = input('What artist do you listen to?')

artists = [artistName]

songNo = input("How many songs do you want to hear?")

getLyrics(artists, 1)
