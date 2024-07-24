from flask import Flask, request, render_template
from feature import read_pdf_files

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def excel_filters():
    if request.method == "POST":
        folder_path = request.form.get("path")
        output_file = read_pdf_files(folder_path)
        return f"Data written to {output_file}  successfully. "
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
