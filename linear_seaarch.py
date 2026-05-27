accounts = [[1,2,3],[3,2,1]]
max_sum=0
for num in accounts:
    sum_1=0
    for i in num:
        sum_1+=i
        if sum_1>max_sum:
            max_sum=sum_1
print(max_sum)
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
words=" ".join(sentences).split()
max_count=0
for count in words:
    word_count=0
    for i in count:
        word_count+=1
    if word_count>max_count:
        max_count=word_count
print(max_count)
sentences=["hjk jkl trewq dfgb utr","erfghj jkloi uytr erty uoyuk","oioiiuy rew rty dswe 2qwasd rewqASZ TYREWQX"]
max_words=0
for sentence in sentences:
    word_count = len(sentence.split())
    if word_count > max_words:
        max_words = word_count
print(max_words)