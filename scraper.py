import requests 
import lxml.html as html
import os



HOME_URL = input("Playlist url: ")
XPATH_PLAYLIST_NAME = '//div[@class="media-bd"]/h1/span[@dir="auto"]/text()'
XPATH_SONG_LIST = '//span[@class="track-name"]/text()'

def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            songList = parsed.xpath(XPATH_SONG_LIST)
            playlistName = parsed.xpath(XPATH_PLAYLIST_NAME)
            #print(songList)
            #print(playlistName)

            #if not os.path.isfile('{playlistName[0]}.txt'):
             #   os.('{playlistName[0]}.txt')
            
            with open(f'{playlistName[0]}.txt', 'w', encoding='utf-8') as f:
                f.write(playlistName[0])
                f.write('\n\n')
                trackCount = 1
                for song in songList:
                    f.write(f'{trackCount}.- {song}')
                    f.write('\n')
                    trackCount += 1
        
        else:
            raise ValueError(f'Error: {response.status_code}')


    except ValueError as ve:
        print(ve)


def run():
    parse_home()

if __name__ == "__main__":
    run()