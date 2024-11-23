class Television:
    """
    A class for Television with controllable power, muting, volume, and channel.
    If the TV is not powered and the mute, volume, or channel methods are called, will not execute.
    If the volume functions are called while the TV is muted, the volume will reset and adjust accordingly.

    :var MIN_VOLUME (int): Minimum volume (0)
    :var MAX_VOLUME (int): Maximum volume (2)
    :var MIN_CHANNEL (int): Minimum channel (0)
    :var MAX_CHANNEL (int): Maximum channel (3)
    """
    # Volume can range between from 0-2
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    # Channels available: 0-3
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initializes the TV with its default settings.
        Power: off, mute: off, volume and channel: minimum.
        """
        self._status: bool = False # Power off
        self._muted: bool = False # Not muted

        self._volume: int = self.MIN_VOLUME # Volume = 0
        self._channel: int = self.MIN_CHANNEL # Channel = 0

        self._previous_volume: int = self._volume # For the mute and volume functions

    def power(self) -> None:
        """
        Controls the power of the TV.
        """
        self._status = not self._status # Flips the power status

    def mute(self) -> None: # False = not muted, True = muted
        """
        Toggles mute on the TV.
        If the TV is muted, volume is set to zero.
        If the TV is unmuted, the volume is restored to its previous value.
        """
        if self._status:
            self._muted = not self._muted
            if self._muted:
                self._previous_volume = self._volume # Remembers the volume before being muted
                self._volume = 0
            else:
                self._volume = self._previous_volume # Restores volume after unmuting

    def channel_up(self) -> None:
        """
        Increases channel number by 1.
        If the max channel (3) is reached, resets back to minimum channel (0).
        """
        if self._status:
            if self._channel == self.MAX_CHANNEL: # If called while channel is max (3), will reset at channel 0
                self._channel = self.MIN_CHANNEL
            else:
                self._channel += 1

    def channel_down(self) -> None:
        """
        Decreases channel number by 1.
        If the minimum channel (0) is reached, resets back to max channel (3).
        """
        if self._status:
            if self._channel == self.MIN_CHANNEL: # If called while channel is minimum (0), will reset at channel 3
                self._channel = self.MAX_CHANNEL
            else:
                self._channel -= 1

    def volume_up(self):
        """
        Increases volume by 1.
        If the max volume (2) is reached and this method is called, the volume will remain max.
        """
        if self._status:
            if self._muted: # If called while muted, will automatically unmute and change the volume
                self._muted = not self._muted
                if self._previous_volume < self.MAX_VOLUME:
                    self._previous_volume += 1
                    self._volume = self._previous_volume
            elif self._volume < self.MAX_VOLUME:
                self._volume += 1

    def volume_down(self):
        """
        Decreases volume by 1.
        If the minimum volume (0) is reached and this method is called, the volume will remain minimum.
        """
        if self._status:
            if self._muted:
                self._muted = not self._muted
                if self._previous_volume > self.MIN_VOLUME:
                    self._previous_volume -= 1
                    self._volume = self._previous_volume
            elif self._volume > self.MIN_VOLUME:
                self._volume -= 1

    def __str__(self) -> str:
        """
        Returns the power status, channel number, and volume in the form of a string.
        """
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"
