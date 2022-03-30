from api.routes.factory import RouterFactory

router = RouterFactory(version="v1", tag="healthcheck").get


@router.get("/healthcheck",
             response_description="API Healthcheck",
             status_code=200)
def healthcheck():
    return {"status": "ok"}