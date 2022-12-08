import feedparser

NewsFeed = feedparser.parse("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")

print('Number of RSS posts :', len(NewsFeed.entries))

# entries = NewsFeed.len

for i in list(range(len(NewsFeed.entries))):
    print('Entry: ' + str(i) + '/' + str(len(NewsFeed.entries)))
    entry = NewsFeed.entries[i]
    print('Post Title :',entry.title)
    print('content:' +str(entry.summary_detail.value) )
