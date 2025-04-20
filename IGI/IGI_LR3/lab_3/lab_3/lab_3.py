import tkinter as tk
from tkinter import filedialog, scrolledtext
import tokenize
from collections import Counter
import io

def analyze_code(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()
    
    tokens = tokenize.tokenize(io.BytesIO(code.encode('utf-8')).readline)
    operators = set()
    operands = set()
    operator_count = Counter()
    operand_count = Counter()
    
    control_keywords = {"if", "else", "elif", "for", "while", "def", "return", "try", "except", "finally", "class", "with"}
    
    for token in tokens:
        if token.type == tokenize.OP or token.string in {':', '(', ')', '[', ']', '{', '}', ',', '=', '+=', '-=', '*=', '/=', '%=', '**', '//'}:
            operators.add(token.string)
            operator_count[token.string] += 1
        elif token.type == tokenize.NAME:
            if token.string in control_keywords:
                operators.add(token.string)
                operator_count[token.string] += 1
            else:
                operands.add(token.string)
                operand_count[token.string] += 1
        elif token.type in {tokenize.NUMBER, tokenize.STRING}:
            operands.add(token.string)
            operand_count[token.string] += 1
    
    n1 = len(operators)
    n2 = len(operands)
    N1 = sum(operator_count.values())
    N2 = sum(operand_count.values())
    
    return n1, n2, N1, N2, operator_count, operand_count

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if file_path:
        n1, n2, N1, N2, operator_count, operand_count = analyze_code(file_path)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"n1 (Unique Operators): {n1}\n")
        result_text.insert(tk.END, f"n2 (Unique Operands): {n2}\n")
        result_text.insert(tk.END, f"N1 (Total Operators): {N1}\n")
        result_text.insert(tk.END, f"N2 (Total Operands): {N2}\n\n")
        result_text.insert(tk.END, "Operator Frequencies:\n")
        for op, count in operator_count.items():
            result_text.insert(tk.END, f"{op}: {count}\n")
        result_text.insert(tk.END, "\nOperand Frequencies:\n")
        for op, count in operand_count.items():
            result_text.insert(tk.END, f"{op}: {count}\n")

# Tkinter GUI
root = tk.Tk()
root.title("Python Code Analyzer")
root.geometry("500x600")

tk.Button(root, text="Open Python File", command=open_file).pack(pady=10)
result_text = scrolledtext.ScrolledText(root, width=60, height=30)
result_text.pack()

root.mainloop()
