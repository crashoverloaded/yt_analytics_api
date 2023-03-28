import sys
from src.exception import CustomException
from src.logger import lg
import requests
import googleapiclient.discovery
from dataclasses import dataclass

@dataclass
class DataCollectionConfig:
    #data_path: str=os.path.join('artifacts',"data.csv")
    developer_key: str=open('src/components/conf.py', 'r').readlines()[0].rstrip().split("=")[1]
    api_service_name:  str= "youtube"
    api_version: str= "v3"
class DataCollection:
    def __init__(self):
        self.collection_config = DataCollectionConfig()

    def initiate_data_collection(self):
        lg.info("Entered the Data collection method/component")
        try:
            DEVELOPER_KEY = self.collection_config.developer_key
            #os.makedirs(os.path.dirname(self.collection_config.data_path),exist_ok=True)
            # GET Request for Channel ID through username
            channel = requests.get("https://www.googleapis.com/youtube/v3/channels?part=snippet,contentDetails,statistics&forUsername={id}&key={api}".format(api=DEVELOPER_KEY, id='krishnaik06'))
            # Getting details of channel(stats) and "uploads" playlist ID
            upload_playlist_ID = channel.json()['items'][0]['contentDetails']['relatedPlaylists']['uploads']
            channel_statistics = channel.json()['items'][0]['statistics']
            lg.info("Fetched 'Upload' playlist ID")
            # Building client
            youtube = googleapiclient.discovery.build(self.collection_config.api_service_name, self.collection_config.api_version, developerKey=DEVELOPER_KEY)
            lg.info("Initiating Youtube Client")
            # Fetching latest 50 videos ID
            videos = youtube.playlistItems().list(playlistId=upload_playlist_ID, part='snippet',maxResults=50).execute()
            lg.info("Fetched VideoID of latest 50 videos")
            # creating a GET Link
            baselink = "https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics"
            for video in videos['items']:
                # videoID for each video
                video_id = video['snippet']['resourceId']['videoId']
                finalsentence = baselink + "&id=" + str(video_id)
                baselink = finalsentence

            # this is final GET link
            final_get_link = finalsentence + "&key=" + DEVELOPER_KEY

            # Fetching results (videos stats , likes  , num of comments , etc.)
            all_stats = requests.get(final_get_link).json()

            return (
                channel_statistics,all_stats
            )
            """
            for item in all_stats['items']:
                print(item['statistics'])
                print(item['snippet']['publishedAt'])
                print(item['snippet']['title'])
                print(item['snippet']['thumbnails']['default']['url'])
            print(channel_statistics)
            """
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj = DataCollection()
    print(obj.initiate_data_collection())