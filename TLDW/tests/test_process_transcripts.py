"""
Module for testing the process_transcripts module.
"""

import unittest
from unittest.mock import patch
from utils.process_transcripts import (
    get_video_id,
    get_video_transcript,
    get_transcript
)

class TestProcessTranscripts(unittest.TestCase):
    """
    Test cases for processTranscripts module.
    """

    def test_smoke(self):
        """Smoke test to check if transcript can be fetched."""
        get_transcript('https://www.youtube.com/watch?v=tlWuP7wESZw')

    def test_video_id_blank(self):
        """Test handling of blank video ID."""
        with self.assertRaises(ValueError):
            get_video_id('')

    def test_video_id_zero(self):
        """Test handling of incorrect video ID length."""
        with self.assertRaises(ValueError):
            get_video_id('https://www.youtube.com/watch?v=')

    def test_improper_id_len(self):
        """Test handling of improper video ID."""
        with self.assertRaises(ValueError):
            get_video_id('https://www.youtube.com/watch?y=tlWuP7wESZw456')

    def test_alphanumeric(self):
        """Test handling of non-alphanumeric characters in video ID."""
        with self.assertRaises(ValueError):
            get_video_id('https://www.youtube.com/watch?v=tlWuP#wESZw456')

    def test_transcript_language(self):
        """Test fetching transcript in a different language."""
        with self.assertRaises(ValueError):
            get_video_transcript('hLpP4rtjACM8')  # Hindi video

    def test_invalid_url(self):
        """Test handling of invalid URL."""
        with self.assertRaises(ValueError):
            get_transcript('https://www.reddit.com/watch?v=LpP4rtjACM8')

    @patch('utils.process_transcripts.DEBUG_MODE', True)  # Patch the DEBUG_MODE to be True
    @patch('builtins.print')  # Patch the print function
    def test_debug_mode_enabled(self, mock_print):
        """Test debug functionality when enabled."""
        # Call the function
        video_id = get_video_id("https://www.youtube.com/watch?v=abc123xyz")

        # Assertions
        self.assertEqual(video_id, "abc123xyz")
        mock_print.assert_called_with("Video ID: abc123xyz")

    @patch('builtins.print')  # Patch the print function
    def test_debug_mode_disabled(self, mock_print):
        """Test debug functionality when disabled."""
        # Call the function
        video_id = get_video_id("https://www.youtube.com/watch?v=abc123xyz")

        # Assertions
        self.assertEqual(video_id, "abc123xyz")
        mock_print.assert_not_called()

    @patch('utils.process_transcripts.YouTubeTranscriptApi.get_transcript')
    def test_api_health_mock(self, mock_get_transcript):
        """Mocking Youtube api to check its working."""
        # Set up mock response
        mock_transcript = [
            {'text': 'This is a mock transcript.'},
            {'text': 'Another mock transcript line.'}
        ]
        mock_get_transcript.return_value = mock_transcript

        # Call the function
        youtube_url = "https://www.youtube.com/watch?v=abc123"
        result = get_transcript(youtube_url)

        # Assert that the result is not empty
        self.assertNotEqual(result, "", "Transcript should not be empty.")

if __name__ == '__main__':
    unittest.main()
