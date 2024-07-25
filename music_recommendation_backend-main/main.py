import uvicorn
from fastapi import FastAPI, Request

from models import RecommendationScheme, Music
from music_recommender import MusicRecommender

app = FastAPI()


@app.post('/recommend')
async def recommend(value: RecommendationScheme):
    recommender = MusicRecommender(value)
    recommendations: list[Music] = recommender()
    return {"recommendations": recommendations}


@app.get('/')
async def main(request: Request):
    return {"status": True}


if __name__ == "__main__":
    uvicorn.run(app)
