from dispatcher import Dispatcher

def tests():
    dispatcher = Dispatcher()
    dispatcher.add_plane("EAA1110","15:43")
    dispatcher.add_plane("ANC3480","12:12")
    dispatcher.add_plane("ABC1230","05:42")
    dispatcher.add_plane("AAC3480","18:43")


    print(dispatcher.queue)
    print(dispatcher.allocate_landing_slot("12:11"))
    print(dispatcher.is_present("ABC1230"))

if __name__ == "__main__":
    tests()
