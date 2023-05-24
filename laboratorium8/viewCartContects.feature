Feature: View cart contents
  As a user
  I want to be able to view the contents of my cart

  Scenario: View cart
    Given I am logged in to the saucedemo website
    When I click on the cart icon
    Then I should see the contents of my cart
    And the cart should display the total price
