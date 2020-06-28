import unittest
from configuration import Configuration

class ConfigurationTestCase(unittest.TestCase):
    def test_init(self):
        key_note_mapping = {'A': 'A1', 'B': 'B2'}
        instrument = 'my_instrument.sf'
        configuration = Configuration(key_note_mapping, instrument)

        assert configuration.key_note_mapping == key_note_mapping
        assert configuration.instrument == instrument
        assert configuration.keys == set(['A', 'B'])
        assert configuration.is_down == {'A': False, 'B': False}


if __name__ == '__main__':
    unittest.main()
