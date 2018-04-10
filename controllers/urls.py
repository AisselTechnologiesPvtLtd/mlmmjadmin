# URL mappings
from libs.regxes import email as e

urls = [
    # Per-maillist profile
    '/api/(%s)$' % e, 'controllers.profile.Profile',

    #
    # Per-maillist subscribers
    #
    # Get subscribers.
    '/api/(%s)/subscribers' % e, 'controllers.subscriber.Subscribers',

    # Check whether given subscriber is member of given mailing list.
    '/api/(%s)/has_subscriber/(%s)' % (e, e), 'controllers.subscriber.HasSubscriber',

    #
    # per-subscriber
    #
    # Get all subscribed mailing lists of given subscriber.
    '/api/subscriber/(%s)/subscribed' % e, 'controllers.subscriber.SubscribedLists',
    # Subscribe one subscriber to multiple mailing lists.
    '/api/subscriber/(%s)/subscribe' % e, 'controllers.subscriber.Subscribe',
]
