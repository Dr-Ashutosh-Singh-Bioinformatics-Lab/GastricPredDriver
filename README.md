# GastricPredDriver: A Tool for Identification of Gastric Cancer from salivary extracellular vesicles (EVs) using Machine Learning for Cancer Driver Genes.
Gastric cancer, originating from the stomach lining, presents a substantial global health challenge due to its high prevalence and mortality rates. Timely detection of gastric cancer is crucial for timely treatment and better patient prognosis. Biomarkers are pivotal in this regard, providing noninvasive means for early detection, facilitating prompt treatment initiation, and potentially boosting survival rates. Hence, the recognition and validation of biomarkers are of primary importance in effectively addressing gastric cancer.


## Introduction

Cancer driver genes are crucial in the onset and progression of various cancers, including gastric cancer. GastricPredDriver is an innovative solution for identifying gastric cancer through a noninvasive method using salivary extracellular vesicles (EVs). By leveraging advanced machine learning algorithms, this cutting-edge technology analyzes salivary biomarkers to provide a highly accurate prognosis of gastric cancer.

Furthermore, the integration of machine learning algorithms allows for continuous refinement of the predictive model's accuracy as more data is gathered, thereby enhancing its reliability and effectiveness over time. GastricPredDriver represents a significant breakthrough in the early detection of gastric cancer, potentially leading to earlier interventions and improved patient outcomes.

To further strengthen our approach, we have selected 39 features using various Feature Selection Methods, including Mutual Information, Recursive Feature Selection, and SelectFromModel with RandomForestRegressor. By employing a combination of Filter, Wrapper, and Embedded feature selection techniques and using an ensemble approach, we identified features present in at least two methods. These 39 features show promise as biomarkers for classifying and predicting normal and cancerous patients from Driver genes. 


## Accuracy Heatmap of the Different Feature Selection Methods for Cancer Driver Genes

![ACC_D](https://github.com/GITractCancer/GastricPredDriver/assets/171772666/f63c0822-4594-4c6f-865e-d445a5d3ffce)


## AUC Heatmap of the Different Feature Selection Methods for Cancer Driver Genes 

![AUC_D](https://github.com/GITractCancer/GastricPredDriver/assets/171772666/d7935da7-cf47-4c6e-adcf-3e6d3b808c78)



## Venn Diagram showing features in atleast in 2 Feature Selection Methods for Cancer Driver Genes

![Driver](https://github.com/GITractCancer/GastricPredDriver/assets/171772666/3fa7e78e-522d-4135-9f84-82d583fee6ab)


Installation and Usage:

You can install the package using the following command:


    git clone https://github.com/GITractCancer/GastricPredDriver.git
    cd GastricPredDriver



### Predict using GastricPredDriver

    import pandas as pd
    from GastricPredDriver import predict

    df = pd.read_csv("path/to/your/data.csv")

    predict(df, model_type='svc')
    print(df)
    
Specify the model type you want to use Models


## Models

The following classifiers are supported:

    svc
    rf
    ab
    xgb
    dt
    et
    lr
    gnb
    knn
    mlp
