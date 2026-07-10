# test_decentromesh.py
"""
Tests for DecentroMesh module.
"""

import unittest
from decentromesh import DecentroMesh

class TestDecentroMesh(unittest.TestCase):
    """Test cases for DecentroMesh class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DecentroMesh()
        self.assertIsInstance(instance, DecentroMesh)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DecentroMesh()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
