from decouple import config
from recommender.api import Recommender

from models import Music, RecommendationScheme


class MusicRecommender:
    def __init__(self, value: RecommendationScheme):
        self.recommender = Recommender(client_id=config('client_id'), client_secret=config('client_secret'))
        self.recommender.artists = value.artist_name
        self.recommender.genres = value.genres
        self.recommender.track_attributes = value.attrs

    def __call__(self) -> list[Music]:
        recommendations = self.recommender.find_recommendations()
        result = []
        for recommendation in recommendations['tracks']:
            print(recommendation)
            result.append(Music(recommendation['name'], recommendation['external_urls']['spotify'],
                                recommendation['artists'][0]['name'], recommendation['album']['images'][0]['url']))

        return result
