Feature: Search
    Explore streams based on the search title

    Background:
        Given Twitch TV site

    Scenario: Watch a stream by game title
        Given search for "StartCraft II" stream
        When I scroll "2" times
        And select a stream
        And wait for page load
        Then stream is playing and take screenshot

    Scenario: Open streamer profile by game title
        Given search for "StartCraft II" stream
        When I scroll "2" times
        And select a streamer profile
        And wait for page load
        Then stream is playing and take screenshot
    
