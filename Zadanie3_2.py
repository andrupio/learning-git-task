print("Zadanie 1")
shopping = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}
for key, value in shopping.items():
    print(f"Idę do", key.capitalize(),
          "kupuję tu następujące rzeczy:", str(value).title())
print(f"W sumie kupuję", sum(len(i) for i in shopping.values()), "produktów")
