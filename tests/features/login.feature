Feature: Login to demo application
  As a registered user
  I want to login
  So that I get access to the bank's online services

  Scenario: Login with demo QR code
    Given The login page is opened
    When The user submits the prefilled contract number
    And The QR code page is opened
    Then The user waits for the fake QR scan
    And The homepage is opened
