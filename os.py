import tkinter as tk
from tkinter import ttk, messagebox

class BankersAlgorithmApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Banker's Algorithm")
        self.style = ttk.Style()
        self.style.theme_use('clam')  
        self.processes = []
        self.available = []
        self.max_resources = []
        self.allocated = []

        self.create_widgets()

    def create_widgets(self):
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.grid(row=0, column=0)

        ttk.Label(self.main_frame, text="Banker's Algorithm", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(self.main_frame, text="Enter the number of processes:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.num_processes_entry = ttk.Entry(self.main_frame)
        self.num_processes_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.main_frame, text="Enter the number of resources:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.num_resources_entry = ttk.Entry(self.main_frame)
        self.num_resources_entry.grid(row=2, column=1, padx=5, pady=5)

        submit_button = ttk.Button(self.main_frame, text="Submit", command=self.submit_counts)
        submit_button.grid(row=3, column=0, columnspan=2, pady=10)

    def submit_counts(self):
        num_processes = int(self.num_processes_entry.get())
        num_resources = int(self.num_resources_entry.get())

        self.processes = [i for i in range(num_processes)]

        available_frame = ttk.LabelFrame(self.main_frame, text="Available Resources", padding=(10, 5))
        available_frame.grid(row=4, column=0, padx=5, pady=5, columnspan=2)

        for i in range(num_resources):
            ttk.Label(available_frame, text=f"Resource {i + 1}:").grid(row=i, column=0, padx=5, pady=5)
            entry = ttk.Entry(available_frame)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.available.append(entry)

        for i in range(num_processes):
            max_frame = ttk.LabelFrame(self.main_frame, text=f"Max Resources for Process {i}", padding=(10, 5))
            max_frame.grid(row=5 + i, column=0, padx=5, pady=5, columnspan=2)

            for j in range(num_resources):
                ttk.Label(max_frame, text=f"Resource {j + 1}:").grid(row=j, column=0, padx=5, pady=5)
                entry = ttk.Entry(max_frame)
                entry.grid(row=j, column=1, padx=5, pady=5)
                self.max_resources.append(entry)

            allocated_frame = ttk.LabelFrame(self.main_frame, text=f"Allocated Resources for Process {i}", padding=(10, 5))
            allocated_frame.grid(row=5 + num_processes + i, column=0, padx=5, pady=5, columnspan=2)

            for j in range(num_resources):
                ttk.Label(allocated_frame, text=f"Resource {j + 1}:").grid(row=j, column=0, padx=5, pady=5)
                entry = ttk.Entry(allocated_frame)
                entry.grid(row=j, column=1, padx=5, pady=5)
                self.allocated.append(entry)

        banker_button = ttk.Button(self.main_frame, text="Run Banker's Algorithm", command=self.run_bankers_algorithm)
        banker_button.grid(row=6 + 2 * num_processes, columnspan=2, pady=10)

    def run_bankers_algorithm(self):
        num_processes = len(self.processes)
        num_resources = len(self.available)

        # Extract input values
        available = [int(entry.get()) for entry in self.available]
        max_resources = [[int(entry.get()) for entry in self.max_resources[i*num_resources:(i+1)*num_resources]] for i in range(num_processes)]
        allocated = [[int(entry.get()) for entry in self.allocated[i*num_resources:(i+1)*num_resources]] for i in range(num_processes)]

        # Banker's Algorithm logic
        work = available[:]
        finish = [False] * num_processes
        seq = []

        for _ in range(num_processes):
            for i in range(num_processes):
                if not finish[i] and all(max_resources[i][j] - allocated[i][j] <= work[j] for j in range(num_resources)):
                    for j in range(num_resources):
                        work[j] += allocated[i][j]
                    finish[i] = True
                    seq.append(i)
                    break

        if all(finish):
            messagebox.showinfo("Result", f"Safe Sequence: {seq}")
        else:
            messagebox.showerror("Error", "Unsafe state!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankersAlgorithmApp(root)
    root.mainloop()