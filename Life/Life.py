import tkinter as tk
from .LifeC import GameOfLife

def StartLife(width, height, cell_size):
    root = tk.Tk()
    gui = LifeGUI(root, width=width, height=height, cell_size=cell_size)
    root.mainloop()

class LifeGUI:
    def __init__(self, master, width=10, height=10, cell_size=30):
        self.master = master
        self.cell_size = cell_size
        self.game = GameOfLife(width, height)
        self.is_running = False  # Флаг для отслеживания состояния игры
        self.canvas = tk.Canvas(master, width=width * cell_size, height=height * cell_size)
        self.canvas.pack()
        
        self.canvas.bind("<Button-1>", self.toggle_cell)
        
        # Кнопки управления
        self.start_button = tk.Button(master, text="Запустить", command=self.start)
        self.start_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(master, text="Остановить", command=self.stop)
        self.stop_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(master, text="Сброс", command=self.reset)
        self.reset_button.pack(side=tk.LEFT)

    def toggle_cell(self, event):
        x = event.x // self.cell_size
        y = event.y // self.cell_size
        if 0 <= x < self.game.width and 0 <= y < self.game.height:
            current_state = self.game.grid[y, x]
            self.game.set_cell(x, y, 1 - current_state)
            self.draw()

    def update(self):
        if self.is_running:
            self.game.update()
            self.draw()
            self.master.after(100, self.update)

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.update()

    def stop(self):
        self.is_running = False

    def reset(self):
        self.game.reset()
        self.draw()

    def draw(self):
        self.canvas.delete("all")
        for y in range(self.game.height):
            for x in range(self.game.width):
                if self.game.grid[y, x] == 1:
                    self.canvas.create_rectangle(
                        x * self.cell_size,
                        y * self.cell_size,
                        (x + 1) * self.cell_size,
                        (y + 1) * self.cell_size,
                        fill="black"
                    )

