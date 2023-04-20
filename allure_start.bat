pytest -s -v --alluredir reports
allure serve reports
rmdir /s reports
