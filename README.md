# Skin Cancer Lesion Classification using HAM10000 Dataset

This is a Skin Cancer  Classification project.In this repository, Skin cancer is a significant health concern, and early detection through image analysis can be a powerful tool in aiding diagnosis.

## Dataset Link

The [HAM10000 dataset Kaggle](https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000) is a collection of dermatoscopic images of skin lesions, containing seven classes of skin cancer lesions:

## Skin Cancer Lesion Classes

| Class                               | Description                                                                                                  |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Melanocytic nevi (nv)               | Melanocytic nevi, also known as moles, are benign skin lesions consisting of melanocytes.                   |
| Melanoma (mel)                      | Melanoma is a malignant skin cancer that arises from melanocytes. It is the most dangerous form of skin cancer. |
| Benign keratosis-like lesions (bkl) | Benign keratosis-like lesions include various non-cancerous skin conditions that resemble actinic keratoses or basal cell carcinomas. |
| Basal cell carcinoma (bcc)          | Basal cell carcinoma is a common form of skin cancer that arises from basal cells in the epidermis.           |
| Actinic keratoses (akiec)           | Actinic keratoses, also known as solar keratoses, are precancerous lesions caused by sun exposure.             |
| Vascular lesions (vas)              | Vascular lesions include various blood vessel-related skin conditions, such as angiomas.                    |
| Dermatofibroma (df)                 | Dermatofibroma is a benign skin condition characterized by fibrous tissue growth in the dermis.               |


## Project Structure

- `data/`: Placeholder for the dataset.
- `models/`: Trained deep learning learning  models.
- `src/`: Source code for data preprocessing, model training, and evaluation.
- `requirements.txt`: project dependencies.

## Getting Started

1. **Installing Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Download and Prepare Dataset:**

   - Download the HAM10000 dataset from [Kaggle](https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000).




3. **Exploration and Model Training:**

   Data cleaning / model training and evaluation.

4. **Replace the path of the model in main.py**
```python
    #Load model
    my_model=load_model("/app/models/model.h5")
```


## Run flask project
```sh
python3 run app.py
```


