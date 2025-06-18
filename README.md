# v1.2

## Key changes

- Running tests on Coder with ToT reasoning

### Metrics

#### Metrics per test (project)

Model: gpt-4.1

| Metryka                               | Project 1 | Project 2 | Project 3 | Project 4 | Project 5 | Project 6 |
| ------------------------------------- | --------- | --------- | --------- | --------- | --------- | --------- |
| Time of generation (s)                | 300.82    | 562.42    | 743.00    | 707.95    | 699.62    | 552.51    |
| Number of lines of code               | 91        | 255       | 809       | 801       | 690       | 443       |
| Number of used tokens                 | 208949    | 441787    | 711946    | 661526    | 545036    | 393723    |
| Number of lines of code after changes | N/A       | 255       | N/A       | N/A       | 690       | 436       |
| Levenshtein distance                  | 0         | 4         | 0         | 0         | 23        | 575       |
| Cyclomatic complexity (avg)           | 3.8       | 2.23      | 3.07      | 2.34      | 1.5       | N/A       |
| Code duplication (%)                  | 0%        | 0%        | 0%        | 0%        | 0%        | 0%        |
| Lint errors (Python)                  | 1         | 5         | 5         | 0         | 1         | N/A       |
| Notes                                 |           |           |           |           |           |           |

Project 5: There is no ability to remove tasks on frontend. Needed to fix CORS (set to all hosts)

#### Aggregation Metrics

| Metryka   | Project 1 | Project 2 | Project 3 | Project 4 | Project 5                                                       | Project 6 |
| --------- | --------- | --------- | --------- | --------- | --------------------------------------------------------------- | --------- |
| % success | 100%      | 100%      | 99,6%     | 100%      | 72,7% (subtracted 25% for not having delete task functionality) |           |

(Limit 1000) characters

Average success: 92,68%
