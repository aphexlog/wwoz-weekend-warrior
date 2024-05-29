
# WWOZ Weekend Warrior

A Spotify playlist generator featuring music from upcoming shows in New Orleans. Drawing from WWOZ's music calendar, the playlist is updated every Monday to showcase artists performing in the city over the upcoming weekend. 



## How it works

Every Monday a python script takes the html code from the upcoming weekend days, parses out the artists, feeds that list to ChatGPT for processing and then updates the WWOZ Weekend Warrior playlist on spotify with 2 of the most popular tracks from each artist on the list, that is if the artist was found on Spotify. 
## Run Locally

Clone the project

```bash
  git clone https://github.com/joesolito/wwoz-weekend-warrior/tree/main
```

Go to the project directory

```bash
  cd wwoz-weekend-warrior/src
```

Install dependencies

```bash
  npm install
```

Run setup, providing api credentials

```bash
  python setup.py
```

Run `run.py` script
```bash
  python run.py
```
## Acknowledgements

 - [WWOZ Livewire Music](https://www.wwoz.org/calendar/livewire-music)
  - [Spotify Web Api](https://developer.spotify.com/documentation/web-api)
   - [ChatGpt API](https://platform.openai.com/docs/api-reference)


