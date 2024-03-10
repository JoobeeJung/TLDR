"""
Module: test_helper_load_validate
Description:
This file contains unit tests for the functionality provided by the helper_load_validate module.
It includes tests to ensure the correctness and robustness of the validate_ted_or_podcast,
validate_input_transcript, and load_data function.
"""

import unittest
import os
import pandas as pd
from utils.helper_load_validate import validate_ted_or_podcast, validate_input_transcript,load_data

class TestHelperLoadValidate(unittest.TestCase):
    """
    TestHelperLoadValidate class contains unit tests for the
    helper_load_validate module.
    """

    def test_validate_ted_or_podcast(self):
        """
        Test the functionality of validate_ted_or_podcast function.
        """
        # Valid case
        self.assertIsNone(validate_ted_or_podcast("ted"))
        self.assertIsNone(validate_ted_or_podcast("podcast"))

        # Invalid case
        with self.assertRaises(TypeError):
            validate_ted_or_podcast(8)

        with self.assertRaises(TypeError):
            validate_ted_or_podcast(None)

        with self.assertRaises(ValueError):
            validate_ted_or_podcast("invalid")

    def test_validate_input_transcript(self):
        """
        Test the functionality of validate_input_transcript function.
        """
        # Test handling of ValueError when user_transcript is empty.
        with self.assertRaises(ValueError):
            validate_input_transcript("")

        # Test handling of TypeError when user_transcript is not a string.
        with self.assertRaises(TypeError):
            validate_input_transcript(1)

    def test_load_data(self):
        """
        Test the functionality of load_data function.
        """
        # TED
        expected_output_path = '../TLDW/data/ted_talks_en.csv'
        self.assertTrue(os.path.exists(expected_output_path))

        # Test is true
        data_df, transcripts = load_data("ted", True)
        self.assertIsInstance(data_df, pd.DataFrame)
        self.assertIsInstance(transcripts, list)
        assert data_df.shape == (5, 19)
        assert len(transcripts) == 5

        # Test is false
        data_df, transcripts = load_data("ted", False)
        self.assertIsInstance(data_df, pd.DataFrame)
        self.assertIsInstance(transcripts, list)
        assert data_df.shape == (4005, 19)
        assert len(transcripts) == 4005

        # Podcast
        expected_output_path = '../TLDW/data/skeptoid_transcripts.csv'
        self.assertTrue(os.path.exists(expected_output_path))

        # Test is true
        data_df, transcripts = load_data("podcast", True)
        self.assertIsInstance(data_df, pd.DataFrame)
        self.assertIsInstance(transcripts, list)
        assert data_df.shape == (5, 9)
        assert len(transcripts) == 5

        # Test is false
        data_df, transcripts = load_data("podcast", False)
        self.assertIsInstance(data_df, pd.DataFrame)
        self.assertIsInstance(transcripts, list)
        assert data_df.shape == (906, 9)
        assert len(transcripts) == 906

        # Edge Case
        # When test is not a valid boolean
        with self.assertRaises(TypeError):
            load_data("podcast", None)

        with self.assertRaises(TypeError):
            load_data("podcast", [])

        with self.assertRaises(TypeError):
            load_data("podcast", 'true')

if __name__ == '__main__':
    unittest.main()
