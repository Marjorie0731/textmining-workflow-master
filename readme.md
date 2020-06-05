# Research workflow: JSON parsing and text mining in Python, R + RMarkdown
This is a team project of course Research in Social Media(RSM) in Tilburg university, aiming to solve the research question by analysing tweets collected on the White House Press briefings from Twitter.

Research question:
How do US Twitter users react to a WH coronavirus press conference according to the main political affiliation of their state?

In this project, the following is completed:
- Pipeline stage "data-preparation"
  - Download raw dataset in a zip file
  - Unzip data
  - Precleaning and parse JSON data to CSV file 
  - Load CSV file, and enrich textual data with text mining metrics using Python's TextBlob package for sentiment analysis
  
- Pipeline stage "analysis"
  - Load output file from previous pipeline stage, run analysis code
  - Produce RMarkdown HTML output with statistics
  
## Dataset
The raw dataset contains 63,856 tweet objects on the White House Press briefings from Twitter. They feature either of the hashtags '#coronavirus', '#DonaldTrump', '#Trump', '#PresidentTrump','#PressBriefing', '#WhiteHouse', '#PressConference', '#Whitehousebriefing','#reopenamerica', and '#coronavirustaskforce'. Each tweet object is stored in JSON format, containing basic information of the tweet such as creating time, text content, user information, etc. 

## Dependencies

- Python via the Anaconda distribution
- TextBlob via `pip install -U textblob`
- NLTK dictionaries; open Python, then type

  ```
  import nltk
  nltk.download('punkt')
  ```
  
- Gnu Make
- R and the following packages:

```
install.packages(c("stargazer", "knitr", "data.table", "ggplot2"))
```

Detailed installation instructions can be found here: [tilburgsciencehub.com/tutorial](http://tilburgsciencehub.com/tutorial)

## How to get started
The best way to get started is by following [our tutorial](http://tilburgsciencehub.com/tutorial).

- Download this repository (either by forking and then cloning, or as a template)
- Open Terminal in project's main directory, type make
- The src/data-preparation and src/analysis directories contain the specific workflow for each stage of the pipeline.
- Tested on Mac and Windows 10

- Many possible improvements remain. Comments and contributions are welcome!
