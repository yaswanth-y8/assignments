from flask import Flask, request, render_template_string

app = Flask(__name__)
DATA_FILE = "today_data.txt"


@app.route("/updatefortoday", methods=['GET', 'POST'])  
def update_for_today():
    if request.method == 'POST':
        data = request.form.get('data')
        if data:
            with open(DATA_FILE, 'a') as f:
                f.write(data + '\n')

    
    with open(DATA_FILE, 'r') as f:
            content = f.read()
    
    
    html = '''
    <h2>Update for Today</h2>
    <form method="post">
        <textarea name="data" rows="4" cols="50" placeholder=""></textarea><br><br>
        <input type="submit" value="submit">
    </form>
    <hr>
    <h3>Previous Data</h3>
    <pre>{{ content }}</pre>
    '''
    return render_template_string(html, content=content)


@app.route("/share", methods=['GET'])
def share():
    
    with open(DATA_FILE, 'r') as f:
        content = f.read()
    

    html = '''
    <h2>Shared Notes</h2>
    <pre>{{ content }}</pre>
    '''
    return render_template_string(html, content=content)


@app.route("/clearnotepadtxt", methods=['GET'])
def clear_notepad_txt():
    open(DATA_FILE, 'w').close()
    return "Notepad text cleared."


if __name__ == "__main__":
    app.run(debug=True)
