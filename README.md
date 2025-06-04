# v1.1

## Key changes

- Disabling reasining

### Metrics

#### Metrics per test (project)

Model: gpt-4.1

| Metryka                               | Project 1 | Project 2 | Project 3 | Project 4 | Project 5                              | Project 6                      |
| ------------------------------------- | --------- | --------- | --------- | --------- | -------------------------------------- | ------------------------------ |
| Time of generation (s)                | 171.98    | 612.75    | 459.72    | 625.31    | 860.55                                 | 385.27                         |
| Number of lines of code               | 128       | 377       | 400       | 292       | 657                                    | 252                            |
| Number of used tokens                 | 102095    | 314406    | 237500    | 324657    | 445496                                 | 207828                         |
| Number of lines of code after changes | 128       | 377       | 400       | 292       | 678                                    | 252                            |
| Levenshtein distance                  | 0         | 0         | 0         | 0         | 293                                    | 146                            |
| Cyclomatic complexity (avg)           | 2,2       | 2,6       | 2,9       | 2,2       | 1,4                                    | 2                              |
| Code duplication (%)                  | 0         | 0         | 0         | 0         | 0                                      | 0                              |
| Lint errors (Python)                  | 0         | 4         | 1         | 0         | 1                                      | N/A                            |
| Notes                                 |           |           |           |           | Added scripts to html, removed exports | added API key, removed exports |

#### Aggregation Metrics

| Metryka   | Project 1 | Project 2 | Project 3 | Project 4 | Project 5 | Project 6 |
| --------- | --------- | --------- | --------- | --------- | --------- | --------- |
| % success | 100%      | 100%      | 100%      | 100%      | 70,7%     | 85,4%     |

(Limit 1000) characters

Average success: 92,68%
