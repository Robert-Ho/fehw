Feature: BOOKING WEDGET

    Feature Description
Background:
    Given Open the url "https://www.fareasthospitality.com"
    And Close the popup

Scenario: Booking success with Book Now CTA
    When Click on Book Now CTA
    Then Booking wedget is display
    When I select Location "Singapore"
    And Select Hotel "Oasia Hotel Downtown"
    And Select Check In Date is TODAY
    And Select Check Out is TODAY + 2
    And Enter number of Guests "1" Adult(s), "1" Child(ren)
    Then Check Availability is enable
    When I click on Check Availability
    Then I should navigate to "Oasia Hotel Downtown by Far East Hospitality - Reservations - Room Availability" page
    And Verify the hotel name is "Oasia Hotel Downtown"
    And Verify number of Guests
    And Verify Check In Date
    And Verify checkout Date