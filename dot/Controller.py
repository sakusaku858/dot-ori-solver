from tkinter import messagebox
import time


class CounterController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.set_controller(self)

    def execute(self):
        # 非連結の場合
        if not self.model.is_connect():
            if self.model.circuitLength != 32:
                messagebox.showwarning("Alert", "Circuit length must be 32.")
                return

            # 計算時間を計測
            start_time = time.time()

            self.model.execute_non_connect()

            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"処理時間 (time.time()): {elapsed_time:.4f}秒")
            return

        # 連結の場合
        if self.model.circuitLength == 32:
            speed = self.view.speed_scale.get()
            self.model.execute(speed)
        else:
            messagebox.showwarning("Alert", "Circuit length must be 32.")

    def clear(self):
        self.model.clear()
        self.view.clear()
        self.view.update_border(0)
        self.view.update_circuit(0)

    def square_click_action(self, row, col):
        # new_valueって何？
        new_value = self.model.switch_dot(row, col)
        self.view.update_dot(new_value, row, col)
        border = self.model.count_border()
        self.view.update_border(border)
        loopLength = self.model.calcLoopLength()
        self.view.update_circuit(loopLength)
