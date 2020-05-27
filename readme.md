#  Reproducible research workflow: JSON parsing and text mining in Python, R + RMarkdown

This is a textmining and statistics analysis workflow using GNU Make, Python and R for a reproducible research workflow.

In this RSM project, the following is done:
- Pipeline stage "data-preparation"
  - Download raw JSON data in a zip file
  - Unzip data
  - Parse JSON data to CSV file
  - Load CSV file, and enrich textual data with text mining metrics using Python's TextBlob package for sentiment analysis
- Pipeline stage "analysis"
  - Load final output file from previous pipeline stage, run precleaning code
  - Produce RMarkdown HTML output with simple statistics
  
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
