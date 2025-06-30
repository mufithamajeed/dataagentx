from huggingface_hub import list_datasets

def search_huggingface(query: str, max_results=5):
    results = list_datasets(search=query, limit=max_results)
    final = []

    for d in results:
        final.append({
            "name": d.id,
            "description": d.cardData["description"] if d.cardData and "description" in d.cardData else "No description available"
        })

    return final


if __name__ == "__main__":
    results = search_huggingface("climate")
    for r in results:
        print(f"\n🧠 {r['name']}\n{r['description']}")

