"""
create a program that takes in a string of text and performs the following tasks using functions
1. Remove all punctuation from the text
2. Converts all letter to lowercase
3. Counts the frequency of each word in the text
4. Print the top 3 most frequent words in the text

Extend further to get an image from the text
1. Generate a wordcloud using the frequent words

Input:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque iaculis sodales felis et varius. Ut ultricies turpis sit amet risus tempus laoreet. Pellentesque tristique mattis sapien a consequat. Integer congue, mauris eget rhoncus finibus, ipsum mauris eleifend mi, eu fringilla lacus est accumsan purus. Nunc porttitor rutrum auctor. Curabitur vestibulum ante est, et finibus nulla dapibus sit amet. Cras justo lorem, fermentum et sapien sed, dictum finibus magna. Vivamus aliquet massa mi, vitae bibendum turpis vestibulum sed. Quisque viverra consectetur nulla. Vestibulum congue nunc sed turpis ornare, id rutrum neque sollicitudin.Donec elementum eu nibh eu elementum. Sed eu eros non nisl pulvinar viverra. Pellentesque pretium tincidunt libero id ultricies. Sed a lectus in ante placerat eleifend sit amet vel risus. Aliquam eget fringilla augue. Donec suscipit, massa a feugiat malesuada, eros libero auctor risus, varius gravida nisl risus at augue. Aenean faucibus nibh a metus mattis porta. Duis pharetra interdum turpis et egestas. Nulla feugiat sem tellus, eget tempus lectus aliquet at. Vestibulum gravida quam diam, et suscipit neque vulputate eget. Cras dapibus pretium nulla in aliquet. Donec venenatis orci ligula, sit amet posuere massa aliquet et. Phasellus nec porta libero. Cras suscipit viverra massa ut tincidunt. Morbi ipsum tellus, finibus in velit accumsan, porttitor posuere nisl. Morbi bibendum vulputate mauris nec aliquam.Sed sit amet commodo nisl. Integer suscipit, quam eu fermentum consectetur, risus dolor vulputate augue, in sagittis ex lacus ac ligula. Maecenas a molestie velit. Nunc eu imperdiet tellus, a interdum dolor. Donec ut augue in tellus luctus finibus. Curabitur tincidunt, neque ut pulvinar accumsan, metus ligula ultricies ligula, non hendrerit risus urna at justo. Suspendisse eu tortor finibus, consectetur enim convallis, convallis felis. Quisque non eros nibh. Ut rhoncus metus sit amet consectetur pellentesque. Vivamus aliquam, dui at malesuada pharetra, urna mauris mollis arcu, at ullamcorper metus mauris nec nisi. Suspendisse commodo felis pharetra mollis varius. Sed pulvinar, ligula nec maximus vulputate, nisl turpis fringilla tortor, nec ultrices eros elit id libero. Quisque molestie odio quis nunc scelerisque, eu condimentum eros porta. Suspendisse potenti.Nulla a orci facilisis, bibendum justo at, faucibus turpis. Vestibulum tempus quam metus, id laoreet metus pretium ut. Quisque tempus imperdiet arcu vitae molestie. Mauris lobortis neque ligula, at accumsan massa gravida quis. Nam sit amet vestibulum ex. Vivamus bibendum, dui non vulputate sodales, turpis justo vestibulum dui, a consequat mi dui vel tellus. Aliquam erat volutpat. Fusce dignissim nulla dapibus, vulputate velit sit amet, rhoncus nibh. Donec ultrices, ipsum nec tempor commodo, quam urna laoreet turpis, efficitur auctor magna enim in neque. Interdum et malesuada fames ac ante ipsum primis in faucibus. Maecenas placerat posuere metus eu efficitur. Duis vel sem magna.Mauris quis enim non turpis tincidunt commodo eu sit amet velit. Donec dignissim efficitur urna at porttitor. Etiam non risus eros. Etiam venenatis tellus ut augue aliquam congue. Ut maximus erat a ipsum posuere, consectetur congue nulla viverra. Suspendisse efficitur nibh in libero pretium egestas. Aenean vestibulum, est eget iaculis suscipit, purus elit rutrum tortor, at varius nunc neque a justo.


1. I do not want letter 'O' to be considered or it should be ignored.
2. Complete top_words function
"""

import string
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def remove_punctuations(text):
    no_punct = ""
    for char in text:
        if char not in string.punctuation: # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
            no_punct += char
    return no_punct


def to_lowercase(text):
    return text.lower()


def count_words(text):
    words = text.split()
    freq = {} # Keys has to be unique
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq


def top_words():
    pass


# Driver Code, Workflow or step by step approach
if __name__ == "__main__":
    text = input("Enter some text: ")
    text = remove_punctuations(text)
    text = to_lowercase(text)
    freq_of_words = count_words(text)

    cus_wordcloud = WordCloud(
        width=800,
        height=800,
        background_color='white'
    ).generate_from_frequencies(freq_of_words)
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(cus_wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()







