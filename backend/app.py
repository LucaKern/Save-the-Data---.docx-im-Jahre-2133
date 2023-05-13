from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import re
import shutil
import zipfile
import xml.etree.ElementTree as ET
from io import StringIO
from pathlib import Path
from pprint import pprint
from bs4 import BeautifulSoup


app = Flask(__name__)
CORS(app)


# dummy function for now
def convert_to_safe_date(file_path):
    # changes = ['<data 1>', '<data 2>']
    # meta_data = ['<meta 1>', '<meta 2>']
    # return changes, meta_data
    temp_directory = 'temp'
    os.mkdir(temp_directory)
    doc_zip = zipfile.ZipFile(file_path)
    new_zip_name = os.path.basename(file_path).replace('.docx', '')
    pattern = re.compile(r'<w:instrText[^>]*>[^D]*(DATE|TIME)[^<]*</w:instrText>')
    replacement = '<w:t>DeepReturn</w:t>'

    doc_zip.extractall(temp_directory)

    replace_count = 0

    for root, _, files in os.walk(temp_directory, topdown=False):
        for name in files:
            filename = os.path.join(root, name)

            if filename.endswith('.xml'):
                with open(filename, 'r') as file:
                    xml_string = file.read()
                # print(xml_string)
                matches = re.findall(pattern, xml_string)

                replace_count += len(matches)
                replaced_string = re.sub(pattern, replacement, xml_string)

                with open(filename, 'w') as file:
                    file.write(replaced_string)

    converted_files_directory = './converted_files'
    if not os.path.exists(converted_files_directory):
        os.mkdir(converted_files_directory)

    shutil.make_archive(new_zip_name, 'zip', temp_directory)
    new_docx_path = os.path.join(converted_files_directory, f'{new_zip_name}.docx')
    os.rename(f'{new_zip_name}.zip', new_docx_path)
    shutil.rmtree(temp_directory)
    return replace_count, new_docx_path


@app.route('/convert', methods=['POST'])
def convert_route():
    print('in da route')
    data = request.get_json()
    file_path = data.get('file_path')
    if not file_path:
        return jsonify({"error": "No file path provided"}), 400

    try:
        changes, new_file_path = convert_to_safe_date(file_path)
        return jsonify({"message": "File successfully converted", "changes": changes, "new_file_path": new_file_path}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=8080)

# how to test this route:
# curl -X POST -H "Content-Type: application/json" -d '{"file_path":"/path/to/your/file"}' http://localhost:8080/convert
