# Project Vision

**Mission:** To create a robust, scalable, and adaptable end-to-end forecasting pipeline that can handle diverse time series complexities with minimal configuration. The framework should empower users to move from raw data to actionable forecasts efficiently.

The project will be developed iteratively through the following versions:

---

## Version 1: Core Forecasting Engine

**Goal:** Establish a foundational, model-driven forecasting pipeline.

- **Deliverables:**
    - Implement a unified `forecast_run` pipeline in [`src/models/pipeline.py`](src/models/pipeline.py).
    - Integrate baseline models ([`src/models/baseline.py`](src/models/baseline.py)) for benchmarking.
    - Integrate classical statistical models like `ARIMA` ([`src/models/arima.py`](src/models/arima.py)) and `ExponentialSmoothing` ([`src/models/exponential_smoothing.py`](src/models/exponential_smoothing.py)).
    - Develop a centralized configuration system ([`src/config.py`](src/config.py)) to control model selection, parameters, and execution flow.
    - Implement core evaluation metrics in [`src/helper/metrics.py`](src/helper/metrics.py).

---

## Version 2: Enhanced EDA and Feature Engineering

**Goal:** Build a comprehensive pre-modeling toolkit for data understanding and feature creation.

- **Deliverables:**
    - Expand the `TimeSeriesEDA` class in [`src/models/eda.py`](src/models/eda.py) to automatically generate a full EDA report.
    - Enhance the `FeatureEngineering` class in [`src/models/feature_engineering.py`](src/models/feature_engineering.py) with more sophisticated features (e.g., rolling windows, date-based features).
    - Standardize and generalize hyperparameter tuning using Optuna, replacing the existing `hyperopt` implementation in [`src/models/exponential_smoothing.py`](src/models/exponential_smoothing.py).

---

## Version 3: Advanced Modeling & External Features

**Goal:** Incorporate machine learning models and external data sources to improve accuracy.

- **Deliverables:**
    - Fully implement and integrate tree-based models like `LightGBM` ([`src/models/lightgbm.py`](src/models/lightgbm.py)).
    - Integrate deep learning models like `NBEATSx` and `NHITS` using the [`NeuralTimeSeries`](src/models/neuralforecast.py) class.
    - Formalize the integration of external features, starting with the LLM-based feature extractor ([`src/models/llm_features.py`](src/models/llm_features.py)) to incorporate insights from unstructured text data.

---

## Version 4: Specialized Forecasting Models

**Goal:** Address specific, challenging forecasting scenarios.

- **Deliverables:**
    - **Cold Start:** Implement models for new products with no historical data. This could involve using product metadata or similarity-based approaches.
    - **Intermittent Demand:** Implement specialized models (e.g., Croston's method, ADIDA) for time series with a high frequency of zero values.

---

## Version 5: MLOps and Productionalization

**Goal:** Make the forecasting pipeline production-ready.

- **Deliverables:**
    - **Model Registry:** Implement a system for versioning and storing trained models.
    - **Inference Service:** Create a simple API (e.g., using FastAPI) for serving predictions from trained models.
    - **Monitoring:** Develop dashboards to monitor forecast accuracy and data drift over time.
    - **Automated Retraining:** Set up a workflow for automatically retraining models when performance degrades or new data is available.

## Version X: Continuous Improvement & Iteration

**Goal:** Foster a cycle of ongoing enhancement and adaptation.

- **Deliverables:**
    - **Performance Profiling:** Regularly profile and optimize critical code paths for speed and memory efficiency.
    - **Code Refactoring:** Continuously refactor the codebase to improve modularity, readability, and maintainability.
    - **Dependency Management:** Keep all project dependencies up-to-date and manage security vulnerabilities.
    - **Incorporate new techiues:** Add better implementations or latest techqiues for improving forecasts.