# test_elasticsearch.py
"""
Tests for Elasticsearch module.
"""

import unittest
from elasticsearch import Elasticsearch

class TestElasticsearch(unittest.TestCase):
    """Test cases for Elasticsearch class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = Elasticsearch()
        self.assertIsInstance(instance, Elasticsearch)
        
    def test_run_method(self):
        """Test the run method."""
        instance = Elasticsearch()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
