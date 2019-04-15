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