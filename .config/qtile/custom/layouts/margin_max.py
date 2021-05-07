from libqtile.layout.max import Max

class MarginMax(Max):
    defaults = [("name", "marginmax", "Name of this layout.")]

    def __init__(self, margin=0, **config):
        super().__init__(**config)
        self.margin = margin

    def configure(self, client, screen_rect):
        if self.clients and client is self.clients.current_client:
            client.place(
                screen_rect.x,
                screen_rect.y,
                screen_rect.width,
                screen_rect.height,
                0,
                None,
                margin=self.margin
            )
            client.unhide()
        else:
            client.hide()