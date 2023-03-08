from unittest import TestCase

import oops_all_itertools as oai


class DoesItImport(TestCase):
    def test_quantity(self):
        """Test that a specific pile of stuff was imported"""
        self.assertEqual(len(dir(oai)), 167)
