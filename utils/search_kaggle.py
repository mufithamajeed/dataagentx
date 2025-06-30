from kaggle.api.kaggle_api_extended import KaggleApi

def search_kaggle(query, max_results=5):
    api = KaggleApi()
    api.authenticate()

    # Kaggle's API does not support page_size — remove it
    datasets = api.dataset_list(search=query, sort_by='hottest')
    results = []

    for ds in datasets[:max_results]:  # manually slice top N
        results.append({
            "title": ds.title,
            "ref": ds.ref,
            "url": f"https://www.kaggle.com/datasets/{ds.ref}",
            "description": ds.subtitle
        })

    return results
