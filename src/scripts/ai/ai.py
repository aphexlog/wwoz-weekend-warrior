from tkinter import X
from bs4 import BeautifulSoup
from openai import OpenAI
import re
import json
import sys
import os

client = OpenAI()

# Define a function to read the content of a file
def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
file_path = "scripts/ai/prompt.txt"
    
# Read the content of the file
file_content = read_file_content(file_path)

def process_artists(index_file):
    with open(index_file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    artists = soup.find_all(href=re.compile("/events/"))

    artistlist =[]
    for artist in artists:
        for string in artist.stripped_strings:
            if "+" in string:
                words = string.split('+')
                for word in string.split('+'):
                    artistlist.append(word.strip())
            else:
                a = repr(string)
                artistlist.append(string)

    list = json.dumps(artistlist)

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"{file_content}. Here is the list {list}"}
    ]
    )

    response = response.choices[0].message.content
    basename = os.path.basename(index_file.rsplit( ".", 1 )[ 0 ])
    # filename.rsplit( ".", 1 )[ 0 ]
    filename = f"scripts/ai/response_data/response-{basename}.json"
    with open(filename, 'w') as fd: 
        fd.write(response)

print("arg1= ", sys.argv[1])
process_artists(sys.argv[1])
