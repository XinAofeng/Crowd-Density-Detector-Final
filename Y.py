from flask import Flask
from body_detect import get_image, chack_image
from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
import os
import time
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/detect')
def detecty():
    get_image()
    chack_image()

@app.route("/frame", methods=['POST'])
def get_frame():
    start_time = time.time()
    upload_file = request.files['file']
    old_file_name = upload_file.filename
    if upload_file:
        file_path = os.path.join('static\\uploads\\test1.jpg')
        upload_file.save(file_path)
        print("success")
        print('file saved to %s' % file_path)
        duration = time.time() - start_time
        print('duration:[%.0fms]' % (duration*1000))
        return 'success'
    else:
        return 'failed'

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(basepath, 'static\\uploads',secure_filename(f.filename))  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        return redirect(url_for('upload'))
    return render_template('upload.html')
    chack_image()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)