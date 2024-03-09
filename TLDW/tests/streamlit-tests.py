import unittest
from streamlit.testing.v1 import AppTest
import streamlit as st

class TestStreamlitApp(unittest.TestCase):
    def setUp(self):
        self.at = AppTest.from_file('../../TLDW/streamlit_app.py', default_timeout=100).run()

    # def test_empty_youtube(self):
    #     self.at.text_input[0].input(" ").run()
    #     self.assertTrue("TypeError")

    # def test_get_transcript_summary_keywords(self):
    #     self.at.text_input[0].input("https://www.youtube.com/watch?v=dQw4w9WgXcQ").run()
    #     self.assertIsNotNone(self.at.session_state.transcript)
    #     self.assertIsNotNone(self.at.session_state.summary)
    #     self.assertIsNotNone(self.at.session_state.keywords)
    #     print("hello?")

    # def test_selected_content_type_ted(self):
    #     self.at.text_input[0].input("https://www.youtube.com/watch?v=dQw4w9WgXcQ").run()
    #     self.at.radio[0].set_value("TED Talks").run()
    #     selected_content_type = self.at.session_state.selected_content_type
    #     self.assertEqual(selected_content_type, "ted")

    # def test_selected_content_type_podcasts(self):
    #     self.at.text_input[0].input("https://www.youtube.com/watch?v=dQw4w9WgXcQ").run()
    #     self.at.radio[0].set_value("Podcasts").run()
    #     selected_content_type = self.at.session_state.selected_content_type
    #     self.assertEqual(selected_content_type, "podcast")

    # def test_sbert_recommender(self):
    #     self.at.text_input[0].input("https://www.youtube.com/watch?v=dQw4w9WgXcQ").run()
    #     self.at.radio[0].set_value("TED Talks").run()
    #     self.at.button[0].click().run()
    #     self.assertEqual(self.at.header[2].value, "Top 3 SBERT Recommendations")
    #     self.assertIsNotNone(self.at.get("expandable"))
        
    # def test_minilm_recommender(self):
    #     self.at.text_input[0].input("https://www.youtube.com/watch?v=dQw4w9WgXcQ").run()
    #     self.at.radio[0].set_value("TED Talks").run()
    #     self.at.button[1].click().run()
    #     self.assertEqual(self.at.header[2].value, "Top 3 MiniLM Recommendations")
    #     self.assertIsNotNone(self.at.get("expandable"))

    # def test_tfidf_recommender(self):
    #     self.at.text_input[0].input("https://www.youtube.com/watch?v=dQw4w9WgXcQ").run()
    #     self.at.radio[0].set_value("TED Talks").run()
    #     self.at.button[2].click().run()
    #     self.assertEqual(self.at.header[2].value, "Top 3 TF-IDF Recommendations")
    #     self.assertIsNotNone(self.at.get("expandable"))
        
    # def test_chatbot(self):
    #     self.at.text_input[0].input("https://www.youtube.com/watch?v=dQw4w9WgXcQ").run()
    #     self.at.radio[0].set_value("TED Talks").run()
    #     self.assertEqual(self.at.header[2].value, "🔎 Learn More - Chat with GEMINI")
    #     self.at.chat_input[0].set_value("What is rick-rolling?").run()
    #     self.assertEqual(self.at.chat_message[1].markdown[0].value, "What is rick-rolling?")
    #     self.assertIsNotNone(self.at.chat_message[0].markdown[0].value) 

    def test_chatbot_promt_blank(self):
        self.at.text_input[0].input("https://www.youtube.com/watch?v=dQw4w9WgXcQ").run()
        self.at.radio[0].set_value("TED Talks").run()
        self.assertEqual(self.at.header[2].value, "🔎 Learn More - Chat with GEMINI")
        self.at.chat_input[0].set_value("").run()
        # self.assertEqual(self.at.chat_message[1].markdown[0].value, "What is rick-rolling?")
        self.assertIsNone(self.at.chat_message[0].markdown[0].value) 

if __name__ == "__main__":
    unittest.main()
