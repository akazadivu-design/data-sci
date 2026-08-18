[🏠 Roadmap home](../README.md)

---

<a id="companion-curricula"></a>
## Guided companion curricula

The two Microsoft curricula below are strong, actively maintained beginner companions. They use the lesson-table navigation, short projects, quizzes, assignments, and solution folders that make a large subject easier to enter. Use their repository root links to follow the newest default-branch content; the reviewed commits provide a dated audit trail.

| Curriculum | Best for | Current scope | Reviewed upstream snapshot |
|---|---|---|---|
| [Microsoft Data Science for Beginners](https://github.com/microsoft/Data-Science-For-Beginners) | A gentle, project-based introduction before the statistics and data modules | 10 weeks · 20 lessons · data ethics, SQL/NoSQL, Python, preparation, visualisation, lifecycle, cloud, and communication | [`4d2ac42`](https://github.com/microsoft/Data-Science-For-Beginners/commit/4d2ac427ad6f022e73a75c4f46a28bbb7978ec3f), reviewed 2026-07-24 |
| [Microsoft ML for Beginners](https://github.com/microsoft/ML-For-Beginners) | Hands-on classical ML practice alongside M9–M14 and M17 | 12 weeks · 26 lessons · regression, classification, clustering, NLP, time series, reinforcement learning, and responsible ML | [`d0d0ea2`](https://github.com/microsoft/ML-For-Beginners/commit/d0d0ea2b2d22cddca31f9c6d108df7daa87a1b46), reviewed 2026-07-24 |

### Where the Microsoft lessons fit

| This roadmap | Guided lesson groups | How to use them |
|---|---|---|
| [M1 Programming](../curriculum/1-foundations.md#module-1), [M5 Probability](../curriculum/1-foundations.md#module-5), [M6 Statistics](../curriculum/2-statistics-and-data.md#module-6) | [Defining data science and introductory statistics](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction) | Use as an accessible first pass; keep this roadmap's exercises for mathematical depth. |
| [M7 Wrangling, EDA, and visualisation](../curriculum/2-statistics-and-data.md#module-7) | [Working with data](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data) and [data visualisation](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/3-Data-Visualization) | Complete the guided notebooks, then rebuild one analysis with validation and a reproducible pipeline. |
| [M8a Databases and SQL](../curriculum/2-statistics-and-data.md#module-8a) | [Relational and NoSQL lessons](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data) | Use lessons 5–6 for practice before advanced SQL, query plans, warehousing, and dbt. |
| [M9 Regression](../curriculum/3-classical-ml.md#module-9) | [Regression lessons](https://github.com/microsoft/ML-For-Beginners/tree/main/2-Regression) and [model web app](https://github.com/microsoft/ML-For-Beginners/tree/main/3-Web-App) | Pair the projects with this roadmap's derivations, diagnostics, regularisation, and cross-validation. |
| [M10 Classification](../curriculum/3-classical-ml.md#module-10) | [Classification lessons](https://github.com/microsoft/ML-For-Beginners/tree/main/4-Classification) | Practise model comparison, then add calibration, leakage checks, and error analysis. |
| [M11 Unsupervised learning](../curriculum/3-classical-ml.md#module-11) | [Clustering lessons](https://github.com/microsoft/ML-For-Beginners/tree/main/5-Clustering) | Use for a visual K-means project before PCA, mixture models, and manifold learning. |
| [M14 Time series](../curriculum/4-probabilistic-ml.md#module-14) | [Time-series lessons](https://github.com/microsoft/ML-For-Beginners/tree/main/7-TimeSeries) | Start with ARIMA and SVR, then continue to probabilistic forecasting and foundation models. |
| [M16 Representation learning](../curriculum/5-deep-learning.md#module-16) | [Introductory NLP lessons](https://github.com/microsoft/ML-For-Beginners/tree/main/6-NLP) | Treat these as classical NLP prerequisites before transformers and generative models. |
| [M17 Reinforcement learning](../curriculum/5-deep-learning.md#module-17) | [Reinforcement-learning lessons](https://github.com/microsoft/ML-For-Beginners/tree/main/8-Reinforcement) | Use the Q-learning projects as the practical on-ramp to modern deep and offline RL. |
| [M23 Safety](../curriculum/6-frontier-production.md#module-23), [M24 Operations](../curriculum/6-frontier-production.md#module-24), [M25 Product DS](../curriculum/6-frontier-production.md#module-25) | [ML in the wild](https://github.com/microsoft/ML-For-Beginners/tree/main/9-Real-World), [data-science lifecycle](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle), and [cloud lessons](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/5-Data-Science-In-Cloud) | Use for case studies; follow this roadmap for current evaluation, governance, MLOps, and communication depth. |

> **Selection rule:** use the Microsoft courses when you want a guided beginner lesson or a small practice project. Use the primary university courses and books in each module when you need formal depth. The companion courses supplement this roadmap; they do not replace its mathematics, deep learning, data engineering, or production-AI modules.

### Suggested study rhythm

For each module, use a simple four-step loop:

1. **Learn** — complete the primary course or lecture sequence.
2. **Read** — work through the listed primary text and exercises.
3. **Implement** — reproduce core algorithms without relying only on high-level APIs.
4. **Ship** — complete the module project with tests, documentation, and a short results memo.

> **Resource policy:** free and open resources are preferred. Some books are listed as optional references when no equivalent open source is as strong.

---

[🏠 Roadmap home](../README.md)
