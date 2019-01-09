import requests


BASE_URL = "https://www.googleapis.com/youtube/v3"


def get_dislikes(api_key, video_id):
    url = f"{BASE_URL}/videos"

    payload = {
        "key": api_key,
        "part": ["statistics"],
        "id": video_id,
    }

    response = requests.get(url, params=payload)
    return int(response.json()["items"][0]["statistics"]["dislikeCount"])
