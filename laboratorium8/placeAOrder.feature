Feature: Place an order
  As a user
  I want to be able to place an order for the products in my cart

  Scenario: Place an order
    Given I am logged in to the saucedemo website
    And I have added products to my cart
    When I proceed to checkout
    And I enter my shipping and payment details
    And I click the "Finish" button
    Then my order should be placed successfully
    And I should see an order confirmation page
