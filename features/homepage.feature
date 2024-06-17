Feature: Verify the Home Page of OrangeHRM
  Scenario: Verify the title of OrangeHRM
    Given launch the Chrome browser
    When OrangeHRM URL is given
    Then Verify the title of homepage
    And Close the Chrome browser
