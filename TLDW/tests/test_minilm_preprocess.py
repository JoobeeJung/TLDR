"""
Module: test_minilm_preprocess
Description:
This module contains unit tests for the preprocess_minilm function in the minilm_preprocess module.
"""

import unittest
import os
import pickle
import numpy as np
from utils.minilm_preprocess import preprocess_minilm

class TestMiniLMPreprocess(unittest.TestCase):
    """
    Unit tests for the preprocess_minilm function.
    Note: We set test to True in the preprocess_minilm function so that we don't end up creating
    embeddings for the complete dataset, since it takes very long. With setting test to True, we
    take a small subset of the original dataset and ensure that the preprocess_minilm function works
    properly on it, which in turn ensures that the preprocess_minilm function works properly on the
    complete dataset.
    """

    # Smoke tests
    def test_smoke_ted(self):
        """
        Smoke test to ensure that the embedding file for the TED Talk dataset is created in test
        mode.
        """
        preprocess_minilm("ted", True)
        expected_output_path = '../TLDW/tests/test_output/test_ted_sentTrans_embeddings.pkl'
        self.assertTrue(os.path.exists(expected_output_path))

    def test_smoke_ted_org_embeddings(self):
        """
        Smoke test to ensure that embedding file for the complete TED Talks dataset exists.
        Note: the preprocess_minilm method is not called due to excessive time requirements.
        """
        expected_output_path = '../TLDW/data/ted_sentTrans_embeddings.pkl'
        self.assertTrue(os.path.exists(expected_output_path))

    def test_smoke_podcast(self):
        """
        Smoke test to ensure that the embedding file for the podcast dataset is created in test
        mode.
        """
        preprocess_minilm("podcast", True)
        expected_output_path = '../TLDW/tests/test_output/test_podcast_sentTrans_embeddings.pkl'
        self.assertTrue(os.path.exists(expected_output_path))

    def test_smoke_podcast_org_embeddings(self):
        """
        Smoke test to ensure that embedding file for the complete podcast dataset exists.
        Note: the preprocess_minilm method is not called due to excessive time requirements.
        """
        expected_output_path = '../TLDW/data/podcast_sentTrans_embeddings.pkl'
        self.assertTrue(os.path.exists(expected_output_path))

    # One Shot tests
    def test_oneshot_ted(self):
        """
        One shot test to ensure that the embedding file for the ted dataset is correct.
        This is tested by loading the embeddings and checking their shape.
        """
        preprocess_minilm("ted", True)
        expected_output_path = '../TLDW/tests/test_output/test_ted_sentTrans_embeddings.pkl'
        self.assertTrue(os.path.exists(expected_output_path))
        with open(expected_output_path, 'rb') as file:
            embeddings = pickle.load(file)
        assert isinstance(embeddings, list), "TED embeddings should be a list"
        assert len(embeddings) == 5, "Unexpected number of TED embeddings"
        assert isinstance(embeddings[0], np.ndarray), "Embeddings should be numpy arrays"
        assert embeddings[0].shape == (384,), "Unexpected shape of TED embeddings"

    def test_oneshot_ted_org_embeddings(self):
        """
        One shot test to ensure that the embedding file for the complete ted dataset is correct.
        This is tested by loading the embeddings and checking their shape.
        """
        expected_output_path = '../TLDW/data/ted_sentTrans_embeddings.pkl'
        self.assertTrue(os.path.exists(expected_output_path))
        with open(expected_output_path, 'rb') as file:
            embeddings = pickle.load(file)
        assert isinstance(embeddings, list), "TED embeddings should be a list"
        assert len(embeddings) == 4005, "Unexpected number of TED embeddings"
        assert isinstance(embeddings[0], np.ndarray), "Embeddings should be numpy arrays"
        assert embeddings[0].shape == (384,), "Unexpected shape of TED embeddings"

    def test_oneshot_podcast(self):
        """
        One shot test to ensure that the embedding file for the podcast dataset is correct.
        This is tested by loading the embeddings and checking their shape.
        """
        preprocess_minilm("podcast", True)
        expected_output_path = '../TLDW/tests/test_output/test_podcast_sentTrans_embeddings.pkl'
        self.assertTrue(os.path.exists(expected_output_path))
        with open(expected_output_path, 'rb') as file:
            embeddings = pickle.load(file)
        assert isinstance(embeddings, list), "Podcast embeddings should be a list"
        assert len(embeddings) == 5, "Unexpected number of Podcast embeddings"
        assert isinstance(embeddings[0], np.ndarray), "Embeddings should be numpy arrays"
        assert embeddings[0].shape == (384,), "Unexpected shape of Podcast embeddings"

    def test_oneshot_podcast_org_embeddings(self):
        """
        One shot test to ensure that the embedding file for the complete podcast dataset is correct.
        This is tested by loading the embeddings and checking their shape.
        """
        expected_output_path = '../TLDW/data/podcast_sentTrans_embeddings.pkl'
        self.assertTrue(os.path.exists(expected_output_path))
        with open(expected_output_path, 'rb') as file:
            embeddings = pickle.load(file)
        assert isinstance(embeddings, list), "Podcast embeddings should be a list"
        assert len(embeddings) == 906, "Unexpected number of Podcast embeddings"
        assert isinstance(embeddings[0], np.ndarray), "Embeddings should be numpy arrays"
        assert embeddings[0].shape == (384,), "Unexpected shape of Podcast embeddings"

    # Edge Tests
    def test_edge_ted_or_podcast1(self):
        """
        Test to ensure that ValueError is raised when an invalid value is provided for
        ted_or_podcast.
        """
        with self.assertRaises(ValueError):
            preprocess_minilm("empty", True)

    def test_edge_ted_or_podcast2(self):
        """
        Test to ensure that TypeError is raised when ted_or_podcast is not a string.
        """
        with self.assertRaises(TypeError):
            preprocess_minilm(8, True)

    def test_edge_ted_or_podcast3(self):
        """
        Test to ensure that TypeError is raised when ted_or_podcast is None.
        """
        with self.assertRaises(TypeError):
            preprocess_minilm(None, True)

    def test_edge_test1(self):
        """
        Test to ensure that TypeError is raised when test is None.
        """
        with self.assertRaises(TypeError):
            preprocess_minilm('ted', None)

    def test_edge_test2(self):
        """
        Test to ensure that TypeError is raised when test is not a boolean.
        """
        with self.assertRaises(TypeError):
            preprocess_minilm('ted', [])

    def test_edge_test3(self):
        """
        Test to ensure that TypeError is raised when test is not a boolean.
        """
        with self.assertRaises(TypeError):
            preprocess_minilm('ted', 'true')

if __name__ == '__main__':
    unittest.main()
