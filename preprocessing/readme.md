## Data preprocessing for visualizations module

This repository contains files used to develop **data.json** for use in **visualizations** module.

+ **pantheon.tsv**

  This dataset is taken from [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/28201) and contains a manually verified dataset of individuals that have transcended linguistic, temporal, and geographic boundaries. The **Pantheon 1.0 dataset** includes the 11,341 biographies present in more than 25 languages in Wikipedia and is enriched with:

  + manually verified demographic information (place and date of birth, gender)
  + a taxonomy of occupations classifying each biography at three levels of aggregation and
  + two measures of global popularity including the number of languages in which a biography is present in Wikipedia (L), and the Historical Popularity Index (HPI) a metric that combines information on L, time since birth, and page-views (2008-2013).


+ **prepare_json.ipynb** - Jupyter notebook that generates the JSON file from dataset.

+ **data.json** - the json file to be used in **visualizations** module.

  Sample entries in **data.json**

```
[
    {
      "category_type": "POLITICIAN",
      "name": "Abraham Lincoln",
      "id": 307,
      "description": "UNITED STATES"
    },
    {
      "category_type": "PHILOSOPHER",
      "name": "Aristotle",
      "id": 308,
      "description": "Greece"
    }
]
```

###### Dataset URL : https://dataverse.harvard.edu/file.xhtml?persistentId=doi:10.7910/DVN/28201/VEG34D&version=1.0
