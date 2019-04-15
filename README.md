# crime-map
Scraping HUPD crime reports and rendering visually


### Tested modules: 

- ~~Textract~~
- ~~PyPDF2~~
- ~~Tabula~~ (works well enough, will take some RegEx finangling, but is usable
- Camelot (works very nicely, but completely omits time and address line other than first line) <- take that back. I think it works perfectly

### Future todos: 
- Optimise the way that the pdfs are scraped to account for the weird case
- Currently returns an error 404 if HUPD is behind in posting logs. Is there a better way to handle this?
- There may be an issue of missing entries 
    - If scraper throws an error while partway through a file, after debugging and restarting the scraper, I suspect it may skip over the half scraped file
    - Potential fixes include emptying and rescraping the directory (will be necessary anyway if I want to have more than a months worth of entries there)
- Also, checking the most recently scraped file is currently very slow because it checks through every single entry to find the most recent one. There has to be a faster way to do this since SQLite can do it so quickly