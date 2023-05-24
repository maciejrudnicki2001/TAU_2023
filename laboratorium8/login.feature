Feature: Login functionality
  As a user
  I want to be able to log in to the website

  Scenario: Successful login
    Given I am on the saucedemo website
    When I enter my username and password
    And I click the "Login" button
    Then I should be logged in successfully
    And I should see the inventory page
