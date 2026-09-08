# Foundations M0–M5: Evidence-Based Improvement Plan

**Repository:** https://github.com/akazadivu-design/data-sci<br>
**Inspected commit:** `a412833204cb334a9c7f96dcd9f3c66029fb38f4` (`master`; commit dated 2026-08-30)<br>
**Original inspection and research:** 2026-09-06; original report completed 2026-09-07<br>
**Revision:** 1.1, reviewed 2026-09-08 against the same commit after fetching upstream; selected primary sources rechecked. See Sections 1, 9, and 10 for revision scope.<br>
**Scope:** M0 proof literacy/precalculus, M1 Python, M2 calculus, M3 linear algebra, M4 algorithms, M5 probability, and their entry/exit dependencies.<br>
**Companion status:** `Foundations_Agentic_AI_Implementation_Prompt.md` was named in the original report but was not supplied for this revision and was not found in the checkout. This plan is self-contained; Section 7.5 supplies the implementation handoff. No companion contents are assumed.

> **Main recommendation:** Keep the strong university resources and project-first philosophy. Replace exhaustive, inconsistently sequenced requirements with a prerequisite-safe core, clearly optional depth, usable diagnostics, and evidence of individual mastery.

## Contents

1. Executive assessment
2. Evidence-linked findings
3. Prerequisite-safe architecture
4. Module-by-module improvements
5. Diagnostic and assessment design
6. Learning workflow and workload
7. Implementation backlog and file map
8. Acceptance criteria
9. Research method and limitations
10. Sources

## 1. Executive assessment

This repository does **not** primarily need more courses. Its own contribution guide says to replace rather than pile on resources. The most valuable work is to improve **sequencing, scope, assessment, correctness, and access**.

### Preserve these strengths

- CS50P, MIT OCW, Harvard Stat 110, Hammack, Axler, and Mathematics for Machine Learning are strong anchors.
- The Pick-One guide and beginner onboarding recognize choice overload.
- M1, M2, M4, and M5 already have concrete projects, tests, documentation, and results memos.
- M3 already includes conditioning, numerical stability, QR, and SVD. These are **not missing topics**; their prioritization and assessment need improvement.
- There is already an AI-use policy, an audit trail, a progress tracker, and an internal-link checker. Improve these rather than create competing systems.
- Explicit module anchors and the documentation-only architecture should remain stable.

### Highest-impact actions

1. Supply the promised diagnostic, with actual questions, scoring, and strand-specific routing.
2. Teach core linear algebra before matrix calculus; gate randomized algorithms on elementary probability.
3. Distinguish core, reinforcement, and research extensions; synchronize all completion rules.
4. Teach a small scientific-Python bridge before numerical projects need it.
5. Correct AutoDiff, gradient-check, simulation-testing, bibliography, licensing, and access claims.
6. Keep projects, but add independent problem solving and delayed retrieval. Public visibility alone is not mastery.
7. Make the plan executable: bounded resource selections, outcome-level evidence, source-access records, and review ownership. Do not replace course overload with assessment bureaucracy.

### What changed in revision 1.1

- **Removed an unearned prerequisite:** M5 teaches covariance; it does not require prior “M3 covariance.” M3 may introduce centered data and Gram matrices algebraically without probability theory.
- **Distinguished selected paths from full courses:** a deterministic M4 selection is not all MIT 6.006, whose official prerequisites include probability. A discrete-first M5 selection is not permission to take all Stat 110 without calculus.
- **Made downstream preservation explicit:** retain Normal/Student-t and multivariate Normal readiness, not just MGFs/CLT, for M9/M11; inventory content consumers as well as written prerequisite bullets.
- **Made assessment usable:** anchored rubric levels, self-review versus independent review, retakes after answer exposure, small public practice examples, and no automatic two-week progression lock.
- **Tightened numerical contracts:** `lstsq` rank/residual semantics, QR's rank limitation, JAX's default 32-bit mode, and NumPy RNG reproducibility conditions.
- **Made free-first verifiable:** free instruction, practice, feedback, and core execution are distinct checks. An instructor-only solution manual is not a learner feedback route.
- **Added a bounded handoff and release controls:** exact resource mapping is a prerequisite to implementation, not something an agent may invent; proposal changes do not authorize changes to the live curriculum.

These are refinements, not a recommendation to add more required courses. The original 15 sample diagnostic items, six module analyses, and evidence-linked findings remain, with targeted corrections below.

### Inspection baseline

The original report records that the complete **495-line Foundations page** was read, alongside the root README, START-HERE, contribution policy, curriculum index, Pick-One guide, tracker, practitioner track, Foundations-relevant book entries, tooling documentation, and audit excerpts. Downstream prerequisite declarations in statistics, classical ML, and deep learning were checked for consequences of moving material. The Foundations page contains approximately **9,402 whitespace-delimited words** and **60 distinct external URL tokens**, measured by a simple URL scan.

The existing checker was run against the inspected checkout:

```text
python3 tools/check_links.py
checked 660 internal links across 36 md files; 0 failures
```

This establishes internal-link integrity, **not** instructional correctness, external-link validity, or complete free access. High-risk external claims were checked selectively; not every video timestamp or software version in the repository was independently verified.

**Revision baseline:** on 2026-09-08, fetching upstream still resolved `origin/master` to the inspected SHA. The Foundations page was read in full again; the README, contribution policy, tracker, tooling guidance, and downstream prerequisite declarations were checked. The checker was rerun and returned the same **660 internal links across 36 Markdown files; 0 failures** before adding this report. The original line/word/URL counts above describe the original inspection, not a new exhaustive measurement.

**Delivery scope:** a revised planning document only, prepared for a documentation-review PR. Live learner requirements, course files, workflows, and module numbering are unchanged. A PR containing this plan is not approval of its RFC-gated recommendations. Proposed cut scores, study hours, schedules, and pilot criteria below are **design hypotheses**, not validated educational results. Source checks newly performed in this revision are separated from inherited research in Section 9.

## 2. Evidence-linked findings

All repository links are pinned to the inspected commit. “F” means `curriculum/1-foundations.md`. Source IDs S01–S28 resolve in Section 10; the dated recheck ledger in Section 9 identifies what was newly verified.

**Priority:** P0 = correctness/access/prerequisite blocker; P1 = substantial instructional improvement; P2 = maintenance enhancement. Priority does not override the repository's RFC process.

| ID | Priority | Repository evidence | Finding and action |
|---|---|---|---|
| F01 | P0 | [F:18–37](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L18-L37) | A “15-question, 60-minute” diagnostic is advertised, but six external resource pointers are supplied, not one defined instrument. “Pick one” cannot assess six strands. The MIT `exam_a` endpoint returned **404**. Supply an original screen and answer guidance. |
| F02 | P0 | [F:35–58](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L35-L58); [tracker:16–18](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/guides/progress-tracker.md#L16-L18) | Aggregate versus every-strand rules disagree; strict `>70%` differs from “mandatory if <70%.” More fundamentally, failure in probability does not imply a need to repeat all M0. Separate entry readiness from placement out of later material. |
| F03 | P0 | [F:260–295](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L260-L295); [F:327–332](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L327-L332) | M2 includes derivatives of SVD/eigendecompositions before M3 teaches linear algebra, while M3 explicitly requires M2. This is a **content-level dependency loop**, not necessarily a cycle in the written module edges. MIT matrix calculus requires both subjects; MIT 18.06 says calculus knowledge is unnecessary [S03, S04]. Introduce sub-passes without renumbering. |
| F04 | P0 | [F:387–399](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L387-L399) | M4 requires only Python, but default MIT 6.006 expects discrete mathematics and checks readiness with Problem Set 0 [S06]. Its randomized/streaming material also needs probability. Add task-specific prerequisite gates. |
| F05 | P0 | [F:152–163](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L152-L163), [278–285](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L278-L285), [403–406](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L403-L406) | Paid books appear under “Required Reading,” contrary to free-first policy. Label paid references optional and supply a free route covering instruction **and practice**. A live publisher page is not a free book. |
| F06 | P0 | [F:104–108](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L104-L108), [272](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L272), [347](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L347) | Verified metadata corrections: Hammack is not simply CC-BY; Parr–Howard arXiv v3 is July 2018, not a 2024 revision; the Cambridge book is by **Jeffrey A. Fessler and Raj Rao Nadakuditi**, not Hero/Fessler/Townsend [S01, S16, S17]. Update all affected references. |
| F07 | P0 | [F:108](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L108), [197](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L197), [287](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L287) | Blanket Coursera “free audit” claims are unsafe. Coursera announced that first-module preview replaces auditing [S15]. Verify course-specific access; preview/trial/aid eligibility is not universally free completion. |
| F08 | P1 | [F:174](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L174), [288–318](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L288-L318) | NumPy/pandas are routed toward M7, but M2/M3/M5 require array programming earlier. Add a small NumPy/plotting bridge at M1 exit; retain dataframe engineering in M7 [S10]. |
| F09 | P1 | [Pick-One:64–71](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/guides/how-to-read-a-module.md#L64-L71); [F:202–205](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L202-L205) | One-course advice conflicts with a three-step Python resource stack and multi-course M2 outcomes. MITx 18.01.1x alone cannot cover all M2. Define one primary resource **per bounded pass**, not one course supposedly covering unrelated advanced extensions. |
| F10 | P1 | [F:329–368](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L329-L368), [453–475](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L453-L475) | Introductory concepts are mixed with full Axler, Krylov solvers, Orlicz norms, and Radon–Nikodym derivatives. Preserve these as extensions. Axler describes its text as a second course [S18]. |
| F11 | P0 | [F:297–302](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L297-L302) | AD complexity conflates a single JVP/VJP with constructing a full Jacobian. Fix notation and qualify “always” scalar outputs in ML [S11]. |
| F12 | P0 | [F:314–318](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L314-L318) | A universal `1e-6` gradient check lacks dtype, scale, step size, and domain conditions. The fast lane skips analytic gradients yet must pass an unspecified comparison. The memo presupposes momentum beats GD on Rosenbrock. Require independent references and ask **whether/when** optimizers win [S12]. |
| F13 | P0 | [F:487–490](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L487-L490) | The random walk lacks start, transition probabilities, boundaries, and stopping rule. Fixed-seed agreement is not a statistical guarantee. Specify the stochastic model, uncertainty, and censoring; separate deterministic tests from stochastic experiments. |
| F14 | P1 | [F:357–362](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L357-L362); [project rule:93–101](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/README.md#L93-L101) | M3 has five compulsory mini-projects but lacks the common test/README/memo specification. Add centering, non-unique SVD factors, rank-deficiency tests, and offline fixtures. |
| F15 | P1 | [START-HERE:87–95](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/START-HERE.md#L87-L95) | “Passing quizzes is not evidence; a repository is” confuses visibility with competence. Both can provide different evidence. Add independent transfer checks and delayed retrieval. Keep course assessment answers private where required [S09, S13, S14]. |
| F16 | P1 | [F:60](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L60), [101](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L101), [158–162](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L158-L162), [219](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L219) | Claims such as “60%+ of self-learners,” “10× force-multiplier,” and industry universals lack adequate support in the inspected text. Difficulty is not proof of learning. Replace hype with bounded motivation; distinguish testimony from research. |
| F17 | P1 | [tracker:20–27](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/guides/progress-tracker.md#L20-L27), [59–60](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/guides/progress-tracker.md#L59-L60) | Checkbox labels concatenate alternatives with `+`; one project checkbox covers M1–M5. Track chosen path, individual gates, artifact locations, and review dates. |
| F18 | P1 | [F:290–295](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L290-L295), [329–332](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L329-L332), [471–475](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/curriculum/1-foundations.md#L471-L475) | Short budgets combine several university courses and advanced extensions. MIT estimates about **150 hours for 18.06 alone** [S04]. Re-estimate selected scope, including practice and projects. |
| F19 | P2 | [tools README:5–9](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/tools/README.md#L5-L9) | The link-check workflow is staged under `tools/`, not active in `.github/workflows/`. Install only with approved permissions. Add semantic review: a green link checker cannot catch prerequisite loops or paywalls. |

## 3. Prerequisite-safe architecture

### 3.1 Preserve module IDs; define learning passes

Do not rename `module-0` through `module-5`, delete `math-diagnostic`, or renumber later modules. Introduce explicit sub-pass anchors inside the existing page. The following labels are proposed learning passes, not new top-level modules.

```text
Algebra screen -> M0a targeted remediation, where needed
Logic screen   -> M0b core proof/notation bridge
Python screen  -> M1 core -> M1 scientific-Python bridge

M0a readiness --------------------------> M2a single-variable calculus
M0a + M0b notation/definitions ----------> M3 vector basics -> M3 core linear algebra
M2a + M3 vector basics -----------------> M2b multivariable calculus
M2b + M3 core --------------------------> M2c matrix calculus/basic optimization

M0b counting/logic ---------------------> M5a discrete probability
M5a + M2a integration ------------------> M5b univariate continuous probability
M5b univariate + M2b integration slice
  + M3 vector/matrix basics ------------> M5b joint/vector probability and exit
M1 + M0b proof/counting ----------------> M4 deterministic algorithms
M4 core + M5a --------------------------> M4 randomized/streaming extension

M2b/M2c + M3 core + M5 core + M1 --------> optional full EE364A extension
M0b + M3 core --------------------------> optional Axler proof extension
M5 core + suitable real analysis -------> advanced probability extension
```

**Meaning of the edges:** a named skill means demonstrated readiness, not compulsory completion of every earlier module. M3 vector basics covers vectors, dot products, matrix shapes/products, transpose, and linear maps; it is a checkpoint inside M3, not another course. Basic notation can be learned alongside M3; a completed 8–12-proof portfolio is not an entry requirement for computational linear algebra. M2b's integration slice means iterated integrals over simple domains and change of variables before joint-density transformations, not the whole optimization pass. Teach covariance in M5; do not require it beforehand. Full Stat 110 states calculus (mainly single-variable) and matrix familiarity as prerequisites [S25]. A discrete-first selection is our curricular adaptation, not Harvard's full-course prerequisite policy.

**Coding gate:** numerical labs in M2/M3/M5 additionally require the M1 scientific-Python bridge. Paper-based mathematics need not wait until the Weather CLI is finished. M5a can begin without calculus; its simulations need Python. This separates prerequisites for understanding mathematics from prerequisites for implementing it.

Provide a plain-text ordered list alongside any diagram. Color or a diagram renderer must not be necessary to navigate.

### 3.2 Avoid a false choice between exhaustive theory and videos

| Depth | Meaning | Evidence |
|---|---|---|
| **Core** | Bounded, problem-solving foundation for the track; includes reasoning and code. | Independent gate, selected practice, working artifact, explanation. |
| **Reinforcement** | Replacement explanation or extra practice for a detected gap. | Re-attempt that objective; no unnecessary module restart. |
| **Research extension** | Deeper proofs, numerical methods, measure theory, or specialized algorithms. | Explicit prerequisites and extension-specific problems. |

The applied fast lane may be shorter, but still needs shape reasoning, probability calculations, debugging, and independent explanations. Mark **partial** completion honestly. A short M5 intuition pass is not sufficient evidence for M6's full prerequisite contract.

### 3.3 Honor downstream dependencies

Before moving a topic, resolve its consumer:

- M6 explicitly expects MGFs, CLT, and joint distributions: keep an elementary MGF component in full M5 core unless a separate M6 change is approved.
- M9 explicitly expects Normal/Student-t distributions and M11 expects multivariate Gaussian distributions: retain these in full M5, including conditions and elementary calculations. Their presence is not optional just because an abbreviated topic list omits them.
- M10 expects Lagrange multipliers and quadratic forms: require a just-in-time optimization bridge before its derivation track.
- M15 currently names “M3 (matrix calculus),” although the main matrix-calculus block lives in M2: point to the actual retained sub-pass.
- M8a/M8b assume randomized/streaming algorithms; M8b also assumes async Python. If these leave M4/M1 core, link explicit extensions before those modules.
- Leave SQL, dataframe engineering, full ML modeling, deployment, and GPU programming outside this revision except for necessary prerequisite cross-links.

### 3.4 Default route and bounded resource contract

One simple valid order is: **targeted M0 and M1 → M3 → M2a → M5a → M4 deterministic core → M2b → M2c → M5b**. M0 and M1 may run alongside each other; M3's paper mathematics need not wait for M1's project. M2a and M3 may be interchanged once their skill gates are met. M5a may start earlier after counting/logic readiness. This is a default navigation path, not a newly validated optimal sequence; stable module numbers remain unchanged. Prefer at most one substantial mathematics pass and one coding pass at a time as a workload heuristic, not a requirement.

| Pass | Primary instruction and bounded selection | Practice/feedback route | Stop condition |
|---|---|---|---|
| M0a / M0b | Khan only for missed algebra skills; Hammack selected sets, logic, counting, proof, relations/functions sections [S01]. | Selected text exercises/hints plus original rubric-scored proofs. | Relevant readiness gaps repaired; proof portfolio for full M0b credit. |
| M1 / numerical bridge | CS50P core [S02]; official NumPy array/shape/indexing/linear-algebra/RNG basics [S10]. | Course tasks under its own rules; original CLI and small array exercises. | Python and numerical readiness demonstrated; one artifact may supply multiple evidence items. |
| M2a | MIT 18.01SC differentiation, integration, and selected approximation/series material [S21]. | OCW problem sessions and exams/solutions; selected, not all course content. | Single-variable outcomes demonstrated, including integration needed by M5. |
| M3 | MIT 18.06SC systems/subspaces, least squares, eigenvalues/PSD/SVD [S04]. | OCW problems/solutions plus the bounded least-squares/PCA lab. | Computational, geometric, reasoning, and numerical-stability outcomes demonstrated. |
| M2b / M2c | Selected MIT 18.02SC topics via the official course linked in S03; then MML chapter 5 and selected chapter 7 material [S19]. | OCW practice plus original shape-checked derivative/optimization problems. | Multivariable prerequisites and compact gradient-lab outcomes demonstrated. |
| M4 deterministic | Selected MIT 6.006 notes on complexity, structures, sorting, graph search, and DP [S06]. | Mapped course problems and a bounded original search/DP artifact. | Core invariants, algorithms, and boundary cases demonstrated; not full-course equivalence. |
| M5a / M5b | Selected Stat 110 counting through discrete expectation; then continuous/joint distributions and retained downstream topics [S07, S25]. | Harvard strategic practice, mixed homework, and available solutions [S08]. | Full M5 exit includes the downstream checklist in Section 3.3, not just simulation. |

**Required before learner-facing release:** replace topic-level selections with a compact manifest: outcome ID, edition/session/section, selected exercise identifiers, feedback location, artifact/gate evidence, prerequisites, and estimated effort. Verify each selection actually exists and covers its outcome; never invent exercise numbers. This table is a scope blueprint, not a finished week-by-week syllabus. If a core outcome has no mapped instruction or feedback, either supply an original reviewed exercise or explicitly propose moving that outcome; do not declare the pass implementation-ready.

“One primary resource” does not mean “one course plus a compulsory second textbook.” A course's own notes/book and exercises may be sufficient. MML is a useful reference but its main exercise solutions are offered through an instructor-manual request; the public page also lists separate additional exercises and tutorial solutions [S19]. Do not assume all textbook answer keys are freely available to self-learners. This outcome–instruction–assessment alignment follows CMU's design guidance [S26], not a claim of measured effectiveness for this exact route.

## 4. Module-by-module improvements

### M0 — Mathematical maturity bridge

**Keep:** algebra/functions, quantifiers, definitions, counterexamples, direct proof, contrapositive, contradiction, induction, sets, and basic counting.

**Improve:**

1. Assess algebra repair and proof literacy separately. A learner may need one without the other.
2. Replace “do 200 exercises” as the apparent completion bar with a mapped selection and a proof portfolio. Extra exercise volume remains available.
3. Use Hammack chapters 1–10 selectively; add targeted sections from **11–12** for relations, functions, injection/surjection, and image/preimage. The current chapter range does not cover all named outcomes [S01].
4. Move extensive number theory, the Chinese Remainder Theorem, advanced cardinality, and proof assistants to extensions. Preserve induction and counting needed by M4/M5.
5. Change “check every symbolic claim within five minutes” to: use computation to find mistakes; successful numerical checks do not replace proof. State domains and assumptions. For real x, `sqrt(x**2) = abs(x)`, not generally x.
6. Replace claims that all non-completers cannot reason with a concrete readiness check recognizing prior knowledge.

**Exit artifact:** 8–12 original short proofs/counterexamples, revised after feedback, plus a notation/error log. Use original questions or references to external exercises, not copied textbook chapters.

**Gate:** negate nested quantifiers; distinguish converse from contrapositive; find a counterexample; prove a simple statement by induction with a correct base case and induction step. Grade domain/statement, strategy, logical validity, and explanation separately.

**Resource choice:** Hammack remains the primary free text; Khan is targeted precalculus remediation. Velleman and Lean are optional. Hammack's PDF states **CC BY-NC-ND 4.0**, not this repository's CC BY-SA license [S01]. Free reading does not authorize unrestricted adaptation or republication.

### M1 — Python and scientific-computing readiness

**Keep:** CS50P, reading/debugging code, exceptions, file I/O, functions, basic classes, tests, Weather CLI, and deliberate AI use.

**Core boundary:** basic Python → modular CLI → tests/simple annotations → scientific-Python bridge. Defer advanced `Protocol`/`Generic`/`Annotated`, async frameworks, production Pydantic, branch protection, Docker, and multi-framework setup to later bridges. Property-based testing is useful reinforcement, not an industry-universal entry requirement.

**Add a 10–15-hour scientific-Python bridge**, included in the proposed M1 budget:

- Arrays versus lists; `shape`, `ndim`, `dtype`; 1-D arrays versus row/column arrays.
- Indexing, masks, copies/views, `axis`, broadcasting, `*` versus `@`.
- Translating a sum/dot product into code; checking a loop against vectorized code.
- `float64`, approximate comparisons, non-finite values, and simple plotting.
- `np.random.default_rng(seed)` and RNG injection rather than repeatedly resetting global state.
- Running a script from a clean environment; avoiding hidden notebook state.

Use official NumPy material [S10] as a focused bridge. Keep pandas/Polars and substantial data cleaning in M7. NumPy introduced `Generator` in 1.17; legacy global `np.random` functions did not all change to the new generator [S22].

**Weather CLI acceptance refinements:**

- State the free API provider and relevant usage terms; offer a local fixture adapter. Under the proposed access policy, an offline fixture mode must satisfy core assessment without signup or a live request; a successful live demo may be optional. This relaxes the existing real-API deliverable and therefore needs approval, not an errata-only edit.
- Required tests need no API keys or live network. Test valid data, missing city, malformed response, timeout, and cache hit/expiry.
- Define cache key, expiry, units, and malformed-cache behavior.
- Accept either simple functions or justified classes. Architecture should serve the program, not demonstrate OOP unnecessarily.
- Keep CI a stretch unless its mandatory status is deliberately changed everywhere.

**Gate:** debug an unfamiliar short program; write a small file-processing function unaided; explain aliasing; fix a broadcasting error; show a test detects a deliberately introduced bug.

**Resource choice:** CS50P already works as the primary beginner course. Its official site supports browser-only study [S02], so VS Code should not be mandatory for entry. Scrimba/Helsinki are alternatives, not compulsory lead-ins. The free learning route and optional certificates must be labeled separately.

### M2 — Calculus, matrix calculus, and optimization

**Three passes:**

- **M2a:** functions, limits, derivatives, chain rule, Taylor approximation, integration, substitution/integration by parts, and elementary numerical integration.
- **M2b:** partial derivatives, gradients, directional derivatives, Jacobians, Hessians, multiple integrals, change of variables, and one constrained-optimization example. Requires relevant M3 vector/linear-map knowledge.
- **M2c:** scalar objectives of vectors, shape-checked chain rules, least-squares gradients, a small computational graph, GD, and a JVP/VJP introduction. Requires M3 core.

**Defer:** a full vector-field theorem sequence, calculus of variations, differentiation through SVD/ODE/PDE solvers, all cone-program families, full duality theory, and exhaustive optimizer APIs. Retain links with later-use cases. Full EE364A belongs after its linear-algebra and probability prerequisites [S05].

**Correct AutoDiff wording:** for `f: R^n -> R^m` with evaluation cost C, a single directional JVP or VJP typically costs a constant-factor multiple of C under the usual AD model. Constructing a full Jacobian by basis sweeps takes roughly n forward sweeps or m reverse sweeps. Reverse mode is especially suitable for scalar-loss gradients, not universally best for all ML computations. Explain the reverse-mode memory trade-off [S11].

**Gradient lab:** start with finite differences, analytic gradients for a quadratic and Rosenbrock, and plain GD. Add momentum, Adam, and logistic loss in staged extensions, or keep them required only with sufficient instruction and workload allowance.

**Acceptance contract:**

- State formulas, dimensions, dtype, test/start points, stop criteria, iteration caps, and learning rates.
- Use central finite differences over a small logarithmic step-size sweep. Report absolute and scale-aware relative error; smaller h is not always better. SciPy `check_grad` uses **forward**, not central, differences and returns an L2 error [S12]; do not claim it implements this proposed central-difference experiment.
- Test deterministic, smooth, well-scaled fixtures with documented tolerances. `1e-6` can be a fixture-specific target, not a rule for arbitrary functions/dtypes [S12].
- If a fast-lane learner skips derivations, supply independent reference gradients. Do not compare finite differences with the same implementation used as its own oracle.
- Assert expected behavior on a convex quadratic; report Rosenbrock successes/failures. Ask **whether and under what settings** momentum outperforms GD, not why it necessarily does.
- Contour trajectories apply to two-dimensional objectives; use suitable summaries otherwise.
- For a convex quadratic `f(x)=0.5*x.T@H@x-b.T@x`, state that H is symmetric positive definite and use `0 < alpha < 2/lambda_max(H)` for the fixed-step GD convergence fixture. A stop on iteration limit is not convergence. Include non-finite iterates and invalid shapes as explicit failure states.
- If using JAX in an extension, enable `jax_enable_x64` before creating arrays/compiling and assert the actual dtype, or explicitly use a 32-bit error budget. JAX defaults to 32-bit mode and may truncate a requested `float64` when X64 is disabled [S28]. AD does not make a nonsmooth point differentiable; avoid such points in the smooth gradient contract.

**Resource choice:** use a complete open MIT 18.01SC route rather than a lone differentiation-course link [S21]. Select 18.02 material for M2b and MML chapter 5 for a compact M2c bridge [S19]. Full MIT matrix calculus is optional deeper study, not an unannounced beginner prerequisite.

### M3 — Linear algebra

**Core:** vectors/maps, systems, rank/null space, basis, orthogonality, projections, least squares, QR, symmetric eigenproblems, PSD matrices, SVD, conditioning, and PCA geometry. Teach before M2c.

**Retain as extensions:** Axler's deeper operator theory/proofs; randomized SVD; Lanczos/Arnoldi/GMRES; advanced sparse methods; low-precision GPU issues. Fix the “two-pass” heading that currently contains three passes.

**Project proposal:** one coherent **least-squares + PCA lab**, with two sections sharing tests and a memo. Image compression, PageRank, and spectral clustering become extensions. This changes mandatory requirements and needs approval. Until approved, add a clear definition of done to all five existing minis.

**Acceptance contract:**

- Begin with a tiny synthetic matrix; offer a bounded MNIST subset or other dataset later. Tests run offline.
- Compare QR/SVD/`lstsq` on well-conditioned, ill-conditioned, and rank-deficient cases. A basic reduced-QR plus triangular solve assumes full column rank; it should detect/reject rank deficiency or use a documented rank-aware fallback, not be required to return the same unique coefficient vector on every matrix. Normal-equation inversion is a cautionary demonstration, not the default solver [S20].
- Set and report the numerical rank cutoff. `lstsq` returns a minimum-norm least-squares solution; its empty `residuals` array does **not** imply zero residual. Compute `norm(A @ x - b)` directly. With nonunique minimizers, compare fitted values/objective and, only when required, the minimum-norm property [S20].
- Distinguish residual size, coefficient error, and sensitivity. A tiny residual need not mean accurate coefficients.
- PCA: center columns, state scaling policy, and choose the smallest k such that `sum(s[:k]**2)/sum(s**2) >= 0.95` when variance is positive. Handle zero variance explicitly.
- Verify reconstruction and rank-k error against the singular-value tail within tolerance.
- Do not compare singular/eigenvectors by exact sign. Compare reconstruction or an identified subspace; repeated singular values at the truncation boundary need special care.
- If evaluating prediction, fit centering/PCA only on training data. Label a pure reconstruction demonstration as such. Before M5, explain `X_centered.T @ X_centered` as a centered Gram matrix and PCA as reconstruction/geometry; introduce population covariance and sampling interpretation in M5 rather than silently assuming them in M3.

**Gate:** reason about shapes, recognize non-invertibility, explain projection, solve a small system, and diagnose ill-conditioning. Research learners add selected proofs; proving the spectral theorem is not a universal applied gate.

**Resource choice:** MIT 18.06SC primary [S04], MML chapters 2–4 free reference [S19], Axler optional second course [S18]. Correct Fessler/Nadakuditi attribution if retaining that paid extension [S17].

### M4 — Algorithms and data structures

**Core:** complexity, invariants, arrays/lists/dicts/sets, stacks/queues/heaps, binary search, sorting, recursion, BFS/DFS, shortest paths, and a small DP formulation. Link each to a data task: top-k records, deduplication, dependency ordering, or path search.

**Readiness:** M1 plus demonstrated proof/counting knowledge and a small recursion/graph-notation bridge. MIT 6.006's full published prerequisites include sets, relations/logic, combinatorics, proofs, recursion, number theory, graph theory, **and probability** [S06]. A selected deterministic path can start earlier only after its actual lessons and exercises are screened for these dependencies. Expected-time hashing/randomized quicksort and streaming error analysis require appropriate M5a knowledge; worst-case and amortized analysis are not the same as expected-case analysis. Problem Set 0 is useful optional self-study evidence, not a guarantee that the brief M0 bridge substitutes for all 6.042J. For full 6.006, honor its full readiness contract.

**Defer:** all balanced-tree variants, every string-matching algorithm, Karger's algorithm, PTAS/FPTAS, and primal-dual algorithms from the universal core. Keep the specific hashing/streaming topics expected by M8a/M8b in a named data-engineering extension.

**Meal-planner acceptance contract:**

- Define the finite food list, integer servings/caps, units, objective, tolerances, repeat rule, and meaning of a meal/day.
- Start with a tiny one-day exact-search fixture, then expand to seven days.
- Cross-check small cases by exhaustive enumeration. Independently validate constraints on every returned plan.
- Distinguish **optimal**, **feasible**, **infeasible**, and **unknown/time limit**. Timeout is not proof of infeasibility.
- Compare identical formulations, inputs, objectives, and budgets. State complexity for the actual problem; do not indiscriminately call an optimization problem “NP-complete.”
- Make solver comparison a stretch or supply a small modeling bridge. Core DSA must not secretly require an integer-programming course. Avoid a single project that demands every listed algorithm: use short separate invariant/BFS/DP problems for uncovered outcomes rather than expanding the meal planner. Treat food data as synthetic educational inputs, not dietary or medical advice.

**Gate:** state a loop invariant, analyze time/space cost, trace BFS, select a data structure, and implement one DP recurrence with boundary cases.

**Resource choice:** Python-based MIT 6.006 rather than a compulsory Java course in parallel. Its syllabus says CLRS is useful but **not required**; free notes and exercises remain the default [S06].

### M5 — Probability

**Core sequence:** sample spaces/counting → conditioning/Bayes → discrete RVs → expectation/variance → continuous RVs/integration (including Normal/Student-t) → joint distributions/covariance and multivariate Normal → conditional expectation → LLN/CLT and elementary MGF use → simple Monte Carlo. Include finite-state Markov-chain basics and elementary entropy/cross-entropy where later modules need them.

**Research extensions:** sub-Gaussian theory, McDiarmid/Bernstein in depth, Orlicz norms, Fano, Radon–Nikodym derivatives, and dominated/monotone convergence. Supply genuine prerequisites and exercises, not a reassurance-only preview. Explain that MGFs may not exist, and an MGF proof of CLT uses stronger assumptions than the usual IID finite-variance CLT statement.

**Practice:** directly link Harvard's topic-organized strategic practice **and** mixed homework with solutions [S08]. Topic practice builds fluency; mixed problems test method selection. Replace “30 lines proves you learned probability” with readable work and explicit assumptions.

**Monte Carlo model specification:**

1. **Birthday:** IID uniform birthdays over a stated number of days; disclose the simplification.
2. **Monty Hall:** host knows the prize, always opens an eligible goat door, always offers switching; specify tie-breaking if necessary.
3. **Coupon collector:** IID uniform draws over m types; expectation is `m * sum(1/k for k in 1..m)`.
4. **Random walk:** simple symmetric walk on `{0,...,N}`, start at i, absorbing boundaries 0 and N, and T = first absorption. Compare absorption probabilities and `E[T] = i(N-i)`. Compute finite-horizon hitting-time probabilities by a state-probability recurrence; report survival beyond the horizon rather than discard unfinished paths.

**Testing policy:**

- Separate exact deterministic invariants/tiny enumerations from stochastic estimation experiments.
- Seeds support reproducibility under stated conditions, not correctness guarantees or universal cross-version bitwise identity. Record NumPy version, bit generator, seed, call shapes/order, and environment; its compatibility policy is deliberately narrower than “same seed always means same output” [S27]. Choose sample counts and tolerances before examining results.
- For K IID Bernoulli estimation tasks, a sufficient Hoeffding/union-bound budget for absolute error at most epsilon with total failure probability at most delta is `N_trials >= log(2*K/delta)/(2*epsilon**2)`. This bound does **not** automatically cover unbounded hitting times or coupon-collection times.
- Use separate moment/error analysis for unbounded quantities; report assumptions. Do not make stochastic continuous-integration tests depend on a brittle “one seed must pass a 95% confidence interval” assertion. State whether “CI” means continuous integration or confidence interval.
- For a bounded first version of the absorbing-walk experiment, estimate `P(T <= H)` and `E[min(T,H)]` at a stated horizon H, alongside the survivor fraction. For integer-valued T, `E[min(T,H)] = sum(P(T > t) for t in 0..H-1)`; compare with the finite-state recurrence. Never label a truncated mean or the mean of completed paths as `E[T]`. The untruncated mean comparison needs separately justified simulation/error control.
- For coupon collection, use the exact expectation as an analytic reference; simulation intervals for its unbounded time need their own justification. Report standard-error approximations as approximations, not a finite-sample guarantee. Do not repeatedly change seeds/sample counts until a desired result passes.
- Plot multiple independent replicate runs; empirical errors need not shrink monotonically.
- LLN is not a finite-sample error bound. The usual Monte Carlo `1/sqrt(N)` standard-error behavior needs appropriate variance/dependence conditions; include a heavy-tail counterexample.

**Gate:** compute a Bayes posterior, distinguish independence from zero correlation, use a joint table, calculate expectation/variance, state CLT assumptions, and explain simulation uncertainty.

**Resource choice:** Stat 110 and Blitzstein–Hwang remain the default [S07, S08]. Stanley Chan is a computational alternative; the current author site lists a **2026 second edition**. Update old metadata only alongside chapter/exercise remapping [S23]. MacKay and Vershynin should not become two additional cover-to-cover requirements.

## 5. Diagnostic and assessment design

### 5.1 Replace the broken diagnostic with an original, two-purpose screen

Keep a 15-item diagnostic if desired, but explicitly separate **entry readiness** from **placement checks**. Do not claim this new instrument is standardized, psychometrically validated, or equivalent to passing university exams.

Proposed original item blueprint below. Allow paper or accessible text responses. Budget approximately 45–60 minutes initially, offer untimed use, and revise the timing after pilots. Answers should be separate or collapsed in the learner-facing version.

| # | Strand | Original sample item | Expected answer / evidence |
|---|---|---|---|
| 1 | Algebra | Solve `3(2x-1)=9`. | `x=2`, with valid rearrangement. |
| 2 | Algebra/functions | For `f(x)=log(x-1)`, state the real domain; solve `f(x)=0`. | `x>1`; solution `x=2`. |
| 3 | Algebra/functions | With `f(x)=x^2`, `g(x)=x+1`, compare `f(g(x))` and `g(f(x))`; are they equal for every real x? | `(x+1)^2` versus `x^2+1`; no, e.g. `x=1`. |
| 4 | Logic | Negate: “For every real x there exists real y such that y>x.” | “There exists real x such that for every real y, y<=x.” |
| 5 | Proof | Prove the sum of two odd integers is even. | Write `2a+1` and `2b+1`, sum `2(a+b+1)`. |
| 6 | Proof | Disprove: if `ab=0` for real a,b, then both a and b are zero. | Counterexample such as `a=0,b=1`. |
| 7 | Python | What does `a=[1]; b=a; b.append(2); print(a)` output, and why? | `[1,2]`; both names refer to the same list. |
| 8 | Python | Write a function returning the number of positive numbers in a list. Include tests for an empty list and mixed signs. | Correct loop/comprehension and boundaries; count only values `>0`. |
| 9 | Python | A function divides by `len(xs)`; what must it do when xs is empty? Give a defensible contract and a test. | Explicit policy such as `ValueError`; consistency between contract and test. |
| 10 | Calculus placement | Differentiate `(3x+1)^2`, naming the rule. | `6(3x+1)`; chain rule. |
| 11 | Calculus placement | Evaluate the integral of `2x` from 0 to 1 and explain what it accumulates. | `1`; accumulated signed area/change. |
| 12 | Linear algebra placement | If A is `3x2` and B is `2x4`, what is the shape of AB? Is BA defined? | `3x4`; BA is not defined. |
| 13 | Linear algebra placement | Do `x+y=2` and `2x+2y=4` have a unique solution? Explain. | Infinitely many; second equation is redundant. |
| 14 | Probability placement | Disease prevalence is 1%; sensitivity 90%; false-positive rate 9%. Find P(disease given positive). | `0.009/(0.009+0.0891)`, approximately `9.17%`; not 90%. |
| 15 | Probability placement | Two fair dice: probability of total 7? Explain the sample space. | `6/36=1/6` from 36 equally likely ordered pairs. |

**Routing, not a misleading global pass score:**

- Items 1–3: targeted M0a repair for missed skills. Do not infer trigonometry/complex-number readiness from this tiny sample; screen those separately before using them.
- Items 4–6: M0b reasoning bridge where needed. Passing these does not certify induction, relations, or all M0 outcomes.
- Items 7–9: M1 entry; demonstrated competence can trigger a larger M1 challenge assessment rather than forced repetition.
- Items 10–15: failure means “study this later module,” not “repeat all M0.” Success merely invites its complete challenge gate; it never waives an entire module by itself.
- M4 gets its own readiness gate for induction, counting, recursion, and complexity, rather than adding advanced algorithms to a beginner entry screen.

Initially score each item as **demonstrated / partial / not yet**, with a brief reason. Use **not attempted / not previously studied** as a separate administrative status rather than inferring a misconception from a blank response. Let a complete novice skip later placement items and start M0/M1; the 15-item screen is optional routing support, not an admission exam. Avoid arbitrary combined percentages for these heterogeneous skills. A maintainer-reviewed gate can later adopt cut scores after piloting.

### 5.2 Module completion must combine evidence

Propose the following common contract for M0–M5:

1. **Practice evidence:** selected problems mapped to core outcomes, including corrections.
2. **Independent gate:** a small unseen or equivalent task without AI-generated solutions, with reasonable accessibility accommodations.
3. **Artifact evidence:** correct project/proof portfolio, appropriate tests, reproducible instructions, and a short limitations memo.
4. **Explanation:** a brief written or oral defense of one result, assumption, and failure mode.
5. **Delayed check:** a short retrieval/reapplication task approximately two weeks later; missed skills trigger targeted review, not automatic loss of all progress. Record “core evidence complete; delayed review due” and allow progression once immediate prerequisite skills are demonstrated. Do not add a compulsory two-week wait between modules.

A provisional rubric can score **correctness, reasoning, verification, and communication** from 0–3. Use these anchors for each dimension: **0** = absent/invalid; **1** = partial, with a substantive gap or substantial prompting; **2** = adequate independent demonstration for the stated task; **3** = adequate plus a valid changed-case explanation or limitation. Communication measures an understandable argument, not accent, speed, verbosity, or visual polish. Record missing/unattempted work separately from an evaluated zero.

For a provisional readiness decision, require at least 2 in correctness and reasoning on the specified critical skills, appropriate verification for the task, and a targeted repair for any critical gap. Do not average a broken method away with presentation points. The task-specific rubric must define what counts as a critical error and what verification is applicable. These are pilot rules, not calibrated cut scores; compare example responses and evaluator agreement before claiming reliability.

**Publication policy:** original portfolio work can be public, but course assessment solutions, private data, credentials, or restricted material must not be. CS50P specifically restricts making assessment solutions available and using outside AI to suggest/complete answers [S09]. A curriculum's AI policy does not override the source course's policy. Offer private review or sanitized evidence where necessary.

### 5.3 Gate operations and original calibration examples

**Keep the system light:** reuse selected practice and existing projects as evidence. The proof portfolio is M0's artifact, not an additional project. One well-designed task may show several outcomes. A full M1 course project may count as the CLI artifact only if its outcomes match and source-course sharing rules permit the chosen evidence; do not force duplicate projects merely to fill boxes. Module credit remains distinct from external course credit/certification.

**Who reviews:** self-learners may compare against reviewed keys and mark evidence **self-assessed**. A peer/tutor/maintainer can mark it **independently reviewed**, stating the reviewer role and what was checked; this is not institutional accreditation. An AI tutor can provide hints or feedback where allowed but cannot supply independent assurance of its own generated key or grade. Where no reviewer is available, preserve honest self-assessment status rather than making a paid tutor a hidden prerequisite.

**Answer exposure and retakes:** publish worked practice and rubric examples openly. After seeing a key, do not call the identical question “unseen.” Use a reviewed parallel form requiring a changed reasoning step, not just renamed variables. Retake only the missing objective after feedback and practice; log attempt, assistance, and changes. In an open repository, task secrecy is not guaranteed, so avoid proctoring/certification claims. Use “independent attempt on a changed task” where unseen status cannot be established. Do not require cameras, biometrics, or invasive monitoring.

The following original examples calibrate expectations; **they are public practice, not a complete challenge bank or a module waiver**:

| Pass / objective | Public example | Key evidence and likely misconception |
|---|---|---|
| M0b / induction | Prove `1+3+...+(2n-1)=n^2` for integers `n>=1`. | Base `n=1`; assume the sum for n, add `2n+1` to obtain `(n+1)^2`. Checking a few n values is not a proof. |
| M1 bridge / shapes | `X` has shape `(4,3)` and `y` shape `(4,)`. How do you subtract y from every column of X? | `X - y[:, None]`, result `(4,3)`, checked against nested loops. `X-y` does not broadcast; summing along the wrong axis is not a repair. |
| M2c / derivative | For `f(w)=0.5*sum((Aw-b)^2)` (Euclidean least squares), give the gradient and its shape when A is `(m,n)`. | `A.T @ (A @ w - b)`, shape `(n,)`; explain the chain rule and test a nonstationary point. A zero-only test misses many bugs. |
| M3 / rank | Let `A=[[1,1],[2,2]]`, `b=[1,2]`. Describe least-squares solutions and the minimum-norm one. | Every `x1+x2=1` fits exactly; minimum-norm solution `(0.5,0.5)`. Nonunique coefficients do not mean different fitted values. |
| M4 / bounded DP | Minimum number of coins totaling t with denominations `{1,3,4}`, unlimited copies, integer `t>=0`. Give recurrence and solve t=6. | `D[0]=0`; `D[t]=1+min(D[t-c])` over `c<=t`; `D[6]=2` using `3+3`. Greedy `4+1+1` fails; state time `O(t*k)` for k denominations. |
| M5 / independence | X is uniform on `{-1,0,1}`; `Y=X^2`. Are X and Y uncorrelated? Independent? | `E[X]=E[XY]=0`, so covariance is zero; not independent since `P(Y=0 given X=0)=1` but `P(Y=0)=1/3`. |

Before release, complete the outcome manifest and create reviewed parallel tasks for each critical skill not covered here. Record two types of evidence separately: **instructional coverage** (what was taught/practiced) and **assessment coverage** (what the learner demonstrated). A single correct gradient or Bayes question cannot certify all M2/M5 outcomes [S26].

## 6. Learning workflow and workload

### 6.1 Research-backed learning practices, with honest limits

Dunlosky et al. rate **practice testing** and **distributed practice** highly across varied learning settings [S13]. The IES guide recommends alternating worked examples with independent problems, fading guidance, linking concrete and abstract representations, and asking explanatory questions [S14]. AERO synthesizes evidence for spaced retrieval and notes that there is **no single optimal spacing interval** [S24].

Apply those principles without claiming an exact schedule is scientifically optimal:

1. Attempt a short retrieval question before reopening notes.
2. Study one worked example and explain each step.
3. Solve a similar problem with partial guidance.
4. Solve a changed problem independently.
5. Get corrective feedback; record the mistake and its cause.
6. Revisit the skill after a delay and in a different context.

**Suggested review dates:** 2, 7, 14, and 45 days after initial study, adjusted to forgetting and task difficulty; the approximately day-14 task can serve as the delayed check rather than adding another assessment. These are an operational starting point, not research-established universal intervals.

**Example 10-hour week:** 3 hours course/reading, 3 hours exercises, 2 hours project work, 1 hour cumulative retrieval, 1 hour feedback/correction. Adjust ratios for experience and topic; do not turn a “2:1 build-to-watch” heuristic into a universal law.

**Inter-module retrieval examples:**

- In M3, reuse M0 proof habits to explain why a proposed set is not a subspace.
- In M2c, reuse M3 shape reasoning when deriving a least-squares gradient.
- In M5, revisit M0 counting and M1 simulation code on the same probability question.
- In M4's randomized extension, revisit M5 expectation rather than introduce probability notation without preparation.

These sources support design principles, not a proven outcome for this specific repository. The IES guide primarily targets school instruction, although it discusses college research; transfer to adult self-study should be evaluated, not assumed.

### 6.2 An honest planning envelope

The following is a **proposed selected-core budget**, not an instruction to finish every linked course/book, not an institution's official estimate, and not a promise of employment. It includes practice and artifacts but excludes deep research extensions.

| Area | Proposed active study hours | Scope/assumption |
|---|---:|---|
| M0 targeted bridge | 40–80 | Depends strongly on prior algebra/proof knowledge; may be partially waived. |
| M1 core and NumPy bridge | 100–150 | One primary Python path, Weather CLI, numerical readiness. |
| M2a–c | 140–220 | Selected single/multivariable calculus and compact matrix-calculus bridge; not all EE364A/18.S096. |
| M3 core | 120–170 | Computational/geometric course with selected applications, not full Axler plus all advanced material. |
| M4 core | 80–120 | Selected algorithmic spine and bounded project, not the entire extension menu. |
| M5 core | 120–170 | Probability practice and simulation; no full measure-theory/concentration course. |
| **Total** | **600–910** | Before individual waivers or extra remediation. |
| **With illustrative 10% revision buffer** | **660–1,001** | About 66–100 weeks at 10 hours/week, or 33–50 at 20 hours/week. |

These are active-work hours, not video runtimes or attendance counts. Credit reused artifacts and overlapping topics once; include gate preparation, feedback, and delayed review inside each module budget rather than charging them again. Track deep algebra remediation and any approved extension separately. A learner choosing a full alternative course with more hours must use that route's actual workload, not the default range.

Parallel study can improve sequencing but does not eliminate the total work. Measure actual hours from volunteers and revise these ranges. Do not substitute these Foundations-only figures for the repository's full-roadmap or employment claims without a separate scope review. MIT's roughly 150-hour 18.06 estimate is a useful reality check, not proof of the other numbers [S04].

### 6.3 Beginner access and privacy

- Give a CPU-only, low-bandwidth path; no paid API, GPU, deployment account, or large dataset should be needed for core assessment.
- Use browser-first instruction where available; provide a minimal local setup when projects require it.
- Provide text descriptions of diagrams, readable equations, and untimed practice options.
- Private review or sanitized portfolio evidence must be possible when publication would disclose sensitive data or violate a course policy.
- AI assistance for original practice can use hints, questions, and review of an existing attempt. Unassisted gates and source-course rules remain distinct.

## 7. Implementation backlog and file map

### 7.1 Respect the repository's contribution process

[CONTRIBUTING.md](https://github.com/akazadivu-design/data-sci/blob/a412833204cb334a9c7f96dcd9f3c66029fb38f4/CONTRIBUTING.md#L159-L172) requires an RFC for changes to prerequisite chains or curriculum shape, with approximately a month for comment before merging. It also asks contributors to discuss substantive rewrites first.

**Separate two tracks:**

- **Errata track:** factual corrections, broken URLs, unsupported version claims, correct license/access labeling, and precision fixes that do not silently alter learning requirements.
- **RFC-gated track:** sub-pass sequencing, mandatory-versus-optional scope, diagnostic routing, project-count changes, alternative completion evidence, and revised prerequisites.

A high priority does not grant permission to bypass review. Prepare the RFC and a proposed patch if requested, but do not claim proposed architecture is accepted or merge it automatically.

### 7.2 Prioritized work packages

Effort is an approximate **maintainer/agent editing-and-review budget**, not learner study time. External approval and learner pilots add calendar time.

| Plan | Work package | Depends on | Estimated effort | Completion evidence |
|---|---|---|---:|---|
| P1 | Freeze baseline and build claim ledger. | None | 2–4 hours | Commit SHA, inspected files, checker output, claim/source/access log. |
| P2 | Correct high-confidence errata and access/license labels. | P1 | 4–8 hours | Every changed claim has a primary source; no blanket free-audit claim or false author/license assertion. |
| P3 | Draft/submit RFC for core scope and dependency redesign. | P1 | 3–6 hours + review | Acyclic sub-pass graph, downstream mapping, alternatives, migration policy, maintainer decision. |
| P4 | Apply approved module structure and synchronize navigation. | P2, approved P3 | 8–16 hours | Every M0–M5 core outcome has prerequisites, one default resource/pass, practice, and gate. |
| P5 | Add diagnostic, assessment blueprints, and project acceptance criteria. | Approved P3, P4 | 10–20 hours | Actual original questions/keys, calibrated examples, deterministic/stochastic test policy, accessible options. |
| P6 | Validate and pilot; release with migration notes. | P4, P5 | 6–12 hours + pilot | No broken internal links, semantic review signed off, small pilot feedback, versioned change summary. |

**Recommended first implementation:** P1–P2 and the P3 RFC. This improves trust immediately without unexpectedly changing the requirements for current learners.

### 7.3 Existing files to modify, and why

| File | Authorized scope after appropriate review |
|---|---|
| `curriculum/1-foundations.md` | Core/extension labels, sub-pass anchors, corrected claims, default paths, project contracts. Keep it navigable, not a replacement textbook. |
| `guides/how-to-read-a-module.md` | Match the actual pass/resource choices and completion requirements. Remove misleading cumulative interpretations. |
| `guides/progress-tracker.md` | Separate each module/pass, chosen resource, gate, artifact, and delayed review. Avoid `+` strings implying every book/course. |
| `START-HERE.md` | Explain the usable entry screen and why publication is not the only evidence; avoid sending novices through graduate-level placement exams. |
| `README.md` | Make only necessary entry/track/free-access consistency corrections; preserve overall roadmap. |
| `curriculum/README.md` | Keep index titles consistent; amend project/completion policy only after approval. |
| `guides/practitioner-track.md` | Match prerequisite-safe re-entry, minimum practical math gates, and partial-versus-full completion. |
| `resources/books.md` | Correct authors, editions/licenses/access status; identify paid references as optional. |
| `guides/sources.md` | Add concise evidence categories and relevant research sources without turning learner pages into bibliographies. |
| `audit/VERIFICATION.md` | Append a dated section; do not overwrite historical checks or imply previous verification is current. |
| `CHANGELOG.md` | Record corrections and, when approved, scope changes and migration rules. |
| `curriculum/2-statistics-and-data.md`, `3-classical-ml.md`, `5-deep-learning.md` | Only dependency cross-links necessary to preserve M6/M8/M9/M10/M11/M15/M17 contracts; no unrelated expansion. |
| `tools/README.md` and existing staged workflow | Clarify/check workflow status; enable only with permission. Do not rerun historical split/build scripts. |

**Small new documents, only if approved and needed to control page length:**

- `coursepages/m0-m5-foundations/README.md` — shared assessment index and use instructions.
- `coursepages/m0-m5-foundations/diagnostic.md` — original 15-item screen and routing.
- `coursepages/m0-m5-foundations/assessment-guide.md` — answer guidance, rubrics, gate examples, and model/test contracts.

Do not create six empty course directories or add a web framework, package manager, or notebook suite to the curriculum repository. Learner code belongs in learner repositories unless maintainers explicitly approve a separate executable companion.

### 7.4 Migration for current learners

- Preserve previous project credit; do not require all projects to be rebuilt under a new format.
- Let learners document missing evidence against a short bridge checklist.
- Keep old explicit anchors and link legacy requirements to the corresponding new pass.
- Mark proposed/approved changes and effective date clearly.
- Do not call someone “done” in the full track when only the applied subset was completed.

### 7.5 Self-contained implementation handoff

**Authorized by this revision:** improve and submit this planning document for review. **Not authorized by merely accepting the report:** merge curriculum changes, enable Actions, change repository permissions, publish learner work, incur course/API charges, or treat an RFC as already accepted.

For a later implementation request:

1. Inspect the actual default branch and current diff; revalidate every claim touched by the patch. Use `master` only if it remains the default; do not assume `main` or overwrite concurrent work.
2. Work through P1–P2 first. If an “erratum” changes what learners must submit, its review classification is RFC-gated even if the change improves access or assessment.
3. For P3, present the proposed path, scope matrix, downstream topic owners, migration, and alternatives (minimal errata only; retain full courses with honest budgets; selected-core redesign). Obtain the maintainer decision through the repository's RFC process before implementing new requirements.
4. Treat the Section 3.4 manifest as the single **proposed** completion contract; after approval, publish its canonical requirements in the existing Foundations page and derive the guide/tracker wording from them. This audit plan must not become a competing learner syllabus.
5. For each P4–P5 patch, name an editing owner and a separate content reviewer where available. Require at least one manual prerequisite trace and one independent answer-key check; record missing review rather than fabricating sign-off. Keep documentation-only architecture.
6. Run link/diff checks and test the stated mathematical fixtures. Review changed-source access, not merely HTTP status. Submit a focused PR with scope, evidence, limitations, migration, and any changelog follow-up. Do not merge automatically.

**Access ledger fields:** source URL; course/edition; checked date; final destination; instruction/practice/feedback availability; signup/payment/region constraints; reuse license; reviewer observation; unresolved items. Use **verified for stated scope / partially verified / inaccessible in this check / not checked**. A 200 page can be a login or unrelated landing page; a 403/429/5xx can be transient or automated-access related, not proof the resource is permanently dead. Recheck required default paths at release and after reported failures; periodic maintenance is a proposed policy, not a claim of perpetual verification.

**Stop conditions:** no approved RFC for changed requirements; an unresolved prerequisite consumer; an invented/unverified exercise mapping; a required route blocked by payment; an incorrect answer key; or a failed validation. Report the blocker and retain current learner requirements. Approval must not be inferred from a green automated check.

## 8. Acceptance criteria

### Correctness and sequencing

- [ ] Every core outcome has a prerequisite location, instructional source, practice route, and assessment.
- [ ] M3 core does not require completion of advanced M2 matrix calculus.
- [ ] Matrix calculus requires the needed M3 and multivariable knowledge.
- [ ] Randomized algorithms name elementary probability prerequisites.
- [ ] M6/M8a/M8b/M9/M10/M11/M15 downstream contracts are preserved or explicitly approved for change; M17 retains its M5 Markov-chain/expectation dependency.
- [ ] M5 teaches covariance rather than requiring prior probability theory from M3; full-course versus selected-path prerequisites are explicitly different.
- [ ] Every core outcome has an actual mapped section/exercise/feedback route; topic-level suggestions alone do not pass release review.
- [ ] No unconditional optimizer winner, universal numerical tolerance, or unspecified random-walk model remains.
- [ ] No task compares an implementation with itself and calls that independent validation.

### Resource access and evidence

- [ ] Required instruction, practice, feedback, and core execution can be completed free, without assuming a free trial, paid tutor, instructor-only manual, or financial-aid approval.
- [ ] Publisher landing pages, full text, free previews, paid certificates, and account requirements are distinguished.
- [ ] Hammack, Axler, and other external licenses are not conflated with the repository license.
- [ ] Specific edition/revision/author claims have primary-source evidence.
- [ ] HTTP 403 is not called “browser verified” without an actual successful browser/rendered check.
- [ ] Unsupported prevalence, career, adoption, and multiplier claims are removed or appropriately qualified.

### Assessment and usability

- [ ] A promised diagnostic has actual items, response guidance, routing, limitations, and timing assumptions.
- [ ] Mastery is not reduced to video completion, raw exercise count, or public GitHub visibility.
- [ ] Core versus extension requirements agree across module page, Pick-One table, tracker, and project rule.
- [ ] Numerical projects have small offline fixtures, tolerances, edge cases, and bounded compute needs.
- [ ] Statistical experiments state model, seed/RNG/environment policy, uncertainty, and assumptions; truncated and uncensored quantities are not conflated.
- [ ] QR limitations, rank cutoffs, empty residual arrays, and actual JAX dtype are covered where used.
- [ ] Self-assessed and independently reviewed evidence are distinguished; exposed practice questions are not called unseen gates.
- [ ] Delayed review has a due status, not an automatic two-week progression lock; evidence reuse prevents duplicate project requirements.
- [ ] Course assessment answers and private data are not required to be public.
- [ ] AI-generated answer keys and proofs receive independent checking; an agent does not grade its own output as sufficient verification.

### Repository release

- [ ] Existing explicit anchors remain present and module numbers are unchanged.
- [ ] Run `python3 tools/check_links.py`; report current output, not the historical baseline as if newly obtained.
- [ ] Run `git diff --check` and manually review links, tables, equations, and collapsed sections on GitHub rendering where possible.
- [ ] Document unsupported tools, denied permissions, skipped checks, and unresolved source access honestly.
- [ ] Submit only approved-scope changes to the actual upstream default branch, currently `master`; do not assume `main`.

### Pilot before claiming success

Use two stages rather than pretending a 600–910-hour curriculum can be validated in a brief usability session:

1. **Navigation/diagnostic pilot:** a small voluntary convenience sample covering novice, returning-math, analyst, and Python-experienced learners. Ask each to choose a route, identify the next task, find the free practice/feedback, and interpret an example completion decision. Log ambiguity and actual time; do not conflate unfamiliar content with interface failure.
2. **One-pass learning pilot:** volunteers study a bounded pass using the manifest, log active hours and assistance, complete a changed independent task, and try a delayed transfer check around two weeks later. Check feasibility and rubric disagreements before expanding to other passes. Report both participants who started and those who returned; missing follow-up is not automatically failure or success.

Predefine an owner, observation window, and revision decision. A **proposed release minimum** is no unresolved correctness/access/prerequisite blocker, a working practice-feedback route for every selected outcome, and reviewed examples for critical rubric distinctions. Publish observed time ranges and unresolved problems rather than promising a completion-rate uplift. Reviewer disagreement triggers rubric clarification; disproportionate remediation for a learner subgroup triggers investigation, not a lower hidden standard.

Participation and logging are optional. Collect only data needed for these questions, allow pseudonyms and deletion requests, state the retention period in advance, and report aggregates without identifiable work. No public raw learner logs are required. A convenience pilot can find usability problems and produce workload observations; it cannot establish causal improvements, validate the entire Foundations sequence, or predict employability.

## 9. Research method and limitations

### Original report method (2026-09-06; retained provenance)

1. Cloned the public repository at a fixed commit and read the material identified in Section 1.
2. Ran the existing internal-link checker and inspected active versus staged workflows.
3. Used online search to discover official syllabi, author/publisher pages, software documentation, and learning-science references.
4. Opened primary sources rather than relying only on search snippets.
5. Used JavaScript-rendered retrieval when normal retrieval failed for relevant pages, including the Michigan book announcement.
6. Checked Hammack's PDF front matter directly: edition 3.4, copyright 2018, CC BY-NC-ND 4.0. Its author page confirms a February 2025 minor revision.
7. Confirmed the diagnostic endpoint's final HTTP result as 404; successful retrieval of the Stat 110 landing/practice pages was observed in this research session despite older repository bot-gate notes.

### Revision checks actually performed (2026-09-08)

The original method above is historical provenance, not a claim that every step was repeated. This revision read the full uploaded plan, fetched upstream, reread the full Foundations page and supporting repository guidance, reran the existing checker, and opened selected primary online sources. The changes do not depend on a new unverified “latest edition” claim.

| Evidence rechecked | Observation / limits |
|---|---|
| Upstream default branch and baseline | GitHub reports `master`; fetched baseline remains `a412833204cb334a9c7f96dcd9f3c66029fb38f4`. No live curriculum changes were made. |
| MIT diagnostic `exam_a` URL | Fresh HTTP GET followed redirects and returned 404. |
| Hammack author page and PDF [S01] | Author page and PDF front matter directly read again: edition 3.4, copyright 2018, CC BY-NC-ND 4.0; chapter map supports relations/functions correction. |
| MIT matrix calculus, linear algebra, and algorithms [S03, S04, S06] | Syllabi opened; confirmed prerequisite distinctions, 18.06's approximately 150 hours, 6.006's probability prerequisite and optional CLRS. No complete course taken. |
| Stanford EE364A [S05] | Current page opened; linear algebra/probability/Python prerequisites, public textbook/slides links, enrolled-student video access, and a course-specific LLM policy. Not an authenticated enrollment audit. |
| Harvard practice, honesty, and course scope [S08, S09, S25] | Pages opened; practice/solution structure, assessment sharing/AI restrictions, calculus/matrix prerequisites, Normal/t/MVN coverage. Not every practice PDF downloaded. |
| Coursera [S15] | Official preview-replaces-audit announcement opened again; does not establish individual course completion access. |
| MML [S19] | Companion page opened; free PDF route and chapter map confirmed, main instructor manual distinguished from separate additional exercises/tutorial solutions. No blanket public-solution claim. |
| NumPy, SciPy, JAX [S11, S12, S20, S27, S28] | Documentation read for AD sweeps, forward-difference `check_grad`, rank/residual semantics, RNG conditions, and X64 configuration. These documentation checks are not an execution of the optional JAX project. |
| AERO and CMU [S24, S26] | Guidance opened for spacing/retrieval and outcome–assessment alignment. Does not validate this plan's exact gates or schedule. |

All other original source entries are retained with their original verification scope; **not all S01–S24 were rechecked**. In particular, this revision does not independently reconfirm every inherited author/edition/reprint claim. Changed resource selections must be checked again during implementation. The revised diagnostic/example mathematics and project contracts still require human review before serving as authoritative assessment keys.

### What was not done

- No full completion of the cited university courses or independent execution of every possible learner project.
- No exhaustive audit of all external URLs, all source videos, university-attribution claims, or package versions.
- No authenticated enrollment audit for every course, country, certificate, or financial-aid path.
- No empirical measurement of this repository's completion/dropout rate, hiring outcomes, or effect of the proposed changes.
- No claim that M0–M5 alone provides complete research preparation. Analysis, statistics, and deeper specialization remain important later.

A resource can be freely readable yet have reuse restrictions. Link to restricted third-party material and author original questions rather than copy or relicense it. Source availability and content can change after the research date; implementation must recheck claims it touches.

## 10. Sources

S01–S24 retain the original report's 2026-09-06 verification statements unless updated below. The Section 9 ledger identifies the subset rechecked on 2026-09-08. S25–S28 were newly opened for this revision. Learning-science sources justify general principles, not exact study hours, pass marks, or guaranteed outcomes. Stable, older foundational courses are retained intentionally rather than relabeled as new editions.

| ID | Source | What it supports / verification scope |
|---|---|---|
| S01 | Richard Hammack, [Book of Proof author page](https://richardhammack.github.io/BookOfProof/) and [PDF](https://richardhammack.github.io/BookOfProof/Main.pdf) | Free third-edition text; chapter locations; February 2025 revision notice. PDF front matter directly checked for CC BY-NC-ND 4.0. |
| S02 | Harvard, [CS50P official course](https://cs50.harvard.edu/python/) | Beginner Python content, practice/testing, free OpenCourseWare, browser-first option; account and certificate distinctions. |
| S03 | MIT, [18.S096 Matrix Calculus syllabus](https://ocw.mit.edu/courses/18-s096-matrix-calculus-for-machine-learning-and-beyond-january-iap-2023/pages/syllabus/) | Explicit linear-algebra and multivariable-calculus prerequisites; advanced scope and public notes. |
| S04 | MIT, [18.06SC Linear Algebra syllabus](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/syllabus/) | Calculus knowledge not required to learn linear algebra; structured independent study; approximately 150-hour MIT estimate. |
| S05 | Stanford, [EE364A](https://web.stanford.edu/class/ee364a/) | Linear-algebra/probability prerequisites, Python/CVXPY expectations, free textbook/slides; some current course services and videos are enrollment-based. |
| S06 | MIT, [6.006 Introduction to Algorithms syllabus](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/syllabus/) | Python plus discrete-math prerequisites, Problem Set 0, free notes, and CLRS explicitly not required. |
| S07 | Harvard, [Stat 110](https://stat110.hsites.harvard.edu/) | Official free online second-edition book route and relationship between course/videos. |
| S08 | Harvard, [Strategic Practice and Homework Problems](https://stat110.hsites.harvard.edu/strategic-practice-problems) | Topic-organized practice, mixed homework, and solutions. Page content inspected; not every linked PDF downloaded. |
| S09 | Harvard, [CS50P Academic Honesty](https://cs50.harvard.edu/python/honesty/) | Restrictions on distributing assessment solutions and using non-CS50 AI to suggest/complete assessed answers/code. |
| S10 | NumPy, [Absolute beginners guide](https://numpy.org/doc/stable/user/absolute_beginners.html) | Arrays, shapes, axes, views, broadcasting, array operations, and modern RNG entry points. Relevant sections inspected. |
| S11 | JAX, [Forward- and reverse-mode autodiff](https://docs.jax.dev/en/latest/jacobian-vector-products.html) | Single JVP/VJP cost versus full Jacobian, scalar-loss gradients, and memory trade-offs. |
| S12 | SciPy, [`check_grad`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.check_grad.html) | Gradient checking against finite differences, step-size dependence, and definition of reported error; not a universal `1e-6` guarantee. |
| S13 | Dunlosky et al. (2013), [Improving Students' Learning With Effective Learning Techniques](https://pubmed.ncbi.nlm.nih.gov/26173288/) | Review rates practice testing/distributed practice highly; distinguishes weaker evidence for other techniques. DOI: `10.1177/1529100612453266`. Abstract/review summary inspected. |
| S14 | Pashler et al., IES (2007), [Organizing Instruction and Study to Improve Student Learning](https://ies.ed.gov/ncee/wwc/practiceguide/1), [guide PDF](https://ies.ed.gov/ncee/WWC/Docs/PracticeGuide/20072004.pdf) | Worked examples alternating with problems, fading guidance, spaced review, explanatory questions, concrete/abstract links; relevant recommendations and limitations inspected. |
| S15 | Coursera (August 2025), [New course preview experience](https://blog.coursera.org/introducing-courseras-new-course-preview-experience/) | Official announcement that preview replaces audit for nearly every course; exceptions and financial aid mean course-level verification remains necessary. |
| S16 | Parr and Howard, [The Matrix Calculus You Need For Deep Learning](https://arxiv.org/abs/1802.01528) | Submission history gives v3 as July 2, 2018; contradicts the asserted arXiv 2024 revision. |
| S17 | University of Michigan, [Textbook announcement](https://ece.engin.umich.edu/stories/new-textbook-teaches-students-about-matrix-methods-and-their-real-world-applications) | Confirms Jeffrey A. Fessler and Raj Rao Nadakuditi as authors, graduate-course context, and Julia examples. Retrieved using JS rendering after the ordinary fetch failed. |
| S18 | Sheldon Axler, [Linear Algebra Done Right](https://linear.axler.net/) | Free fourth edition, CC BY-NC license, second-course positioning; author site listed an August 2026 PDF update when inspected. |
| S19 | Deisenroth, Faisal, Ong, [Mathematics for Machine Learning companion](https://mml-book.github.io/) | Free maintained PDF, chapters 2–7, examples/tutorials; canonical public reference is `https://mml-book.com/`. Rechecked 2026-09-08: main instructor manual is request-based, separate additional exercises/tutorial solutions are listed. No unverified “December 2025 update” claim needed. |
| S20 | NumPy, [`linalg.lstsq`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html) | Least-squares/minimum-norm semantics, rank determination, singular values, and residual-output edge cases. |
| S21 | MIT, [18.01SC Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) | Independent-study material with lectures, worked examples, problems, and exams/solutions. Legacy optional Java applets need not be required. |
| S22 | NumPy, [What's new or different in random generation](https://numpy.org/doc/stable/reference/random/new-or-different.html) | `Generator` introduced in 1.17; distinction from legacy `RandomState` and global random functions. |
| S23 | Stanley H. Chan, [Introduction to Probability for Data Science](https://probability4datascience.com/) | Current author page identifies 2026 second edition, free-textbook framing, and learning-material categories. New edition needs remapping rather than a blind year replacement. |
| S24 | Australian Education Research Organisation, [Spacing and retrieval practice guide](https://www.edresearch.edu.au/guides-resources/practice-guides/spacing-and-retrieval-practice-guide-full-publication) | Research synthesis on retrieval, feedback, cumulative review, transfer, and context-dependent spacing intervals. |
| S25 | Harvard, [About Stat 110](https://stat110.hsites.harvard.edu/about) | Newly checked 2026-09-08: calculus (mainly single variable) and matrix familiarity prerequisites; published course topics include covariance, Normal/t, multivariate Normal, and Markov chains. |
| S26 | Carnegie Mellon Eberly Center, [Align Assessments, Objectives, Instructional Strategies](https://www.cmu.edu/teaching/assessment/basics/alignment.html) | Newly checked 2026-09-08: explicit alignment of objectives, learning activities, and assessments; institutional design guidance, not an outcome evaluation of this roadmap. |
| S27 | NumPy, [Random compatibility policy](https://numpy.org/doc/stable/reference/random/compatibility.html) | Newly checked 2026-09-08: stream reproducibility depends on generator, seed, calls/arguments, build/environment; `Generator` does not promise universal cross-version bitwise stability. |
| S28 | JAX, [Default dtypes and the X64 flag](https://docs.jax.dev/en/latest/101/default_dtypes.html) | Newly checked 2026-09-08 after following the documentation redirect: X64 defaults off; explicit float64 requests can be truncated; configure precision deliberately. |

---

**Recommended handoff:** use this report and Section 7.5; the unprovided companion prompt is not required. Start with baseline verification and errata. Require explicit maintainer review and the RFC decision before changing prerequisite order, project obligations, or completion requirements. A plan-review PR does not implement or approve those changes.
