class Television:
    # Volume can range between from 0-2
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    # Channels available: 0-3
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self._status = False # Power off
        self._muted = False # Not muted

        self._volume = self.MIN_VOLUME # Volume = 0
        self._channel = self.MIN_CHANNEL # Channel = 0

        self._previous_volume = self._volume # For the mute and volume functions

    def power(self):
        self._status = not self._status # Flips the power status

    def mute(self): # False = not muted, True = muted
        if self._status:
            self._muted = not self._muted
            if self._muted:
                self._previous_volume = self._volume # Remembers the volume before being muted
                self._volume = 0
            else:
                self._volume = self._previous_volume # Restores volume after unmuting

    def channel_up(self):
        if self._status:
            if self._channel == self.MAX_CHANNEL: # If called while channel is max (3), will reset at channel 0
                self._channel = self.MIN_CHANNEL
            else:
                self._channel += 1

    def channel_down(self):
        if self._status:
            if self._channel == self.MIN_CHANNEL: # If called while channel is minimum (0), will reset at channel 3
                self._channel = self.MAX_CHANNEL
            else:
                self._channel -= 1

    def volume_up(self):
        if self._status:
            if self._muted: # If called while muted, will automatically unmute and change the volume
                self._muted = not self._muted
                if self._previous_volume < self.MAX_VOLUME:
                    self._previous_volume += 1
                    self._volume = self._previous_volume
            elif self._volume < self.MAX_VOLUME:
                self._volume += 1

    def volume_down(self):
        if self._status:
            if self._muted:
                self._muted = not self._muted
                if self._previous_volume > self.MIN_VOLUME:
                    self._previous_volume -= 1
                    self._volume = self._previous_volume
            elif self._volume > self.MIN_VOLUME:
                self._volume -= 1

    def __str__(self):
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"


# WANTED OUTPUTS:

# 1: Power = True, Channel = 0, Volume = 0
# 2: Power = True, Channel = 2, Volume = 1
# 3: Power = True, Channel = 1, Volume = 0
# 4: Power = False, Channel = 1, Volume = 0
# 5: Power = True, Channel = 3, Volume = 2
# 6: Power = True, Channel = 1, Volume = 1
# 7: Power = True, Channel = 3, Volume = 0
# 8: Power = True, Channel = 3, Volume = 1
# 9: Power = True, Channel = 3, Volume = 0
# 10: Power = True, Channel = 3, Volume = 2
# 11: Power = False, Channel = 3, Volume = 2