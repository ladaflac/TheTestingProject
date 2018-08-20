Feature: Payments
  As a consumer
  I want to pay the bills
  So that my debt gets paid off

  Scenario: Account transfer success
    Given The Account transfer input page is opened
    When The user enters mandatory payment fields
    And The user submits the form
    Then The confirmation page is opened
    And The user submits the form
    And The success message is displayed

  Scenario: Account transfer validation error
    Given The Account transfer input page is opened
    When The user submits the form
    Then The error message is displayed
