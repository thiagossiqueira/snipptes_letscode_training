'''
Writing a class for your package
We've covered how classes can be written in Python. In this exercise, you'll be creating the beginnings of a Document class that will be a foundation for text analysis in your package. Once the class is written you will modify your package's __init__.py file to make it easily accessible by your users.

Below is the structure of where you'll be working.

working_dir
├── text_analyzer
│    ├── __init__.py
│    ├── counter_utils.py
│    ├── document.py
└── my_script.py

1)
*You are working in document.py.
*Finish the def statement that will create a new Document instance when a user calls Document().
*Use your knowledge of PEP 8 conventions to complete the definition of the newly named class method.
'''


# Define Document class
class Document:
  """A class for text analysis

  :param text: string of text to be analyzed
  :ivar text: string of text to be analyzed; set by `text` parameter
  """

  # Method to create a new instance of MyClass
  def __init__(self, text):
    # Store text parameter to the text attribute
    self.text = text


'''
Question
You just completed writing the Document class for your package in document.py. Which of the following lines would correctly import this class in __init__.py using relative import syntax?

Answer:
from .document import Document
'''

'''
Using your package's class
You just wrote the beginnings of a Document class that you'll build upon to perform text analysis. In this exercise, you'll test out its current functionality of storing text.

Below is the document tree that you've built up so far when developing your package. You'll be working in my_script.py.

working_dir
├── text_analyzer
│    ├── __init__.py
│    ├── counter_utils.py
│    ├── document.py
└── my_script.py

Instructions
*import your text_analyzer package.
*Create an instance of Document with the datacamp_tweet variable that's been loaded into your session.
*Print the contents of the text attribute of your newly created Document instance.
'''
# Import custom text_analyzer package
import text_analyzer

# Create an instance of Document with datacamp_tweet
my_document = text_analyzer.Document(text=datacamp_tweet)

# Print the text attribute of the Document instance
print(my_document.text)

'''
Writing a non-public method
In the lesson, we covered how to add functionality to classes using non-public methods. By defining methods as non-public you're signifying to the user that the method is only to be used inside the package.

In this exercise, you will define a non-public method that will be leveraged by your class to count words.

Instructions
*Counter from collections has been loaded into your environment, as well as the function tokenize().
*Add a method named count_words as a non-public method.
*Give your non-public method the functionality to count the contents tokens attribute using Counter().
*Utilize your new function in the __init__ method.
'''


class Document:
  def __init__(self, text):
    self.text = text
    # Tokenize the document with non-public tokenize method
    self.tokens = self._tokenize()
    # Perform word count with non-public count_words method
    self.word_counts = self._count_words()

  def _tokenize(self):
    return tokenize(self.text)

  # non-public method to tally document's word counts with Counter
  def _count_words(self):
    return Counter(self.tokens)


'''
Using your class's functionality
You've now added additional functionality to your Document class's __init__ method that automatically processes text for your users. In this exercise, you'll act as one of those users to see the benefits of your hard work.

The Document class (copied below) has been loaded into your environment (complete with your new updates).

class Document:
  def __init__(self, text):
    self.text = text
    # pre tokenize the document with non-public tokenize method
    self.tokens = self._tokenize()
    # pre tokenize the document with non-public count_words
    self.word_counts = self._count_words()

  def _tokenize(self):
    return tokenize(self.text)

  # non-public method to tally document's word counts with Counter
  def _count_words(self):
    return Counter(self.tokens)

Instructions
*Create a new Document instance from the datacamp_tweets data set loaded into your environment. The datacamp_tweets object is a single string containing hundreds of tweets written by DataCamp & DataCamp users.
*Print the first 5 tokens from datacamp_doc.
*Print the top 5 most common words that were calculated by the non-public _count_words() method automatically in the Document.__init__ method.
'''

# create a new document instance from datacamp_tweets
datacamp_doc = Document(text=datacamp_tweets)

# print the first 5 tokens from datacamp_doc
print(datacamp_doc.tokens[:5])

# print the top 5 most used words in datacamp_doc
print(datacamp_doc.word_counts.most_common(5))

'''
Using inheritance to create a class
You've previously written a Document class for text analysis, but your NLP project will now have a focus on Social Media data. Your general Document class might be useful later so it's best not destroy it while your focus shifts to tweets.

Instead of copy-pasting the already written functionality, you will use the principles of 'DRY' and inheritance to quickly create your new SocialMedia class.

Instructions
*Document has been preloaded in the session.
*Complete the class statement to create a SocialMedia class that inherits from Document.
*Define SocialMedia's __init__() method that initializes a Document.
'''


# Define a SocialMedia class that is a child of the `Document class`
class SocialMedia(Document):
  def __init__(self, text):
    Document.__init__(self, text)


'''
Adding functionality to a child class
You've just written a SocialMedia class that inherits functionality from Document. As of now, the SocialMedia class doesn't have any functionality different from Document. In this exercise, you will build features into SocialMedia to specialize it for use with Social Media data.

For reference, the definition of Document can be seen below.

class Document:
    # Initialize a new Document instance
    def __init__(self, text):
        self.text = text
        # Pre tokenize the document with non-public tokenize method
        self.tokens = self._tokenize()
        # Pre tokenize the document with non-public count_words
        self.word_counts = self._count_words()

    def _tokenize(self):
        return tokenize(self.text)

    # Non-public method to tally document's word counts
    def _count_words(self):
        # Use collections.Counter to count the document's tokens
        return Counter(self.tokens)

1)
The function filter_word_counts() has been loaded in your session. Use help() to see its proper usage.
Finish the _count_hashtags method using filter_word_counts() so that only words_counts starting with # remain.
'''


# Define a SocialMedia class that is a child of the `Document class`
class SocialMedia(Document):
  def __init__(self, text):
    Document.__init__(self, text)
    self.hashtag_counts = self._count_hashtags()

  def _count_hashtags(self):
    # Filter attribute so only words starting with '#' remain
    return filter_word_counts(self.word_counts, '#')


'''
2)
*Fill in the first line ofSocialMedia's __init__ method using the parent class to properly utilize inheritance.
*Properly call the _count_mentions method in __init__ to add a new feature to SocialMedia.
'''


# Define a SocialMedia class that is a child of the `Document class`
class SocialMedia(Document):
  def __init__(self, text):
    Document.__init__(self, text)
    self.hashtag_counts = self._count_hashtags()
    self.mention_counts = self._count_mentions()

  def _count_hashtags(self):
    # Filter attribute so only words starting with '#' remain
    return filter_word_counts(self.word_counts, first_char='#')

  def _count_mentions(self):
    # Filter attribute so only words starting with '@' remain
    return filter_word_counts(self.word_counts, first_char='@')


'''
Using your child class
Thanks to the power of inheritance you were able to create a feature-rich, SocialMedia class based on its parent, Document. Let's see some of these features in action.

Below is the full definition of SocialMedia for reference. Additionally, SocialMedia has been added to __init__.py for ease of use.

class SocialMedia(Document):
    def __init__(self, text):
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()

    def _count_hashtags(self):
        # Filter attribute so only words starting with '#' remain
        return filter_word_counts(self.word_counts, first_char='#')      

    def _count_mentions(self):
        # Filter attribute so only words starting with '@' remain
        return filter_word_counts(self.word_counts, first_char='@')

Instructions
*import your text_analyzer custom package.
*Define dc_tweets as an instance of SocialMedia with the preloaded datacamp_tweets object as the text.
*print the 5 most_common mentioned users in the data using the appropriate dc_tweets attribute.
*Use text_analyzer's plot_counter() method to plot the most used hashtags in the data using the appropriate dc_tweets attribute.
'''

# Import custom text_analyzer package
import text_analyzer

# Create a SocialMedia instance with datacamp_tweets
dc_tweets = text_analyzer.SocialMedia(text=datacamp_tweets)

# Print the top five most most mentioned users
print(dc_tweets.mention_counts.most_common(5))

# Plot the most used hashtags
text_analyzer.plot_counter(dc_tweets.mention_counts)

'''
Exploring with dir and help
A new method has been added to the Document class. The method is a convenience wrapper around the plot_counter() function you wrote in an earlier exercise. In this exercise, you'll use dir() and help() to identify how to utilize the new method.

1)
*import the text_analyzer package.
*Define my_doc as an instance of Document with the text stored in datacamp_tweets. datacamp_tweets has been pre-loaded in your environment.
'''
# Import needed package
import text_analyzer

# Create instance of document
my_doc = text_analyzer.Document(datacamp_tweets)

'''
2)
Question
Use dir to show all of my_doc's methods and attributes. What is the name of the new plot method from the resulting list.

Answer:
plot_counts
'''

'''
3)
*Run help() on the plot method you discovered with dir() to see how to properly use the functionality.
*Plot my_doc's word counts using the new plot method.
'''
# Import needed package
import text_analyzer

# Create instance of document
my_doc = text_analyzer.Document(datacamp_tweets)

# Run help on my_doc's plot method
help(my_doc.plot_counts)

# Plot the word_counts of my_doc
my_doc.plot_counts()

'''
Creating a grandchild class
In this exercise you will be using inheritance to create a Tweet class from your SocialMedia class. This new grandchild class of Document will be able to tackle Twitter specific details such as retweets.

Instructions
*Complete the class statement so that Tweets inherits from SocialMedia. SocialMedia has already been loaded in your environment.
*Use super() to call the __init__ method of the parent class.
*Define retweet_text. Use help() to complete the call to filter_lines with the correct parameter name. filter_lines has already been loaded in your environment.
*return retweet_text from _process_retweets as an instance of SocialMedia.
'''
# Define a Tweet class that inherits from SocialMedia
class Tweets(SocialMedia):
    def __init__(self, text):
        # Call parent's __init__ with super()
        super().__init__(self, text)
        # Define retweets attribute with non-public method
        self.retweets = self._process_retweets()

    def _process_retweets(self):
        # Filter tweet text to only include retweets
        retweet_text = filter_lines(self.text, first_chars='RT')
        # Return retweet_text as a SocialMedia object
        return SocialMedia(retweet_text)

'''
Using inherited methods
You've now defined a Tweets class that's inherited methods from both Document and SocialMedia. In this exercise, you'll use inherited methods to visualize text from both tweets and retweets.

Be aware that this is real data from Twitter and as such there is always a risk that it may contain profanity or other offensive content (in this exercise, and any following exercises that also use real Twitter data).

1)
import your text_analyzer package.
Define my_tweets as an instance of Tweets using the datacamp_tweets data that has been pre-loaded into your environment.
'''
# Import needed package
import text_analyzer

# Create instance of Tweets
my_tweets = text_analyzer.Tweets(datacamp_tweets)

'''
2)
*Use the plot_counts() method to plot the top 'hashtag_counts'.
*Make sure to check the documentation for my_tweets.plot_counts.
'''
# Import needed package
import text_analyzer

# Create instance of Tweets
my_tweets = text_analyzer.Tweets(datacamp_tweets)

# Plot the most used hashtags in the tweets
my_tweets.plot_counts('hashtag_counts')

'''
3)
Use the plot_counts() method of the retweets attribute to plot the most used hashtags in the retweets subset of the data.
'''
# Import needed package
import text_analyzer

# Create instance of Tweets
my_tweets = text_analyzer.Tweets(datacamp_tweets)

# Plot the most used hashtags in the retweets
my_tweets.retweets.plot_counts('hashtag_counts')
