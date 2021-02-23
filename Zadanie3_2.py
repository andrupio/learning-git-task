print("Zadanie 1")
shopping = {
    "piekarnia": ["chleb", "bułki", "pączek", "ptyś", "bułka słodka"],
    "sklep mobilny": ["marchew", "seler", "rukola"],
    "sklep zoologiczny": ["żółw czerwonolicy", "chomik", "papuga"]
}
for key, value in shopping.items():
    print(f"Idę do", key.capitalize(),
          "kupuję tu następujące rzeczy:", str(value).title())
print(f"W sumie kupuję", sum(len(i) for i in shopping.values()), "produktów")
print("Special greetings to the Mentor")
