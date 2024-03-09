# import unittest
# import os
# from utils.bert_preprocess import preprocess_bert

# class TestBertPreprocess(unittest.TestCase):
    
#     # Smoke tests
#     # def test_smoke_ted(self):
#     #     preprocess_bert("ted")
#     #     self.assertTrue(os.path.exists('TLDW/ted_sbert_embeddings.pt'))

#     # def test_smoke_podcast(self):
#     #     preprocess_bert("podcast")
#     #     self.assertTrue(os.path.exists('TLDW/podcast_sbert_embeddings.pt'))

#     # def test_one_shot_podcast(self):
#     #     preprocess_bert("podcast")  # Assuming skeptoid_transcripts.csv is a small dataset
#     #     self.assertTrue(os.path.exists('podcast_sbert_embeddings.pt'))

#     # Edge Tests
#     def test_edge_value_error(self):
#         with self.assertRaises(ValueError):
#             preprocess_bert("empty")
    
#     def test_edge_type_error(self):
#         with self.assertRaises(TypeError):
#             preprocess_bert(8)


# if __name__ == '__main__':
#     unittest.main()
