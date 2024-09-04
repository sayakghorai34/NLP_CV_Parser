import tkinter as tk
import tkinter.ttk as ttk
from pdfminer.high_level import extract_text
from extractors.name import extract_names
from extractors.education import extract_education
from extractors.phone import extract_phone_number
from extractors.email import extract_emails
from extractors.skills import extract_skills

def extract_text_from_pdf(pdf_path):
    txt = extract_text(pdf_path)
    if txt:
        return txt.replace('\t', ' ')
    return None

def process(initial_filepath, root):
    from tkinter import filedialog as fd

    filepath = fd.askopenfilename(initialdir=initial_filepath, title='Select file', filetypes=(('pdf files', '*.pdf'),))
    
    text = extract_text_from_pdf(filepath)
    name_information = extract_names(text)
    education_information = extract_education(text)
    phone = extract_phone_number(text)
    email = extract_emails(text)
    skills = extract_skills(text)

    result_window = tk.Tk()
    result_window.title("Extracted Information")
    result_window.geometry("600x350")

    tk.Label(result_window, text="Extracted Information", font=("Arial", 20)).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(result_window, text="Name \t: ").grid(row=1, column=0, sticky="w", padx=10)
    tk.Label(result_window, text=", ".join(name_information) if name_information else "N/A", wraplength=450).grid(row=1, column=1, sticky="w", padx=10)

    tk.Label(result_window, text="Education\t: ").grid(row=2, column=0, sticky="w", padx=10)
    tk.Label(result_window, text=", ".join(education_information) if education_information else "N/A", wraplength=450).grid(row=2, column=1, sticky="w", padx=10)

    tk.Label(result_window, text="Phone\t: ").grid(row=3, column=0, sticky="w", padx=10)
    tk.Label(result_window, text=phone if phone else "N/A", wraplength=450).grid(row=3, column=1, sticky="w", padx=10)

    tk.Label(result_window, text="Email\t: ").grid(row=4, column=0, sticky="w", padx=10)
    tk.Label(result_window, text=", ".join(email) if email else "N/A", wraplength=450).grid(row=4, column=1, sticky="w", padx=10)

    tk.Label(result_window, text="Skills\t: ").grid(row=5, column=0, sticky="w", padx=10)
    tk.Label(result_window, text=", ".join(skills) if skills else "N/A", wraplength=450).grid(row=5, column=1, sticky="w", padx=10)

if __name__ == '__main__':
    width = 600
    height = 300

    root = tk.Tk()
    root.title("CV Parser")
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

    button = ttk.Button(root, text='Click to Open CV File')
    button.config(command=lambda filepath='.': process(filepath, root))
    button.pack(fill=tk.X)

    root.mainloop()