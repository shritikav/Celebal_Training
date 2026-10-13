
import re

news_paragraph = """Government is set to issue Google a notice after the firm’s AI platform Gemini threw up unsubstantiated allegations in response to a query on PM Modi. Minister of state for IT Rajeev Chandrasekhar took a serious view of the matter after it was flagged by a user on X. “These are direct violations of Rule 3(1)(b) of Intermediary Rules (IT rules) of IT act and violations of several provisions of the criminal code,” he posted on X, in a clear indication that govt intends to initiate action. Gemini attributed allegations of rising authoritarianism and communalism under Modi to unnamed “experts”, as per the X post."""


# 1. Check presence of Modi
def check_modi(news):
    return "Modi" in news


# 2. Count words
def count_words(news):
    return len(news.split())


# 3. Count occurrences of the word 'the'
def count_the(news):
    words = re.findall(r"\bthe\b", news, re.IGNORECASE)
    return len(words)


# 4. Check presence of digits
def check_digits(news):
    return any(char.isdigit() for char in news)


# 5. Remove articles: a, an, the
def remove_articles(news):
    words = news.split()

    filtered_words = [
        word for word in words
        if word.lower().strip('.,!?;:"“”') not in ["a", "an", "the"]
    ]

    return " ".join(filtered_words)


# 6. Remove vowels from each word
def remove_vowels(news):
    return re.sub(r"[aeiouAEIOU]", "", news)


# Main program
if __name__ == "__main__":
    print("Presence of 'Modi':", check_modi(news_paragraph))

    print("Number of words:", count_words(news_paragraph))

    print("Number of occurrences of 'the':", count_the(news_paragraph))

    print("Presence of digits:", check_digits(news_paragraph))

    compact_news = remove_articles(news_paragraph)
    print("Compact news data without articles:")
    print(compact_news)

    vowel_free_news = remove_vowels(compact_news)
    print("Compact news data without vowels:")
    print(vowel_free_news)
