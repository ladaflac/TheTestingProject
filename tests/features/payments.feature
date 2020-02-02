Feature: Payments
  As an account owner
  I want to make money transfers
  So that my debt gets paid off

  @case_id=C12
  Scenario: Account transfer success
    Given The Account transfer input page is opened
    When The user enters mandatory payment fields
    And The user submits the form
    Then The success message is displayed
    And Payment is saved
    And The number of transfers in the database increases by 1
      """
      Note: Not a good test if the tests are running in paralell!
      """

  # todo find a way to read the error msg
#  @case_id=C13
#  Scenario: Account transfer validation error
#    Given The Account transfer input page is opened
#    When The user submits the form
#    Then The error message is displayed
