import requests


url = "http://127.0.0.1:5000/get_form"

data = {
    "info": "John's Bio",
    "email_box": "john@mail.ru",
    "birthday": "1991.01.01",
    "cell_number": "+70987654321"
}

data2 = {
    "information": "John's Bio",
    "email_box": "john@mail.ru",
    "birthday": "1991.01.01",
    "cell_number": "+70987654321"
}

data3 = {
    "name": "Form template name",
    "lead_email": "email@gmail.com",
    "phone_number": "+71234567890",
    "order_date": "21.05.2003"
}


response = requests.post(url, data=data)
response2 = requests.post(url, data=data2)
response3 = requests.post(url, data=data3)


print(response.text)
print(response2.text)
print(response3.text)
