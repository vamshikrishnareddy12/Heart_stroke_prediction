# Data Description

1. **age**: The person's age in years.

2. **sex**: The person's sex (1 = male, 0 = female).

3. **cp**: Chest pain type (1 = typical angina, 2 = atypical angina, 3 = non-anginal pain, 4 = asymptomatic).

4. **trestbps**: Resting blood pressure (in mm Hg on admission to the hospital).

5. **chol**: Serum cholesterol in mg/dl.

6. **fbs**: Fasting blood sugar > 120 mg/dl (1 = true; 0 = false).

7. **restecg**: Resting electrocardiographic results (0 = normal, 1 = having ST-T wave abnormality, 2 = showing probable or definite left ventricular hypertrophy).

8. **thalach**: Maximum heart rate achieved.

9. **exang**: Exercise induced angina (1 = yes; 0 = no).

10. **oldpeak**: ST depression induced by exercise relative to rest.

11. **slope**: Slope of the peak exercise ST segment (1 = upsloping, 2 = flat, 3 = downsloping).

12. **ca**: Number of major vessels (0–3) colored by fluoroscopy.

13. **thal**: Thallium stress test result (3 = normal; 6 = fixed defect; 7 = reversible defect).

14. **num**: Diagnosis of heart disease (0 = absence, 1-4 = presence/severity). Many projects convert this to a binary **target** (0 = no disease, 1 = disease).

**Notes:** Missing values in the raw files are marked with `?`. We converted those to `NaN`. We then either dropped rows with missing values or imputed them (see your notebook).
