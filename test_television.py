import unittest
from television import Television


class TestTelevision(unittest.TestCase):
    def setUp(self):
        self.test_tv = Television()

    def test_init(self):
        """These tests are for when the TV is first powered up on initialization"""
        self.assertFalse(self.test_tv._status, "Should be off by default") # Test the power status
        self.assertFalse(self.test_tv._muted, "Should not be muted by default") # Tests if the TV is muted

        self.assertEqual(self.test_tv._volume, 0, "Default volume should be 0") # Tests if the volume is minimum
        self.assertEqual(self.test_tv._channel, 0, "Starts on channel 0") # Tests if the channel starts at 0

        self.assertEqual(self.test_tv._previous_volume, 0)

    def test_power(self):
        # Power on
        self.test_tv.power()
        self.assertTrue(self.test_tv._status, "Should be on")
        self.assertFalse(self.test_tv._muted, "TV should be unmuted")
        self.assertEqual(self.test_tv._volume, 0, "Volume should be 0")
        self.assertEqual(self.test_tv._channel, 0, "Should be on channel 0")

        #Power off
        self.test_tv.power()
        self.assertFalse(self.test_tv._status, "Should be off")
        self.assertFalse(self.test_tv._muted, "TV should be unmuted")
        self.assertEqual(self.test_tv._volume, 0, "Volume should be 0")
        self.assertEqual(self.test_tv._channel, 0, "Should be on channel 0")

    def test_mute(self):
         """Test one: power on, +1 volume, mute"""
        self.test_tv.power()
        self.test_tv.volume_up()
        self.test_tv.mute()
        self.assertTrue(self.test_tv._status, "Should be on")
        self.assertTrue(self.test_tv._muted, "Should be muted")
        self.assertEqual(self.test_tv._volume, 0, "Volume should currently be 0, since it is muted")
        self.assertEqual(self.test_tv._channel, 0, "Should be on channel 0")

        """Test two: Power on, not muted"""
        # Power is already on
        self.test_tv.mute()
        self.assertTrue(self.test_tv._status, "Should be on")
        self.assertFalse(self.test_tv._muted, "Should be unmuted")
        self.assertEqual(self.test_tv._volume, 1, "Volume should now be 1 after unmuting")
        self.assertEqual(self.test_tv._channel, 0, "Should be on channel 0")

        """Test three: Power off, muted"""
        self.test_tv.power() # Powering off
        self.test_tv.mute()
        self.assertFalse(self.test_tv._status, "Should be off")
        self.assertFalse(self.test_tv._muted, "Mute should not work if the TV has no power")
        self.assertEqual(self.test_tv._volume, 1, "Volume should be at 1")
        self.assertEqual(self.test_tv._channel, 0, "Should be on channel 0")

        """Test four: Power off, not muted"""
        # Power is still off
        self.test_tv.mute() # Attempting to mute it
        self.test_tv.mute() # Attempting to unmute it
        self.assertFalse(self.test_tv._status, "Should be off")
        self.assertFalse(self.test_tv._muted, "Mute should not work if the TV has no power")
        self.assertEqual(self.test_tv._volume, 1, "Volume should be at 1")
        self.assertEqual(self.test_tv._channel, 0, "Should be on channel 0")

    def test_channel_up(self):
       """Test one: Power off, +1 channel"""
        # Power is already off
        self.test_tv.channel_up()
        self.assertFalse(self.test_tv._status, "Should be off")
        self.assertFalse(self.test_tv._muted, "Should be unmuted")
        self.assertEqual(self.test_tv._volume, 0, "Volume should be at 0")
        self.assertEqual(self.test_tv._channel, 0, "Channel functions should not execute if the TV has no power")

        """Test two: Power on, +1 channel"""
        self.test_tv.power()
        self.test_tv.channel_up()
        self.assertTrue(self.test_tv._status, "Should be on")
        self.assertFalse(self.test_tv._muted, "Should be unmuted")
        self.assertEqual(self.test_tv._volume, 0, "Volume should be at 0")
        self.assertEqual(self.test_tv._channel, 1, "Channel should now be at 1")

        """Test three: TV on, 1 over max channel"""
        # TV still powered, previously on channel 1
        self.test_tv.channel_up() # Channel 2
        self.test_tv.channel_up() # Channel 3
        self.test_tv.channel_up() # Test
        self.assertTrue(self.test_tv._status, "Should be on")
        self.assertFalse(self.test_tv._muted, "Should be unmuted")
        self.assertEqual(self.test_tv._volume, 0, "Volume should be at 0")
        self.assertEqual(self.test_tv._channel, 0, "Channel should be back at 0")

    def test_channel_down(self):
        """Test one: Power off, -1 channel"""
        self.test_tv.channel_down()
        self.assertFalse(self.test_tv._status, "Should be off")
        self.assertFalse(self.test_tv._muted, "Should be unmuted")
        self.assertEqual(self.test_tv._volume, 0, "Volume should be at 0")
        self.assertEqual(self.test_tv._channel, 0, "Should be at channel 0")

        """Test two: Power on, 1 channel below minimum"""
        self.test_tv.power()
        self.test_tv.channel_down()
        self.assertTrue(self.test_tv._status, "Should be on")
        self.assertFalse(self.test_tv._muted, "Should be unmuted")
        self.assertEqual(self.test_tv._volume, 0, "Volume should be at 0")
        self.assertEqual(self.test_tv._channel, 3, "Should be at channel 3 now")


    def test_volume_up(self):
        """Test one: Power off, +1 volume"""
        # Power is off
        self.test_tv.volume_up()
        self.assertFalse(self.test_tv._status, "Should be off")
        self.assertFalse(self.test_tv._muted, "Should be unmuted")
        self.assertEqual(self.test_tv._volume, 0, "Volume should have remained 0")
        self.assertEqual(self.test_tv._channel, 0, "Should be at channel 0")

        """Test two: Power on, +1 volume"""
        self.test_tv.power()
        self.test_tv.volume_up()
        self.assertTrue(self.test_tv._status, "Should be on")
        self.assertFalse(self.test_tv._muted, "Should be unmuted")
        self.assertEqual(self.test_tv._volume, 1, "Volume should be at 1 now")
        self.assertEqual(self.test_tv._channel, 0, "Should be at channel 0")

        """Test three: Power on, muted, +1 volume"""
        # Power is on
        self.test_tv.mute()
        self.test_tv.volume_up() # Volume was previously 1
        self.assertTrue(self.test_tv._status, "Should be on")
        self.assertFalse(self.test_tv._muted, "Add volume pressed after mute-- should not be muted anymore")
        self.assertEqual(self.test_tv._volume, 2, "Volume should be at 2")
        self.assertEqual(self.test_tv._channel, 0, "Should be at channel 0")

        """Test four: Power on, 1 over maximum volume"""
        self.test_tv.volume_up()  # Volume was previously 2, which is max
        self.assertTrue(self.test_tv._status, "Should be on")
        self.assertFalse(self.test_tv._muted, "Should be unmuted")
        self.assertEqual(self.test_tv._volume, 2, "Volume should stay 2, since it is max")
        self.assertEqual(self.test_tv._channel, 0, "Should be at channel 0")

    def test_volume_down(self):
        """Test one: Power off, -1 volume"""
        # Power is off
        self.test_tv.volume_down()
        self.assertFalse(self.test_tv._status, "Should be off")
        self.assertFalse(self.test_tv._muted, "Should be unmuted")
        self.assertEqual(self.test_tv._volume, 0, "Volume should be at 0")
        self.assertEqual(self.test_tv._channel, 0, "Should be at channel 0")

        """Test two: Power on, max volume (required for testing), -1 volume"""
        self.test_tv.power()
        self.test_tv.volume_up()
        self.test_tv.volume_up() # Maxed
        self.test_tv.volume_down()
        self.assertTrue(self.test_tv._status, "Should be on")
        self.assertFalse(self.test_tv._muted, "Should be unmuted")
        self.assertEqual(self.test_tv._volume, 1, "Volume should be at 1 now")
        self.assertEqual(self.test_tv._channel, 0, "Should be at channel 0")

        """Test three: Power on, muted, -1 volume"""
        # Power is on
        self.test_tv.mute()
        self.test_tv.volume_down()  # Volume was previously 1
        self.assertTrue(self.test_tv._status, "Should be on")
        self.assertFalse(self.test_tv._muted, "Subtract volume pressed after mute-- should not be muted anymore")
        self.assertEqual(self.test_tv._volume, 0, "Volume should be at 0")
        self.assertEqual(self.test_tv._channel, 0, "Should be at channel 0")

        """Test four: Power on, 1 below minimum volume"""
        self.test_tv.volume_down()  # Volume was previously 0, which is minimum
        self.assertTrue(self.test_tv._status, "Should be on")
        self.assertFalse(self.test_tv._muted, "Subtract volume pressed after mute-- should not be muted anymore")
        self.assertEqual(self.test_tv._volume, 0, "Volume should stay 0, since it is minimum")
        self.assertEqual(self.test_tv._channel, 0, "Should be at channel 0")

if __name__ == "__main__":
    unittest.main()
