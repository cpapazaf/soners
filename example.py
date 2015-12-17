
import functools
import tornado.ioloop
from soners.soners_server import SonersServer
from tornado.gen import coroutine

@coroutine
def temperature(device, temperature):
    print(temperature)


if __name__ == '__main__':

    my_sensor = SonersServer([('^T:(?P<temperature>.*)$', temperature)]) 
    my_sensor.listen() 
    tornado.ioloop.IOLoop.current().start()
