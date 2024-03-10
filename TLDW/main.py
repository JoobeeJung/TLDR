from utils.process_transcripts import get_transcript
from utils.summarize_transcripts import get_ai_extract 
from utils.bert_preprocess import preprocess_bert
from utils.bert_get_recommendations import get_bert_recs
from utils.minilm_preprocess import preprocess_minilm
from utils.minilm_get_recommedations import get_minilm_recs
from utils.tdidf_preprocess import preprocess_tdidf
from utils.tdidf_get_recommendations import get_tdidf_recs

def main():
    video_url = input("Please enter the YouTube video URL: ")
    transcript = get_transcript(video_url)
    #print(transcript)
    #summary = get_ai_extract("Summarize this transcript within 250 words, output a paragraph: ", transcript)
    # keywords = get_ai_extract("Generate the top 10 most important keywords: ", transcript)
    #print("This is the summary of the transcript:")
    #print(summary)
    # print("----------------------------------------------------------------")
    # print("These are the top 10 keywords:")
    # print(keywords)

    # Roberta
    # preprocess_bert("ted", False)
    # get_bert_recs(transcript, "ted")
    # preprocess_bert("podcast", False)
    # get_bert_recs(transcript, "podcast")

    # # Sentence-transformer -> all-MiniLM-L6-v2
    # preprocess_minilm("ted", False)
    # get_minilm_recs(transcript, "ted")
    # preprocess_minilm("podcast", False)
    # get_minilm_recs(transcript, "podcast")

    # # tdidf
    # preprocess_tdidf("ted", False)
    # get_tdidf_recs(transcript, "ted")
    # # preprocess_tdidf("podcast", False)
    # get_tdidf_recs(transcript, "podcast")

if __name__ == '__main__':
    main()