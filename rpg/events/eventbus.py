class EventBus:

    def __init__(self):
        self.player_walks_listeners = []

    def add_player_walks_listener(self, player_walks_listener):
        self.player_walks_listeners.append(player_walks_listener)

    def dispatch_player_walks_event(self, player_walks_event):
        for listener in self.player_walks_listeners:
            listener.coinCollected(player_walks_event)
