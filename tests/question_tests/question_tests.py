#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config
from src.question_c.question_c import get_most_likely_ancestor_consensus

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())


    def test_add_inventory(self):
        positions = dict()
        pnum = 'position1'
        pplace = '2'

        dna1 = 'GCATATCATCCATAT'
        dna2 = 'CATA'

        self.assertEqual(get_most_likely_ancestor_consensus(dna1, dna2), {'position1': 2, 'position2': 11})
