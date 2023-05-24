Feature: Add product to cart
  As a user
  I want to be able to add products to my cart

  Scenario: Add a product to the cart
    Given I am logged in to the saucedemo website
    When I select a product
    And I click the "Add to Cart" button
    Then the product should be added to my cart
