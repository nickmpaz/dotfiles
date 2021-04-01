from libqtile.layout.base import _SimpleLayoutBase


class MarginMax(_SimpleLayoutBase):
    """Maximized layout

    A simple layout that only displays one window at a time, filling the
    screen_rect. This is suitable for use on laptops and other devices with
    small screens. Conceptually, the windows are managed as a stack, with
    commands to switch to next and previous windows in the stack.
    """

    defaults = [("name", "marginmax", "Name of this layout.")]

    def __init__(self, margin=0, **config):
        super().__init__(**config)
        self.add_defaults(MarginMax.defaults)
        self.margin = margin

    def clone(self, group):
        return super().clone(group)

    def add(self, client):
        return super().add(client, 1)

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

    cmd_previous = _SimpleLayoutBase.previous
    cmd_next = _SimpleLayoutBase.next

    cmd_up = cmd_previous
    cmd_down = cmd_next