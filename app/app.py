import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommendation System", layout="wide")

load_dotenv()

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("Anime Recommendation System")
query = st.text_input("Enter anime description or title for recommendations eg: light hearted anime with school settings")
if query:
    with st.spinner("Generating recommendations for you..."):
        response = pipeline.recommend(query)
        st.markdown("### Recommended Animes: ")
        st.write(response)
        