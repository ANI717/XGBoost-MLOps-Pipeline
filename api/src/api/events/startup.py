def include_event(app, logger): 
    @app.on_event("startup")
    async def startup_event():
        body = "Application Startup Complete"
        logger.info(body)
