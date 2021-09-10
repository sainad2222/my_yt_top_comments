# Usage

1. Clone this repository
2. Go to [takeout](https://takeout.google.com/settings/takeout) and download
   youtube takeout
3. Copy "my-comments.html" from extracted takeout folder to current directory
4. Install dependencies
   `pip install -r requirements.txt`
5. Generate Youtube Data API v3 key and replace it with 'API_KEY' from [Google Cloud Console](https://console.cloud.google.com/)
6. Run main.py
   `python main.py`

# Features

- Progress bar support

![prog_bar](https://user-images.githubusercontent.com/44405294/132900384-93a06ad3-68b0-47ad-a287-945b45e0b227.png)

- outputs results to a html file(blurred unrelevant parts)

![screenshot](https://user-images.githubusercontent.com/44405294/132900530-7fdf00d7-bf43-4e90-ac6b-5a2d5180e165.png)

