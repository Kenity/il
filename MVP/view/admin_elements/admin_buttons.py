import customtkinter as ctk


class Buttons(ctk.CTk):
    def __init__(self, frames):
        self.frames = frames

        self.students_btn = ctk.CTkButton(self.frames.navigate_frame, text = 'Студенты')
        self.students_btn.pack(padx = 5, pady = 3)

        self.teachers_btn = ctk.CTkButton(self.frames.navigate_frame, text = 'Преподаватели')
        self.teachers_btn.pack(padx = 5, pady = 3)

        self.course_btn = ctk.CTkButton(self.frames.navigate_frame, text = 'Курсы')
        self.course_btn.pack(padx = 5, pady = 3)

        self.record_btn = ctk.CTkButton(self.frames.navigate_frame, text = 'Записи')
        self.record_btn.pack(padx = 5, pady = 3)

        self.report_btn = ctk.CTkButton(self.frames.navigate_frame, text = 'Отчёты')
        self.report_btn.pack(padx = 5, pady = 3)

        self.close_btn = ctk.CTkButton(self.frames.navigate_frame, text = 'Выйти', command = lambda: self.on_close())
        self.close_btn.pack(side = 'bottom', pady = 3)

    def on_close(self):
        self.frames.main_frame.quit()
