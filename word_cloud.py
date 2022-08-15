import wordcloud
from matplotlib import pyplot as plt

def calculate_frequencies():
    f=open("proj.txt")
    file_contents=f.read()
	     
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    res={}   #creating empty dictionary
    content=file_contents.split()
    for word in content:
        if word in uninteresting_words:
            pass
        else:
            for letter in word:
                if letter in punctuations:
                    letter.replace(punctuations,"")
            if word not in res.keys():
                res[word]=0
            else:
                res[word]+=1
    print(res)
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(res)
    return cloud.to_array()


# Display your wordcloud image

myimage = calculate_frequencies()
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()