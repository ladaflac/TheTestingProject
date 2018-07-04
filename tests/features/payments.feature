@wip
Feature: Payments
  As a consumer
  I want to pay the bills
  So that my debt gets paid off

  @wip
  Scenario: Account transfer success
    Given The Account transfer input page is opened
    When The user enters mandatory payment fields
    And The user submits the data
    Then The confirmation page is opened
    And The success message is displayed

  @wip
  Scenario: Account transfer validation error
    Given The Account transfer input page is opened
    When The user does not enter all mandatory payment details
    And The user submits the data
    Then The error message is displayed