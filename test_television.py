import unittest
from television import Television


class TestTelevision(unittest.TestCase):
    test_tv = Television()
    def test_init(self):
        # These tests are for when the TV is first powered up on initialization
        self.assertFalse(self.test_tv._status, "Should be off by default") # Test the power status
        self.assertFalse(self.test_tv._muted, "Should not be muted by default") # Tests if the TV is muted

        self.assertEqual(self.test_tv._volume, 0, "Default volume should be 0") # Tests if the volume is minimum
        self.assertEqual(self.test_tv._channel, 0, "Starts on channel 0") # Tests if the channel starts at 0

        self.assertEqual(self.test_tv._previous_volume, 0)

    def test_power(self):
        # Power on
        self.test_tv.power()
        self.assertTrue(self.test_tv._status, "Should be on")
        self.assertFalse(self.test_tv._muted, "TV should not be muted")
        self.assertEqual(self.test_tv._volume, 0, "Volume should still be zero")
        self.assertEqual(self.test_tv._channel, 0, "Should still be on channel 0")

        #Power off
        self.test_tv.power()
        self.assertFalse(self.test_tv._status, "Should be turned off again")
        self.assertFalse(self.test_tv._muted, "TV should still not be muted")
        self.assertEqual(self.test_tv._volume, 0, "Volume should still be zero")
        self.assertEqual(self.test_tv._channel, 0, "Should still be on channel 0")

    def test_mute(self):
        '''Test one: power on, +1 volume, mute'''
        # Power on
        self.test_tv.power()
        self.assertTrue(self.test_tv._status, "Should be on")
        self.assertFalse(self.test_tv._muted, "Should still not be muted")
        self.assertEqual(self.test_tv._volume, 0, "Volume should still be zero")
        self.assertEqual(self.test_tv._channel, 0, "Should still be on channel 0")
        # +1 volume
        self.test_tv.volume_up()
        self.assertTrue(self.test_tv._status, "Should be on")
        self.assertFalse(self.test_tv._muted, "Should still not be muted")
        self.assertEqual(self.test_tv._volume, 1, "Volume should now be one")
        self.assertEqual(self.test_tv._channel, 0, "Should still be on channel 0")
        # Mute
        self.test_tv.mute()
        self.assertTrue(self.test_tv, "Should now be muted")
        self.assertEqual(self.test_tv._channel, 0, "Should still be on channel 0")
        self.test_tv.power() # Turns off

        '''Test two: Power on, not muted'''
        self.test_tv.power()
        self.test_tv._muted()
        self.assertFalse(self.test_tv._muted, "TV should not be muted")
        self.assertEqual(self.test_tv._volume, 0, "Volume should still be zero")
        self.assertEqual(self.test_tv._channel, 0, "Should still be on channel 0")

    def test_channel_up(self):
        pass

    def test_channel_down(self):
        pass

    def test_volume_up(self):
        pass

    def test_volume_down(self):
        pass



if __name__ == "__main__":
    unittest.main()

