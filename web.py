
from flask import Flask,render_template,request,redirect
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
currentDir = os.path.dirname(__file__)
@app.route('/home')
def meesho():
    from main import meeshoPdf
    # meeshoPdf("test.xlsx","Files")
    return render_template('dragDrop.html')


@app.route('/meesho', methods=["GET", "POST"])
def upload_image():
    
    if request.method == "POST":
        image = request.files['file']
        if image.filename == '':
            print(image)
            return redirect(request.url)

        filename = secure_filename(image.filename)
        basedir = os.path.join(currentDir, filename)
        image.save(basedir)
        print(basedir)
        # remove(basedir)
        from main import to_excel,meeshoPdf
        to_excel(basedir)
        folderloc = request.form['loc']
        print(folderloc,"--")
        meeshoPdf("output.xlsx",folderloc)
       
       
        return redirect('/meesho')
    
    return render_template('chooseFile.html')

if __name__ == "__main__":
    app.run(debug=True,port = 7900)