pytest -s -v --alluredir=allure-results
allure serve /b allure-results
rmdir /s /Q allure-results