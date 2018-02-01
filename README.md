# Circus spider
python/splash scrapy project

## Instalation
*note:* requires python v3.6.*

before running the project you need to pull down a couple of dependencies:

- install scrapy by running `pip install scrapy`
- install scrapy-splash by running `pip install scrapy-splash`
- install scrapinghub/splash by running `docker pull scrapinghub/splash`


## Running the crawler 

First you need to run the splash server by running in a separate terminal `docker run -p 8050:8050 -p 5023:5023 scrapinghub/splash --max-timeout 300`

Then run `scrapy crawl outcome_odds`

It will generate a circus.sqlite database right in the root of the project, that database will include the **odd** and the **event** tables.
