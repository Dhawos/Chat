from datetime import datetime

def check_channel(channel_name):
    def check_channel_decorator(func):
        def func_wrapper(message):
            if(channel_name != message.channel.name):
                print("Command used in wrong channel")
            else:
                return func()
        return func_wrapper
    return check_channel_decorator



