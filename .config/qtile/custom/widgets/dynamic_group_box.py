from libqtile import widget
from libqtile.log_utils import logger

class DynamicGroupBox(widget.GroupBox):
    def calculate_workspace_symbol(self, group):
        for window in group.windows:
            logger.warning(window.name)

        if len(group.windows) == 0:
            return ""

        windows = " | ".join([window.name for window in group.windows])
        logger.warning(windows)
        if "Slack" in windows:
            return ""
        elif "Spotify" in windows:
            return ""
        elif "Visual Studio Code" in windows:
            return "﬏"
        elif "Google Chrome" in windows:
            return ""
        elif "Terminal" in windows:
            return ""

        return ""

    def draw(self):
        self.drawer.clear(self.background or self.bar.background)

        offset = self.margin_x
        for i, g in enumerate(self.groups):
            to_highlight = False
            is_block = (self.highlight_method == 'block')
            is_line = (self.highlight_method == 'line')

            bw = self.box_width([g])

            if self.group_has_urgent(g) and self.urgent_alert_method == "text":
                text_color = self.urgent_text
            elif g.windows:
                text_color = self.active
            else:
                text_color = self.inactive

            if g.screen:
                if self.highlight_method == 'text':
                    border = self.bar.background
                    text_color = self.this_current_screen_border
                else:
                    if self.block_highlight_text_color:
                        text_color = self.block_highlight_text_color
                    if self.bar.screen.group.name == g.name:
                        if self.qtile.current_screen == self.bar.screen:
                            border = self.this_current_screen_border
                            to_highlight = True
                        else:
                            border = self.this_screen_border
                    else:
                        if self.qtile.current_screen == g.screen:
                            border = self.other_current_screen_border
                        else:
                            border = self.other_screen_border
            elif self.group_has_urgent(g) and \
                    self.urgent_alert_method in ('border', 'block', 'line'):
                border = self.urgent_border
                if self.urgent_alert_method == 'block':
                    is_block = True
                elif self.urgent_alert_method == 'line':
                    is_line = True
            else:
                border = self.background or self.bar.background

            self.drawbox(
                offset,
                self.calculate_workspace_symbol(g),
                border,
                text_color,
                highlight_color=self.highlight_color,
                width=bw,
                rounded=self.rounded,
                block=is_block,
                line=is_line,
                highlighted=to_highlight
            )
            offset += bw + self.spacing
        self.drawer.draw(offsetx=self.offset, width=self.width)