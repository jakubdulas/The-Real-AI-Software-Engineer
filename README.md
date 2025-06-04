# v1.1

## Key changes

- Disabling reasining

### Metrics

#### Metrics per test (project)

Model: gpt-4.1

| Metryka                               | Project 1 | Project 2                                 | Project 3                                                 | Project 4                                 | Project 5   | Project 6 |
| ------------------------------------- | --------- | ----------------------------------------- | --------------------------------------------------------- | ----------------------------------------- | ----------- | --------- |
| Time of generation (s)                | 92.25     | 167.72                                    | 450.09                                                    | 200.06                                    | 287.23      | 196.37    |
| Number of lines of code               | 77        | 188                                       | 372                                                       | 227                                       | 313         | 243       |
| Number of used tokens                 | 45590     | 85116                                     | 234158                                                    | 95994                                     | 171589      | 112006    |
| Number of lines of code after changes | N/A       | 191                                       | N/A                                                       | 227                                       | 322         | 238       |
| Levenshtein distance                  | 0         | 61                                        | 0                                                         | 31                                        | 140         | 142       |
| Cyclomatic complexity (avg)           | 5.25      | 3.2                                       | 3.65                                                      | 2.44                                      | 1.81        | N/A       |
| Code duplication (%)                  | 0%        | 0%                                        | 0%                                                        | 0%                                        | 0%          | 0%        |
| Lint errors (Python)                  | 1         | 0                                         | 0                                                         | 0                                         | 0           | N/A       |
| Notes                                 |           | Function to validate input was badly used | Agent added ability to select O or X for Human vs AI game | Created dir 'snake_game' which is useless | CORS Errors |           |

#### Aggregation Metrics

| Metryka   | Project 1 | Project 2 | Project 3 | Project 4 | Project 5 | Project 6 |
| --------- | --------- | --------- | --------- | --------- | --------- | --------- |
| % success | 100%      | 93,9%     | 100%      | 96,9%     | 86%       | 85,8%     |

(Limit 1000) characters

Average success: 93,77%
