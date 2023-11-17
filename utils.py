from datetime import datetime


def validate_email(email):
    return ('@' in email) and email.count('.') >= 1


def validate_phone(phone):
    return phone[0] == '+' and phone[1:].isnumeric() and len(phone) == 12


def validate_date(date):
    formats = ['%Y.%m.%d', '%d.%m.%Y']
    
    for date_format in formats:
        try:
            datetime.strptime(date, date_format)
            return True
        except ValueError:
            continue
    
    return False


def get_field_type(value):
    if validate_date(value):
        return "date"
    elif validate_phone(value):
        return "phone"
    elif validate_email(value):
        return "email"
    else:
        return "text"


def find_matching_template(templates, data):
    for template in templates:
        template_fields = set(template.keys())
        data_fields = set(data.keys())

        if template_fields.issubset(data_fields):
            match = True
            text_field_name = None

            for field, value in template.items():
                if data.get(field) != value:
                    match = False
                    break

                if get_field_type(value) == 'text':
                    text_field_name = value

            if match and text_field_name:
                return text_field_name

    return None