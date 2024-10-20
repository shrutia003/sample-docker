import re
from collections import Counter
import socket

def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text) 
        return words, Counter(words)

def split_contractions(text):
    text = re.sub(r"(\w+)\'(m|re|s|ve|ll|d|t)", r"\1 \2", text)
    return text

def main():
    #File paths  
    file1 = '/home/data/IF.txt'
    file2 = '/home/data/AlwaysRememberUsThisWay.txt'
    output_file = '/home/data/output/result.txt'
    
    words1, counter1 = count_words(file1)
    total_words_file1 = len(words1)
    
    with open(file2, 'r') as file:
        text2 = split_contractions(file.read().lower())
        words2 = re.findall(r'\b\w+\b', text2)
        counter2 = Counter(words2)
    total_words_file2 = len(words2)
    
    grand_total = total_words_file1 + total_words_file2

    top3_file1 = counter1.most_common(3)
    top3_file2 = counter2.most_common(3)
    
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    with open(output_file, 'w') as f:
        f.write(f"Total words in IF.txt: {total_words_file1}\n")
        f.write(f"Total words in AlwaysRememberUsThisWay.txt: {total_words_file2}\n")
        f.write(f"Grand total of words: {grand_total}\n")
        f.write(f"Top 3 words in IF.txt: {top3_file1}\n")
        f.write(f"Top 3 words in AlwaysRememberUsThisWay.txt: {top3_file2}\n")
        f.write(f"Container IP address: {ip_address}\n")

    with open(output_file, 'r') as f:
        print(f.read())

if __name__ == '__main__':
    main()
