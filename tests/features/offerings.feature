Feature: Offerings
  As a logged-in user
  I want to see the bank's products
  So that I can start using a product I don't have yet

  @case_id=C11
  Scenario: Offerings overview
    Given The Offerings page is opened
    Then The user sees the menu with all products
