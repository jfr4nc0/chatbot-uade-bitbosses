from src.assistant_rag.pipelines.etl_pipeline import load_and_merge_data


def generate_embeddings():
    merged_data = load_and_merge_data()
    merged_data.head()
    print(merged_data.columns)
    print(merged_data.info())