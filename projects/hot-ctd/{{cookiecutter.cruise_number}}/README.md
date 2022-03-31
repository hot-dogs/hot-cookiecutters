The directory structure of your new project looks like this:

```
├── README.md                              <- The top-level README for developers using this project.
│
├── history.{{cookiecutter.cruise_number}} <- It is the processing history of the cruise.
│
├── metobs                                 <- Contains the original meteorological observations
│                                             data from the HOT cruise.
│
├── notebooks                              <- Jupyter notebooks. Naming convention is a number (for ordering),
│                                             the creator's initials, and a short `-` delimited description, e.g.
│                                             `1.0-fcp-initial-data-exploration`.
│
├── orig                                   <- The original, immutable CTD data.
│
├── reports                                <- Generated CTD analysis as HTML, PDF, LaTeX, etc.
│   └── figures                            <- Generated graphics and figures to be used in reporting
│
├── thermosal                              <- Contains thermosalinograph data processing results
│
└── underway                               <- Contains the original underway data
```







