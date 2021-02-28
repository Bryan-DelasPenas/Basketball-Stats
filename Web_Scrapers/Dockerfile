# Dockerfile -> Image -> Container

FROM python:3.8

# The source directory for this dockerfile
WORKDIR C:\Users\Bryan\Desktop\Basketball-Stats\Web_Scrapers

# Add the subdirectories
ADD Python_Scrapers Python_Scrapers
ADD Run_Scraper Run_Scraper

RUN pip install beautifulsoup4 lxml pandas requests unidecode

CMD ["python", ".\Run_Scraper\get_output.py"]