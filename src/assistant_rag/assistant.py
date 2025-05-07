from src.assistant_rag.pipelines.etl_pipeline import load_and_merge_data

def main():
    data = load_and_merge_data()
    print(data)


if __name__ == "__main__":
    main()