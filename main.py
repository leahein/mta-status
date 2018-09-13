from google.transit import gtfs_realtime_pb2
import requests

from secure import MTA_KEY

def main():
    '''run main MTA feed'''

    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get(
        f'http://datamine.mta.info/mta_esi.php'
        f'?key={MTA_KEY}'
    )
    feed.ParseFromString(response.content)
    while True:
        for entity in feed.entity:
            print(entity)


if __name__ == '__main__':
    main()
