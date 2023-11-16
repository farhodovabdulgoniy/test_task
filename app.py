from flask import (
    Flask,
    request,
    jsonify,
)
from utils import (
    find_matching_template,
    get_field_type,
)
from tinydb import TinyDB


app = Flask(__name__)
DB = TinyDB('database.json')


@app.route('/get_form', methods=['POST'])
def get_form():
    data = request.form.to_dict()

    templates = DB.table('form_templates').all()
    template_name = find_matching_template(templates, data)

    if template_name:
        return jsonify({"template_name": template_name})
    else:
        field_types = {field: get_field_type(data[field]) for field in data}
        return jsonify(field_types)


if __name__ == '__main__':
    app.run(debug=True)
