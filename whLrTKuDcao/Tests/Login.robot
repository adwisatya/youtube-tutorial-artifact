*** Settings ***
Resource	../Resources/Web.robot
Test Setup	Prepare environment

*** Test Cases ***
Halaman login harus bisa diakses
	[Documentation]		Halaman login bisa diakses denga valid ssl
	[Tags]	Login
	Web.Masuk dan cek login page

Halaman login harus bisa diakses dup
        [Documentation]         Halaman login bisa diakses denga valid ssl
        [Tags]  LoginDUp
        Web.Masuk dan cek login page
