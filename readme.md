![Readme-Header](https://i.pinimg.com/564x/0e/40/6c/0e406c713b1fdd4806fa4df035a1f512.jpg)

#### This project used my assigned NLP project as a starting point to determine if I could improve the model. Resampling provided the greatest improvement in prediction while accuracy increased only 3%, the average F1 score increased 14%. 

- Scraped 1K GitHub repositories with Harry Potter in the search
- Filtered out those without a readme file or program language
- Filtered for only the top 4 represented program languages: JavaScript, Java, HTML, Python
- Cleaned and prepared data using regex and toktoktokenizer
- Removed common english stop words and additional words found to create noise in dataset
- Vetorized data using TF-IDF
- Initial attempts to improve model by adding data, reducing noise, and testing multiple algorithms did not significantly increase accuracy
- Determined imbalanced dataset might be contributing factor and Resampled data with SMOTE
- This only improved the average model accuracy by 3%, but improved the average F1 score by 14%


<a href="https://www.freepik.com/vectors/background">Background vector created by macrovector - www.freepik.com</a>