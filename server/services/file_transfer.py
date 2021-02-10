import app_config
import io
import os

from datetime import datetime
from werkzeug.utils import secure_filename
from zipfile import ZipFile, is_zipfile


def is_allowed(filename, allowed_extensions=app_config.ALLOWED_EXTENSIONS):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

def save_file(xmind_file): #TODO: Exceptions
    if xmind_file and is_allowed(xmind_file.filename, ['xmind']):
        xmind_file_as_bytes = io.BytesIO(xmind_file.read())
        input_xmind_zipfile = ZipFile(xmind_file_as_bytes)
        name_list = input_xmind_zipfile.namelist()
        if "content.json" not in name_list:
            return True
        for file_name in name_list:
            if file_name[-1] != '/' and not is_allowed(file_name):
                return True
        new_filename = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.xmind"
        path = os.path.join("data", new_filename)
        with open(path, "wb") as outfile:
            outfile.write(xmind_file_as_bytes.getbuffer())
    else:
        return True
    return False