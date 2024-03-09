"""
Module: test_tdidf_preprocess
Description:
This module contains unit tests for the preprocess_tdidf function in the tdidf_preprocess module.
"""

import unittest
import os
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from utils.tdidf_preprocess import preprocess_tdidf

class TestTdidfPreprocess(unittest.TestCase):
    """
    Unit tests for the preprocess_tdidf function.
    """

    # Smoke tests
    def test_smoke_ted(self):
        """
        Smoke test to ensure that the preprocessed file for the TED Talk dataset is created in test
        mode.
        """
        preprocess_tdidf("ted", True)
        expected_output_path = '../TLDW/tests/test_output/test_ted_tdidf_preprocessed.csv'
        self.assertTrue(os.path.exists(expected_output_path))

    def test_smoke_ted_org_embeddings(self):
        """
        Smoke test to ensure that the preprocessed file for the complete TED Talks dataset exists.
        Note: the preprocess_tdidf method is not called due to excessive time requirements.
        """
        expected_output_path = '../TLDW/data/ted_tdidf_preprocessed.csv'
        self.assertTrue(os.path.exists(expected_output_path))

    def test_smoke_podcast(self):
        """
        Smoke test to ensure that the preprocessed file for the podcast dataset is created in test
        mode.
        """
        preprocess_tdidf("podcast", True)
        expected_output_path = '../TLDW/tests/test_output/test_podcast_tdidf_preprocessed.csv'
        self.assertTrue(os.path.exists(expected_output_path))

    def test_smoke_podcast_org_embeddings(self):
        """
        Smoke test to ensure that the preprocessed file for the complete podcast dataset exists.
        Note: the preprocess_tdidf method is not called due to excessive time requirements.
        """
        expected_output_path = '../TLDW/data/podcast_tdidf_preprocessed.csv'
        self.assertTrue(os.path.exists(expected_output_path))

    # One Shot tests
    def test_oneshot_ted(self):
        """
        One shot test to ensure that the preprocessed file for the ted dataset is correct.
        This is tested by checking if the file exists, its contents, and if the tfidf_vectorizer
        object is correctly saved.
        """
        preprocess_tdidf("ted", True)
        expected_output_path = '../TLDW/tests/test_output/test_ted_tdidf_preprocessed.csv'
        expected_vectorizer_path = '../TLDW/tests/test_output/test_ted_tfidf_vectorizer.joblib'
        self.assertTrue(os.path.exists(expected_output_path))
        self.assertTrue(os.path.exists(expected_vectorizer_path))

        # Check the content of the preprocessed file
        data_df = pd.read_csv(expected_output_path)
        self.assertIsInstance(data_df, pd.DataFrame)
        self.assertEqual(data_df.shape[0], 5)  # Checking number of rows in the test mode

        # Check if tfidf_vectorizer object is correctly saved
        loaded_vectorizer = joblib.load(expected_vectorizer_path)
        self.assertIsInstance(loaded_vectorizer, TfidfVectorizer)

        # Check dimensions of TF-IDF matrix
        tfidf_matrix = loaded_vectorizer.transform(data_df['transcript'])
        self.assertEqual(tfidf_matrix.shape[0], 5)  # Expected number of documents

        # Expected number of features should be greater than 0
        self.assertGreater(tfidf_matrix.shape[1], 0)

    def test_oneshot_ted_org_embeddings(self):
        """
        One shot test to ensure that the preprocessed file for the complete ted dataset is correct.
        This is tested by checking if the file exists and its contents.
        """
        expected_output_path = '../TLDW/data/ted_tdidf_preprocessed.csv'
        self.assertTrue(os.path.exists(expected_output_path))
        expected_vectorizer_path = '../TLDW/data/ted_tfidf_vectorizer.joblib'
        self.assertTrue(os.path.exists(expected_vectorizer_path))

        # Check the content of the preprocessed file
        data_df = pd.read_csv(expected_output_path)
        self.assertIsInstance(data_df, pd.DataFrame)
        self.assertEqual(data_df.shape[0], 4005)

        # Check if tfidf_vectorizer object is correctly saved
        loaded_vectorizer = joblib.load(expected_vectorizer_path)
        self.assertIsInstance(loaded_vectorizer, TfidfVectorizer)

        # Check dimensions of TF-IDF matrix
        tfidf_matrix = loaded_vectorizer.transform(data_df['transcript'])
        self.assertEqual(tfidf_matrix.shape[0], 4005)  # Expected number of documents

        # Expected number of features should be greater than 0
        self.assertGreater(tfidf_matrix.shape[1], 0)

    def test_oneshot_podcast(self):
        """
        One shot test to ensure that the preprocessed file for the podcast dataset is correct.
        This is tested by checking if the file exists, its contents, and if the tfidf_vectorizer
        object is correctly saved.
        """
        preprocess_tdidf("podcast", True)
        expected_output_path = '../TLDW/tests/test_output/test_podcast_tdidf_preprocessed.csv'
        expected_vectorizer_path = '../TLDW/tests/test_output/test_podcast_tfidf_vectorizer.joblib'
        self.assertTrue(os.path.exists(expected_output_path))
        self.assertTrue(os.path.exists(expected_vectorizer_path))

        # Check the content of the preprocessed file
        data_df = pd.read_csv(expected_output_path)
        self.assertIsInstance(data_df, pd.DataFrame)
        self.assertEqual(data_df.shape[0], 5)  # Checking number of rows in the test mode

        # Check if tfidf_vectorizer object is correctly saved
        loaded_vectorizer = joblib.load(expected_vectorizer_path)
        self.assertIsInstance(loaded_vectorizer, TfidfVectorizer)

        # Check dimensions of TF-IDF matrix
        tfidf_matrix = loaded_vectorizer.transform(data_df['text'])
        self.assertEqual(tfidf_matrix.shape[0], 5)  # Expected number of documents

        # Expected number of features should be greater than 0
        self.assertGreater(tfidf_matrix.shape[1], 0)

    def test_oneshot_podcast_org_embeddings(self):
        """
        One shot test to ensure that preprocessed file for the complete podcast dataset is correct.
        This is tested by checking if the file exists and its contents.
        """
        expected_output_path = '../TLDW/data/podcast_tdidf_preprocessed.csv'
        self.assertTrue(os.path.exists(expected_output_path))
        expected_vectorizer_path = '../TLDW/data/podcast_tfidf_vectorizer.joblib'
        self.assertTrue(os.path.exists(expected_vectorizer_path))

        # Check the content of the preprocessed file
        data_df = pd.read_csv(expected_output_path)
        self.assertIsInstance(data_df, pd.DataFrame)
        self.assertEqual(data_df.shape[0], 906)

        # Check if tfidf_vectorizer object is correctly saved
        loaded_vectorizer = joblib.load(expected_vectorizer_path)
        self.assertIsInstance(loaded_vectorizer, TfidfVectorizer)

        # Check dimensions of TF-IDF matrix
        tfidf_matrix = loaded_vectorizer.transform(data_df['text'])
        self.assertEqual(tfidf_matrix.shape[0], 906)  # Expected number of documents

        # Expected number of features should be greater than 0
        self.assertGreater(tfidf_matrix.shape[1], 0)

    # Edge Tests
    def test_edge_ted_or_podcast1(self):
        """
        Test to ensure that ValueError is raised when an invalid value is provided for
        ted_or_podcast.
        """
        with self.assertRaises(ValueError):
            preprocess_tdidf("empty", True)

    def test_edge_ted_or_podcast2(self):
        """
        Test to ensure that TypeError is raised when ted_or_podcast is not a string.
        """
        with self.assertRaises(TypeError):
            preprocess_tdidf(8, True)

    def test_edge_ted_or_podcast3(self):
        """
        Test to ensure that TypeError is raised when ted_or_podcast is None.
        """
        with self.assertRaises(TypeError):
            preprocess_tdidf(None, True)

    def test_edge_test1(self):
        """
        Test to ensure that TypeError is raised when test is None.
        """
        with self.assertRaises(TypeError):
            preprocess_tdidf('ted', None)

    def test_edge_test2(self):
        """
        Test to ensure that TypeError is raised when test is not a boolean.
        """
        with self.assertRaises(TypeError):
            preprocess_tdidf('ted', [])

    def test_edge_test3(self):
        """
        Test to ensure that TypeError is raised when test is not a boolean.
        """
        with self.assertRaises(TypeError):
            preprocess_tdidf('ted', 'true')

if __name__ == '__main__':
    unittest.main()
