# Dockerfile.shiny
FROM rocker/verse:4.4.1

RUN apt-get update && apt-get install -y --no-install-recommends \
	libx11-dev \
	libcurl4-openssl-dev \
	libssl-dev \
	zlib1g-dev \
	pandoc \
	libicu-dev \
    && rm -rf /var/lib/apt/lists/*

RUN R -e \ 
		'options(repos = "https://packagemanager.posit.co/cran/__linux__/jammy/2024-09-17"); install.packages("remotes");\
		remotes::install_github("openpharma/clinsight", ref = "dev")'	

RUN tlmgr update --all --self && \
  tlmgr install kvoptions ltxcmds kvsetkeys etoolbox xcolor \
  geometry booktabs mdwtools pdftexcmds infwarerr epstopdf-pkg \
  amsmath latex-amsmath-dev texlive-scripts auxhook bigintcalc \
  bitset etexcmds gettitlestring hycolor hyperref intcalc kvdefinekeys \
  letltxmacro pdfescape refcount rerunfilecheck stringenc uniquecounter \ 
  zapfding ec multirow wrapfig float pdflscape tabu varwidth threeparttable \
  environ trimspaces ulem
  
# Expose the port Shiny Server runs on (default is 3838)
EXPOSE 3838

#CMD ["R", "-e", "shiny::runApp(host = '0.0.0.0', port=3838)"]

ENV GOLEM_CONFIG_ACTIVE="default"
CMD ["R", "-e", "options('shiny.port'=3838, shiny.host='0.0.0.0', golem.app.prod = TRUE); clinsight::run_app()"]