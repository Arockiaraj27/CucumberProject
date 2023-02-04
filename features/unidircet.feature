Feature: Uni login
    Scenario: Login to uni CRM with valid Parameters
    Given I launch chrome browser
    When I open the uni CRM Signin page
    And Enter the username "admission@unidirect.org" and password "london2020"
    And Click the login button
    Then user must login into the dashboard page successfully