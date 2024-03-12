

"""
Test suite for the chat_to_search module.
"""
import unittest
from unittest.mock import patch, MagicMock
from utils.chat_to_search import get_search_result

class TestGetSearchResult(unittest.TestCase):
    """
    Test case for the get_search_result function.
    """
    @patch("utils.chat_to_search.ChatGoogleGenerativeAI")
    @patch("utils.chat_to_search.initialize_agent")
    @patch("utils.chat_to_search.DuckDuckGoSearchRun")
    # pylint: disable=line-too-long
    def test_get_search_result(self, mock_search_run, mock_initialize_agent, mock_chat_generative_ai):
        """
        Test by mocking response of get_search_result
        """
        # Mock necessary objects
        mock_chat_generative_ai_instance = MagicMock()
        mock_chat_generative_ai_instance.invoke.return_value = "Mocked response"
        mock_chat_generative_ai.return_value = mock_chat_generative_ai_instance

        mock_search_run_instance = MagicMock()
        mock_search_run_instance.run.return_value = "Mocked search result"
        mock_search_run.return_value = mock_search_run_instance

        mock_initialize_agent_instance = MagicMock()
        mock_initialize_agent_instance.run.return_value = "Mocked agent response"
        mock_initialize_agent.return_value = mock_initialize_agent_instance

        # Mock user input
        context = "Mocked context"
        user_prompt = "Mocked user prompt"

        # Call the function
        result = get_search_result(context, user_prompt)

        # Assertions
        self.assertNotEqual(result, "", "Result should not be empty.")

if __name__ == '__main__':
    unittest.main()
