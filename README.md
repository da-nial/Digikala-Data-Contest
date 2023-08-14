# Digikala Data Science Contest Solutions

This repository contains my solutions for
the [Digikala Data Science Contest](https://quera.org/contest/assignments/20120/problems/66283) held in Fall 2021, where
I ranked 4th.
The complete problem statements and datasets for each task can be found in the
contest [page](https://quera.org/contest/assignments/20120/problems/66283), in Persian.

The contest had 6 machine learning problems based on Digikala's datasets.

## Problem 1: Sales Forecast

**Goal**: Predict the sales quantity for each product at different time intervals.

**Input Dataset**:

| **Column** | **Description**         |
|------------|-------------------------|
| id         | Row ID                  |
| date       | Record date             |
| seller     | Seller's information    |
| item       | Product ID              |
| sales      | Number of products sold |

**Output Format**:

```
id,sales
0,100
1,100
2,100
```

**Evaluation Metric**: Symmetric mean absolute percentage error (SMAPE)

**Solution Approach**:

- Preprocessed the data by filling missing values and extracting relevant time-related features (Week, Year, Month, Day,
  IsWeekStarting, IsQuarterEnding, etc), as these time specs have an important influence on sell trends.
- Utilized the `fastai` library to create a tabular neural network model (`tabular_learner`) for training.

## Problem 2: Accepting Comments

**Goal**: Develop a model to automatically accept or reject comments based on their content.

**Input Dataset**:

| **Column**          | **Description**         |
|---------------------|-------------------------|
| id                  | Comment ID              |
| title               | Comment title           |
| comment             | Comment text            |
| advantages          | Mentioned advantages    |
| disadvantages       | Mentioned disadvantages |
| title_fa_product    | Product's Persian name  |
| title_fa_category   | Category's Persian name |
| is_buyer            | Buyer status            |
| verification_status | Label for acceptance    |
| rate                | Given product rating    |

**Output Format**:

```
id,verification_status
0,0
1,1
2,1
```

**Evaluation Metric**: F1 Score

**Solution Approach**:

- Employed the LSTM architecture from the `keras` library.
- Utilized [fasttext](https://fasttext.cc/) embeddings to enhance the model's performance.
- Tested [hazm](https://github.com/roshan-research/hazm), a preprocessing library for Persian text, to clean the train
  data.

## Problem 3: Sentiment Analysis

**Goal**: Predict product ratings based on users' textual comments.

**Input Dataset**: Same as Problem 2.

**Output Format**:

```
id,rate
0,57.45
1,88.09
2,81.00
3,46.02
```

**Evaluation Metric**: Symmetric mean absolute percentage error (SMAPE)

**Solution Approach**:

- Experimented with different approaches by viewing the task as both a regression and a categorical problem.
- Utilized embeddings from `fasttext` and added a prediction head, consisting of linear layers to the previously used
  LSTM architecture.

## Problem 4: Color Detection

**Goal**: Build a model to detect the color of clothing products from images.

**Input Dataset**:

| **Column** | **Description**          |
|------------|--------------------------|
| file_name  | Image file name          |
| color_id   | Numeric color identifier |

**Evaluation Metric**: Precision

**Solution Approach**:

- Experimented with both `keras` (InceptionV3) and `fastai` (ResNet101) models for this task.

## Problem 5: Users Online Time Prediction

**Goal**: SQL skills evaluation.

## Problem 5: Product Processing

**Goal**: Python programming skills evaluation.

**Task**:

- Given a warehouse layout with conveyors and processing units, determine the maximum number of products that can be
  processed within a day.

**Solution Approach**:

- The code for this problem is available at [product_processing.py](Product_Processing/product_processing.py)

## Contributors

I thank my dear friends, [Amirhossein Rajabpour](https://github.com/amirhossein-Rajabpour/)
and [Alex Gholamian](https://github.com/alxgh) for their invaluable help with these tasks.