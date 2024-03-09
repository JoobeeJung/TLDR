"""
Module: test_bert_preprocess
Description:
This module contains unit tests for the preprocess_bert function in the bert_preprocess module.
"""

import unittest
import os
import torch
from utils.bert_preprocess import preprocess_bert

class TestBertPreprocess(unittest.TestCase):
    """
    Unit tests for the preprocess_bert function.
    Note: We set test to True in the preprocess_bert function so that we don't end up creating
    embeddings for the complete dataset, since it takes very long. With setting test to True, we
    take a small subset of the original dataset and ensure that the preprocess_bert function works
    properly on it, which in turn ensures that the preprocess_bert function works properly on the
    complete dataset.
    """

    # Smoke tests
    def test_smoke_ted(self):
        """
        Smoke test to ensure that the embedding file for the TED Talk dataset is created in test
        mode.
        """
        preprocess_bert("ted", True)
        expected_output_path = '../TLDW/tests/test_output/test_ted_sbert_embeddings.pt'
        self.assertTrue(os.path.exists(expected_output_path))

    def test_smoke_ted_org_embeddings(self):
        """
        Smoke test to ensure that embedding file for the complete TED Talks dataset exists.
        Note: the process_bert method is not called due to excessive time requirements.
        """
        expected_output_path = '../TLDW/data/ted_sbert_embeddings.pt'
        self.assertTrue(os.path.exists(expected_output_path))

    def test_smoke_podcast(self):
        """
        Smoke test to ensure that the embedding file for the podcast dataset is created in test
        mode.
        """
        preprocess_bert("podcast", True)
        expected_output_path = '../TLDW/tests/test_output/test_podcast_sbert_embeddings.pt'
        self.assertTrue(os.path.exists(expected_output_path))

    def test_smoke_podcast_org_embeddings(self):
        """
        Smoke test to ensure that embedding file for the complete podcast dataset exists.
        Note: the process_bert method is not called due to excessive time requirements.
        """
        expected_output_path = '../TLDW/data/podcast_sbert_embeddings.pt'
        self.assertTrue(os.path.exists(expected_output_path))

    # One Shot tests
    def test_oneshot_ted(self):
        """
        One shot test to ensure that the embedding file for the ted dataset is correct.
        This is tested by checking it's shape.
        """
        preprocess_bert("podcast", True)
        expected_output_path = '../TLDW/tests/test_output/test_ted_sbert_embeddings.pt'
        self.assertTrue(os.path.exists(expected_output_path))
        embeddings = torch.load(expected_output_path)
        assert embeddings.shape == (5, 1024), "Ted Embeddings dimensions mismatch"

    def test_oneshot_ted_org_embeddings(self):
        """
        One shot test to ensure that the embedding file for the complete ted dataset is correct.
        This is tested by checking it's shape.
        """
        expected_output_path = '../TLDW/data/ted_sbert_embeddings.pt'
        self.assertTrue(os.path.exists(expected_output_path))
        embeddings = torch.load(expected_output_path)
        assert embeddings.shape == (4005, 1024), "Ted Embeddings dimensions mismatch"

    def test_oneshot_podcast(self):
        """
        One shot test to ensure that the embedding file for the podcast dataset is correct.
        This is tested by checking it's shape.
        """
        preprocess_bert("podcast", True)
        expected_output_path = '../TLDW/tests/test_output/test_podcast_sbert_embeddings.pt'
        self.assertTrue(os.path.exists(expected_output_path))
        embeddings = torch.load(expected_output_path)
        assert embeddings.shape == (5, 1024), "Podcast Embeddings dimensions mismatch"

    def test_oneshot_podcast_org_embeddings(self):
        """
        One shot test to ensure that the embedding file for the complete podcast dataset is correct.
        This is tested by checking it's shape.
        """
        expected_output_path = '../TLDW/data/podcast_sbert_embeddings.pt'
        self.assertTrue(os.path.exists(expected_output_path))
        embeddings = torch.load(expected_output_path)
        assert embeddings.shape == (908, 1024), "Podcast Embeddings dimensions mismatch"

    # Edge Tests
    def test_edge_ted_or_podcast1(self):
        """
        Test to ensure that ValueError is raised when an invalid value is provided for
        ted_or_podcast.
        """
        with self.assertRaises(ValueError):
            preprocess_bert("empty", True)

    def test_edge_ted_or_podcast2(self):
        """
        Test to ensure that TypeError is raised when ted_or_podcast is not a string.
        """
        with self.assertRaises(TypeError):
            preprocess_bert(8, True)

    def test_edge_ted_or_podcast3(self):
        """
        Test to ensure that TypeError is raised when ted_or_podcast is None.
        """
        with self.assertRaises(TypeError):
            preprocess_bert(None, True)

    def test_edge_test1(self):
        """
        Test to ensure that TypeError is raised when test is None.
        """
        with self.assertRaises(TypeError):
            preprocess_bert('ted', None)

    def test_edge_test2(self):
        """
        Test to ensure that TypeError is raised when test is not a boolean.
        """
        with self.assertRaises(TypeError):
            preprocess_bert('ted', [])

    def test_edge_test3(self):
        """
        Test to ensure that TypeError is raised when test is not a boolean.
        """
        with self.assertRaises(TypeError):
            preprocess_bert('ted', 'true')

# if __name__ == '__main__':
#     unittest.main()
