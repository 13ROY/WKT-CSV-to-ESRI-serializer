##from lettuce import *
##from nose.tools import assert_equals
##import sys
##import os
##sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
##from src.feed_store import FeedStore
##
##@before.all
##def setup_stores():
##    world.keepers = {}
##    world.feeders = {}
##    world.bad_foods = []
##
##@step('I have an empty feed store')
##def create_new_feedstore(step):
##    world.feed_store = FeedStore()
##
##@step('I have a keeper "([^"]*)')
##def add_new_keeper(step, keeper_name):
##    world.keepers[keeper_name] = BirdKeeper(keeper_name)
##
##@step('I have a feeder "([^"]*)')
##def add_new_feeder(step, feeder_name):
##    world.feeders[feeder_name] = BirdFeeder(feeder_name,world.feed_store)
##
##@step('"([^"]*)" are particularly bad for birds')
##def add_bad_food(step, bad_food):
##    world.bad_foods.append(bad_food)
##
##@step('"([^"]*)" made lots of requests yesterday')
##def previous_requests(step, keeper_name):
##    for request in step.hashes:
##        world.feed_store.deposit_feed(request['feed type'],int(request['feed amount']))
##
##@step('"([^"]*)" requests "([^"]*)" to deliver "([^"]*)" "([^"]*)" to the feed store')
##def feed_request(step, keeper_name, feeder_name, feed_amount, feed_type):
##    world.keepers[keeper_name].make_feed_request(feed_type,int(feed_amount),world.feeders[feeder_name])
##
##@step('we request to replay all of "([^"]*)" requests from yesterday')
##def replay_requests(step, keeper_name):
##    print('We need to implement replay')
##    pass
##
##@step('the feed store must contain "([^"]*)" "([^"]*)"')
##def feed_store_contains(step, feed_amount, feed_type):
##    assert_equals(world.feed_store.get_feed_amount(feed_type), int(feed_amount))
##
##@step('the system must be able to detect that "([^"]*)" was responsible')
##def detect_who_is_responsible(step, keeper_responsible):
##    print('We need to implement querying our request history')
##    pass