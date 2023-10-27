from options.default import WindowDefault as WD


class BoardOptions:
    def __init__(self, win_w, win_h):
        self.win_w, self.win_h = win_w, win_h
        self.line_w = int(0.6 * self.win_w)
        self.line_h = int(0.6 * self.win_h)
        self.scale_x = 0.33
        self.scale_y = 0.33

    def build_lines(self):
        if self.win_w ==WD.WIDTH and self.win_h == WD.HEIGHT:
           # lines = {
           #     "TOP":(200,250),
           #     "DOWN":(200,350),
           #     "LEFT": (300,150),
           #     "RIGHT": (400, 150)
           # }
            lines = {
                "TOP":(int(self.scale_x * self.line_w),int(2 * self.scale_y * self.line_h)),
                "DOWN":(int(self.scale_x * self.line_w),int(3 * self.scale_y * self.line_h)),
                "LEFT": (int(2 *self.scale_x * self.line_w), int(self.scale_y * self.line_h)),
                "RIGHT": (int(3* self.scale_x * self.line_w), int(self.scale_y * self.line_h))
            }

            return lines