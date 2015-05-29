host_url = 'http://5.45.123.141:8080'
site_mapping = {
    "login": {
        "url": host_url + "/index.xhtml",
        "username": "//form[@class='registration-form']//input[@id='user_name']",
        "password": "//form[@class='registration-form']//input[@name='password']",
        "sign_in_btn": "//form[@class='registration-form']//input[@type='submit']",
    },
}