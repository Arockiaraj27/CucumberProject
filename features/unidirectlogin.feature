Feature: Uni login
    Scenario: Login to uni CRM with valid Parameters
    Given I launch chrome browser
    When I open the uni CRM Signin page
    And Enter the username "admission@unidirect.org" and password "london2020"
    And Click the login button
    Then user must login into the dashboard page successfully


  Scenario Outline: Login to uni CRM with valid Parameters
    Given I launch chrome browser
    When I open the uni CRM Signin page
    And Enter the username "<user>" and password "<password>"
    And Click the login button
    Then user must login into the dashboard page successfully
    Examples:
      | user | password |
      |arockia.gaipp@gmail.com | 12345 |
      |rioraj@gmail.com | 12345 |
      |gokul.gaipp@gmail.com | 12345 |
      |revathi@gmail.com | 12345 |
      |admission@unidirect.org | london2020 |
