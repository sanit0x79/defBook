import tkinter as tk
import json
from openai import OpenAI
import os
from tkinter import filedialog, messagebox

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
definitionCache = {}

def getDefinition(word, maxTokens=40):
    if word in definitionCache:
        return definitionCache[word]
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"Give a concise, one-sentence definition of '{word}'"}],
            max_tokens=maxTokens
        )
        definition = completion.choices[0].message.content
        definitionCache[word] = definition
        return definition
    except Exception as e:
        return f"Error fetching definition: {str(e)}"

def updateDefinitions():
    inputTextContent = inputText.get(1.0, tk.END).strip()
    lines = inputTextContent.splitlines()
    for line in lines:
        word = line.strip().lower()
        if word:
            if word in definitionCache:
                definition = definitionCache[word]
            else:
                definition = getDefinition(word)
            outputText.insert(tk.END, f"{word.capitalize()} = \"{definition}\"\n")

def saveNotebook():
    notebookData = {
        "inputWords": inputText.get(1.0, tk.END).strip().splitlines(),
        "definitions": definitionCache
    }
    filePath = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
    if filePath:
        with open(filePath, "w") as file:
            json.dump(notebookData, file)
        messagebox.showinfo("Save Notebook", "Notebook saved successfully.")

def loadNotebook():
    filePath = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if filePath:
        with open(filePath, "r") as file:
            notebookData = json.load(file)

        inputText.delete(1.0, tk.END)
        inputText.insert(tk.END, "\n".join(notebookData.get("inputWords", [])))

        global definitionCache
        definitionCache = notebookData.get("definitions", {})

        outputText.delete(1.0, tk.END)  # Clear output before loading new definitions
        for word, definition in definitionCache.items():
            outputText.insert(tk.END, f"{word.capitalize()} = \"{definition}\"\n")
        messagebox.showinfo("Load Notebook", "Notebook loaded successfully.")

root = tk.Tk()
root.title("DefBook GPT-4o-Mini")

inputLabel = tk.Label(root, text="Type words below (one per line):")
inputLabel.pack(pady=5)
inputText = tk.Text(root, height=10, width=40)
inputText.pack(pady=5)

fetchButton = tk.Button(root, text="Fetch Definitions", command=updateDefinitions)
fetchButton.pack(pady=5)

saveButton = tk.Button(root, text="Save Notebook", command=saveNotebook)
saveButton.pack(pady=5)

loadButton = tk.Button(root, text="Load Notebook", command=loadNotebook)
loadButton.pack(pady=5)

outputLabel = tk.Label(root, text="Definitions:")
outputLabel.pack(pady=5)
outputText = tk.Text(root, height=10, width=60, state="normal", wrap="word")
outputText.pack(pady=5)

root.geometry("700x600")
root.mainloop()
