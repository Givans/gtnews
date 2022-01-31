# gtnews
# NewsApp ( Kenya News )
### [Working Demo](http://gtupdates.herokuapp.com/).
A bit overview, it uses mediastack.com API to get news and get JSON data back. Then it is parsed using a json library.

#### Note: To run the app you have to add [mediastack.com](https://mediastack.com/signup) key. I have taken this step to due to limited access to daily request for News. Getting a key would take just few seconds :)

#### Setup API Key
1. Visit [mediastack.com](https://mediastack.com/signup) to get your API Key
2. Copy your API Key from accounts section
3. Open `views.py` *(in your app)*
   - Add the following line:
    ```
    api_key="YOUR_API_KEY"
    ``` 
   - if you are from adifferent country you can cjange the country as follows in views.py:
     ```
      url = f'http://api.mediastack.com/v1/news?access_key={api_key}&keywords={search}&countries=ke'
    ``` 
    replace 'ke' with your countries initials eg espn or us
      


#### Demo
- ##### Home
<img src="app.gif" width="40%">

- ##### Widget
<img src="widget.gif" width="40%">


#### Credits
- [Dennis Ivy](https://www.youtube.com/channel/UCTZRcDjjkVajGL6wd76UnGg) For teaching me Django

### [Web Developer](http://givansot.herokuapp.com/).
