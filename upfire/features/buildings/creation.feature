Feature: Planets creation
  # Enter feature description here

  Scenario: With a single landmass
    Given an empty solar system
    When I create planet "Earth" with default settings
    Then planet "Earth" should have "1" Landmass
    And that landmass should have capacity "10000"
    And the same spare capacity
