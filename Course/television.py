 

class Television:
    def __init__(self) -> None:
        self.__status : bool = False
        self.__volume : int = 0
        self.__channel : int = 0

    @property
    def status(self) -> bool:
        return self.__status
    
    @status.setter
    def status(self, status : bool):
        self.__status = status

    @property
    def volume(self) -> int:
        return self.__volume
    
    @volume.setter
    def volume(self, volume : int):
        self.__volume = volume

    @property
    def channel(self) -> int:
        return self.__channel
    
    @channel.setter
    def channel(self, channel : int):
        self.__channel = channel

    def turn_on_off(self)->None:
        self.status = not self.status

        if self.status:
            print('Status TV On')
        else:
            print('Status TV Off')

    def more_volume(self) -> None:
        self.volume += 1
        print(f'Volume increased to {self.volume}')

    def less_volume(self) -> None:
        self.volume -= 1
        print(f'Volume decreased to {self.volume}')

    def more_channel(self) -> None:
        self.channel += 1
        print(f'Channel increased to {self.channel}')

    def less_channel(self) -> None:
        self.channel -= 1
        print(f'Channel decreased to {self.channel}')

    def change_channel(self, channel: int)-> None:
        self.channel = channel
        print(f'Channel changed to {self.channel}')


class RemoteControl:

    def __init__(self, tv : Television) -> None:
        self.__tv : Television = tv

    @property
    def television(self)->Television:
        return self.__tv
    
    def turn_on_off(self) -> None:
        self.__tv.turn_on_off()

    def more_volume(self)->None:
        self.television.more_volume()

    def less_volume(self)->None:
        self.television.less_volume()

    def more_channel(self)->None:
        self.television.more_channel()

    def less_channel(self)->None:
        self.television.less_channel()

    def change_channel(self, channel) -> None:
        self.television.change_channel(channel)

if __name__ == '__main__':
    tv: Television = Television()
    tv.turn_on_off()
    tv.more_volume()
    tv.more_channel()
    tv.more_channel()
    tv.more_channel()
    tv.change_channel(42)
    tv.turn_on_off()

    remote: RemoteControl = RemoteControl(tv)
    remote.turn_on_off()
    remote.more_volume()
    remote.more_channel()
    remote.more_channel()
    remote.more_channel()
    remote.change_channel(42)
    remote.turn_on_off()