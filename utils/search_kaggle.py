from kaggle.api.kaggle_api_extended import KaggleApi

def search_kaggle(query: str, max_results=5):
    api = KaggleApi()
    api.authenticate()

    datasets = api.dataset_list(search=query, sort_by='hottest')[:max_results]

    results = []
    for d in datasets:
        results.append({
            "title": d.title,
            "ref": d.ref,
            "url": f"https://www.kaggle.com/datasets/{d.ref}"
        })

    return results


if __name__ == "__main__":
    results = search_kaggle("climate")
    for r in results:
        print(f"\n🌍 {r['title']}\n{r['url']}")

