import os
from flask import request, render_template, Flask, redirect, url_for
from Etract_data import load_data, save_data, check_and_create_file_in_directory
from translate_en_to_vi import translate_en_to_vi
from datetime import datetime

app = Flask(__name__, template_folder=os.path.join('App', 'templates'), static_folder=os.path.join('App', 'static'))

check_and_create_file_in_directory("input_llm.txt")
check_and_create_file_in_directory("output_llm.txt")
check_and_create_file_in_directory("database.txt")

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text_input = request.form["text"]
        text_inputs = load_data("input_llm.txt")
        text_outputs = load_data("output_llm.txt")
        
        if text_input:
            text_input = text_input.replace("\n", "")
            text_input = " ".join(text_input.split())
            text_inputs.append(text_input)
            text_outputs.append(translate_en_to_vi(text_input))
            save_data("input_llm.txt", text_inputs)
            save_data("output_llm.txt", text_outputs)
            return render_template("translated.html", original_text = text_input, translate_text = text_outputs[-1])
        
    return render_template("index.html")

@app.route('/translated', methods=['GET', 'POST'])
def translated():
    database = load_data("database.txt")
    database.append(str(len(load_data("input_llm.txt"))))
    database.append(str(datetime.now()))
    database.append(request.form['original_text'].replace("\n", ""))
    database.append(request.form['translate_text'].replace("\n", ""))
    database.append(str(int(request.form.get('rating', 0))))
    save_data("database.txt", database)
    
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)

