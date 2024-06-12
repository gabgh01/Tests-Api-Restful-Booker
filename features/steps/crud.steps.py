import requests
from behave import given, when, then


@given(u'the API endpoint is "{endpoint}"')
def step_impl(context, endpoint):
    context.api_endpoint = endpoint
    print(endpoint)


# get
@when(u'I request the user with id {user_id}')
def step_impl(context, user_id):
    context.user_id = user_id
    print('userId', user_id)
    response = requests.get(f"{context.api_endpoint}/{user_id}")
    context.response = response



@then(u'the response status code should be {status_code}')
def step_impl(context, status_code):
    assert context.response.status_code == int(
        status_code), f"Expected get method  {status_code} but got {context.response.status_code}"


# create
@when(u'I as user want to create new user in api booker with body')
def step_impl(context):
    for r in context.table:
        print(r['firstname'])
        body = {"firstname": r['firstname'], "lastname": r["lastname"], "totalprice": int(r['totalprice']),
                "depositpaid": r['depositpaid'], "bookingdates": {"checkin": r["checkin"], "checkout": r['checkout']},
                "additionalneeds": r['additionalneeds']}

    context.body = body
    response = requests.post(f"{context.api_endpoint}", json=context.body)
    context.response = response


@then(u'the new user should be create with status code {status_code}')
def step_impl(context, status_code):
    assert context.response.status_code == int(status_code), f"Expected creation {status_code} but got {context.response.status_code}"


# update
@given(u'I need get token authentication from endpoint "{auth_endpoint}" with data')
def step_impl(context, auth_endpoint):
    context.api_endpoint = auth_endpoint
    for r in context.table:
        body = {"username": r["username"], "password": r["password"]}
    auth_response = requests.post(f"{context.api_endpoint}", json=body)
    if auth_response.status_code == 200:
        context.token = auth_response.json()['token']
    else:
        raise Exception(f"Failed to get token: {auth_response.status_code} {auth_response.text}")


@when(u'request is update user with id {user_id} in api "{endpoint}"')
def step_impl(context, user_id, endpoint):
    for r in context.table:
        body = {"firstname": r['firstname'], "lastname": r["lastname"], "totalprice": int(r['totalprice']),
                "depositpaid": r['depositpaid'], "bookingdates": {"checkin": r["checkin"], "checkout": r['checkout']},
                "additionalneeds": r['additionalneeds']}

    context.user_body = body
    headers = {"Content-Type": "application/json", "Accept": "application/json", "Cookie": f"token={context.token}"}
    print('headers', headers)

    response = requests.put(f"{endpoint}/{user_id}", json=context.user_body, headers=headers)
    context.response_user_update = response
    print('response status', context.response_user_update.status_code)



@then(u'I should see user is update whit firtsname "{firtsname}"')
def step_impl(context, firtsname):
    assert context.response_user_update.status_code == 200, f"Expected status code 200 but got {context.response_user_update.status_code}"
    response_data = context.response_user_update.json()

    assert response_data['firstname'] == firtsname, f"Expected firstname to be {firtsname} but got {response_data['firstname']}"


# delete

@when(u'request is delete user with id {user_id} from api "{endpoint}"')
def step_impl(context, user_id, endpoint):
    headers = {"Content-Type": "application/json", "Accept": "application/json", "Cookie": f"token={context.token}"}
    print('headers', headers)

    response = requests.delete(f"{endpoint}/{user_id}", headers=headers)
    context.response_user_delete = response
    print('response status', context.response_user_delete.status_code)



@then(u'I should see user is delete whit and api response status {status_code:n}')
def step_impl(context,status_code):
    print('statuscode',status_code)
    assert context.response_user_delete.status_code == status_code, f"Expected status code {status_code} but got {context.response_user_delete.status_code}"
