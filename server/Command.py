from datetime import datetime

def check_channel(channel_name):
    def check_channel_decorator(func):
        def func_wrapper(self,**kwargs):
            if(channel_name != kwargs.get("channel")):
                print("Command used in wrong channel")
            else:
                return func(self,**kwargs)
        return func_wrapper
    return check_channel_decorator



