*** Settings ***
Library		SeleniumLibrary

*** Keywords ***

Prepare environment
	Create Webdriver	Chrome
Masuk dan cek login page
	go to	https://mail.yahoo.com
	Wait Until Page Contains	Berikutnya	10s
