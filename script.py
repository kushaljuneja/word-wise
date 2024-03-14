import json

NOTION_API_KEY = ...
RESEND_API_KEY = ...

NUM_WORDS = ...


def setup():
	"""
	update API keys by reading secrets.json
	update NUM_WORDS by reading params.json

	throw error if any of params are invalid
	API KEY can be invalid if connection not established
	NUM WORDS can be invalid if not set of out of range (0, 10)
	"""
	...


def query_notion_to_get_words_and_scores():
	...


def select_top_n_words_from_list(word_score_list: list):
	...


def send_mail(word_score_list: list):
	...


if __name__ == '__main__':
	setup()
	word_score_list = query_notion_to_get_words_and_scores()
	filtered_word_score_list = select_top_n_words_from_list(word_score_list)
	send_mail(filtered_word_score_list)
