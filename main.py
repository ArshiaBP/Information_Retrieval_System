import processor.get_index
from processor import champion_score
from processor import high_idf_score


def main():
    query = str(input())
    process_type = input("for selecting champion lists: 1 & for selecting high IDF lists: 2\n")
    dictionary = processor.get_index.get_dictionary()
    length = processor.get_index.calculate_length(dictionary)
    if process_type == 1:
        champion_score.calculate_cosine_champion(query, length, dictionary)
    else:
        index_counts = high_idf_score.choose_high_idf(query, dictionary)
        high_idf_score.calculate_cosine_high_idf(index_counts, length, dictionary)


if __name__ == "__main__":
    main()
