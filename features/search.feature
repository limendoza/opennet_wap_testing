Feature: Search
    Explore streams based on the search title

    Background:
        Given Twitch TV website

    Scenario: Watch a stream by game title
        Given search for "StartCraft II" stream
        When I scroll "2" times
        And select a stream
        And wait for page load
        Then stream is playing and take screenshot

    
    
