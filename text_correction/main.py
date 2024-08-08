from textblob import TextBlob

def correct_text(text: str) -> str:
    textblob = TextBlob(text)
    corrected_text = textblob.correct()
    return corrected_text

print(correct_text("I make manys speling mistakesss."))
print(correct_text("I realy enjoy eating ice creem on hot days."))
print(correct_text("The childern were playing in the park all afternun."))
print(correct_text("He tryed to fix the broked chair but failed."))