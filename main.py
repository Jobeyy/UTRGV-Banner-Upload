import customtkinter as tk
from customtkinter import filedialog
from helper import *
from CTkMessagebox import CTkMessagebox
import os

tk.set_appearance_mode("System")
tk.set_default_color_theme("blue")
class CSVUploader(tk.CTk):
      width = 900
      height = 600
      
      def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("UTRGV UREC Banner Fix")
        self.geometry(f'{self.width}x{self.height}')
        
        
        self.header = tk.CTkLabel(self, text="UTRGV UREC Banner Fix", font=tk.CTkFont(size=50, weight='bold'))
        self.header.place(relx= 0.5, rely=0.3, anchor=tk.CENTER)
        self.text =tk.CTkLabel(self, text= "Please Choose A CSV File", font=tk.CTkFont(size=15, weight="bold"))
        self.text.place(relx = 0.5, rely = 0.4, anchor= tk.CENTER)
        self.button = tk.CTkButton(self, height= 50, text="Choose CSV File", command=self.select_file)
        self.button.place(relx = 0.5, rely = 0.5, anchor= tk.CENTER)
        self.creator = tk.CTkLabel(self, text="Created by Jobey Farias") 
        self.creator.place(relx=0.99, rely=0.99, anchor=tk.SE)


      def select_file(self):
        try:        
          file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])            
          with open(file_path, "r") as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

            dataset = remove_2nd_address(rows)
            dataset = check_state(rows)
            dataset = check_phone_number(rows)
            dataset = check_zip_code(rows)
            self.prompt_save_location(dataset)
        except FileNotFoundError:
          CTkMessagebox(title="Error", message="File Cannot Be Found Or File Not Chosen.", icon="cancel")

      def prompt_save_location(self, dataset):
        CTkMessagebox(title="Information", message="Please select a directory to save the split CSV files.", icon="info")
        self.save_files(dataset)

      def save_files(self, dataset):
        try:
            directory = filedialog.askdirectory()
            if not directory:
                return 
            chunk_size = 5000
            total_rows = len(dataset)
            for i in range(0, total_rows, chunk_size):
                chunk = dataset[i:i + chunk_size]
                if len(chunk) < chunk_size and i > 0:
                    break
                filename = os.path.join(directory, f"file_part_{i // chunk_size + 1}.csv")
                with open(filename, "w", newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(chunk)
            CTkMessagebox(title="Success", message="Files have been saved successfully.", icon="check")
        except Exception as e:
            CTkMessagebox(title="Error", message=str(e), icon="cancel")

if __name__ == "__main__":
    app = CSVUploader()
    app.mainloop()
