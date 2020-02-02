Feature: Accounts on the homepage
  As a logged-in user
  I want to see all my products contracted with the bank
  So that I can make financial decisions


  Scenario Outline: Account balance check
    Given The accounts are displayed
    And The account type is "<account type>"
    Then Account balance is "<value type>"

    Examples: Money accounts
      | account type  | value type  |
      | UBS Konto     | currency    |
      | UBS Fondskonto| currency    |
      | UBS Sparkonto | currency    |

    Examples: Loyalty accounts
      | account type  | value type  |
      | UBS KeyClub   | points      |
