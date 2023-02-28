# Valerdat app

### Usage and notes
- To import products from  local json file, use:
```sh
python manage.py importproducts /path-to-file
``` 
- To test the API first run migrations (for product model)
```sh
python manage.py makemigrations                    
python manage.py migrate
``` 
- Now start app in development mode and open the postman collection
    - Excercise 1. Contains the post and get request to create / retrieve products 
        - TODO: 
            - Implement pagination
            - For fast queryng we must implement a cache layer
    - Exercise 2. Contains the word_finder request. Here the word list is downloaded from https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt, in order to make it optimal we must define the common list of word an treat it local or cached storaged instead of download it every time.
    - Exercise 3. Contains the search request. To use it, is needed to run before the importproducts command.
- Notes:
    - The json file with fake products is copied to /test/data
    - The postman collection in stored in /test/api
    - The app mantains the SQLite original storage