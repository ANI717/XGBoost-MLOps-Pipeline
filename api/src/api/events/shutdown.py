def include_event(app, logger):
    @app.on_event("shutdown")
    async def shutdown_event():
        body = "Application Shutdown Complete"
        logger.info(body)
