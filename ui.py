import tkinter as tk
import utils

from generate_ppt import generate_ppt

settings = utils.get_settings()
config = utils.get_config()
api_options = utils.get_api_list()
model_options = ["Select an API first"]


def set_model_options(api_name):
    models = utils.get_model_list_from_api(api_name)
    model_selection.set("Select a model")

    model_dropdown['menu'].delete(0, 'end')
    for model in models:
        model_dropdown['menu'].add_command(
            label=model,
            command=lambda value=model: model_selection.set(value)
        )


def save_api_key():
    api_key = api_key_entry.get().strip()
    utils.save_config(api_key)


def generate_ppt_and_set_result():
    result = generate_ppt(prompt_entry.get(), api_selection.get(), model_selection.get(), number_of_slides_entry.get())
    result_label.config(text=result)


window = tk.Tk()

window.title("Presentation Generator")
window.configure(padx=20, pady=20)

api_key_label = tk.Label(window, text="API Key:")
api_key_entry = tk.Entry(window)

prompt_label = tk.Label(window, text="Prompt: (write me a PPT presentation about...)")
prompt_entry = tk.Entry(window)

api_selection = tk.StringVar()
api_selection.set("Select an option")
api_label = tk.Label(window, text="Select generation API: ")
api_dropdown = tk.OptionMenu(window, api_selection, *api_options, command=set_model_options)

model_selection = tk.StringVar()
model_selection.set("Select an API first.")
model_label = tk.Label(window, text="Select script generation model: ")
model_dropdown = tk.OptionMenu(window, model_selection, *model_options)

number_of_slides_label = tk.Label(window, text="Number of slides: ")
number_of_slides_entry = tk.Entry(window)

generate_button = tk.Button(window, text="Submit", command=generate_ppt_and_set_result)

save_api_key_button = tk.Button(window, text="Save API Key", command=save_api_key)

result_label = tk.Label(window, text="")

if config.get('api_key'):
    api_key_entry.insert(0, config['api_key'])

api_key_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
api_key_entry.grid(row=0, column=1, padx=5, pady=5)

save_api_key_button.grid(row=0, column=2, padx=5, pady=5)

prompt_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
prompt_entry.grid(row=1, column=1, padx=5, pady=5)

api_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
api_dropdown.grid(row=2, column=1, padx=5, pady=5)

model_label.grid(row=3, column=0, sticky="w", padx=5, pady=5)
model_dropdown.grid(row=3, column=1, padx=5, pady=5)

number_of_slides_label.grid(row=4, column=0, sticky="w", padx=5, pady=5)
number_of_slides_entry.grid(row=4, column=1, padx=5, pady=5)

generate_button.grid(row=5, column=0, columnspan=2, pady=10)
result_label.grid(row=6, column=0, columnspan=2, pady=5)

window.mainloop()
