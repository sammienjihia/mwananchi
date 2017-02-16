import difflib
from sms.models import Insms




def sequencematch(uinput):
    message = []
    global message
    messages = Insms.objects.exclude(msg_type_status=False)

    for row in messages:

        sentence = row.text.lower().split()

        for words in sentence:

            s = difflib.SequenceMatcher(None, uinput.lower(), words)
            ratio = round(s.ratio(), 3)

            if ratio >= 0.6:

                message.append(row)

    return message


def sequence_match_ratio(word1, word2):
    s = difflib.SequenceMatcher(None, word1, word2)
    ratio = round(s.ratio(), 3)
    return ratio
