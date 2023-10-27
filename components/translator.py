from objects.Board import Board


class Translator:
    def __init__(self, board: Board = None):
        self.x, self.y = None, None
        print("Translator has been initiated")
        self.board = board if board != None else 1
        self.turn = 'X'
    """
        mouse_x: x pos of mouse in the screen.
        mouse_y: y pos of mouse in the screen.
        params: window params for x and y translation. Basically the position of the cells

    """
    def translate(self,mouse_x,mouse_y, params = None):
        if self.board != None and params == None:
            # CELL 0 0
            if mouse_x < self.board.lines["TOP"][0] + int (self.board.board_options.line_w * self.board.board_options.scale_x) and \
               mouse_y < self.board.lines["TOP"][1] and mouse_x > self.board.lines["TOP"][0] and\
               mouse_y > self.board.lines["TOP"][1] - self.board.board_options.line_h *self.board.board_options.scale_y:                
                return [0,0]
            
            # CELL 0 1
            if mouse_x > self.board.lines["TOP"][0] + int (self.board.board_options.line_w * self.board.board_options.scale_x) and \
               mouse_x < self.board.lines["TOP"][0] + int (2*self.board.board_options.line_w * self.board.board_options.scale_x) and \
               mouse_y < self.board.lines["TOP"][1]  and\
               mouse_y > self.board.lines["TOP"][1] - self.board.board_options.line_h *self.board.board_options.scale_y :
                return [0,1]
            
            # CELL 0 2
            if mouse_x > self.board.lines["TOP"][0] + int (self.board.board_options.line_w * self.board.board_options.scale_x) and \
               mouse_x < self.board.lines["TOP"][0] + int (3*self.board.board_options.line_w * self.board.board_options.scale_x) and \
               mouse_y < self.board.lines["TOP"][1]  and\
               mouse_y > self.board.lines["TOP"][1] - self.board.board_options.line_h *self.board.board_options.scale_y :
                return [0,2]
            
            # CELL 1 0
            if mouse_x < self.board.lines["TOP"][0] + int (self.board.board_options.line_w * self.board.board_options.scale_x) and \
               mouse_y > self.board.lines["TOP"][1] and\
               mouse_x > self.board.lines["TOP"][0] and\
               mouse_y < self.board.lines["TOP"][1] + self.board.board_options.line_h *self.board.board_options.scale_y:               
                return [1,0]
            
            # CELL 2 0
            if mouse_x < self.board.lines["TOP"][0] + int (self.board.board_options.line_w * self.board.board_options.scale_x) and \
               mouse_y > self.board.lines["TOP"][1] + self.board.board_options.line_h *self.board.board_options.scale_y and\
               mouse_x > self.board.lines["TOP"][0] and\
               mouse_y < self.board.lines["TOP"][1] + 2 * self.board.board_options.line_h *self.board.board_options.scale_y:
                return [2,0]
            
            # CELL 1 1
            if mouse_x > self.board.lines["TOP"][0] + int (self.board.board_options.line_w * self.board.board_options.scale_x) and \
               mouse_x < self.board.lines["TOP"][0] + int (2*self.board.board_options.line_w * self.board.board_options.scale_x) and \
               mouse_y > self.board.lines["TOP"][1] and\
               mouse_y < self.board.lines["TOP"][1] + self.board.board_options.line_h *self.board.board_options.scale_y:
                return [1,1]
            
             # CELL 1 2
            if mouse_x > self.board.lines["TOP"][0] + int (self.board.board_options.line_w * self.board.board_options.scale_x) and \
               mouse_x < self.board.lines["TOP"][0] + int (3*self.board.board_options.line_w * self.board.board_options.scale_x) and \
               mouse_y > self.board.lines["TOP"][1] and\
               mouse_y < self.board.lines["TOP"][1] + self.board.board_options.line_h *self.board.board_options.scale_y:
                return [1,2]
            
             # CELL 2 1
            if mouse_x > self.board.lines["TOP"][0] + int (self.board.board_options.line_w * self.board.board_options.scale_x) and \
               mouse_x < self.board.lines["TOP"][0] + int (2*self.board.board_options.line_w * self.board.board_options.scale_x) and \
               mouse_y > self.board.lines["TOP"][1] + self.board.board_options.line_h *self.board.board_options.scale_y and\
               mouse_y < self.board.lines["TOP"][1] + 2 * self.board.board_options.line_h *self.board.board_options.scale_y:
                return [2,1]
            
             # CELL 2 2
            if mouse_x > self.board.lines["TOP"][0] + int (self.board.board_options.line_w * self.board.board_options.scale_x) and \
               mouse_x < self.board.lines["TOP"][0] + int (3*self.board.board_options.line_w * self.board.board_options.scale_x) and \
               mouse_y > self.board.lines["TOP"][1] + self.board.board_options.line_h *self.board.board_options.scale_y and\
               mouse_y < self.board.lines["TOP"][1] + 2 * self.board.board_options.line_h *self.board.board_options.scale_y:
                return [2,2]

        return None
    
   

    def translate_inverse_x(self, cell_y, cell_x):
        first_point_x = self.board.lines["TOP"][0] + self.board.board_options.line_w * self.board.board_options.scale_y * cell_x
        if cell_y == 0:
            first_point_y =  int(self.board.lines["TOP"][1] - self.board.board_options.line_h *self.board.board_options.scale_y)
        else:
            first_point_y = (int(self.board.lines["TOP"][1]) - self.board.board_options.line_h *self.board.board_options.scale_y ) + (self.board.board_options.line_h * self.board.board_options.scale_y * (cell_y))

        second_point_x = self.board.lines["TOP"][0] + int (self.board.board_options.line_w * self.board.board_options.scale_x * (cell_x + 1))
        second_point_y = self.board.lines["TOP"][1] + int (self.board.board_options.line_h * self.board.board_options.scale_y * (cell_y))

        return ([
            first_point_x,first_point_y
        ], [
            second_point_x, second_point_y
        ])

      
    
    def translate_inverse_o(self, cell_x, cell_y):
        center_cell = self.get_cell_center(cell_x, cell_y)
        return center_cell,  int(int(self.board.board_options.line_w * self.board.board_options.scale_x * 0.7)/2)

 
    def get_cell_center (self, cell_y, cell_x):
        factor_x = cell_x +1
        factor_y = cell_y + 1

        center_x = int(((self.board.lines["TOP"][0] +  int (self.board.board_options.line_w * self.board.board_options.scale_x * cell_x) ) + (self.board.lines["TOP"][0] + int (self.board.board_options.line_w * self.board.board_options.scale_x * factor_x))) / 2)
        if cell_y == 0:
            center_y = int(((self.board.lines["TOP"][1]+ (self.board.lines["TOP"][1] - self.board.board_options.line_h *self.board.board_options.scale_y))/2))
        else:
            point_y = self.board.lines["TOP"][1] - self.board.board_options.line_h *self.board.board_options.scale_y
            center_y = int(((point_y + (self.board.board_options.line_h *self.board.board_options.scale_y * cell_y))+ (point_y + self.board.board_options.line_h *self.board.board_options.scale_y * factor_y))/2)

        return (center_x, center_y)
    

    def get_coors_cell(self, cell_beg, cell_end):
        cell_y_beg = cell_beg[1]
        cell_x_beg = cell_beg[0]

        cell_x_end = cell_end[0]
        cell_y_end = cell_end[1]

        cell_beg = self.get_cell_center(cell_x_beg, cell_y_beg)
        cell_end = self.get_cell_center(cell_x_end, cell_y_end)

        return cell_beg, cell_end
    
    

    