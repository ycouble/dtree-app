import app_config
import io
import os

from datetime import datetime
from werkzeug.utils import secure_filename
from zipfile import ZipFile, is_zipfile

from services.exceptions import FileUploadError


RESOURCE_DIR = "resources/"

def is_allowed(filename, allowed_extensions=app_config.ALLOWED_EXTENSIONS):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

def open_xmind_file(xmind_file):
    if not xmind_file or not is_allowed(xmind_file.filename, ['xmind']):
        raise FileUploadError("Not valid xmind file")
    xmind_file_as_bytes = io.BytesIO(xmind_file.read())
    xmind_zipfile = ZipFile(xmind_file_as_bytes)
    name_list = xmind_zipfile.namelist()
    if "content.json" not in name_list:
        raise FileUploadError("No content.json file found in xmind file")
    for file_name in name_list:
        if file_name[-1] != '/' and not is_allowed(file_name):
            raise FileUploadError(f"{file_name} is not allowed to be upload")
    return xmind_zipfile, xmind_file_as_bytes

def get_secure_filename(filename):
    return secure_filename(filename)

def create_new_path():
    # TODO: check unique path
    new_filename = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}/"
    path = os.path.join("data", new_filename)
    return path

def save_xmind_files(xmind_file_as_bytes, dtree):
    try:
        os.mkdir(dtree.dir_name)
    except OSError:
        raise FileUploadError(f"Directory creation {dtree.dir_name} failed")

    with open(dtree.dir_name + dtree.filename, "wb") as outfile:
        outfile.write(xmind_file_as_bytes.getbuffer())
    
    xmind_zipfile = dtree.input_zip
    name_list = xmind_zipfile.namelist()
    for file_name in name_list:
        if RESOURCE_DIR in file_name and RESOURCE_DIR != file_name:
            xmind_zipfile.extract(file_name, path=dtree.dir_name)
