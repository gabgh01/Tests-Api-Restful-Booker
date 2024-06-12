Feature: Test api restful-booker

  @get
  Scenario: Get booker
    Given the API endpoint is "https://restful-booker.herokuapp.com/booking"
    When I request the user with id 10
    Then the response status code should be 200

  @create
  Scenario: Create Booker
    Given the API endpoint is "https://restful-booker.herokuapp.com/booking"
    When I as user want to create new user in api booker with body:
      | firstname | lastname | totalprice | depositpaid | checkin    | checkout   | additionalneeds |
      | Gabo      | ccc      | 111        | true        | 2024-01-01 | 2024-06-01 | Breakfast       |
    Then the new user should be create with status code 200

    @update
  Scenario: Update user booker
    Given I need get token authentication from endpoint "https://restful-booker.herokuapp.com/auth" with data:
      | username | password    |
      | admin    | password123 |
    When request is update user with id 10 in api "https://restful-booker.herokuapp.com/booking"
      | firstname | lastname | totalprice | depositpaid | checkin    | checkout   | additionalneeds |
      | Gabo      | ccc      | 111        | true        | 2024-01-01 | 2024-06-01 | Breakfast       |

    Then I should see user is update whit firtsname "Gabo"


  @delete
  Scenario: delete user booker
    Given I need get token authentication from endpoint "https://restful-booker.herokuapp.com/auth" with data:
      | username | password    |
      | admin    | password123 |
    When request is delete user with id 20 from api "https://restful-booker.herokuapp.com/booking"
    Then I should see user is delete whit and api response status 201
