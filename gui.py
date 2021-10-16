from tkinter import *

class Gui:

    def __init__(self, width, height):
        self.__matrix = [[0 for i in range(10)] for j in range(10)]
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.resizable(False, False)
        self.__canvas = Canvas(self.__root, height = height, width = width, bg="white")
    
    def __create_grid(self, event=None):
        w = self.__canvas.winfo_width()
        h = self.__canvas.winfo_height()
        self.__canvas.delete("grid_line")
        v_lines = len(self.__matrix[0]) # number of vertical lines
        h_lines = len(self.__matrix) # number of horizontal lines
        rect_width = self.__width / v_lines
        rect_height = self.__height / h_lines

        def onDrag(event):
            draggedId = event.widget.find_closest(event.x, event.y)[0]
            event.widget.itemconfigure(draggedId, fill="#000fff")
            for i in range(len(self.__matrix)):
                for j in range(len(self.__matrix[i])):
                    if draggedId in self.__matrix[i][j]:
                        self.__matrix[i][j][draggedId] = 1
                        
        y_pos = 0
        for i in range(len(self.__matrix)):
            x_pos = 0 # keep track of where we're at currently
            for j in range(len(self.__matrix[i])):
                rect_id = self.__canvas.create_rectangle(x_pos, y_pos, x_pos + rect_width, y_pos + rect_height, fill='#000000', outline='#fff')
                self.__canvas.tag_bind(rect_id, '<B1-Motion>', onDrag)
                self.__matrix[i][j] = {rect_id: 0}
                x_pos += rect_width
            y_pos += rect_height

                


    def setup(self, m_size=[10, 10]): # m_size : size of matrix [Rows x Columns]
        self.__matrix = [[0 for i in range(m_size[0])] for j in range(m_size[1])]
        self.__canvas.pack()
        self.__canvas.bind("<Configure>", self.__create_grid)
        self.__root.mainloop()
        

