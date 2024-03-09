# """
# This fule contains unit tests for the functionality provided
# by the bert_get_recommendations module. It includes tests to ensure
# the correctness and robustness of the get_bert_recs function.
# """

# import unittest
# import os
# from utils.bert_get_recommendations import get_bert_recs

# class TestBertGetRecommendations(unittest.TestCase):
#     """
#     TestBertGetRecommendations class contains unit tests for the
#     bert_get_recommendations module.
#     """

#     user_transcript = "This is a test transcript."

#     with open('tests/user_transcript1.txt', 'r') as file:
#         user_transcript1 = file.read()

#     def test_smoke_file_exists_ted(self):
#         """
#         Test if the required embedding file for TED Talks exists.
#         """
#         file_path = './ted_sbert_embeddings.pt'
#         self.assertTrue(os.path.exists(file_path), f"The file {file_path} does not exist.")

#     def test_smoke_data_exists_ted(self):
#         """
#         Test if the required data file for TED Talks exists.
#         """
#         file_path = './ted_talks_en.csv'
#         self.assertTrue(os.path.exists(file_path), f"The file {file_path} does not exist.")

#     def test_smoke_file_exists_podcast(self):
#         """
#         Test if the required embedding file for podcast exists.
#         """
#         file_path = './podcast_sbert_embeddings.pt'
#         self.assertTrue(os.path.exists(file_path), f"The file {file_path} does not exist.")

#     def test_smoke_data_exists_podcast(self):
#         """
#         Test if the required data file for podcast exists.
#         """
#         file_path = './skeptoid_transcripts.csv'
#         self.assertTrue(os.path.exists(file_path), f"The file {file_path} does not exist.")

#     def test_smoke_ted(self):
#         """
#         Test the functionality of get_bert_recs for TED Talks.
#         """
#         ted_or_podcast = "ted"
#         recommendations = get_bert_recs(self.user_transcript, ted_or_podcast)
#         print("Smoke test - ted: passed.")
#         self.assertFalse(recommendations.empty)

#     def test_smoke_podcast(self):
#         """
#         Test the functionality of get_bert_recs for Podcasts.
#         """
#         ted_or_podcast = "podcast"
#         recommendations = get_bert_recs(self.user_transcript, ted_or_podcast)
#         print("Smoke test - podcast: passed.")
#         self.assertFalse(recommendations.empty)

#     def test_one_shot_ted(self):
#         """
#         Test the functionality of get_bert_recs for ted talks, given a specific transcript.
#         """
#         ted_or_podcast = "ted"
#         recommendations = get_bert_recs(self.user_transcript1, ted_or_podcast)
#         print("One-shot test - ted: passed.")
#         self.assertTrue(recommendations.iloc[0]['title'] == "Averting the climate crisis")

#     def test_one_shot_podcast(self):
#         """
#         Test the functionality of get_bert_recs for podcasts, given a specific transcript.
#         """
#         ted_or_podcast = "podcast"
#         recommendations = get_bert_recs(self.user_transcript1, ted_or_podcast)
#         print("One-shot test - podcast: passed.")
#         self.assertTrue(recommendations.iloc[0]['title'] == "Email Myths")

#     # Edge Tests
#     def test_edge_value_error_arg1(self):
#         """
#         Test handling of ValueError when user_transcript is empty.
#         """
#         with self.assertRaises(ValueError):
#             get_bert_recs("", "ted")

#     def test_edge_type_error_arg1(self):
#         """
#         Test handling of TypeError when user_transcript is not a string.
#         """
#         with self.assertRaises(TypeError):
#             get_bert_recs(1, "ted")

#     def test_edge_value_error_arg2(self):
#         """
#         Test handling of ValueError when ted_or_podcast is invalid.
#         """
#         with self.assertRaises(ValueError):
#             get_bert_recs("Correct", "empty")

#     def test_edge_type_error_arg2(self):
#         """
#         Test handling of TypeError when ted_or_podcast is not a string.
#         """
#         with self.assertRaises(TypeError):
#             get_bert_recs("Correct", 8)

# if __name__ == '__main__':
#     unittest.main()
