pytest -v --alluredir=allure-results
allure generate --clean allure-results -o allure-report
java -DconfigFile=telegram_config.json -jar allure-notifications-4.2.1.jar
allure serve allure-report
rmdir /s /Q allure-results && rmdir /s /Q allure-report