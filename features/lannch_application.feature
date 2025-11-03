Feature: automation exercise
  Launch heroku app and perform actions on it

  @smoke
  Scenario: signup in to app
    Given I launch application
    Then I clicked on signup

  Scenario Outline: login to application
    Given I launch application
    When I enter "<email>" and "<password>"
    When I click on submit button
    Then I verify successfully login
    Examples:
      | email              | password |
      |mkadam661@gmail.com | Manish123|






