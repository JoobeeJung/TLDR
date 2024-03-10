"""
Module: test_tdidf_get_recommendations
Description:
This module contains unit tests for the functionality provided by the get_tdidf_recs function
in the tdidf_get_recommendations module.
"""

import unittest
import os
from utils.tdidf_get_recommendations import get_tdidf_recs

class TestTdidfGetRecommendations(unittest.TestCase):
    """
    TestTdidfGetRecommendations class contains unit tests for the tdidf_get_recommendations module.
    """

    user_transcript = "This is a test transcript."

    with open('tests/user_transcript1.txt', 'r') as file:
        user_transcript1 = file.read()

    def test_smoke_embeddings_exists_ted(self):
        """
        Test if the required embedding file for TED Talks exists.
        """
        expected_output_path = '../TLDW/data/ted_tdidf_preprocessed.csv'
        self.assertTrue(os.path.exists(expected_output_path))

    def test_smoke_vectorizer_exists_ted(self):
        """
        Test if the required data file for TED Talks exists.
        """
        expected_datafile_path = "../TLDW/data/ted_tfidf_vectorizer.joblib"
        self.assertTrue(os.path.exists(expected_datafile_path))

    def test_smoke_embeddings_exists_podcast(self):
        """
        Test if the required embedding file for podcast exists.
        """
        expected_output_path = '../TLDW/data/podcast_tdidf_preprocessed.csv'
        self.assertTrue(os.path.exists(expected_output_path))

    def test_smoke_vectorizer_exists_podcast(self):
        """
        Test if the required data file for TED Talks exists.
        """
        expected_datafile_path = "../TLDW/data/podcast_tfidf_vectorizer.joblib"
        self.assertTrue(os.path.exists(expected_datafile_path))

    def test_smoke_ted(self):
        """
        Test the functionality of get_tdidf_recs for TED Talks.
        """
        ted_or_podcast = "ted"
        recommendations = get_tdidf_recs(self.user_transcript, ted_or_podcast)
        print("Smoke test - ted: passed.")
        self.assertFalse(recommendations.empty)

    def test_smoke_podcast(self):
        """
        Test the functionality of get_tdidf_recs for Podcasts.
        """
        ted_or_podcast = "podcast"
        recommendations = get_tdidf_recs(self.user_transcript, ted_or_podcast)
        print("Smoke test - podcast: passed.")
        self.assertFalse(recommendations.empty)

    def test_one_shot_ted(self):
        """
        Test the functionality of get_tdidf_recs for TED Talks, given a specific transcript.
        """
        ted_or_podcast = "ted"
        recommendations = get_tdidf_recs(self.user_transcript1, ted_or_podcast)
        print("One-shot test - ted: passed.")
        self.assertTrue(recommendations.iloc[0]['title'] == "Averting the climate crisis")

    def test_one_shot_podcast(self):
        """
        Test the functionality of get_tdidf_recs for Podcasts, given a specific transcript.
        """
        ted_or_podcast = "podcast"
        recommendations = get_tdidf_recs(self.user_transcript1, ted_or_podcast)
        print("One-shot test - podcast: passed.")
        self.assertTrue(
            recommendations.iloc[0]['title'] == "What THEY Don't Want You to Know About UFOs")

    # Edge Tests
    def test_edge_user_transcript1(self):
        """
        Test handling of ValueError when user_transcript is empty.
        """
        with self.assertRaises(ValueError):
            get_tdidf_recs("", "ted")

    def test_edge_user_transcript(self):
        """
        Test handling of TypeError when user_transcript is not a string.
        """
        with self.assertRaises(TypeError):
            get_tdidf_recs(1, "ted")

    def test_edge_ted_or_podcast1(self):
        """
        Test to ensure that ValueError is raised when an invalid value is provided for
        ted_or_podcast.
        """
        with self.assertRaises(ValueError):
            get_tdidf_recs(self.user_transcript, "empty")

    def test_edge_ted_or_podcast2(self):
        """
        Test to ensure that TypeError is raised when ted_or_podcast is not a string.
        """
        with self.assertRaises(TypeError):
            get_tdidf_recs(self.user_transcript, 8)

    def test_edge_ted_or_podcast3(self):
        """
        Test to ensure that TypeError is raised when ted_or_podcast is None.
        """
        with self.assertRaises(TypeError):
            get_tdidf_recs(self.user_transcript, None)

if __name__ == '__main__':
    unittest.main()
