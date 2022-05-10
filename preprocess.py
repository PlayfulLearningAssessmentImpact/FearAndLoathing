#!/usr/bin/env python3

from pandas import read_csv, concat, DataFrame

# import nltk

# nltk.download("punkt")
# sentence_detector = nltk.data.load("tokenizers/punkt/english.pickle")

# test = """
# This letter was addressed to Nicholas Broune, Esq., the editor of the
# "Morning Breakfast Table," a daily newspaper of high character; and,
# as it was the longest, so was it considered to be the most important
# of the three. Mr. Broune was a man powerful in his profession,--and
# he was fond of ladies. Lady Carbury in her letter had called herself
# an old woman, but she was satisfied to do so by a conviction that no
# one else regarded her in that light. Her age shall be no secret to
# the reader, though to her most intimate friends, even to Mr. Broune,
# it had never been divulged. She was forty-three, but carried her
# years so well, and had received such gifts from nature, that it was
# impossible to deny that she was still a beautiful woman. And she
# used her beauty not only to increase her influence,--as is natural
# to women who are well-favoured,--but also with a well-considered
# calculation that she could obtain material assistance in the
# procuring of bread and cheese, which was very necessary to her, by
# a prudent adaptation to her purposes of the good things with which
# providence had endowed her. She did not fall in love, she did not
# wilfully flirt, she did not commit herself; but she smiled and
# whispered, and made confidences, and looked out of her own eyes into
# men's eyes as though there might be some mysterious bond between her
# and them--if only mysterious circumstances would permit it. But the
# end of all was to induce some one to do something which would cause
# a publisher to give her good payment for indifferent writing, or an
# editor to be lenient when, upon the merits of the case, he should
# have been severe. Among all her literary friends, Mr. Broune was the
# one in whom she most trusted; and Mr. Broune was fond of handsome
# women. It may be as well to give a short record of a scene which had
# taken place between Lady Carbury and her friend about a month before
# the writing of this letter which has been produced. She had wanted
# him to take a series of papers for the "Morning Breakfast Table," and
# to have them paid for at rate No. 1, whereas she suspected that he
# was rather doubtful as to their merit, and knew that, without special
# favour, she could not hope for remuneration above rate No. 2, or
# possibly even No. 3. So she had looked into his eyes, and had left
# her soft, plump hand for a moment in his. A man in such circumstances
# is so often awkward, not knowing with any accuracy when to do one
# thing and when another! Mr. Broune, in a moment of enthusiasm, had
# put his arm round Lady Carbury's waist and had kissed her. To say
# that Lady Carbury was angry, as most women would be angry if so
# treated, would be to give an unjust idea of her character. It was a
# little accident which really carried with it no injury, unless it
# should be the injury of leading to a rupture between herself and
# a valuable ally. No feeling of delicacy was shocked. What did it
# matter? No unpardonable insult had been offered; no harm had been
# done, if only the dear susceptible old donkey could be made at once
# to understand that that wasn't the way to go on!
# """

# for s in sentence_detector.tokenize(test.strip().replace("\n", " ")):
#     print(s)
#     print()

# # Make a shuffled version
# data = read_csv("data.csv")

# new_rows = []
# for index, df_row in data.iterrows():
#     row = list(df_row.values)
#     metadata = row[:-1]
#     text = str(row[-1])
#     for s in sentence_detector.tokenize(text.strip().replace("\n", " ")):
#         new_row = [*metadata, s]
#         new_rows.append(new_row)

# sentences = DataFrame(new_rows, columns=data.columns)
# sentences.to_csv("sentences.csv")
# print(sentences)

data = read_csv("sentences.csv")
shuf = data.sample(frac=1)
shuf.to_csv("shuf.csv")

# Export base rate inflated subsets for each code
## AI
ai_rows = (
    shuf.Text.str.lower().str.contains("algorithm") |
    shuf.Text.str.lower().str.contains(" ai ") |
    shuf.Text.str.lower().str.contains("artificial intelligence") |
    shuf.Text.str.lower().str.contains("machine to measure") |
    shuf.Text.str.lower().str.contains("kind of formula")
)

ai_inflated = concat([shuf.sample(n=4*sum(ai_rows)), shuf[ai_rows]])
ai_inflated.sample(frac=1).to_csv("shuf-ai.csv")