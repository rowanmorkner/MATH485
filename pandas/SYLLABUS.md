# Python for Data Science — Pandas & Friends

A self-paced course for someone who already knows R/tidyverse and wants fluency in the Python data stack.

Each module has:
- `lesson.md` — concepts, syntax, and R equivalents where helpful
- `problems.py` — function stubs to fill in (like leetcode)
- `test_problems.py` — run `pytest` to check your answers
- `data/` — bundled datasets (when needed)

Run a single module's tests: `pytest 01_series_and_dataframes/test_problems.py -v`
Run everything: `pytest -v`

---

## Module 01 — Series & DataFrames (The Basics)
> *R equivalent: vectors, tibbles/data.frames*

- Creating Series and DataFrames from dicts, lists, numpy arrays
- Indexing: `.loc[]`, `.iloc[]`, boolean indexing
- Column selection, renaming, dropping
- `.head()`, `.tail()`, `.shape`, `.dtypes`, `.describe()`
- Setting and resetting index

## Module 02 — Reading & Writing Data
> *R equivalent: read_csv, read_tsv, readRDS*

- `pd.read_csv()`, `pd.read_json()`, `pd.read_excel()`
- Writing: `.to_csv()`, `.to_json()`
- Handling common gotchas: encoding, dtypes on read, `parse_dates`
- Working with messy real-world files

## Module 03 — Selecting & Filtering
> *R equivalent: dplyr::select, filter, slice*

- Boolean masks and `.query()`
- `.isin()`, `.between()`, string methods (`.str.contains()`)
- Chaining conditions (`&`, `|`, `~`)
- Selecting columns by dtype, pattern

## Module 04 — Transforming & Creating Columns
> *R equivalent: dplyr::mutate, case_when*

- Assignment with `df["col"] = ...`
- `.apply()`, `.map()`, `np.where()`, `np.select()`
- String methods: `.str.lower()`, `.str.split()`, `.str.extract()`
- Datetime accessors: `.dt.year`, `.dt.dayofweek`, etc.

## Module 05 — Grouping & Aggregation
> *R equivalent: dplyr::group_by + summarize*

- `.groupby()` basics: single and multi-column
- `.agg()` with named aggregations
- `.transform()` vs `.apply()` (window functions vs collapse)
- Pivot tables: `pd.pivot_table()`

## Module 06 — Joining & Combining Data
> *R equivalent: dplyr joins, bind_rows*

- `pd.merge()`: inner, left, right, outer
- Join on index vs columns, handling key mismatches
- `pd.concat()` (row-wise and column-wise)
- Diagnosing join issues: duplicates, missing keys

## Module 07 — Missing Data
> *R equivalent: NA handling, tidyr::drop_na, replace_na*

- `NaN` vs `None` vs `pd.NA`
- `.isna()`, `.fillna()`, `.dropna()`
- Interpolation: `.interpolate()`
- Strategy: when to drop vs fill vs flag

## Module 08 — Reshaping Data
> *R equivalent: tidyr::pivot_longer, pivot_wider*

- `.melt()` (wide → long) and `.pivot()` (long → wide)
- `.stack()` / `.unstack()`
- `.explode()` for list columns
- Multi-index basics

## Module 09 — Visualization with Matplotlib & Seaborn
> *R equivalent: ggplot2*

- Quick pandas plots: `df.plot()`, `df.plot.scatter()`, `df.plot.hist()`
- Matplotlib fundamentals: `fig, ax` pattern, labels, legends
- Seaborn: `sns.scatterplot`, `sns.boxplot`, `sns.heatmap`
- Customization: themes, color palettes, multi-panel figures
- Saving figures

## Module 10 — NumPy Essentials for Pandas Users
> *R equivalent: base R vectorized operations, matrix ops*

- Array creation, indexing, slicing
- Broadcasting and vectorized operations
- Linear algebra basics: `np.dot`, `np.linalg`
- Random number generation: `np.random`
- When to use numpy vs pandas

## Module 11 — Exploratory Data Analysis (EDA) Workflow
> *Putting it all together*

- Full EDA pipeline on a real dataset
- Profiling: shape, dtypes, nulls, distributions
- Correlations and `.corr()`
- Feature-target relationships
- Identifying outliers

## Module 12 — Feature Engineering & ML Prep
> *R equivalent: recipes, caret preprocessing*

- Encoding categoricals: `pd.get_dummies()`, `LabelEncoder`, `OrdinalEncoder`
- Scaling/normalizing: `StandardScaler`, `MinMaxScaler`
- Train/test split: `train_test_split()`
- Building a simple pipeline with `sklearn.pipeline`
- Quick model fit + evaluation (not the focus — just enough to see the pipeline work)

## Module 13 — Performance & Idiomatic Pandas
> *Writing code that doesn't make you wait*

- Vectorization vs loops (why `apply` is often slow)
- `.eval()` and `.query()` for large DataFrames
- Memory optimization: downcasting dtypes, categorical dtype
- Method chaining style

## Module 14 — Real-World Capstone
> *End-to-end project*

- Messy real-world dataset
- Clean → explore → engineer features → visualize → model-ready output
- No hand-holding — just requirements and tests
