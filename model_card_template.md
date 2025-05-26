# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This is a Random Forest Classifier that has been trained to predict whether a person earns more than $50K annually based on the census data provided in census.csv. Several demographic and employment-related features are utilized and implemented using scikit-learn. The model is saved as a '.pkl' file.

## Intended Use
This model will be used as part of a FastAPI implementation.

This model was created as part of the Udactiy Machine Learning DevOps course, and is not intended for real-world decision-making or production deployment. 

## Training Data
This model was trained on the Adult Census Income dataset from the UC Irvine Machine Learning Repository. The extraction on this dataset was taken from the 1994 Census database. This dataset contains demographic information such as education, occupation, marital status, race, and more. The target variable, salary, indicates whether an individual's income exceeds $50K annually. The dataset was split into training and testing subsets using an 80/20 split., stratified on salary to maintain class balance. 

## Evaluation Data
The evaluation data consists of the 20% test split from the original census dataset and kept separate from the training data. This subset mainstains the distribution of salary, the target variable, to ensure meaningful evaluation. Model performance was assessed on the full test as set, as well as on slices of the data. Each slice of the data corresponds to a single unique value of a categorical features, such as workclass, education, or race.

## Metrics
Model evaluation was based on three classification metrics:
- Precision: Measures the proportion of positive identifications that were correct.
- Recall: Measures the proporation of positives that were correctly identified.
- F1 Score: the harmonic mean of precision and recall.

### Overall Performance on the Test Set:
- Precision: 0.7353
- Recall: 0.6378
- F1 SCore: 0.6831

### Performance on Categorical Slices
Performance was also evaluated across slices of the data grouped by individual categorical features, such as those mentioned in the Evaluation Data section of the card. These results can be found in the 'slice_output.txt' file and demonstrate how the model performs for various subgroups.

## Ethical Considerations
This model was trained on census data extracted from the 1994 database. Therefore, this model will reflect any existing societal biases related to race, gender, education, and income that were present during that time. As a result, this model may unintentionally amplify or raise those inherent biases.

Due to this potential bias, the model's predictions could impact decisions that affect an individual's opportunities or classification. This is why this model is not intended for real-world decision-making or production deployment. 

If this model is utilized in a production environment, fairness audits and ongoing monitoring need to be a part of the long-term maintanence and upkeep of this model.

## Caveats and Recommendations
### Caveats
- This model was developed for education purposes and should not be deployed into production without addressing the inherent potential for bias.
- This model was trained on a specific, older census dataset, and may not generalize well to other datasets or populations.
- Performance varies significantly across data slices

### Recommendations
- Conduct fairness audits and bias mitigation steps before utilizing in any real-world application.
- Restrain or fine-tune the model with updated data if deployed in a changing environment.
- Consider utilizing alternate models if higher accuracy or interpretability is needed. 