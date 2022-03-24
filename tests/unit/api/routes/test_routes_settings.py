from api.routes.factory import RouterFactory


def testing_prefix_on_current_version_is_correct():

    router = RouterFactory(version="v1", tag="management-api").get

    prefix = "/api/v1"

    assert prefix == router.prefix

def testing_tags_on_current_version_is_correct():

    router = RouterFactory(version="v1", tag="management-api").get

    tag = "management-api-v1"

    assert tag == router.tags[0]
    
def testing_responses_on_current_version_is_correct():

    router = RouterFactory(version="v1", tag="management-api").get

    responses = {404: {"description": "Not found"}}

    assert responses == router.responses
