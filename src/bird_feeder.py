import feed_store
from time import sleep

class BirdFeeder():
    def __init__(self, feeder_name, feed_store):
        self.feeder_name = feeder_name
        self.feed_store = feed_store

    def deliver_feed(self, feed_type, feed_amount, requesting_keeper):
        print "Hey {0}, I'm going to get {1} {2}".format(requesting_keeper, feed_amount, feed_type)
        #sleep(10)
        self.feed_store.deposit_feed(feed_type, feed_amount)
        #sleep(10)
        print "Hey {0}, I've put {1} {2} into the feed store".format(requesting_keeper, feed_amount, feed_type)

    def get_feeder_name(self):
        return self.feeder_name