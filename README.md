# AR Research Tool
A Python tool for tracking emerging artists and comparing their growth on YouTube.

## What it does
Program takes a list of artists and analyses their YouTube performance (views and subscribers). It then filters out "non-emerging" artists (artists with more than 500,000 subscribers). The collected data is turned into a .csv (spreadsheet) file. When the program is run twice or more, it will produce a new .csv file with updated analytics, and also a growth calculator based on the previous report, so you can see how each artist is performing on YouTube over time.

## Why I built it
From my experience working in A&R and the broader music industry, I found myself having to manually track artist performance across platforms. This program was built to help automate that research and flag artists that are early in their careers and worth paying attention to.

## How it works
This program will locate the YouTube channels of artists based on the names given in the artists.txt file. It will retrieve their channel name, subscriber count and total view count. If the channel has over 500k subscribers, the artist gets filtered out as "non-emerging", and is not included in the final report. It then puts the name, views and subscriber count into a readable .csv file. When run additional times with the same artists.txt file, it will also generate a growth percentage based on their current numbers compared to the last snapshot saved. This growth metric will be reported in the "current" .csv.

## Tech Stack
Python: the language used to write all files in this program
YouTube Data API v3: used to retrieve the artists' channel data for analysis
pandas: used for analysis, calculations and comparisons of channels and artists
Google API Python Client: library for Python to use and communicate with Google's APIs
python-dotenv: loads the .env files to keep API credentials secure and out of the code

## How to run it
### Step 1: Clone the repo
```bash
git clone https://github.com/agw03/ar-research-tool.git
cd ar-research-tool/ar-research-tool 
```
### Step 2: Create and activate a virtual environment
```bash
python3.11 -m venv venv
source venv/bin/activate
```
### Step 3: Install dependencies
```bash
pip3 install -r requirements.txt
```
### Step 4: Add API credentials
Create a .env file in the root folder using:
```
YOUTUBE_API_KEY=your_key_here
```
You need to enable the YouTube API v3 in Google Cloud Console, then you can get the key from console.cloud.google.com
### Step 5: Add artists
Add the names of the artist(s) you want to track to data/artists.txt, one per line.
### Step 6: Run program
```bash
python3 -m src.main
```



## Sample output
The emerging report only shows artists under 500k subscribers. The growth report tracks all artists in artists.txt.
```
Name: Arlo Parks | Subscribers: 105000 | Views: 44674860 | Emerging: True
Name: Hotel Mira | Subscribers: 14500 | Views: 3787528 | Emerging: True
Name: Chase Petra | Subscribers: 13500 | Views: 4855331 | Emerging: True
Name: All Time Low | Subscribers: 22400 | Views: 358603320 | Emerging: True

--- Growth Report ---
Arlo Parks: +10.5%
Hotel Mira: +45.0%
Chase Petra: +28.6%
All Time Low: +15.5%
```
