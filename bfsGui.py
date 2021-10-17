from tkinter import *
from entryState import EntryState
from graph import Graph

class BFSGui:

    def __init__(self, width, height):
        self.__matrix = [[0 for i in range(10)] for j in range(10)]
        self.__stage = 0 # defines what operation should be executed with right mouse click. 0 = set starting node, 1 = set target node
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.resizable(False, False)
        self.__canvas = Canvas(self.__root, height = height, width = width, bg="white")
        self.startCallback = None
    
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
        

        def onRightClick(event):
            clickedId = event.widget.find_closest(event.x, event.y)[0]
            
            # loop through nodes to see if there already is a edge which should be removed
            shouldRemoveCurrentTarget = True
            shouldRemoveCurrentStart = True
            for i in range(len(self.__matrix)):
                for j in range(len(self.__matrix[i])):
                    if clickedId in self.__matrix[i][j]:
                        if self.__stage == 0:
                            if self.__matrix[i][j][clickedId] != EntryState.EMPTY:
                                shouldRemoveCurrentStart = False
                        elif self.__stage == 1:
                            if self.__matrix[i][j][clickedId] != EntryState.EMPTY:
                                shouldRemoveCurrentTarget = False
            
            # if a value should be removed, remove it 
            for i in range(len(self.__matrix)):
                for j in range(len(self.__matrix[i])):
                        for key in self.__matrix[i][j]:
                            if self.__stage == 0:
                                if self.__matrix[i][j][key] == EntryState.START and shouldRemoveCurrentStart == True:
                                    self.__matrix[i][j][key] = EntryState.EMPTY
                                    event.widget.itemconfigure(key, fill="#000000")
                            elif self.__stage == 1:
                                if self.__matrix[i][j][key] == EntryState.TARGET and shouldRemoveCurrentTarget == True:
                                    self.__matrix[i][j][key] = EntryState.EMPTY
                                    event.widget.itemconfigure(key, fill="#000000")

            # finally loop nodes to set the new start/target edge
            for i in range(len(self.__matrix)):
                for j in range(len(self.__matrix[i])):
                    if clickedId in self.__matrix[i][j]:
                        if self.__stage == 0:
                            if self.__matrix[i][j][clickedId] == EntryState.EMPTY:
                                self.__matrix[i][j][clickedId] = EntryState.START
                                event.widget.itemconfigure(clickedId, fill="#ff0000")
                                self.__stage = 1
                        elif self.__stage == 1:
                            if self.__matrix[i][j][clickedId] == EntryState.EMPTY:
                                self.__matrix[i][j][clickedId] = EntryState.TARGET
                                event.widget.itemconfigure(clickedId, fill="#00ff00")
                                self.__stage = 0
                        
        y_pos = 0
        for i in range(len(self.__matrix)):
            x_pos = 0 # keep track of where we're at currently
            for j in range(len(self.__matrix[i])):
                rect_id = self.__canvas.create_rectangle(x_pos, y_pos, x_pos + rect_width, y_pos + rect_height, fill='#000000', outline='#fff')
                self.__canvas.tag_bind(rect_id, '<B1-Motion>', onDrag)
                self.__canvas.tag_bind(rect_id, '<Button-3>', onRightClick)
                self.__matrix[i][j] = {rect_id: EntryState.EMPTY}
                x_pos += rect_width
            y_pos += rect_height

    def __start(self):
        # Todo: continue from here
        connections = []
        graph = Graph()
        print(graph)

    def setup(self, m_size=[10, 10]): # m_size : size of matrix [Rows x Columns]
        self.__matrix = [[0 for i in range(m_size[0])] for j in range(m_size[1])]
        self.__canvas.pack()
        self.__canvas.bind("<Configure>", self.__create_grid)
        menubar = Menu(self.__root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Start", command=self.__start)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.__root.destroy)
        menubar.add_cascade(label="File", menu=filemenu)
        self.__root.config(menu=menubar)
        self.__root.mainloop()
        
