# v0.3

## Key changes

- Added conversation summary

### Metrics

#### Metrics per test (project)

| Metryka                     | Agent A | Agent B | ... |
| --------------------------- | ------- | ------- | --- |
| Time of generation (s)      | 15      | 30      |     |
| Number of lines of code     | 250     | 180     |     |
| Number of used tokens       | 850     | 900     |     |
| Levenshtein distance        | 120     | 70      |     |
| Cyclomatic complexity (avg) | 4.5     | 3.1     |     |
| Code duplication (%)        | 18%     | 5%      |     |
| Lint errors                 | 12      | 2       |     |

#### Aggregation Metrics

| Metryka           | Agent A | Agent B | ... |
| ----------------- | ------- | ------- | --- |
| % Tests completed | 70%     | 95%     |     |

(Limit 1000) characters
Test 1 - Perfect - passed - 100%
Test 2 - Changed 10 characters - passed - (1000-10)/1000 % = 99%
Test 3 - Changed 150 ch - passed - (1000 - 150) / 1000 % = 85%
Test 4
Test 5
Test 6

Avg (100% + 99% + 85% + ...)/6 = Final result

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
