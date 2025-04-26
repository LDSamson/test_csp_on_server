# Dockerfile.shiny
FROM ldsamson/clinsight:latest

# Copy the app directory into the image
COPY app/ /home/appuser/

# Expose the port Shiny Server runs on (default is 3838)
EXPOSE 3838

#CMD ["R", "-e", "shiny::runApp(host = '0.0.0.0', port=3838)"]

ENV GOLEM_CONFIG_ACTIVE="default"
CMD ["R", "-e", "options('shiny.port'=3838, shiny.host='0.0.0.0', golem.app.prod = TRUE); clinsight::run_app()"]