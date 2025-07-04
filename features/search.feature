Feature: Search
    Explore streams based on the search title

    Background:
        Given Twitch TV website

    Scenario Outline: Watch a stream by game title
        Given search for <game_title> stream
        When I scroll <number_of_scrolls> times
        And select <order> stream
        And wait for page load
        Then stream is playing and take screenshot

    Examples: 
        | game_title    | number_of_scrolls | order  |
        | StartCraft II |         2         | first  |
        | Dota 2        |         4         | last   |
        | CS 2          |         6         | random |
    
