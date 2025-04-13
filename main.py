from trends.fetch_trends import get_trending_topics
from script_gen.generate_script import create_script
from video_gen.make_video import text_to_voice, generate_video
from seo.seo_optimizer import generate_seo
from uploader.youtube_upload import upload_video

def run_full_pipeline():
    topic = get_trending_topics()[0]['query']
    script = create_script(topic)
    text_to_voice(script, "voice.mp3")
    generate_video("voice.mp3", "output.mp4")
    seo_data = generate_seo(topic)
    upload_video("output.mp4", seo_data['title'], seo_data['desc'], seo_data['tags'])

if __name__ == "__main__":
    run_full_pipeline()
from trends.fetch_trends import get_trending_topics
from script_gen.generate_script import create_script
from video_gen.make_video import text_to_voice, generate_video
from seo.seo_optimizer import generate_seo
from uploader.youtube_upload import upload_video
import logging

def run_full_pipeline():
    try:
        topic = get_trending_topics()[0]['query']
        script = create_script(topic)
        text_to_voice(script, "voice.mp3")
        generate_video("voice.mp3", "output.mp4")
        seo_data = generate_seo(topic)
        upload_video("output.mp4", seo_data['title'], seo_data['desc'], seo_data['tags'])
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run_full_pipeline()