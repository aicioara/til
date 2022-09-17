# Omnibox

Omnibox is the name of the multi-search-engine search bar that google added a few years ago. It allows the user to select an internal search engine temporarily. For example, the user may type youtube.com (or just "y" if youtube is the first suggestion), press tab and see the search bar turn into an omnibar ("Search YouTube"). The user can then add the search query for YouTube. Needless to say, this is a huge optimization because it saves the user an additional mouse movement (to the search bar) and an additional page load.

Google used to automatically detect when a website had an internal search engine and conveniently add that website's Ombibox integration. This probably caused some websites to abuse the privilege, so newer versions of chrome require users to automatically add the search engine.

To do that, go to chrome://settings/searchEngines, navigate down to site search and manually "Activate" the websites that you wish (should have been visited already), or add new ones.

As a bonus, you may change the default omnibox parameters and add new ones. For instance, I very rarely search github for arbitrary repositories, but I almost daily search my own repositories. Here is a good search term to add for that.

```
https://github.com/aicioara?tab=repositories&q=%s
```

And here are some more rules that I found useful.

```
# youtube.com
https://www.youtube.com/results?search_query=%s&page={startPage?}&utm_source=opensearch

# tldr.sh
https://tldr.ostera.io/%s
```
