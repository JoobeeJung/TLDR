# Continuous Integration Example Repository

![Build/Test Workflow](https://github.com/JoobeeJung/TLDW/actions/workflows/build_test.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/JoobeeJung/TLDW/badge.svg?branch=main)](https://coveralls.io/github/JoobeeJung/TLDW?branch=main)

# TL;DW: UW MSDS DATA515 Summarization Tool with LLMs

## The Project Type: Recommendation + Summarization System
## Questions of Interest
- What Ted Talks or Podcasts can I watch to learn more about the YouTube video I just watched?
- Can you give me a summary of the YouTube video that I watched?
- What are some of the summary statistics of the YouTube video I watched? (Metadata)
- What are some podcasts or TED Talks I can watch for a topic of my choosing?
    
## Goals for the project output (what are you going to produce?)
- The goal for this project will be to output a web application where a user will have the chance to insert a YouTube video link and can prompt the application to recommend Ted Talks or podcasts that they can watch to learn more about the topic from the YouTube video they watched.
    
## Data sources you will use
- Youtube Transcript API: to obtain transcripts of a YouTube video based on its link
- Ted Talks Transcript: https://www.kaggle.com/datasets/miguelcorraljr/ted-ultimate-dataset 
- Podcast Transcript Dataset: https://www.kaggle.com/datasets/sentinel3734/skeptoid-podcast-transcripts
- ChatGPT API: to create the summaries from the inputted YouTube video link
