# v0.2

## Key changes

- Improved prompts, especially coder system and tools prompts.
- Sharing the output from researcher to documenter.
- Removing backlog for PM.

### Metrics

#### Metrics per test (project)

| Metryka                               | Project 1 | Project 2 | Project 3 | Project 4 | Project 5 | Project 6 |
| ------------------------------------- | --------- | --------- | --------- | --------- | --------- | --------- |
| Time of generation (s)                | 171.98    | 612.75    | 459.72    | 625.31    | 860.55    | 385.27    |
| Number of lines of code               | 128       | 377       | 400       | 292       | 657       | 252       |
| Number of used tokens                 | 102095    | 314406    | 237500    | 324657    | 445496    | 207828    |
| Number of lines of code after changes | 128       | 377       | 400       | 292       | 678       | 252       |
| Levenshtein distance                  | 0         | 0         | 0         | 0         | 293       |           |
| Cyclomatic complexity (avg)           |           |           |           |           |           |           |
| Code duplication (%)                  |           |           |           |           |           |           |
| Lint errors                           |           |           |           |           |           |           |

#### Aggregation Metrics

| Metryka   | Project 1 | Project 2 | Project 3 | Project 4 | Project 5 | Project 6 |
| --------- | --------- | --------- | --------- | --------- | --------- | --------- |
| % success | 100%      | 100%      | 100%      | 100%      | 70,7%     |           |

(Limit 1000) characters

Average success:

### Report

1. Project no 2 started to work after chenigng 7 character. The method list_notes() was called but never created.

### Uniwersalne narzędzia

| Narzędzie       | Opis                                                                                                                                 |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **SonarQube**   | Kompleksowe narzędzie do statycznej analizy kodu. Obsługuje wiele języków, mierzy błędy, code smells, bezpieczeństwo, test coverage. |
| **Codacy**      | SaaS do automatycznej oceny jakości kodu — styl, złożoność, pokrycie testami. Integruje się z GitHub/GitLab.                         |
| **CodeClimate** | Analiza jakości kodu i złożoności. Możliwość oceny pull requestów. Wspiera wiele języków.                                            |
| **DeepSource**  | Alternatywa dla Codacy i CodeClimate. Świetne do CI/CD.                                                                              |
| **Semgrep**     | Lekki, szybki skaner kodu — znajdowanie błędów i luk w zabezpieczeniach na poziomie składni.                                         |

### Python

| Narzędzie                | Opis                                                                                |
| ------------------------ | ----------------------------------------------------------------------------------- |
| **pylint**               | Analiza stylu i błędów logicznych. Podaje score (0–10).                             |
| **flake8**               | Lekkie narzędzie do sprawdzania stylu wg PEP8, integruje `pyflakes`, `pycodestyle`. |
| **black**                | Formatowanie kodu zgodnie z ustalonym stylem (opinia: „nie ma dyskusji”).           |
| **mccabe**               | Mierzy cyklomatyczną złożoność.                                                     |
| **radon**                | Oblicza metryki: złożoność, maintainability index, itp.                             |
| **bandit**               | Skaner bezpieczeństwa dla Pythona — znajdzie np. `eval()` i inne niebezpieczeństwa. |
| **pytest + coverage.py** | Testy jednostkowe i pokrycie testami (coverage %).                                  |
